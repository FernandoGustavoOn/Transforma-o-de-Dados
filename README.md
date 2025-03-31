# Transformação de Dados

Este repositório contém o código e os arquivos gerados para o **Teste de Transformação de Dados**. O objetivo é extrair tabelas do PDF "Anexo I - Rol de Procedimentos e Eventos em Saúde", salvá-las em formato estruturado `.csv`, e compactar o resultado em um arquivo `.zip`.

---

## Objetivos do Projeto

O projeto realiza as seguintes etapas:
1. **Extração das tabelas do PDF:**
   - Localiza e extrai as tabelas do documento `Anexo_I_Rol.pdf`.
   - Processa e limpa os dados extraídos, removendo quebras de linha e espaços desnecessários.
2. **Substituição de abreviações:**
   - Coluna "OD" transformada em "Seg. Odontológica".
   - Coluna "AMB" transformada em "Seg. Ambulatorial".
3. **Salvamento em `.csv`:**
   - Todas as tabelas são unificadas em um arquivo `anexo_I.csv`.
4. **Compactação do arquivo `.csv`:**
   - O arquivo `anexo_I.csv` é compactado em um arquivo `.zip` denominado `Teste_Fernando.zip`.

---

## Estrutura dos Arquivos

- **`transformacao.py`:** Código Python que executa todas as etapas mencionadas.
- **`pdfs/`:** Contém o PDF usado como entrada.
  - `Anexo_I_Rol.pdf`: Documento contendo as tabelas a serem extraídas.
- **`anexo_I.csv`:** Arquivo CSV gerado com os dados estruturados.
- **`Teste_Fernando.zip`:** Arquivo compactado contendo o CSV.
- **`README.md`:** Documentação detalhada do projeto.

---

## Pré-requisitos

Antes de executar o projeto, certifique-se de:
1. Ter o Python 3.7 ou superior instalado.
2. Instalar as bibliotecas necessárias:
   - `pdfplumber` para extração de tabelas do PDF.
   - `csv` e `zipfile` (já incluídas no Python).
3. Instale as dependências rodando:
   ```bash
   pip install pdfplumber
