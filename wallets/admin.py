from django.contrib import admin

from .models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("uuid", "balance", "created_at")
    search_fields = ("uuid",)
    ordering = ("-created_at",)
