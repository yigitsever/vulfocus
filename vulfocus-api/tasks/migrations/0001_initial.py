# Generated by Django 2.2.10 on 2020-05-07 09:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskInfo',
            fields=[
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(verbose_name='任务创建用户 ID')),
                ('task_name', models.CharField(max_length=255, verbose_name='任务名称')),
                ('task_status', models.IntegerField(default=1)),
                ('task_start_date', models.DateTimeField(auto_now_add=True, verbose_name='任务创建时间')),
                ('task_end_date', models.DateTimeField(null=True, verbose_name='任务结束时间')),
                ('operation_type', models.CharField(max_length=255, verbose_name='执行操作名称')),
                ('operation_args', models.TextField(default='', verbose_name='执行操作参数')),
                ('task_msg', models.TextField(default='', verbose_name='任务执行消息')),
                ('is_show', models.BooleanField(default=False, verbose_name='任务是否被查看')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'task_info',
            },
        ),
    ]
