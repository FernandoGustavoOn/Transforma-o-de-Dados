import pdfplumber
import csv
import zipfile  # Importar o módulo zipfile
import os

# Função para substituir abreviações por descrições completas
def substituir_abreviacoes(row):
    """
    Substitui abreviações específicas nas células da linha.
    Exemplo: "OD" -> "Seg. Odontológica", "AMB" -> "Seg. Ambulatorial".
    """
    return [cell.replace("OD", "Seg. Odontológica").replace("AMB", "Seg. Ambulatorial") for cell in row]

# Função para processar uma tabela extraída
def processar_tabela(tabela):
    """
    Limpa e processa uma tabela extraída do PDF.
    Remove quebras de linha, espaços extras e substitui abreviações.
    """
    cleaned_table = []
    for row in tabela:
        # Substituir abreviações e limpar células
        cleaned_row = substituir_abreviacoes(row)
        cleaned_row = [cell.replace("\n", " ").strip() if cell else "" for cell in cleaned_row]
        cleaned_table.append(cleaned_row)
    return cleaned_table

# Função principal para extrair tabelas do PDF e salvar em CSV
def extrair_tabelas_pdf(caminho_pdf, caminho_csv):
    """
    Extrai tabelas de um arquivo PDF e salva todas em um único arquivo CSV.
    """
    with pdfplumber.open(caminho_pdf) as pdf:
        todas_tabelas = []

        # Iterar pelas páginas do PDF
        for i, pagina in enumerate(pdf.pages):
            if i >= 10:  # Limitar a extração às primeiras 10 páginas para ser mais rapido o teste
                break
            
            tabela = pagina.extract_table()
            if tabela:
                print(f"Tabela encontrada na página {i + 1}")
                # Processar e adicionar a tabela à lista
                tabela_processada = processar_tabela(tabela)
                todas_tabelas.append(tabela_processada)
            else:
                print(f"Nenhuma tabela encontrada na página {i + 1}")

        # Salvar todas as tabelas no arquivo CSV
        if todas_tabelas:
            salvar_tabelas_csv(todas_tabelas, caminho_csv)
            print(f"Tabelas salvas com sucesso no arquivo '{caminho_csv}'")
        else:
            print("Nenhuma tabela encontrada no PDF.")

# Função para salvar tabelas em um arquivo CSV
def salvar_tabelas_csv(tabelas, caminho_csv):
    """
    Salva uma lista de tabelas em um único arquivo CSV.
    Adiciona uma linha em branco entre as tabelas.
    """
    with open(caminho_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for tabela in tabelas:
            writer.writerows(tabela)
            writer.writerow([])  # Linha em branco entre tabelas

# Função para compactar o arquivo CSV em um ZIP
def compactar_csv_em_zip(caminho_csv, caminho_zip):
    """
    Compacta o arquivo CSV em um arquivo ZIP.
    """
    if os.path.exists(caminho_csv):
        # Arquivo CSV existe, agora vamos compactá-lo
        with zipfile.ZipFile(caminho_zip, mode="w", compression=zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(caminho_csv, arcname=os.path.basename(caminho_csv))  # Adiciona o CSV ao ZIP
            print(f"Arquivo compactado com sucesso em '{caminho_zip}'")
    else:
        print(f"Erro: Arquivo CSV não encontrado: {caminho_csv}")

# nome do Zip
nome = "Fernando"

# Executar o script
if __name__ == "__main__":
    caminho_pdf = "pdfs/Anexo_I_Rol.pdf"  # Caminho do arquivo PDF
    caminho_csv = "anexo_I.csv"           # Caminho do arquivo CSV de saída

    # Extrair tabelas e salvar no CSV
    extrair_tabelas_pdf(caminho_pdf, caminho_csv)

    # Caminho do arquivo ZIP de saída
    caminho_zip = f"Teste_{nome}.zip" 
    compactar_csv_em_zip(caminho_csv, caminho_zip)  # Compactar o CSV em um arquivo ZIP
    print(f"Compactado o arquivo CSV em '{caminho_zip}'...")
    