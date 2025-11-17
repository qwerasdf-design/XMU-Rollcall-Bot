import requests, csv

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "x-lc-id": "s0QbLDG5u6IrBSx9dC4yFiLr-gzGzoHsz",
    "x-lc-key": "jEivEsoel0KxBdX4gDuO5Sak"
}

results = []

for ch in 'abcdefghijklmnopqrstuvwxyz0123456789':
    query_url = f"https://api-org.tronclass.com.cn/orgs?keywords={ch}"
    response = requests.get(query_url, headers=headers)
    data = response.json()
    for result in data['results']:
        if result not in results:
            results.append(result)

for result in results:
    if result.get('apiUrl'):
        print(result['orgName'], result['apiUrl'])
        with open("result.csv", "a", newline="", encoding="utf-8") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([result['orgName'], result['apiUrl']])