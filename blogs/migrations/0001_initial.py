# Generated by Django 4.1.4 on 2023-01-31 16:24

import blogs.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=225, unique=True)),
                ('slug', models.SlugField(max_length=250)),
                ('subtitle', models.CharField(blank=True, max_length=300, null=True)),
                ('cover_image', models.ImageField(default='https://tinyurl.com/y9ppmvs4', upload_to=blogs.models.upload_to_path)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('arts', 'ARTS'), ('games', 'GAMES'), ('home', 'HOME'), ('healthHEALTH', 'Health'), ('technology', 'TECHNOLOGY'), ('recreation', 'RECREATION'), ('business', 'BUSINESS'), ('society', 'SOCIETY'), ('sports', 'SPORTS'), ('science', 'SCIENCE')], max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'DRAFT'), ('publish', 'PUBLISH')], default='draft', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
