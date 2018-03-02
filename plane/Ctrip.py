import re, os, json, requests;
from .Plane import Plane;

class Ctrip(object):
    
    def getAirCitys(self):
        ''' 获取机票所有城市的代码 '''
        url = 'http://webresource.c-ctrip.com/code/cquery/resource/address/flight/flight_new_poi_gb2312.js?CR_2017_07_18_00_00_00'
        response = requests.get(url,verify=False)
        station = re.findall(u'([\u4e00-\u9fa5]+)\(([A-Z]+)\)', response.text)
        return dict(station)


    def getAirTicket(self, dCity, aCity, Date):
        ''' 获取机票列表 '''
        headers = {
            "Cookie":"__utma=1.648580680.1500052197.1500052197.1500052197.1; __utmz=1.1500052197.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; StartCity_Pkg=PkgStartCity=2; _abtest_userid=b2d8ec09-8300-49f5-8c56-e5955eaebf55; adscityen=Shanghai; DomesticUserHostCity=SHA|%c9%cf%ba%a3; appFloatCnt=3; manualclose=1; _gat=1; Union=SID=155952&AllianceID=4897&OUID=baidu81|index|||; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; _bfa=1.1500052197098.egn3q.1.1500391644124.1500450359041.3.22; _bfs=1.3; page_time=1500052199151%2C1500052201106%2C1500052253071%2C1500052266599%2C1500052737639%2C1500053169759%2C1500053269047%2C1500053304153%2C1500391645891%2C1500391646865%2C1500391653279%2C1500391706616%2C1500391781672%2C1500391867587%2C1500391895364%2C1500392129113%2C1500392312502%2C1500392677979%2C1500450360502%2C1500450527168%2C1500450552188; _RF1=112.64.216.79; _RSG=6Ba6XNJ5wCACiIoqsdEcXA; _RGUID=a33a1535-e11a-42c6-a866-3a7db4c92b0c; _ga=GA1.2.648580680.1500052197; _gid=GA1.2.1686685369.1500391650; traceExt=campaign=CHNbaidu81&adid=index; __zpspc=9.4.1500450554.1500450554.1%231%7Cbaidu%7Ccpc%7Cbaidu81%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _jzqco=%7C%7C%7C%7C1500391649757%7C1.719992437.1500052197549.1500450529881.1500450554792.1500450529881.1500450554792.undefined.0.0.20.20; _bfi=p1%3D100101991%26p2%3D101027%26v1%3D22%26v2%3D21; MKT_Pagesource=PC;",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        }
        url = ("http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1={}&ACity1={}&SearchType=S&DDate1={}&IsNearAirportRecommond=0&LogToken=0dc7fd99662349069c123f0a8bfcae95&rk=7.387068566272421154925&CK=51BF6E070FF329F1DDD90CEF097B4B86&r=0.5811166470511521823610").format(dCity,aCity,Date)
        try:
            r = requests.get(url,headers = headers,verify=False)
        except:
            raise ExceptionHandle(code=0, message="请求异常");
        # 获取机票详情
        airline_tickets = r.json()['fis'];
        airline_company = r.json()['als'];
        # 格式化机票数据
        ticket_data = Plane(airline_tickets, airline_company).format();
        return ticket_data;