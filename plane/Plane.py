import json;

class Plane(object):
    def __init__(self, tickets, companys):
        self.tickets = tickets;
        self.companys = companys;
    
    def format(self):
        final_tickets = [];
        for ticket in self.tickets:
            final_tickets.append({
                'company': {
                    'code': ticket['alc'], # 航空公司代码
                    'name': self.companys[ticket['alc']] # 航空公司名称
                },
                'depart': {
                    'city_code': ticket['dcc'],
                    'city_name': ticket['dcn'],
                    'airport_code': ticket['dpc'],
                    'airport_name': ticket['dpbn'],
                    'station_floor': ticket['dsmsn'],
                    'time': ticket['dt']
                },
                'arrive': {
                    'city_code': ticket['acc'], # 城市代码
                    'city_name': ticket['acn'], # 城市名称
                    'airport_code': ticket['apc'], # 机场代码
                    'airport_name': ticket['apbn'], # 机场名称
                    'station_floor': ticket['asmsn'], # 站楼
                    'time': ticket['at'] # 时间
                },
                'price': ticket['lp'], # 票价
                'fn': ticket['fn'], # 班次
                'time_rate': json.loads(ticket['confort'])['HistoryPunctualityArr'] # 准点率
            });
        
        return final_tickets;