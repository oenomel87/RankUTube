import requests
import configparser
import sys
import dateutil.parser
from . import config, db_conn
from .entity.channel import Channel

def send_request(page_token = None):
    params = {
        'part': 'snippet',
        'type': 'channel',
        'key': config.CONFIG['API_KEY']
    }

    if page_token is not None:
        params['pageToken'] = page_token

    req = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
    req.raise_for_status()
    return req.json()

def parse_result(result, session):
    items = result['items']
    for i in range(len(items)):
        snippet = items[i]['snippet']
        print(snippet['channelId'] + ' ' + snippet['title'])
        if is_new_channel(snippet['channelId'], session):
            add_channel(snippet, session)
    return result['nextPageToken'] if 'nextPageToken' in result else None

def add_channel(snippet, session):
    channel = Channel(channel_id=snippet['channelId'], title=snippet['title'], 
        published_at=dateutil.parser.parse(snippet['publishedAt']))
    session.add(channel)

def is_new_channel(channel_id, session):
    count =  session.query(Channel).filter_by(channel_id=channel_id).count()
    return count == 0

def crawling():
    limit = 0
    page_token = None
    db_session = db_conn.session()
    try:
        while True:
            response = send_request(page_token)
            page_token = parse_result(response, db_session)
            if page_token is None or limit > 100:
                break
            limit += 1
        db_session.commit()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        db_session.rollback()
    finally:
        db_session.close()