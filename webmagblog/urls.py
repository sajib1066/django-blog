from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('category/<name>', views.category_page, name='category'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
handler404 = views.error_404
handler500 = views.error_500

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
