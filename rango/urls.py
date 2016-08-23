from django.conf.urls import url
from rango import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^search/', views.search, name='search'),
	url(r'^goto/', views.track_url, name='goto'),
	url(r'^add_profile/$', views.register_profile, name='register_profile'),
	url(r'^profile/', views.profile, name='profile'),
	url(r'^like_category/$', views.like_category, name='like_category'),
	url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
	url(r'^auto_add_page/$', views.auto_add_page, name='auto_add_page'),
]