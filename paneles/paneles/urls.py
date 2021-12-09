"""paneles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url,include
from django.urls import path
from django.conf import settings
from apps.home import urls

from django.contrib.auth.decorators import login_required
from apps.home.views import InicioView 
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path(r'', include('apps.home.urls') ),
    path(r'', include('apps.usuario.urls') ),
    url(r'.*/$',InicioView.as_view() )

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

