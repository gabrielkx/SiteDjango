from django.contrib import admin
from subscriptions.models import Subscription
from django.utils.timezone import now

class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display= ('name' ,'email', 'phone', 'cpf', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone' , 'cpf', 'created_at' , 'paid')
    list_filter = ('created_at', 'paid')
    def subscribed_today(self,obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'Inscrito Hoje?'
    subscribed_today.boolean = True
admin.site.register(Subscription,SubscriptionModelAdmin)
