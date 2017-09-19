from django.conf.urls import url
import views

urlpatterns = [

    url(r'^$', views.displayForm),
    url(r'^survey_form$', views.showResults),
    url(r'^survey_form/back', views.goBack)

]