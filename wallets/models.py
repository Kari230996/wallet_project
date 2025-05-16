from django.db import models
import uuid


class Wallet(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Уникальный идентификатор"
    )
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name="Баланс"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Кошелёк"
        verbose_name_plural = "Кошельки"

    def __str__(self):
        return f"Кошелёк {self.uuid}"
