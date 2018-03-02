import json;

class Music(object):
    def __init__(self, media_id, song_id, title, status, url, play_url = '', singer = [], album = {}, data = {}):
        self.media_id = media_id;
        self.song_id = song_id;
        self.title = title;
        self.singer = singer;
        self.album = album;
        self.data = data;
        self.status = 1 if status else 0;
        self.url = url;
        self.play_url = play_url;
    
    def toDict(self):
        singer = [];
        for singe in self.singer:
            singer.append({
                'id': singe['id'],
                'mid': singe['mid'],
                'name': singe['name']
            });
        
        return {
            'media_id': self.media_id,
            'song_id': self.song_id,
            'url': self.url,
            'play_url': self.play_url,
            'title': self.title,
            'singer': singer,
            'album': {
                'id': self.album['id'],
                'mid': self.album['mid'],
                'name': self.album['name'],
            },
            'data': self.data,
            'status': self.status
        };

class MusicList(object): 
    def __init__(self):
        self.music_list = [];

    def add(self, music):
        assert isinstance(music, Music);
        self.music_list.append(music);
    
    def __getitem__(self, index):
        return self.music_list[index];
    
    def toList(self):
        json = [];
        for music in self.music_list:
            json.append(music.toDict());
        return json;

    def toJson(self):
        return json.dumps(self.toList());
            
    def __str__(self):
        return self.toJson();
