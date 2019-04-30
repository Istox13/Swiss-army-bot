import urllib.request
import os


def download(url, name):
    if not os.path.exists('Music'):
        os.system('mkdir Music')
        
    path = 'Music/' + name + '.mp3'

    if not os.path.exists(path):
        try:
            urllib.request.urlretrieve(url, path)
        except AttributeError:
            name = str(hash(url))
            path = 'Music/' + name + '.mp3'
            urllib.request.urlretrieve(url, path)
    print('OK')

    return path

import json, requests

class VK_lib:
    
    def get_name(id=463892171):
        s = requests.post("https://vrit.me/action.php",data={
            "method": "audio.get",
            "count": 1000000000,
            "offset": 0,
            "user_id": id})

        s = json.loads(s.text)
        return s['title']

    def get_count(self, id=463892171):
        s = requests.post("https://vrit.me/action.php",data={
            "method": "audio.get",
            "count": 1000000000,
            "offset": 0,
            "user_id": id})

        s = json.loads(s.text)

        return s['count']

    def get_dict(id=463892171):
        s = requests.post("https://vrit.me/action.php",data={
            "method": "audio.get",
            "count": 1000000000,
            "offset": 0,
            "user_id": id})

        s = json.loads(s.text)
        music = dict()
        ms = s['html'].split('\n')
        n_ms = list()
        while ms:
            if len(ms) >= 13:
                n_ms.append(ms[:13])
            ms = ms[13:]
        error_url = 0
        for n, i in enumerate(n_ms):
            composition = dict()
            composition['artist'] = i[11].strip().split('<div class="artist">')[1].split('<')[0]
            composition['name'] = i[10].strip().split('<div class="title">')[1].split('<')[0]
            composition['image'] =  i[1].strip().split('url(')[1].split("'")[1]
            if composition['image'][:8] != 'https://':
                composition['image'] = 'None'
            composition['long'] = i[9].strip().split('<div class="duration">')[1].split('<')[0]
            composition['url'] = i[2].strip().split('<div class="play" data="')[1].split('"')[0]

            if composition['url']:
                music[str(n - error_url)] = composition
            else:
                error_url += 1
        return music


import pygame

class Player:
    def __init__(self):
        #Определяе какой файл проигрывать
        #music_file = "C://Users/Istox13/Downloads/1.mp3"

        #Устанавливаем параметры Микшера.
        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 2     # 1 is mono, 2 is stereo
        buffer = 2048    # number of samples (experiment to get right sound)
        #Инициализируем микшер.
        pygame.mixer.init(freq, bitsize, channels, buffer)

        #Устанавливаем грокость - максимум.
        pygame.mixer.music.set_volume(1.0)
    
    def set_volume(self, n):
        pygame.mixer.music.set_volume(n)

    def play_music(self, music_file):
        try:
            clock = pygame.time.Clock()
            try:
                #Загружае файл.
                pygame.mixer.music.load(music_file)
                print("Music file %s loaded!" % music_file)
            except pygame.error:
                #Ловим ошибки загрузки
                print("File %s not found! (%s)" % (music_file, pygame.get_error()))
                return
            #Проигрываем
            pygame.mixer.music.play()
            #Ожидаем завершение проигрывания
            
        
        except KeyboardInterrupt:
                # Если пользователь прервёт проигрывание.
                #Завершаем проигрывание, как положено.
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.stop()
                raise SystemExit

    def get_busy(self):
        return pygame.mixer.music.get_busy()
        
    def pause(self):
        pygame.mixer.music.pause()
    
    def stop(self):
        pygame.mixer.music.stop()

    def unpause(self):
        pygame.mixer.music.unpause()