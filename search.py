import requests
from bs4 import BeautifulSoup


class GoogleSearch:
    # Define the function to get search results
    def get_google_results(self, query, num_results=10):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        search_url = f"https://www.google.com/search?q={query}&num={num_results}"

        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract search results
        results = []
        for g in soup.find_all('div', class_='g'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text if g.find('h3') else 'No title'
                results.append({'title': title, 'link': link})

        return results

    def search_url_filter(self, results, url_str="", num_results=10):
        return [res for res in results if url_str in res["link"]][:num_results]

    def get_hyperlinks(self, results):
        links = []
        for idx, result in enumerate(results):
            out = f"{idx + 1}: {result['title']} - {result['link']}"
            print(out)
            link = (idx + 1, result['title'], result['link'])
            links.append(link)
        return links

if __name__ == "__main__":
    query = "대학생 세미나 brunch.co.kr"
    url_filter = "brunch.co.kr"
    num_results = 10

    search = GoogleSearch()
    results_orig = search.get_google_results(query, num_results*10)
    results = search.search_url_filter(results_orig, url_filter, num_results)
    links = search.get_hyperlinks(results)
    print(links)
