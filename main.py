from bs4 import BeautifulSoup
import requests
import os

# xdutsuay
# author - @xdutsuay

url = "https://www.linkedin.com/posts/careerencyclopedia_fridayvibes-fridaymood-ugcPost-6925629434209193984-ICLz" \
      "?utm_source=linkedin_share&utm_medium=member_desktop_web "
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/100.0.4896.127 Safari/537.36'}

try:
    with open("data.txt", 'r') as fp:
        file_path = "data.txt"
        if os.stat(file_path).st_size == 0:
            print("file empty")
        content = fp.read()
    list_hrf = [str(content).split("src=")]
    print(list_hrf)
    # print(content)
except:

    response = requests.get(url, HEADERS)
    content = BeautifulSoup(response.text, "html.parser")
    with open("data.txt", 'w', encoding="utf-8") as fp:
        fp.write(str(content))
    # print(content.prettify())
