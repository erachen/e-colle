# Generated by Django 2.1.1 on 2018-10-12 04:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0005_auto_20180509_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='css',
            field=models.CharField(blank=True, default='wstyle_css', max_length=50, null=True, verbose_name='Style préféré'),
        ),
        migrations.AlterField(
            model_name='creneau',
            name='heure',
            field=models.PositiveSmallIntegerField(choices=[(480, '8h00'), (510, '8h30'), (540, '9h00'), (570, '9h30'), (600, '10h00'), (630, '10h30'), (660, '11h00'), (690, '11h30'), (720, '12h00'), (750, '12h30'), (780, '13h00'), (810, '13h30'), (840, '14h00'), (870, '14h30'), (900, '15h00'), (930, '15h30'), (960, '16h00'), (990, '16h30'), (1020, '17h00'), (1050, '17h30'), (1080, '18h00'), (1110, '18h30'), (1140, '19h00'), (1170, '19h30')], default=24),
        ),
        migrations.AlterField(
            model_name='note',
            name='heure',
            field=models.PositiveSmallIntegerField(choices=[(480, '8h00'), (510, '8h30'), (540, '9h00'), (570, '9h30'), (600, '10h00'), (630, '10h30'), (660, '11h00'), (690, '11h30'), (720, '12h00'), (750, '12h30'), (780, '13h00'), (810, '13h30'), (840, '14h00'), (870, '14h30'), (900, '15h00'), (930, '15h30'), (960, '16h00'), (990, '16h30'), (1020, '17h00'), (1050, '17h30'), (1080, '18h00'), (1110, '18h30'), (1140, '19h00'), (1170, '19h30')], default=14),
        ),
        migrations.AlterField(
            model_name='ramassage',
            name='moisDebut',
            field=models.DateField(choices=[(datetime.date(2018, 9, 1), '九月 2018'), (datetime.date(2018, 10, 1), '十月 2018'), (datetime.date(2018, 11, 1), '十一月 2018'), (datetime.date(2018, 12, 1), '十二月 2018'), (datetime.date(2019, 1, 1), '一月 2019'), (datetime.date(2019, 2, 1), '二月 2019'), (datetime.date(2019, 3, 1), '三月 2019'), (datetime.date(2019, 4, 1), '四月 2019')], verbose_name='Début'),
        ),
        migrations.AlterField(
            model_name='ramassage',
            name='moisFin',
            field=models.DateField(choices=[(datetime.date(2018, 9, 1), '九月 2018'), (datetime.date(2018, 10, 1), '十月 2018'), (datetime.date(2018, 11, 1), '十一月 2018'), (datetime.date(2018, 12, 1), '十二月 2018'), (datetime.date(2019, 1, 1), '一月 2019'), (datetime.date(2019, 2, 1), '二月 2019'), (datetime.date(2019, 3, 1), '三月 2019'), (datetime.date(2019, 4, 1), '四月 2019')], verbose_name='Fin'),
        ),
        migrations.AlterField(
            model_name='semaine',
            name='lundi',
            field=models.DateField(choices=[(datetime.date(2018, 1, 1), '01 一月 2018'), (datetime.date(2018, 1, 8), '08 一月 2018'), (datetime.date(2018, 1, 15), '15 一月 2018'), (datetime.date(2018, 1, 22), '22 一月 2018'), (datetime.date(2018, 1, 29), '29 一月 2018'), (datetime.date(2018, 2, 5), '05 二月 2018'), (datetime.date(2018, 2, 12), '12 二月 2018'), (datetime.date(2018, 2, 19), '19 二月 2018'), (datetime.date(2018, 2, 26), '26 二月 2018'), (datetime.date(2018, 3, 5), '05 三月 2018'), (datetime.date(2018, 3, 12), '12 三月 2018'), (datetime.date(2018, 3, 19), '19 三月 2018'), (datetime.date(2018, 3, 26), '26 三月 2018'), (datetime.date(2018, 4, 2), '02 四月 2018'), (datetime.date(2018, 4, 9), '09 四月 2018'), (datetime.date(2018, 4, 16), '16 四月 2018'), (datetime.date(2018, 4, 23), '23 四月 2018'), (datetime.date(2018, 4, 30), '30 四月 2018'), (datetime.date(2018, 5, 7), '07 五月 2018'), (datetime.date(2018, 5, 14), '14 五月 2018'), (datetime.date(2018, 5, 21), '21 五月 2018'), (datetime.date(2018, 5, 28), '28 五月 2018'), (datetime.date(2018, 6, 4), '04 六月 2018'), (datetime.date(2018, 6, 11), '11 六月 2018'), (datetime.date(2018, 6, 18), '18 六月 2018'), (datetime.date(2018, 6, 25), '25 六月 2018'), (datetime.date(2018, 7, 2), '02 七月 2018'), (datetime.date(2018, 7, 9), '09 七月 2018'), (datetime.date(2018, 7, 16), '16 七月 2018'), (datetime.date(2018, 7, 23), '23 七月 2018'), (datetime.date(2018, 7, 30), '30 七月 2018'), (datetime.date(2018, 8, 6), '06 八月 2018'), (datetime.date(2018, 8, 13), '13 八月 2018'), (datetime.date(2018, 8, 20), '20 八月 2018'), (datetime.date(2018, 8, 27), '27 八月 2018'), (datetime.date(2018, 9, 3), '03 九月 2018'), (datetime.date(2018, 9, 10), '10 九月 2018'), (datetime.date(2018, 9, 17), '17 九月 2018'), (datetime.date(2018, 9, 24), '24 九月 2018'), (datetime.date(2018, 10, 1), '01 十月 2018'), (datetime.date(2018, 10, 8), '08 十月 2018'), (datetime.date(2018, 10, 15), '15 十月 2018'), (datetime.date(2018, 10, 22), '22 十月 2018'), (datetime.date(2018, 10, 29), '29 十月 2018'), (datetime.date(2018, 11, 5), '05 十一月 2018'), (datetime.date(2018, 11, 12), '12 十一月 2018'), (datetime.date(2018, 11, 19), '19 十一月 2018'), (datetime.date(2018, 11, 26), '26 十一月 2018'), (datetime.date(2018, 12, 3), '03 十二月 2018'), (datetime.date(2018, 12, 10), '10 十二月 2018'), (datetime.date(2018, 12, 17), '17 十二月 2018'), (datetime.date(2018, 12, 24), '24 十二月 2018'), (datetime.date(2018, 12, 31), '31 十二月 2018'), (datetime.date(2019, 1, 7), '07 一月 2019'), (datetime.date(2019, 1, 14), '14 一月 2019'), (datetime.date(2019, 1, 21), '21 一月 2019'), (datetime.date(2019, 1, 28), '28 一月 2019'), (datetime.date(2019, 2, 4), '04 二月 2019'), (datetime.date(2019, 2, 11), '11 二月 2019'), (datetime.date(2019, 2, 18), '18 二月 2019'), (datetime.date(2019, 2, 25), '25 二月 2019'), (datetime.date(2019, 3, 4), '04 三月 2019'), (datetime.date(2019, 3, 11), '11 三月 2019'), (datetime.date(2019, 3, 18), '18 三月 2019'), (datetime.date(2019, 3, 25), '25 三月 2019'), (datetime.date(2019, 4, 1), '01 四月 2019'), (datetime.date(2019, 4, 8), '08 四月 2019'), (datetime.date(2019, 4, 15), '15 四月 2019'), (datetime.date(2019, 4, 22), '22 四月 2019'), (datetime.date(2019, 4, 29), '29 四月 2019'), (datetime.date(2019, 5, 6), '06 五月 2019'), (datetime.date(2019, 5, 13), '13 五月 2019'), (datetime.date(2019, 5, 20), '20 五月 2019'), (datetime.date(2019, 5, 27), '27 五月 2019'), (datetime.date(2019, 6, 3), '03 六月 2019'), (datetime.date(2019, 6, 10), '10 六月 2019'), (datetime.date(2019, 6, 17), '17 六月 2019'), (datetime.date(2019, 6, 24), '24 六月 2019'), (datetime.date(2019, 7, 1), '01 七月 2019'), (datetime.date(2019, 7, 8), '08 七月 2019'), (datetime.date(2019, 7, 15), '15 七月 2019'), (datetime.date(2019, 7, 22), '22 七月 2019'), (datetime.date(2019, 7, 29), '29 七月 2019'), (datetime.date(2019, 8, 5), '05 八月 2019'), (datetime.date(2019, 8, 12), '12 八月 2019'), (datetime.date(2019, 8, 19), '19 八月 2019'), (datetime.date(2019, 8, 26), '26 八月 2019'), (datetime.date(2019, 9, 2), '02 九月 2019'), (datetime.date(2019, 9, 9), '09 九月 2019'), (datetime.date(2019, 9, 16), '16 九月 2019'), (datetime.date(2019, 9, 23), '23 九月 2019'), (datetime.date(2019, 9, 30), '30 九月 2019'), (datetime.date(2019, 10, 7), '07 十月 2019'), (datetime.date(2019, 10, 14), '14 十月 2019'), (datetime.date(2019, 10, 21), '21 十月 2019'), (datetime.date(2019, 10, 28), '28 十月 2019'), (datetime.date(2019, 11, 4), '04 十一月 2019'), (datetime.date(2019, 11, 11), '11 十一月 2019'), (datetime.date(2019, 11, 18), '18 十一月 2019'), (datetime.date(2019, 11, 25), '25 十一月 2019')], default=datetime.date(2018, 10, 8), unique=True),
        ),
    ]
