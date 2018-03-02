# encoding=utf-8
from .stations import stations

class TrainCollection(object):
    
    def __init__(self, available_trains):
        self.availavle_trains = available_trains

    def getStationName(self, station_code):
        ''' 获取代码对应的站点名称 '''
        station_name = list(stations.keys())[list(stations.values()).index(station_code)];

        if station_name is None:
            raise ExceptionHandle(code=900101, message='站点不存在');

        return station_name;

    @property
    def data(self):
        trains = [];
        for train in self.availavle_trains['result']:
            item = train.split('|');
            trains.append({
                'code': item[3], # 车次ID
                'start': item[4], # 起站点名称
                'start_name': self.getStationName(item[4]),
                'end': item[5], # 终点站名称
                'end_name': self.getStationName(item[5]),
                'from': item[6], # 本次行程的起点站
                'to': item[7], # 本次行程的终点站
                'start_time': item[8], # 开始时间
                'arrive_time': item[9], # 到达时间
                'lishi': item[10], # 历时时间
                # 'can_web_buy': item[11], # 是否可以web购买
                'start_date': item[13], # 查询时间
                # 'gg': item[20] if item[20].strip() else 0, # 
                'gr': item[21] if item[21].strip() else 0, # 高级软卧
                'qt': item[22] if item[22].strip() else 0, # 其他
                'rw': item[23] if item[23].strip() else 0, # 软卧
                'rz': item[24] if item[24].strip() else 0, # 软座
                # 'tz': item[25] if item[25].strip() else 0, # 
                'wz': item[26] if item[26].strip() else 0, # 无座
                # 'yb': item[27] if item[27].strip() else 0, # 
                'yw': item[28] if item[28].strip() else 0, # 硬卧
                'yz': item[29] if item[29].strip() else 0, # 硬座
                'ze': item[30] if item[30].strip() else 0, # 二等座
                'zy': item[31] if item[31].strip() else 0, # 一等座
                'swz': item[32] if item[32].strip() else 0, # 商务座
                'srrb': item[33] if item[33].strip() else 0 # 动软
            });
        return trains;
