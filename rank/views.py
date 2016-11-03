# coding=utf8
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from .models import Company
from .tools import MyMath, CJsonEncoder
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Configs:
    # 每页显示多少item
    # PERPAGE_DATA_NUM = 8
    # 一共有多少页
    # TOTAL_PAGE_NUM = -1
    # 现在是多少页
    # CURRENT_PAGE_NUM = 1
    # 选择器
    SELECTA = "a1"
    SELECTB = "b1"
    SELECTC = "c1"


# Create your views here.
configs = Configs()
myMath = MyMath()


def index(request):
    return HttpResponseRedirect('/search')


def search(request):
    return render_to_response('search.html')


def list(request):
    search = request.GET['search']
    companies = Company.objects.filter(name__icontains=search)
    return render_to_response('list.html', {
        'companies': companies
    })


def company(request, id):
    company = Company.objects.get(id=id)
    return render_to_response('company.html', {
        'company': company
    })


def rank(request):
    selecta = request.GET.get('selecta', configs.SELECTA)
    #记录上次的选择
    # configs.SELECTA = selecta
    selectb = request.GET.get('selectb', configs.SELECTB)
    # configs.SELECTB = selectb
    selectc = request.GET.get('selectc', configs.SELECTC)
    # configs.SELECTC = selectc
    keyword = request.GET.get('search', '')
    page_num = request.GET.get('page', 1)
    page_num = int(page_num)

    qs_data = Company.objects.all().order_by("name")

    if selecta == "a2":
        qs_data = qs_data.filter(type__icontains="上市").exclude(type__icontains="非上市")
    if selecta == "a3":
        qs_data = qs_data.filter(type__icontains="非上市")

    if selectb == "b2":
        qs_data = qs_data.filter(status__icontains="开业")
    if selectb == "b3":
        qs_data = qs_data.filter(status__icontains="存续")

    if selectc == "c1":
        qs_data = qs_data.order_by("name")
    if selectc == "c2":
        qs_data = qs_data.order_by("score")
    if selectc == "c3":
        qs_data = qs_data.order_by("registered_date")
    if selectc == "c4":
        qs_data = qs_data.order_by("registered_capital")


    if len(keyword) > 0:
        qs_data = qs_data.filter(name__icontains=keyword)

    paginator = Paginator(qs_data, 10)
    try:
        page_content = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_content = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_content = paginator.page(paginator.num_pages)

    return render_to_response('rank.html', {'data_list': page_content
        , 'select_a': selecta, 'select_b': selectb, 'select_c': selectc
                                            ,'request':request})


# @csrf_exempt
# def getPages(request):
#     wantPageNum = request.POST.get('wantPageNum', 1)
#     wantPageNum = int(wantPageNum)
#     selecta = request.POST.get('selecta', configs.SELECTA)
#     configs.SELECTA = selecta
#     selectb = request.POST.get('selectb', configs.SELECTB)
#     configs.SELECTB = selectb
#     selectc = request.POST.get('selectc', configs.SELECTC)
#     configs.SELECTC = selectc
#     keyword = request.POST.get('keyword', '')
#
#     qs_data = Company.objects.all().order_by("name")
#     num = -1
#
#     if selecta == "a2":
#         qs_data = qs_data.filter(type__icontains="上市").exclude(type__icontains="非上市")
#     if selecta == "a3":
#         qs_data = qs_data.filter(type__icontains="非上市")
#
#     if selectb != "b1":
#         qs_data = qs_data.filter(status__icontains=selectb)
#
#     if selectc != "name":
#         qs_data = qs_data.order_by(selectc)
#
#     if len(keyword) > 0:
#         qs_data = qs_data.filter(name__icontains=keyword)
#
#     configs.TOTAL_PAGE_NUM = myMath.UpDivision(qs_data.count(), configs.PERPAGE_DATA_NUM)
#
#     qs_data = qs_data.values()
#     dict_list = []
#
#     if wantPageNum < configs.TOTAL_PAGE_NUM:
#         for i in range(int((wantPageNum - 1) * configs.PERPAGE_DATA_NUM),
#                        int(wantPageNum * configs.PERPAGE_DATA_NUM - 1)):
#             dict_list.append(qs_data[i])
#     else:
#         for i in range(int((wantPageNum - 1) * configs.PERPAGE_DATA_NUM), int(len(qs_data) - 1)):
#             dict_list.append(qs_data[i])
#
#     dict_list = json.dumps(dict_list, cls=CJsonEncoder)
#     data = {
#         "data": dict_list,
#         "total_page_num": configs.TOTAL_PAGE_NUM,
#     }
#
#     return HttpResponse(json.dumps(data), content_type="application/json")
