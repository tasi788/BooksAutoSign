from datetime import datetime, timedelta, timezone
import logging
import os
import requests
from nacl import encoding, public
from base64 import b64encode
import sys
from fake_useragent import UserAgent
from json import JSONDecodeError

tz = timezone(timedelta(hours=+8))
today = datetime.now(tz)
logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

GH_REPO = os.getenv('GH_REPO')
GH_TOKEN = os.getenv('GH_TOKEN')
COOKIES = os.getenv('BOOKS_COOKIE', None)
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
BOOKS_ID = os.getenv('BOOKS_ID')
BOOKS_PWD = os.getenv('BOOKS_PWD')
UA = UserAgent()


class Bot:
    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f'https://api.telegram.org/bot{self.token}'

    def sendMessage(self, text: str):
        r = requests.post(self.api_url + '/sendMessage',
                          json={
                              'chat_id': self.chat_id,
                              'text': text,
                              'parse_mode': 'html'
                          })

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


def do_check(cookie: dict = None):
    if not COOKIES:
        logger.fatal('找不到餅乾。')
        sys.exit(1)
    bot = Bot(BOT_TOKEN, CHAT_ID)
    cookies = eval(COOKIES)
    session = requests.Session()
    session = {'user-agent': UA['google chrome']}
    session.cookies = requests.utils.cookiejar_from_dict(cookies)
    r = session.get('https://myaccount.books.com.tw/myaccount/myaccount/getReorder', allow_redirects=False)
    # if r.status_code == 200
    if 'Set-Cookie' in r.headers.keys():
        new_cookies = r.headers['Set-Cookie']
        update_secret('cookies', new_cookies)
        # 塞進 secrets

    r = session.get('https://myaccount.books.com.tw/myaccount/reader/dailySignIn/?ru=P5zqo53d')

    status = None
    msg = ''
    try:
        status = r.json()['status']
        msg = r.json()['msg']
    except JSONDecodeError:
        logger.error('非預期內容')
        logger.error(r.text)

    text = ''
    if status == 'success':
        text += '博客來簽到成功！\n'
        text += '✅ ' + msg[5:]
    if status == None:
        text += '❌ 博客來簽到發生錯誤！'


if __name__ == '__main__':
    do_check()