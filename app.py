from flask import Flask, render_template
from scraper import get_toner_status, get_total_counter, get_toner_status_v2
import requests

app = Flask(__name__)

# Lista de impresoras con detalles
printers = [
    # {
    #     "organo_jurisdiccional": "Otra impresora",
    #     "piso": "PB",
    #     "modelo": "Otro modelo",
    #     "serie": "12345678",
    #     "ip": "10.72.16.3",
    #     "scraping_func": get_toner_status_v2
    # },
    {
        "organo_jurisdiccional": 'OFICINA DE CORRESPONDENCIA COMUN JZDOS. DTO. PROC. PENALES FED. D.F EN RECLUSORIO SUR. CDMX',
        'piso': 'PB',
        'modelo': 'MX-M5071',
        'serie': '9F108279',
        'ip': '10.70.16.1',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '1ER TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PISO 2',
        'modelo': 'MX-B476W',
        'serie': '9F025019',
        'ip': '10.70.16.2',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": 'DEFENSORIA PUBLICA FEDERAL ADSCRITA AL CENTRO DE JUSTICIA PENAL FEDERAL CON SEDE EN RECLUSORIO SUR. CDMX',
        'piso': 'PB',
        'modelo': 'MX-M5071',
        'serie': '95009830',
        'ip': '10.70.16.8',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": 'DEFENSORIA PUBLICA FEDERAL ADSCRITA AL CENTRO DE JUSTICIA PENAL FEDERAL CON SEDE EN RECLUSORIO SUR. CDMX',
        'piso': 'PB',
        'modelo': 'MX-M5071',
        'serie': '95008710',
        'ip': '10.70.16.9',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '2DO TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PB',
            'modelo': 'MX-M5071',
        'serie': '95013659',
        'ip': '10.70.16.10',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": 'DEFENSORIA PUBLICA FEDERAL ADSCRITA AL CENTRO DE JUSTICIA PENAL FEDERAL CON SEDE EN RECLUSORIO SUR.. CDMX',
        'piso': 'PB',
        'modelo': 'MX-M5071',
        'serie': '95014429',
        'ip': '10.70.16.11',
        "scraping_func": get_toner_status
            
        },
    {
        "organo_jurisdiccional": '2DO TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PISO 1',
        'modelo': 'MX-B476W',
        'serie': '9F024789',
        'ip': '10.70.16.12',
        "scraping_func": get_toner_status
            
    },
    {
        "organo_jurisdiccional": '2DO TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PB',
        'modelo': 'MX-B476W',
        'serie': '9F024669',
        'ip': '10.70.16.13',
        "scraping_func": get_toner_status
 
    },
    {
        "organo_jurisdiccional": '2DO TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PB',
        'modelo': 'MX-M5071',
        'serie': '95007780',
        'ip': '10.70.16.17',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '2DO TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PB',
        'modelo': 'MX-M5071',
        'serie': '95010060',
        'ip': '10.70.16.18',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '2DO TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PB',
        'modelo': 'MX-B476W',
        'serie': '9F108319',
        'ip': '10.70.16.19',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '1ER TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PISO 1',
        'modelo': 'MX-B476W',
        'serie': '9F108169',
        'ip': '10.70.16.20',
        "scraping_func": get_toner_status
    },
    {
      "organo_jurisdiccional": '1ER TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
      'piso': 'PISO 2',
      'modelo': 'MX-M5071',
      'serie': '95008640',
      'ip': '10.70.16.22',
      "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '1ER TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PISO 2',
        'modelo': 'MX-B476W',
        'serie': '9F108289',
        'ip': '10.70.16.23',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '1ER TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PISO 2',
        'modelo': 'MX-B476W',
        'serie': '9F107789',
        'ip': '10.70.16.24',
        "scraping_func": get_toner_status
    },
    {
         "organo_jurisdiccional": '2DO TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
         'piso': 'PISO 2',
         'modelo': 'MX-M5071',
         'serie': '95008540',
         'ip': '10.70.16.25',
         "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '2DO TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PISO 1',
        'modelo': 'MX-M5071',
        'serie': '95009840',
        'ip': '10.70.16.26',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '1ER TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PB',
        'modelo': 'MX-B476W',
        'serie': '9F024989',
        'ip': '10.70.16.27',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '1ER TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PISO 2',
        'modelo': 'MX-B476W',
        'serie': '9F109269',
        'ip': '10.70.16.28',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": 'CENTRO DE JUSTICIA PENAL FEDERAL EN EL RECLUSORIO SUR. CDMX',
        'piso': 'PISO 1',
        'modelo': 'MX-M5071',
        'serie': '95008550',
        'ip': '10.70.16.29',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": 'CENTRO DE JUSTICIA PENAL FEDERAL EN EL RECLUSORIO SUR. CDMX',
        'piso': 'PISO 2',
        'modelo': 'MX-M5071',
        'serie': '95006560',
        'ip': '10.70.16.31',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": 'DEFENSORIA PUBLICA FEDERAL ADSCRITA AL CENTRO DE JUSTICIA PENAL FEDERAL CON SEDE EN RECLUSORIO SUR., CDMX',
        'piso': 'PB',
        'modelo': 'MX-M5071',
        'serie': '95008330',
        'ip': '10.70.16.32',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": 'ADMINISTRACION EDIFICIO RECLUSORIO SUR. CDMX',
        'piso': 'PB',
        'modelo': 'MX-C304W',
        'serie': '93016579',
        'ip': '10.70.16.33',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": 'FOTOCOPIADO RECLUSORIO SUR',
        'piso': 'PISO 2',
        'modelo': 'MX-M1205',
        'serie': '95008340',
        'ip': '10.70.16.35',
        "scraping_func": get_toner_status

    },
    {
        "organo_jurisdiccional": '1ER TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PISO 2',
        'modelo': 'MX-M5071',
        'serie': '95000669',
        'ip': '10.70.16.36',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": 'CENTRO DE JUSTICIA PENAL FEDERAL EN EL RECLUSORIO SUR.. CDMX',
        'piso': 'PISO 1',
        'modelo': 'MX-M5071',
        'serie': '95007770',
        'ip': '10.70.16.37',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": 'COORDINACION DE SEGURIDAD',
        'piso': 'PB',
        'modelo': 'MX-B476W',
        'serie': '9F107999',
        'ip': '10.70.16.50',
        "scraping_func": get_toner_status
    },
    {
        "organo_jurisdiccional": '1ER TRIBUNAL COLEGIADO DE APELACIÓN EN MATERIA PENAL DEL 1ER CIRCUITO, CDMX',
        'piso': 'PISO 2',
        'modelo': 'MX-M5071',
        'serie': '95014449',
        'ip': '10.70.16.51',
        "scraping_func": get_toner_status
    },
    
    # Agrega más impresoras aquí
]


@app.route('/')
def index():
    printer_statuses = []
    for printer in printers:
        try:
            toner_status = printer["scraping_func"](f"http://{printer['ip']}/main.html")
            total_counter = get_total_counter(f"http://{printer['ip']}/total_count.html")
        except requests.RequestException as e:
            toner_status = {"error": f"HTTP error: {e}"}
            total_counter = {"error": f"HTTP error: {e}"}
        except Exception as e:
            toner_status = {"error": f"Other error: {e}"}
            total_counter = {"error": f"Other error: {e}"}
        printer_statuses.append({
            "organo_jurisdiccional": printer.get("organo_jurisdiccional", "No especificado"),
            "piso": printer.get("piso", "No especificado"),
            "modelo": printer.get("modelo", "No especificado"),
            "serie": printer.get("serie", "No especificado"),
            "ip": printer.get("ip", "No especificado"),
            "toner_status": toner_status,
            "total_counter": total_counter
        })
    return render_template('index.html', printers=printer_statuses)

if __name__ == '__main__':
    app.run(debug=True)
