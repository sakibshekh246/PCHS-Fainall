"""
URL configuration for pchs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views as v
from Registration.models import Registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pchsAdmin/', v.index,name='useradmin'),
    path('insert/', v.insert, name='cat_insert'),
    path('edit/<int:id>', v.edit_index,name='edit_index'),
    path('update/', v.update,name='cat_update'),
    path('delete/<int:id>', v.delete,name='delete'),
    path('registration/', include('Registration.urls')),
    path('pchsAdmin/registration.html', v.registration_view, name='registration'),
    #path('pchsAdmin/login.html', v.login_view, name='login'),
    #path('pchsAdmin/pchs.html', v.index, name='cat_insert1'),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

