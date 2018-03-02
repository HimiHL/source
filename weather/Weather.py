# -*- coding: utf-8 -*-
import os
import requests
from ..ExceptionHandler import ExceptionHandle;
from .WeatherCollection import WeatherCollection;

class Weather(object):
    def getCityCode(self, province, city, county = None):
        ''' 获取城市ID '''
        def get_city_ids():
            city_id_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "citys.py")
            city_ids = {}
            with open(city_id_path, encoding="utf-8") as f:
                for line in f:
                    city_id, county, city, province = line.split(",")
                    key = province.strip() + city.strip()
                    if key in city_ids.keys():
                        city_ids[key].append(
                            {
                                'city_id': city_id.strip(),
                                'county': county.strip()
                            }
                        );
                    else:
                        city_ids[key] = [{
                            'city_id': city_id.strip(),
                            'county': county.strip()
                        }];
            return city_ids

        city_ids = get_city_ids()
        key = province.strip() + city.strip()
        
        if key in city_ids:
            return city_ids[key]
        raise ExceptionHandle(code=900001, message='城市不存在');

    def getWeather(self, city_id):
        ''' 获取天气 '''
        url = "http://www.weather.com.cn/weather/{city_id}.shtml".format(city_id=city_id)
        r = requests.get(url)
        # 指定编码
        r.encoding = r.apparent_encoding;
        if r.status_code == 200:
            # 将获取到的网页HTML传入
            weather = WeatherCollection(r.text)
            if not weather.data:
                raise ExceptionHandle(code=900002, message='天气查询异常');
        return weather.data;


    