from bs4 import BeautifulSoup
import requests
from datetime import datetime
import streamlit as st
from unidecode import unidecode
import html
import re

def fetch_data():
    url = 'http://www.finep.gov.br/chamadas-publicas?situacao=aberta'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch data: {e}")
        return []

    response.encoding = response.apparent_encoding
    html_content = response.text

    decoded_html = html.unescape(html_content)
    decoded_html = unidecode(decoded_html)
    bs = BeautifulSoup(decoded_html, 'html.parser')

    namelist = bs.findAll('div', {'class': 'item'})
    return [name.get_text(strip=True) for name in namelist]

def extract_dates(data):
    dates = []
    for item in data:
        date_pattern = r"Data de publicação: (\d{2}/\d{2}/\d{4}) Prazo para envio de propostas até: (\d{2}/\d{2}/\d{4})"
        match = re.search(date_pattern, item)
        if match:
            publication_date_str, deadline_date_str = match.groups()
            try:
                publication_date = datetime.strptime(publication_date_str, "%d/%m/%Y")
                deadline_date = datetime.strptime(deadline_date_str, "%d/%m/%Y")
                dates.append((publication_date, deadline_date))
            except ValueError:
                pass
    return dates

def main():
    st.title('Dados da Finep')
    
    if st.button('Atualizar Dados'):
        data = fetch_data()
        st.write('Dados Atualizados:')
        for item in data:
            st.write(item)

        dates = extract_dates(data)
        if dates:
            st.write('Datas identificadas:')
            selected_date = st.date_input('Selecione uma data para envio de propostas:', min_value=min([date[1] for date in dates]), max_value=max([date[1] for date in dates]))
            st.write(f'Data selecionada: {selected_date.strftime("%d/%m/%Y")}')
        else:
            st.write('Nenhuma data identificada para envio de propostas.')

if __name__ == '__main__':
    main()
