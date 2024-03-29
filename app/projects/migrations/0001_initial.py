# Generated by Django 2.2.10 on 2020-03-29 18:58

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.routable_page.models
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(help_text='The basic name for a given project', max_length=120, null=True)),
                ('description', wagtail.core.fields.RichTextField(help_text='A description of this project including questions that it tries to answer, data sources and tools used, etc. ', null=True, verbose_name='Project Description')),
                ('type', models.CharField(choices=[('s', 'Software'), ('r', 'Research')], help_text='The type of work that this project represents', max_length=5, null=True)),
                ('repository', models.URLField(blank=True, help_text='If a software project, provide a link to the repository for the code base.', null=True)),
                ('status', models.CharField(choices=[('pl', 'Planned'), ('ip', 'In Progress'), ('oh', 'On Hold'), ('cp', 'Completed')], help_text='The stage this project is currently at.', max_length=3, null=True)),
                ('categories', modelcluster.fields.ParentalManyToManyField(to='blog.BlogCategory')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('page_title', models.CharField(help_text='Title for list of Projects', max_length=120, null=True)),
                ('page_subtitle', wagtail.core.fields.RichTextField(blank=True, help_text='Sub title text for listing page.', null=True)),
                ('projects_per_page', models.IntegerField(default=5, help_text='Number of projects per page.', verbose_name='Projects per Page')),
            ],
            options={
                'verbose_name': 'Project Listing',
                'verbose_name_plural': 'Project Listings',
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('pub_title', models.CharField(max_length=150, null=True)),
                ('pub_abstract', wagtail.core.fields.RichTextField(help_text='Publication abstract', null=True)),
                ('pub_journal', models.TextField(null=True, verbose_name='Journal of Publication')),
                ('pub_link', models.URLField(blank=True, help_text='Link to publication', null=True)),
                ('pub_date', models.DateField(blank=True, help_text='The rough date when this publication was published.', null=True, verbose_name='Publication Date')),
                ('categories', modelcluster.fields.ParentalManyToManyField(to='blog.BlogCategory')),
                ('gs_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publications', to='projects.Project')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PublicationListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('page_title', models.CharField(help_text='Title for List of Publications', max_length=120, null=True)),
                ('page_subtitle', wagtail.core.fields.RichTextField(blank=True, help_text='Sub title text for listing page.', null=True)),
                ('pubs_per_page', models.IntegerField(default=5, help_text='Define how this listing is paginated', verbose_name='Publications per Page')),
            ],
            options={
                'verbose_name': 'Publication Listing',
                'verbose_name_plural': 'Publication Listings',
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='Scientist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Scientist's first name", max_length=100, null=True)),
                ('last_name', models.CharField(help_text="Scientist's last name", max_length=100, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('institutions', models.ManyToManyField(related_name='scientists', to='projects.Institution')),
            ],
            options={
                'verbose_name': 'Scientist',
                'verbose_name_plural': 'Scientists',
            },
        ),
        migrations.CreateModel(
            name='PublicationAuthorOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='projects.Scientist')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='projects.Publication')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectScientistOrderable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('project', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='collaborators', to='projects.Project')),
                ('scientist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Scientist')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
