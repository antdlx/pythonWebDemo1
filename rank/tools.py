#-*- coding:utf-8 -*-
import datetime
import json


class MyMath:
    def UpDivision(self,a,b):
        a = int(a)
        b = int(b)
        return int((a+b-1)/b)

        # 解决日期不能json编码的问题
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)