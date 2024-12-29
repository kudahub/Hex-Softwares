import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape website and save data in structured format
def scrape_website(url, output_file):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Extract specific data (like titles and links)
        data = []
        for item in soup.find_all('a', class_='example-class'):  # Modify selector based on website
            title = item.get_text(strip=True)
            link = item['href']
            data.append({'title': title, 'link': link})

        # Save data to a CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'link'])
            writer.writeheader()
            writer.writerows(data)

        print(f"Data successfully saved to {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == '__main__':
    website_url = 'https://example.com'  # Replace with the target URL
    output_csv = 'output.csv'  # Specify the output file name
    scrape_website(website_url, output_csv)
