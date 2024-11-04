import requests
from bs4 import BeautifulSoup

def get_toner_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='matrix')
        if not table:
            return {"error": "Table not found on the page"}
        toner_status = {}
        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) > 1 and 'Tóner' in cells[0].text:
                toner_status[cells[0].text.strip()] = cells[1].text.strip()
        return toner_status
    except requests.RequestException as e:
        return {"error": f"HTTP error: {e}"}
    except Exception as e:
        return {"error": f"Other error: {e}"}
    

def get_total_counter(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encuentra la tabla correcta por su encabezado
        table = soup.find('table', class_='matrix')
        rows = table.find_all('tr')
        
        # Busca el valor de "Número de Recuento" bajo "Contador Total"
        for row in rows:
            cells = row.find_all('td')
            if cells and cells[0].text.strip() == "Blanco y negro":
                total_counter = cells[1].text.strip()
                return total_counter
        
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# URL para probar la función
# url = "http://10.70.16.1/total_count.html"
# print(get_total_counter(url))
    
def get_toner_status_v2(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        toner_status_table = soup.find('h2', text='Estado de alimentación').find_next('table')
        toner_status_rows = toner_status_table.find_all('tr')
        
        toner_status = {}
        for row in toner_status_rows[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) == 2 and 'Tóner' in columns[0].text:
                toner_status['Tóner'] = columns[1].text.strip()
        
        if not toner_status:
            return {'error': 'Toner status not found on the page'}
        return toner_status
    except Exception as e:
        return {'error': str(e)}
    
    

def get_total_counter_v2(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        total_counter_table = soup.find('h2', text='Contador Total').find_next('table')
        total_counter_rows = total_counter_table.find_all('tr')
        
        total_counter = {}
        for row in total_counter_rows[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) == 2:
                counter_type = columns[0].text.strip()
                counter_value = columns[1].text.strip()
                total_counter[counter_type] = counter_value
        
        if not total_counter:
            return {'error': 'Total counter not found on the page'}
        return total_counter
    except Exception as e:
        return {'error': str(e)}    

# URL para probar la función
# url = "http://10.70.16.35/device_status.html"
# print(get_toner_status_v2(url))