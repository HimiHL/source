import requests;
import json;
from time import time;
from random import random;
from .Music import Music, MusicList;

class QQMusic(object):
    def search(self, key_word, page = 1, pagesize = 20):
        ''' 根据关键词查找歌曲 '''
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp';
        url += '?new_json=1&aggr=1&cr=1&flag_qc=0&p=%d&n=%d&w=%s' % (page, pagesize, key_word)
        
        try:
            result = requests.get(url);
        except:
            raise ExceptionHandle(code=0, message="请求异常");
            
        data_list = json.loads(result.text[9:-1])['data']['song']['list'];
        song_list = MusicList();
        for line in data_list:
            media_id = line['file']['media_mid'];
            song_id = line['mid'];
            title = line['title'];
            singer = line['singer'];
            album = line['album'];
            status = line['action']['msg'] != 3;
            music = Music(
                media_id = media_id,
                song_id = song_id,
                title = title,
                singer = singer,
                album = album,
                status = status,
                url = 'http://i.y.qq.com/v8/playsong.html?ADTAG=newyqq.song&songmid=%s#webchat_redirect' % format(song_id),
                play_url =  'http://isure.stream.qqmusic.qq.com/C100'+media_id+'.m4a?fromtag=32' 
            )
            song_list.add(music);
        return song_list;
    
    def _get_filename(self, media_id):
        return "M800%s.mp3" % media_id;

    def _get_vkey(self, song_id, media_id, guid):
        filename = self._get_filename(media_id);
        url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?';
        url += 'format=json&platform=yqq&cid=205361747&songmid=%s&filename=%s&guid=%s' \
            % (song_id, filename, guid)
        result = requests.get(url);
        return json.loads(result.text)['data']['items'][0]['vkey'];
    
    def get_music_url(self, song_id, media_id):
        guid = int(random() * 2147483647) * int(time() * 1000) % 10000000000
        try:
            vkey = self._get_vkey(song_id, media_id, guid);
        except json.decoder.JSONDecoderError:
            vkey = self._get_vkey(song_id, media_id, guid);
        url = 'http://dl.stream.qqmusic.qq.com/%s?' % self._get_filename(media_id);
        return  url + 'vkey=%s&guid=%s' % (vkey, guid)