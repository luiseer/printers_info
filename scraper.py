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


def get_toner_status_v2(url):
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
            if len(cells) > 1 and 'Estado del tóner' in cells[0].text:
                toner_status['Estado del tóner'] = cells[1].text.strip()
        return toner_status
    except requests.RequestException as e:
        return {"error": f"HTTP error: {e}"}
    except Exception as e:
        return {"error": f"Other error: {e}"}
    
