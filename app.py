from flask import Flask, request, render_template
from gene_info.get_genes import get_genes_by_chromosomal_location
from gene_info.get_gene_info import get_gene_details, get_omim_from_ensembl

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        chromosome = request.form['chromosome']
        start = request.form['start']
        end = request.form['end']
        email = request.form['email']

        genes = get_genes_by_chromosomal_location(chromosome, start, end)
        for gene in genes:
            gene['summary'] = get_gene_details(gene['gene_id'], email)
            gene['omim'] = get_omim_from_ensembl(gene['gene_id'], email)
            if gene['external_name'] != 'N/A':
                gene['clinvar_link'] = f"https://www.ncbi.nlm.nih.gov/clinvar/?term={gene['external_name']}"
                gene['omim_link'] = f"https://omim.org/entry/{gene['omim']}" if gene['omim'] else 'N/A'
            else:
                gene['clinvar_link'] = 'N/A'
                gene['omim_link'] = 'N/A'

        return render_template('result.html', chromosome=chromosome, start=start, end=end, genes=genes)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
