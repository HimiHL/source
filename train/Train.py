# -*- coding:utf-8 -*-
from ..ExceptionHandler import ExceptionHandle;
from .stations import stations
from .TrainCollection import TrainCollection;
import requests

class Train(object):
        
    def getTicketsByName(self, from_station, to_station, date):
        ''' 传入起始和终点站点中文名称 '''
        # 获取起始站点对应的代码
        from_code = stations.get(from_station);
        # 获取起始站点对应的代码
        to_code = stations.get(to_station);
        # 拼装请求URL
        url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.' \
            'from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.\
            format(date, from_code, to_code)
        requests.packages.urllib3.disable_warnings() # 解决https验证报warning
        # 请求数据，获取JSON文本
        response = requests.get(url, verify=False)

        # 返回数据数组
        return TrainCollection(response.json()['data']).data;

    def getTicketsByCode(self, from_code, to_code, date):
        ''' 传入起始和终点站点的Code '''
        # 拼装请求URL
        url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.' \
            'from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.\
            format(date, from_code, to_code)
        requests.packages.urllib3.disable_warnings() # 解决https验证报warning
        # 请求数据，获取JSON文本
        response = requests.get(url, verify=False)

        # 返回数据数组
        return TrainCollection(response.json()['data']).data;

    def getStationCode(self, station_name):
        ''' 获取所有站点对应的代码 '''
        station_code = stations.get(station_name);
        if station_code is None:
            raise ExceptionHandle(code=900101, message='站点不存在');

        return station_code;

    def getStationName(self, station_code):
        ''' 获取代码对应的站点名称 '''
        station_name = list(stations.keys())[list(stations.values()).index(station_code)];

        if station_name is None:
            raise ExceptionHandle(code=900101, message='站点不存在');

        return station_name;