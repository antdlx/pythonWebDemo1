# coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    name = models.CharField('公司名', max_length=255)
    phone = models.CharField('电话', blank=True, max_length=255)
    email = models.CharField('邮箱', blank=True, max_length=255)
    info_url = models.CharField('数据来源链接', blank=True, max_length=255)
    website = models.CharField('公司官网', blank=True, max_length=255)
    location = models.CharField('地点', blank=True, max_length=255)
    artificial_person = models.CharField('法人', blank=True, max_length=255)
    registered_capital = models.CharField('注册地点', blank=True, max_length=255)
    status = models.CharField('公司状态', blank=True, max_length=255)
    registered_date = models.DateField('注册时间', blank=True, null=True)
    industry = models.CharField('行业', blank=True, max_length=255)
    registered_number = models.CharField('工商注册号', blank=True, max_length=255)
    type = models.CharField('企业类型', blank=True, max_length=255)
    organization_number = models.CharField('组织机构代码', blank=True, max_length=255)
    operation_period = models.CharField('营业期限', blank=True, max_length=255)
    registered_authority = models.CharField('等级机关', max_length=255)
    approved_date = models.DateField('核准日期', blank=True, null=True)
    credit_number = models.CharField('统一信用代码', blank=True, max_length=255)
    registered_location = models.CharField('注册地址', max_length=255)
    business_scope = models.TextField('经营范围', blank=True, null=True)
    country = models.CharField('国家', blank=True, max_length=255)
    market_value = models.TextField('市值或估值', blank=True, max_length=255)
    sales_amount_last_year = models.TextField('上年度销售收入', blank=True)
    sales_profit_last_year = models.TextField('上年度利润', blank=True)
    introduction = models.TextField('官方简介', blank=True)
    major_business = models.TextField('公司业务', blank=True)
    major_product = models.TextField('产品或服务', blank=True)
    company_copyright = models.TextField('软件著作权', blank=True)
    company_copyright_score = models.FloatField('著作权打分', blank=True)
    company_patent = models.TextField('公司专利', blank=True)
    company_patent_score = models.FloatField('专利打分', blank=True)
    company_competition = models.TextField('网络安全技术对抗赛情况', blank=True)
    company_competition_score = models.FloatField('技术对抗赛情况打分', blank=True)
    company_conference = models.TextField('安全大会演示情况', blank=True)
    company_conference_score = models.FloatField('安全大会演示情况打分', blank=True)
    company_loophole = models.TextField('发布漏洞情况', blank=True)
    company_loophole_score = models.FloatField('发布漏洞情况打分', blank=True)
    company_honor = models.TextField('公司资质荣誉', blank=True)
    company_honor_score = models.FloatField('公司资质荣誉打分', blank=True)
    company_market_share = models.TextField('市场占有率', blank=True)
    company_market_share_score = models.FloatField('市场占有率打分', blank=True)
    company_new_product = models.TextField('新产品发布情况', blank=True)
    company_new_product_score = models.FloatField('新产品发布情况打分', blank=True)
    company_award = models.TextField('公司所获奖励', blank=True)
    company_award_score = models.FloatField('公司奖励情况打分', blank=True)
    company_industry_coverage = models.TextField('行业覆盖率', blank=True)
    company_ceo = models.TextField('创始人/CEO', blank=True, max_length=255)
    company_tech_team = models.TextField('技术团队情况', blank=True)
    company_employees_number = models.TextField('公司员工数', blank=True)
    company_employees_number_score = models.FloatField('公司员工数打分', blank=True)
    company_postgraduate = models.TextField('硕士以上员工人数', blank=True)
    company_undergraduate = models.TextField('本科以上员工人数', blank=True)
    company_research_percent = models.TextField('研发人员比例', blank=True)
    company_research_percent_score = models.FloatField('研发人员比例打分', blank=True)
    company_on_market = models.TextField('是否上市(是/否)', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'company'

    @property
    def bids(self):
        return Bid.objects.filter(company=self.id)

    @property
    def copyrights(self):
        return Copyright.objects.filter(company=self.id)

    @property
    def investments(self):
        return Investment.objects.filter(company=self.id)

    @property
    def managements(self):
        return Management.objects.filter(company=self.id)

    @property
    def shareholders(self):
        return Shareholder.objects.filter(company=self.id)


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
