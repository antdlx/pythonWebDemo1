#coding=utf8
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from .models import Company
from Configs import Configs
from tools import MyMath,CJsonEncoder
from django.shortcuts import render

# Create your views here.
configs = Configs()
myMath = MyMath()

def index(request):
    return HttpResponse(u"Welcome!")

def company(request):

    configs.TOTAL_PAGE_NUM = myMath.UpDivision(Company.objects.count(),configs.PERPAGE_DATA_NUM)
    data = Company.objects.all().values()
    dict_list=[]
    if configs.TOTAL_PAGE_NUM == 1:
        for i in range(0,int(len(data)-1)):
            dict_list.append(data[i])
    else:
        for i in range(0,int(configs.PERPAGE_DATA_NUM)):
            dict_list.append(data[i])

    dict_list = json.dumps(dict_list,cls=CJsonEncoder)

    return render_to_response('CompanySearch.html', {'data_list':json.dumps(dict_list)
        ,'perpage_data_num':configs.PERPAGE_DATA_NUM
        ,'total_page_num':configs.TOTAL_PAGE_NUM
        ,'current_page_num':configs.CURRENT_PAGE_NUM})
    # return HttpResponse(dict_list,content_type="application/json")

@csrf_exempt
def getPages(request):
    wantPageNum = request.POST.get('wantPageNum',1)
    wantPageNum = int(wantPageNum)
    selecta = request.POST.get('selecta',configs.SELECTA)
    configs.SELECTA = selecta
    selectb = request.POST.get('selectb',configs.SELECTB)
    configs.SELECTB = selectb
    selectc = request.POST.get('selectc',configs.SELECTC)
    configs.SELECTC = selectc
    keyword = request.POST.get('keyword','')

    qs_data = Company.objects.all().order_by("name")
    num = -1

    if selecta == "a2":
        qs_data = qs_data.filter(type__icontains="上市").exclude(type__icontains="非上市")
    if selecta == "a3":
        qs_data = qs_data.filter(type__icontains="非上市")

    if selectb != "b1":
        qs_data = qs_data.filter(status__icontains=selectb)

    if selectc != "name":
        qs_data = qs_data.order_by(selectc)

    if len(keyword) > 0:
        qs_data = qs_data.filter(name__icontains=keyword)

    configs.TOTAL_PAGE_NUM = myMath.UpDivision(qs_data.count(),configs.PERPAGE_DATA_NUM)

    qs_data = qs_data.values()
    dict_list = []

    if wantPageNum < configs.TOTAL_PAGE_NUM:
        for i in range(int((wantPageNum-1)*configs.PERPAGE_DATA_NUM),int(wantPageNum*configs.PERPAGE_DATA_NUM-1)):
            dict_list.append(qs_data[i])
    else:
        for i in range(int((wantPageNum-1)*configs.PERPAGE_DATA_NUM),int(len(qs_data)-1)):
            dict_list.append(qs_data[i])

    dict_list = json.dumps(dict_list,cls=CJsonEncoder)
    data = {
        "data":dict_list,
        "total_page_num":configs.TOTAL_PAGE_NUM,
    }

    return HttpResponse(json.dumps(data),content_type="application/json")


