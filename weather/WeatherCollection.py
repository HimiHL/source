# encoding=utf-8
from bs4 import BeautifulSoup

class WeatherCollection(object):
        def __init__(self, weather_data):
            self.weather_infos_ = weather_data

        @property
        def data(self):
            soup = BeautifulSoup(self.weather_infos_, 'lxml')
            div_7d = soup.find("div", {'id': "7d"})
            weather_infos = []
            if div_7d:
                day_item = div_7d;
                for day_index in range(1, 8):
                    # 获取每日的天气条目
                    day_item = day_item.find_next("li", {'class': 'skyid'})
                    # 获取当前日期
                    day_des = day_item.find("h1").text
                    # 获取天气状况
                    day_wea = day_item.find("p", {"class": "wea"}).text
                    # 获取最低温度，将单位℃过滤掉
                    day_temperature_low = day_item.find("p", {"class": "tem"}).find("i").text.replace('℃', '');
                    # 获取最高温度
                    # 做if是因为有时候获取当天的天气时，只有最低气温，没有最高气温
                    if day_item.find("p", {"class": "tem"}).find("span") is not None:
                        day_temperature_high = day_item.find("p", {"class": "tem"}).find("span").text.replace('℃', '');
                    else:
                        day_temperature_high = day_temperature_low

                    weather_infos.append({
                        'day': day_des,
                        'high': day_temperature_high,
                        'low': day_temperature_low,
                        'weather': day_wea
                    })
            return weather_infos