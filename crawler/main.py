import requests

def send_request(page_token = None):
    params = {
        'part': 'snippet',
        'type': 'channel',
        'key': 'AIzaSyCFO16b_AB1coDIPiTR7hvX-rGYOYTVmts'
    }

    if page_token is not None:
        params['pageToken'] = page_token

    req = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
    req.raise_for_status()
    return req.json()

def parse_result(result):
    items = result['items']
    for i in range(len(items)):
        snippet = items[i]['snippet']
        print(snippet['channelId'] + ' ' + snippet['title'])
    return result['nextPageToken'] if 'nextPageToken' in result else None

def crawling():
    limit = 0
    page_token = None
    while True:
        response = send_request(page_token)
        page_token = parse_result(response)
        if page_token is None or limit > 100:
            break
        limit += 1

crawling()