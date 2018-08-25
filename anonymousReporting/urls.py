from django.urls import path

from . import views

app_name = 'anonymousReporting'
urlpatterns = [
    path('', views.raise_issue, name='raise_issue'),
    # pay attention to the spacing, no spaces are allowed in between LHS and RHS
    path('<int:authority_id>/', views.authority_detail, name='authority_detail'),
    path('submitComplain', views.submit_complain, name='submit_complain'),
    path('index', views.index, name='index')
]
