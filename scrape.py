import requests
from bs4 import BeautifulSoup
import csv

# Function to extract data from each company card
def extract_data_from_card(card):
    company_name = card.find('a', class_='stretched-link').text.strip()
    industry = card.find('div', class_='text-14 text-brand-blue').text.strip()
    address = card.find('address').text.strip()
    telephone = card.find('a', class_='text-13').text.strip().split(':')[1].strip()
    return [company_name, industry, address, telephone]

# Send a GET request to the webpage
url = 'https://www.goafricaonline.com/dz/annuaire/industrie-pharmaceutique'
response = requests.get(url)

# Parse the HTML content
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract company information from each card
    companies = []
    company_cards = soup.find_all('article', class_='relative')
    for card in company_cards:
        company_data = extract_data_from_card(card)
        companies.append(company_data)

    # Write the extracted information to a CSV file
    with open('pharmaceutical_companies.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Company Name', 'Industry', 'Address', 'Telephone'])
        writer.writerows(companies)

    print("Data written to pharmaceutical_companies.csv successfully.")
else:
    print(f"Failed to retrieve the webpage: {url}")
