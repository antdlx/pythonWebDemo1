from django.contrib import admin

# Register your models here.
from models import Company, Investment, Bid, Management, Copyright, Shareholder

class AdminCompany(admin.ModelAdmin):
    list_display = ('id', 'name','phone','email','info_url', 'location', 'artificial_person')
    search_fields = ('name',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(AdminCompany, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct

class AdminBid(admin.ModelAdmin):
    list_display = ('id', 'name','company')

class AdminInvestment(admin.ModelAdmin):
    list_display = ('id', 'name','company')

class AdminManagement(admin.ModelAdmin):
    list_display = ('id', 'name','company')

class AdminCopyright(admin.ModelAdmin):
    list_display = ('id', 'name','company')

class AdminShareholder(admin.ModelAdmin):
    list_display = ('id', 'name','company')

admin.site.register(Company, AdminCompany)
admin.site.register(Investment, AdminInvestment)
admin.site.register(Bid, AdminBid)
admin.site.register(Management, AdminManagement)
admin.site.register(Copyright, AdminCopyright)
admin.site.register(Shareholder, AdminShareholder)