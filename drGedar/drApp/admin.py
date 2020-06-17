from django.contrib import admin
from .models import *
# Register your models here.
class admincontact(admin.ModelAdmin):
    list_display=('first_name','last_name')

admin.site.register(Contact,admincontact)

#for footer
admin.site.register(footer_image)
admin.site.register(footer_icon)

#for slider
admin.site.register(sli_image)
admin.site.register(slider)

#for dr-gedar-section
admin.site.register(dr_gedar)

#for blog-section
# admin.site.register(blog_section)

#for political-party
admin.site.register(political_party)

#for Testimonial
admin.site.register(testimonial_img)
admin.site.register(Testimonials)

#for Gallery_home
admin.site.register(Gallery_img)
admin.site.register(Gallery_home)

#for about_slider
admin.site.register(about_slider)

#for about_inner
admin.site.register(about_inner)

#for blog
admin.site.register(category)
admin.site.register(Artical)

#for comment
admin.site.register(comment)