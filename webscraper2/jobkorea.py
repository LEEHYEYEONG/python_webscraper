import requests
from bs4 import BeautifulSoup

URL = f"http://www.jobkorea.co.kr/Search/?stext=python&tabType=recruit&Page_No=i"

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "tplPagination newVer wide"}).find_all("a")
    print(pagination)
