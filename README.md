# Gene Information Retrieval Web Application

This web application allows users to retrieve gene information based on specified chromosomal regions. Users can input a chromosome number, start and end positions, and their email address to get a list of genes in that region. The application fetches gene information including gene names, gene IDs, HGNC IDs, summaries, and links to ClinVar and OMIM databases.

## Features

- Input form for chromosome number, start and end positions, and email address.
- Retrieves gene names, gene IDs, HGNC IDs, and summaries from Ensembl and Entrez databases.
- Displays gene information in a table format.
- Provides links to ClinVar and OMIM databases.
- Loading animation during data retrieval.
- Responsive and styled with CSS.

## Technologies Used

- Python
- Flask
- HTML/CSS
- JavaScript
- Requests library
- Biopython library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/gene-info-app.git
    cd gene-info-app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Fill out the form with the chromosome number, start and end positions, and your email address. Click the "Submit" button.

4. Wait for the loading animation to finish, and the results will be displayed in a table format.

## File Structure

