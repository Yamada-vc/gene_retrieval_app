import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient, gene_info_list):
    msg = MIMEMultipart()
    msg['From'] = "your_email@example.com"
    msg['To'] = recipient
    msg['Subject'] = "Gene Information Results"

    html = "<html><body><h1>Gene Information Results</h1><table><thead><tr><th>Gene Name</th><th>Gene ID</th><th>HGNC ID</th><th>Summary</th><th>ClinVar Link</th><th>OMIM Link</th></tr></thead><tbody>"
    for gene in gene_info_list:
        html += f"<tr><td>{gene['name']}</td><td>{gene['gene_id']}</td><td>{gene['hgnc_id']}</td><td>{gene['summary']}</td><td><a href='https://www.ncbi.nlm.nih.gov/clinvar/?term={gene['name']}'>ClinVar</a></td><td><a href='https://omim.org/entry/{gene['omim']}'>OMIM</a></td></tr>"
    html += "</tbody></table></body></html>"

    msg.attach(MIMEText(html, 'html'))

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_password")
        server.sendmail("your_email@example.com", recipient, msg.as_string())
