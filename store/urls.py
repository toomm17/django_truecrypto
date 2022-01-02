from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='home'),
    path('support/', views.SupportPageView.as_view(), name='support'),
    path('faqs/', views.FaqPageView.as_view(), name='faqs'),
    path('news/', views.NewsPageView.as_view(), name='news'),
    path('bots', views.BotsPageView.as_view(), name='bots'),
    # path('news/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    # path('categories/', views.CategoryPageView.as_view(), name='categories'),
    # path('categories/<slug:slug>/', views.CategoryArticlesListView.as_view(), name='category_articles'),
    path('calendar/', views.CalendarPageView.as_view(), name='calendar'),
    path('calendar/tags-date/', views.AjaxTagsRender.as_view(), name='ajax_tags'),
    path('calendar/<int:year>-<int:month>-<int:day>/', views.CalendarDayView.as_view(), name='calendar_day'),
    path('articles/', views.ArticleCategoryView.as_view(), name='articles_category'),
    # path('articles/categories/<slug:slug>/<slug:art_slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    # path('articles/categories/<slug:slug>', views.CategoryDetailView.as_view(), name='category_detail'),
]
