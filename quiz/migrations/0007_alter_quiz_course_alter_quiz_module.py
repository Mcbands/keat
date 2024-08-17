# Generated by Django 4.2.2 on 2024-02-11 14:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_course_category_alter_course_level'),
        ('quiz', '0006_alter_quiz_course_alter_quiz_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(blank=True, null=True,on_delete=django.db.models.deletion.CASCADE, related_name='quiz_course', to='main.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_module', to='main.module'),
            preserve_default=False,
        ),
    ]
