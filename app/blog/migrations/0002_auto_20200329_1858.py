# Generated by Django 2.2.10 on 2020-03-29 18:58

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogauthorsorderable',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Scientist'),
        ),
        migrations.AddField(
            model_name='blogauthorsorderable',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_authors', to='blog.BlogDetailPage'),
        ),
    ]
