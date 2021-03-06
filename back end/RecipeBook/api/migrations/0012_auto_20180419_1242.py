# Generated by Django 2.0.4 on 2018-04-19 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_recipe_voted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(blank=True, max_length=100)),
                ('author_pk', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='api.Author')),
            ],
        ),
        migrations.AlterField(
            model_name='cookstep',
            name='recipe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cook_steps', to='api.Recipe'),
        ),
    ]
