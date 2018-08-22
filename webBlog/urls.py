from django.urls import path
from . import views

app_name = 'webBlog'
urlpatterns = [
    path('', views.index, name='index'),
    path('band/', views.band, name='band'),
    path('tour/', views.tour, name='tour'),
    path('contact/', views.contact, name='contact'),
    
    path('blog/', views.BlogListView.as_view(), name='blog'),
    
    path('polls/', views.IndexView.as_view(), name='polls-index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

