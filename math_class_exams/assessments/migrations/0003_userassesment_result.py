# Generated by Django 2.0.9 on 2018-12-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0002_assessment_threshold'),
    ]

    operations = [
        migrations.AddField(
            model_name='userassesment',
            name='result',
            field=models.CharField(choices=[('0', 'Failed'), ('1', 'Passed')], default='0', max_length=1),
        ),
    ]
