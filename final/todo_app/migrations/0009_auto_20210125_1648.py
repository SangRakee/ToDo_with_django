# Generated by Django 3.1.5 on 2021-01-25 07:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_app', '0008_auto_20210125_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='likes_user',
            field=models.ManyToManyField(blank=True, related_name='likes_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='city',
            field=models.CharField(choices=[('경기', '경기'), ('부산', '부산'), ('울산', '울산'), ('대구,경북', '대구,경북'), ('대전,충청', '대전,충청'), ('광주', '광주'), ('인천', '인천'), ('서울', '서울')], max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='level',
            field=models.CharField(choices=[('1~2(초보)', '1~2(초보)'), ('5(고수)', '5(고수)'), ('3~4(중수)', '3~4(중수)'), ('1~5(전체)', '1~5(전체)')], max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='sex',
            field=models.CharField(choices=[('남녀모두', '남녀모두'), ('남자만', '남자만'), ('여자만', '여자만')], max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.CharField(choices=[('17:00', '17:00'), ('09:00', '09:00'), ('15:00', '15:00'), ('21:00', '21:00'), ('13:00', '13:00'), ('11:00', '11:00'), ('19:00', '19:00')], max_length=80, null=True),
        ),
    ]
