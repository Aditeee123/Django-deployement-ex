from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
url(r'otherpage/', views.other, name='other'),
url(r'fourth/', views.fourth, name='fourth'),
url(r'relative_page/', views.relative_html, name='relative_html')
]
