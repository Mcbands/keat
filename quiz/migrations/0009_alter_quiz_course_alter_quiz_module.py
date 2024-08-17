# Generated by Django 4.2.2 on 2024-02-11 14:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_delete_level_alter_course_category_delete_category'),
        ('quiz', '0008_alter_quiz_course_alter_quiz_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_course', to='main.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quiz',
            name='module',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_module', to='main.module'),
            preserve_default=False,
        ),
    ]
