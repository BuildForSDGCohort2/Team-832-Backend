from django.contrib import admin
#
#from .models import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Account



class AccountAdmin(UserAdmin):
	list_display = ('email','username', 'phoneNumber', 'idNumber', 'date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)



# Register your models here.

#admin.site.register(Profile)

