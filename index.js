const axios = require('axios');

let recursiveLimit = 10;
let recursiveDept = 0;

async function sendSearchRequest(pageToken) {
    const params = {
        part: 'snippet',
        type: 'channel',
        key: 'AIzaSyCFO16b_AB1coDIPiTR7hvX-rGYOYTVmts'
    }

    if(pageToken) {
        params.pageToken = pageToken;
    }
    
    try {
        const res = await axios.get(`https://www.googleapis.com/youtube/v3/search${setQuery(params)}`);
        if(res.status !== 200) {
            throw new Error(`Response status is ${res.status}`);
        }
        parseResult(res.data);
    } catch(err) {
        console.error(err);
    }
}

function setQuery(params) {
    const keys = Object.keys(params);
    let query = '';

    keys.forEach((key, index) => {
        query += `${index ? '&' : ''}${key}=${params[key]}`;
    });

    return query.length ? `?${query}` : '';
}

function parseResult(res) {
    console.log('============================');
    console.log(res.nextPageToken);
    res.items.forEach(item => console.log(item.snippet.channelId, item.snippet.title));
    if(recursiveDept < recursiveLimit) {
        recursiveDept++;
        sendSearchRequest(res.nextPageToken);
    }
}

sendSearchRequest();