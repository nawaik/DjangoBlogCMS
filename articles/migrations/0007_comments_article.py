# Generated by Django 3.0.7 on 2020-06-07 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Articles'),
            preserve_default=False,
        ),
    ]
