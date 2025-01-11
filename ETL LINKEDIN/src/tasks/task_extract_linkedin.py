import requests
from bs4 import BeautifulSoup
from prefect import task

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=4122356494&f_TPR=r86400&geoId=102927786&keywords=python'

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

@task(name='Extraer data de Linkedin')
def task_extract_linkedin():
    response = requests.get(URL, headers=HEADERS)
    jobs = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
       
        div_jobs = soup.find_all('ul', class_='GNeFpPxjdeFrMyXwzuUdIJJtRXnayrrmrOFEQ')
        
        for job in div_jobs:
            nombre = job.find('div', class_='full-width artdeco-entity-lockup__title ember-view').get_text()
            ubi = 'https://neoauto.com/' + job.find('a', class_='c-results__link')['href']
            url = job.find('div',class_='c-results-mount__price').get_text()
            jobs.append({"nombre": nombre, "Ubicación": ubi,"url":url})
    else:
        print(f'Error {response.status_code} {response.reason}')
        
    return jobs