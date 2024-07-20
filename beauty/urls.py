"""
URL configuration for beauty project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('product/<str:name>',views.product, name='product'),
    path('product_details/<str:code>',views.product_details, name='product_details'),
    path('',views.log, name='login'),
    path('cart/',views.cart, name='cart'),
    path('cartadd/<int:code>',views.cartadd, name='cartadd'),
    path('faq/',views.faq, name='faq'),
    path('cart/order/<int:code>',views.order,name='order'),
    path('about/',views.about, name='about'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
