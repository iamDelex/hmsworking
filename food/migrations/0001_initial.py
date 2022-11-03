# Generated by Django 4.0.4 on 2022-06-16 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default='meal.jpg', upload_to='meal')),
                ('price', models.IntegerField()),
                ('min_order', models.IntegerField(default=1)),
                ('max_order', models.IntegerField(default=20)),
                ('display', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Meal',
                'verbose_name_plural': 'Meals',
                'db_table': 'meal',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Shopcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('how_spicey', models.CharField(max_length=50)),
                ('order_no', models.CharField(max_length=50)),
                ('item_paid', models.BooleanField(default=False)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Shopcart',
                'verbose_name_plural': 'Shopcarts',
                'db_table': 'shopcart',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PaidOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('cart_no', models.CharField(blank=True, max_length=36, null=True)),
                ('payment_code', models.CharField(max_length=36)),
                ('paid_item', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=70)),
                ('postal_code', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PaidOrder',
                'verbose_name_plural': 'PaidOrders',
                'db_table': 'paidOrder',
                'managed': True,
            },
        ),
    ]
