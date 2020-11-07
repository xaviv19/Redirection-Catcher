import requests
urls = [
    'https://google.com/drive',
    'http://google.com/images',
    'http://meet.google.com'
]
url_count = 0
for u in urls:
    print("URL:", url_count, sep=" ", end="\n")
    redirection_count = 0
    for x in requests.get(u).history:
        print("\tRedirect " + str(redirection_count) + ": ", end="\n\t")
        print(x.url, end="\n")
        redirection_count += 1
    url_count += 1
