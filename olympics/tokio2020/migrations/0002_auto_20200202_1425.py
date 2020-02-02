# Generated by Django 2.1.15 on 2020-02-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokio2020', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthleteEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=20)),
            ],
            options={
                'db_table': '"Event\'sTables"."Athlete_event"',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='athletes',
            table='"Athlete\'sTables"."Athletes"',
        ),
        migrations.AlterModelTable(
            name='coaches',
            table='"Athlete\'sTables"."Coaches"',
        ),
        migrations.AlterModelTable(
            name='event',
            table='"Event\'sTables"."Events"',
        ),
        migrations.AlterModelTable(
            name='eventvideocomments',
            table='"Student\'sTables"."Event_video_comments"',
        ),
        migrations.AlterModelTable(
            name='sport',
            table='"Athlete\'sTables"."Sports"',
        ),
        migrations.AlterModelTable(
            name='sportmodality',
            table='"Athlete\'sTables"."Sport_Modalities"',
        ),
        migrations.AlterModelTable(
            name='student',
            table='"Student\'sTables"."Students"',
        ),
    ]
