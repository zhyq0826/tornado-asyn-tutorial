
from concurrent.futures import ThreadPoolExecutor
import requests


def main():
    baidu_url = 'http://baidu.com'
    google_url = 'http://google.com'

    with ThreadPoolExecutor(max_workers=2) as e:
        future1 = e.submit(requests.get, baidu_url)
        future2 = e.submit(requests.get, google_url)
        print future1.result()
        print future2.result()



if __name__ == '__main__':
    main()