from bs4 import BeautifulSoup
import requests

url="https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all("a", class_="storylink")

if not titles:
    titles = soup.select("span.titleline > a")

for i, title in enumerate(titles[:30], start=1):
    print(f"{i}. {title.get_text()} - {title['href']}")