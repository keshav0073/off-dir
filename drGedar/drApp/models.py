from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.EmailField()
    number=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.number

#for footer
class footer_image(models.Model):
    img=models.FileField(upload_to='')

    def __str__(self):
        return self.img.url

class footer_icon(models.Model):
    logo=models.FileField(upload_to='')
    image=models.ManyToManyField(footer_image)
    
    class Meta:
        verbose_name = 'Footer-Main'
        verbose_name_plural = 'Footer-Main'

#for slider
class sli_image(models.Model):
    img=models.FileField(upload_to="")

    def __str__(self):
        return self.img.url

    class Meta:
        verbose_name = 'Main Slider-Image'
        verbose_name_plural = 'Main Slider-Image'

class slider(models.Model):
    title=models.CharField(max_length=150,blank=True)
    image=models.ManyToManyField(sli_image)

    class Meta:
        verbose_name = 'Main Slider'
        verbose_name_plural = 'Main Slider'

#for dr-gedar-section
class dr_gedar(models.Model):
    text_in_strong=models.CharField(max_length=150)
    text_out_strong=models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Dr_gedar Section'
        verbose_name_plural = 'Dr_gedar section'


#for political_party section
class  political_party(models.Model):
    side_title=models.CharField(max_length=50,blank=True)
    image=models.FileField(upload_to='',blank=True)
    title=models.CharField(max_length=150)
    message=models.TextField(blank=True)
    signature=models.CharField(max_length=100,blank=True)

    class Meta:
        verbose_name = 'Political_party Section For Home'
        verbose_name_plural = 'Political_party Section For Home'

#for testimonial 
class testimonial_img(models.Model):
    Main_img=models.FileField(upload_to='',)
    video_img=models.FileField(upload_to='',blank=True)

    def __str__(self):
        return self.Main_img.url

class Testimonials(models.Model):
    title=models.CharField(max_length=150,default="Testimonials")
    text=models.TextField(blank=True)
    image=models.ManyToManyField(testimonial_img,blank=True)

    class Meta:
        verbose_name = 'Testimonial Section For Home'
        verbose_name_plural = 'Testimonial Section For Home'


#for Gallery-home
class Gallery_img(models.Model):
    img=models.FileField(upload_to='',)

    def __str__(self):
        return self.img.url

    class Meta:
        verbose_name = 'Gallery-Image'
        verbose_name_plural = 'Gallery-Image'

class Gallery_home(models.Model):
    title=models.CharField(max_length=150,default="Gallery")
    text=models.TextField(blank=True)
    image=models.ManyToManyField(Gallery_img,blank=True)

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'

#for about-slider
class about_slider(models.Model):
    image=models.FileField(upload_to='')
    title=models.CharField(max_length=200,blank=True)

    class Meta:
        verbose_name = 'About_us slider'
        verbose_name_plural = 'About_us slider'

    def __str__(self):
        return self.image.url

#for about-inner
class about_inner(models.Model):
    img=models.FileField(upload_to='',blank=True)
    title=models.CharField(max_length=150)
    text=models.TextField(blank=True)

    class Meta:
        verbose_name = 'About_us'
        verbose_name_plural = 'About_us'

#for blog
class category(models.Model):
    type=models.CharField(max_length=150)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Insert Category For Blog'
        verbose_name_plural = 'Insert Category For Blog'

class Artical(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(max_length=150,unique=True)
    joner=models.ForeignKey(category,on_delete=models.CASCADE)
    write_by=models.CharField(max_length=50)
    date=models.DateField()
    message=models.TextField(blank=True)
    main_image=models.FileField(upload_to='',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

#for comment
class comment(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(blank=False,null=False)
    website=models.URLField(blank=True,null=True)
    text=models.TextField()
    title=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name