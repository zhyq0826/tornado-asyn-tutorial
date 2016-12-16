import concurrent.futures
import requests

from log import log

ulrs = [
    'http://baidu.com',
    'http://sina.com.cn',
    'https://facebook.com',
]

#如果as completed的超时时间到了，但是future的时间未到，则直接报超时
#
#
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
    future_to_url = {e.submit(requests.get, url, timeout=3): url for url in ulrs}
    for future in concurrent.futures.as_completed(future_to_url, timeout=3):
        url = future_to_url[future]
        try:
            data = future.result().text
        except Exception as e:
            log(('%r generated an exception: %s') % (url, e))
        else:
            log('%r page is %d bytes' %(url, len(data)))
