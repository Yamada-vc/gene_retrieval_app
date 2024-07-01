import requests
import re

def get_genes_by_chromosomal_location(chromosome, start, end, species="human"):
    url = f"https://rest.ensembl.org/overlap/region/{species}/{chromosome}:{start}-{end}?feature=gene"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        genes = response.json()
        gene_list = []
        
        for gene in genes:
            gene_info = {
                'gene_id': gene.get('gene_id', ''),
                'external_name': gene.get('external_name', 'N/A'),
                'hgnc_id': extract_hgnc_id(gene.get('description', ''))
            }
            gene_list.append(gene_info)
        
        return gene_list
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return []

def extract_hgnc_id(description):
    match = re.search(r"HGNC:(\d+)", description)
    if match:
        return match.group(1)
    return 'N/A'
