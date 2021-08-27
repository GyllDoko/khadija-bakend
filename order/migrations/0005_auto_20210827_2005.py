# Generated by Django 3.1.5 on 2021-08-27 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210827_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('default_image', models.CharField(blank=True, max_length=10000, null=True)),
                ('quantity', models.SmallIntegerField(default=1, editable=False)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders_products', to='order.order')),
            ],
            options={
                'verbose_name': 'Produit commandé',
                'verbose_name_plural': 'Produits commandés',
            },
        ),
    ]
