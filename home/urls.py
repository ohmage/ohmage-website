from django.conf.urls import patterns, url
import views

urlpatterns = patterns('ohmageWebsite.home.views',
    # main page
    url(r'^$', views.index, name="index")
)
