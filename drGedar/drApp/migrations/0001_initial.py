# Generated by Django 3.0.7 on 2020-06-17 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about_inner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, upload_to='')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'About_us',
                'verbose_name_plural': 'About_us',
            },
        ),
        migrations.CreateModel(
            name='about_slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'About_us slider',
                'verbose_name_plural': 'About_us slider',
            },
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Insert Category For Blog',
                'verbose_name_plural': 'Insert Category For Blog',
            },
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='dr_gedar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_in_strong', models.CharField(max_length=150)),
                ('text_out_strong', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Dr_gedar Section',
                'verbose_name_plural': 'Dr_gedar section',
            },
        ),
        migrations.CreateModel(
            name='footer_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Gallery-Image',
                'verbose_name_plural': 'Gallery-Image',
            },
        ),
        migrations.CreateModel(
            name='political_party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side_title', models.CharField(blank=True, max_length=50)),
                ('image', models.FileField(blank=True, upload_to='')),
                ('title', models.CharField(max_length=150)),
                ('message', models.TextField(blank=True)),
                ('signature', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Political_party Section For Home',
                'verbose_name_plural': 'Political_party Section For Home',
            },
        ),
        migrations.CreateModel(
            name='sli_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name': 'Main Slider-Image',
                'verbose_name_plural': 'Main Slider-Image',
            },
        ),
        migrations.CreateModel(
            name='testimonial_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Main_img', models.FileField(upload_to='')),
                ('video_img', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Testimonials', max_length=150)),
                ('text', models.TextField(blank=True)),
                ('image', models.ManyToManyField(blank=True, to='drApp.testimonial_img')),
            ],
            options={
                'verbose_name': 'Testimonial Section For Home',
                'verbose_name_plural': 'Testimonial Section For Home',
            },
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('image', models.ManyToManyField(to='drApp.sli_image')),
            ],
            options={
                'verbose_name': 'Main Slider',
                'verbose_name_plural': 'Main Slider',
            },
        ),
        migrations.CreateModel(
            name='Gallery_home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Gallery', max_length=150)),
                ('text', models.TextField(blank=True)),
                ('image', models.ManyToManyField(blank=True, to='drApp.Gallery_img')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='footer_icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='')),
                ('image', models.ManyToManyField(to='drApp.footer_image')),
            ],
            options={
                'verbose_name': 'Footer-Main',
                'verbose_name_plural': 'Footer-Main',
            },
        ),
        migrations.CreateModel(
            name='Artical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('write_by', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('message', models.TextField(blank=True)),
                ('main_image', models.FileField(blank=True, upload_to='')),
                ('joner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drApp.category')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]