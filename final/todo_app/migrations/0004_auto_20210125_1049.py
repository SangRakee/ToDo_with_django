# Generated by Django 3.1.5 on 2021-01-25 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20210122_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='content',
        ),
        migrations.AddField(
            model_name='todo',
            name='level',
            field=models.CharField(choices=[('1~2(초보)', '1~2(초보)'), ('5(고수)', '5(고수)'), ('1~5(전체)', '1~5(전체)'), ('3~4(중수)', '3~4(중수)')], max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='todo',
            name='sex',
            field=models.CharField(choices=[('남녀모두', '남녀모두'), ('남자만', '남자만'), ('여자만', '여자만')], max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.CharField(choices=[('13:00', '13:00'), ('11:00', '11:00'), ('15:00', '15:00'), ('21:00', '21:00'), ('17:00', '17:00'), ('19:00', '19:00'), ('09:00', '09:00')], max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='city',
            field=models.CharField(choices=[('대구,경북', '대구,경북'), ('광주', '광주'), ('부산', '부산'), ('경기', '경기'), ('인천', '인천'), ('울산', '울산'), ('대전,충청', '대전,충청'), ('서울', '서울')], max_length=80, null=True),
        ),
    ]
