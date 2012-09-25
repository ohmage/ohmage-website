from django.conf.urls import patterns, url
import views

urlpatterns = patterns('ohmageWebsite.home.views',
    # main page
    url(r'^$', views.home, name="home"),
    url(r'^usage$', views.usage, name="usage"),
    url(r'^projects', views.projects, name="projects"),
    url(r'^papers', views.papers, name="papers"),
    url(r'^contributors', views.contributors, name="contributors")
)
