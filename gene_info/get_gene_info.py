from Bio import Entrez

def get_gene_details(gene_id, email):
    Entrez.email = email
    
    # 遺伝子IDでEntrez esearchを実行
    search_handle = Entrez.esearch(db="gene", term=gene_id)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    if not search_results['IdList']:
        return 'No summary available'

    # 遺伝子IDを取得
    summary_id = search_results['IdList'][0]

    # 遺伝子IDでEntrez esummaryを実行して詳細情報を取得
    summary_handle = Entrez.esummary(db="gene", id=summary_id)
    summary_results = Entrez.read(summary_handle)
    summary_handle.close()

    # Summaryを抽出
    summary = summary_results['DocumentSummarySet']['DocumentSummary'][0].get('Summary', 'No summary available')
    return summary

def get_omim_from_ensembl(ensembl_id, email):
    Entrez.email = email
    
    # Ensembl IDでEntrez esearchを実行
    search_handle = Entrez.esearch(db="gene", term=f"{ensembl_id}[Ensembl]")
    search_results = Entrez.read(search_handle)
    search_handle.close()

    if not search_results['IdList']:
        return None

    # 遺伝子IDを取得
    gene_id = search_results['IdList'][0]

    # 遺伝子IDでEntrez esummaryを実行して詳細情報を取得
    summary_handle = Entrez.esummary(db="gene", id=gene_id)
    summary_results = Entrez.read(summary_handle)
    summary_handle.close()

    # OMIM番号を抽出
    omim_numbers = summary_results['DocumentSummarySet']['DocumentSummary'][0].get('Mim', [])
    if omim_numbers:
        return omim_numbers[0]  # 最初のOMIM番号を返す
    return None
