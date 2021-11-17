from datetime import datetime, timedelta, timezone
import logging
import os
import requests
from nacl import encoding, public
from base64 import b64encode
import sys
from fake_useragent import UserAgent

tz = timezone(timedelta(hours=+8))
today = datetime.now(tz)
logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

GH_REPO = os.getenv('GH_REPO')
GH_TOKEN = os.getenv('GH_TOKEN')
COOKIES = os.getenv('BOOKS_COOKIE')
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
BOOKS_ID = os.getenv('BOOKS_ID')
BOOKS_PWD = os.getenv('BOOKS_PWD')
UA = UserAgent()# .google

def update_secret(keys: str, value: str):
    base_url = f'https://api.github.com/repos/{GH_REPO}/actions/secrets'
    headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'token {GH_TOKEN}'}
    resp = requests.get(base_url + '/public-key', headers=headers)
    if 'key' not in resp.json():
        logger.critical('讀取 GH 公鑰失敗')
        sys.exit(1)
    public_key = resp.json()['key']
    key_id = resp.json()['key_id']

    public_key = public.PublicKey(public_key.encode('utf-8'), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = b64encode(
        sealed_box.encrypt(value.encode('utf-8'))).decode('utf-8')

    data = {'encrypted_value': encrypted, 'key_id': key_id}
    resp = requests.put(
        base_url + f'/{keys}',
        headers=headers,
        json=data)
    if resp.status_code in [201, 204]:
        logger.info('上傳 SECRET 成功')
    else:
        logger.critical('上傳 SECRET 失敗。')


def update_cookie(cookie: dict = None):
    # requests
    cookies = ''
    headers = {
        'user-agent': UA['google chrome']
        }

    r = requests.get('https://myaccount.books.com.tw/myaccount/myaccount/getReorder',
                 cookies=cookies,headers=headers)
    # with open('test.html', 'w', encoding='utf8') as f:
    #     f.write(r.text)
    # print(r.text)

    pass

def check_in():
    pass
