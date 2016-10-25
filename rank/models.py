# -*- coding:utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

import datetime
import json

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    info_url = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    artificial_person = models.CharField(max_length=255)
    registered_capital = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    registered_date = models.DateField(blank=True, null=True)
    industry = models.CharField(max_length=255)
    registered_number = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    organization_number = models.CharField(max_length=255)
    operation_period = models.CharField(max_length=255)
    registered_authority = models.CharField(max_length=255)
    approved_date = models.DateField(blank=True, null=True)
    credit_number = models.CharField(max_length=255)
    registered_location = models.CharField(max_length=255)
    business_scope = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=255)
    market_value = models.CharField(max_length=255)
    sales_amount_last_year = models.CharField(max_length=255)
    sales_profit_last_year = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    major_business = models.TextField()
    major_product = models.CharField(max_length=255)
    company_copyright = models.TextField()
    company_copyright_score = models.FloatField()
    company_patent = models.TextField()
    company_patent_score = models.FloatField()
    company_competition = models.TextField()
    company_competition_score = models.FloatField()
    company_conference = models.TextField()
    company_conference_score = models.FloatField()
    company_loophole = models.TextField()
    company_loophole_score = models.FloatField()
    company_honor = models.TextField()
    company_honor_score = models.FloatField()
    company_market_share = models.TextField()
    company_market_share_score = models.FloatField()
    company_new_product = models.TextField()
    company_new_product_score = models.FloatField()
    company_award = models.TextField()
    company_award_score = models.FloatField()
    company_industry_coverage = models.TextField()
    company_ceo = models.CharField(max_length=255)
    company_tech_team = models.TextField()
    company_employees_number = models.CharField(max_length=255)
    company_employees_number_score = models.FloatField()
    company_postgraduate = models.CharField(max_length=255)
    company_undergraduate = models.CharField(max_length=255)
    company_research_percent = models.CharField(max_length=255)
    company_research_percent_score = models.FloatField()
    company_on_market = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    # 解决日期不能json编码的问题
    class CJsonEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime.datetime):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(obj, datetime.date):
                return obj.strftime("%Y-%m-%d")
            else:
                return json.JSONEncoder.default(self, obj)

    # 解决get方法获得的具体实例不能json编码的问题
    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        dic = {}
        for attr in fields:
            dic[attr] = getattr(self,attr)
        import json
        return json.dumps(dic, cls=self.CJsonEncoder)


    class Meta:
        managed = False
        db_table = 'company'


class Bid(models.Model):
    name = models.CharField(max_length=255)
    person = models.CharField(max_length=255)
    date = models.DateField()
    company = models.ForeignKey(Company)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'bid'


class Copyright(models.Model):
    name = models.CharField(max_length=255)
    shorthand = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    classification = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    company = models.ForeignKey(Company)


    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'copyright'



class Investment(models.Model):
    name = models.CharField(max_length=255)
    artificial_person = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    company = models.ForeignKey(Company)


    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'investment'


class Management(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    company = models.ForeignKey(Company)


    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'management'


class Shareholder(models.Model):
    name = models.CharField(max_length=255)
    artificial_person = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    company = models.ForeignKey(Company)


    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'shareholder'
