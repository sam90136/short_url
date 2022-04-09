import requests
import json
from bs4 import BeautifulSoup as bs


def short_url(o_url):
    print(f'input url: {o_url}')
    url0 = 'https://picsee.co/developers/'
    html_str = requests.get(url0)
    soup = bs(html_str.text, 'html.parser')
    pre_str = soup.findAll('code', limit=1)
    # o_url = 'http://www.google.com'
    
    token_str = pre_str[0].text

    url1 = f'https://api.pics.ee/v1/links/?access_token={token_str}'
    dic = dict(
        url=o_url
    )
    r = requests.post(url1, dic)
    print(f'r_status.code: {r.status_code}')
    short_url_str = json.loads(r.text)['data']['picseeUrl']
    print(f'short url: {short_url_str}')


input_url = str(input('請輸入url:')).strip()
url = input_url if (input_url[:7] == 'http://' or input_url[:8] == 'https://') else "http://www.google.com"
short_url(url)
