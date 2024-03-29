# Generated by Django 4.2.4 on 2023-08-21 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remaining_installment', models.CharField(max_length=20)),
                ('installment', models.CharField(max_length=20)),
                ('create_date', models.DateField()),
                ('due_date', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DebtCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('penalty_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('invalid_date', models.CharField(max_length=20)),
                ('valid_date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=50)),
                ('e_mail', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rd_installment', models.CharField(max_length=20)),
                ('pay_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pay_date', models.DateField()),
                ('ip', models.GenericIPAddressField()),
                ('debt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debtPaymentSystem.debt')),
            ],
        ),
        migrations.AddField(
            model_name='debt',
            name='debt_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debtPaymentSystem.debtcategory'),
        ),
        migrations.AddField(
            model_name='debt',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debtPaymentSystem.person'),
        ),
    ]
