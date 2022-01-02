from datetime import datetime, timezone

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View

from .models import Article, Category, Event, Tag
from .utils import diff_dates, ajax_renderer_date


class MainPageView(TemplateView):
    template_name = 'base.html'


class SupportPageView(TemplateView):
    template_name = 'store/help.html'


class FaqPageView(TemplateView):
    template_name = 'store/faq.html'


class NewsPageView(ListView):
    model = Article
    context_object_name = 'news'
    template_name = 'store/news.html'

    def get_queryset(self):
        return Article.objects.filter(is_news=True)


class NewsDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'store/news_detail.html'

    def get_queryset(self):
        return Article.objects.filter(slug=self.kwargs.get('slug'))


class CategoryArticlesListView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'store/articles.html'

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs.get('slug'))


class BotsPageView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'store/bots.html')


class CalendarPageView(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'store/calendar_month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = datetime.today().strftime('%Y-%m-%d')
        event_last_day = Event.objects.order_by('-date').first().date
        
        all_dates = Event.objects.filter(date__gte=datetime.now(timezone.utc)).values('date').order_by('date').distinct()
        
        deadline_dates = Event.objects.filter(date__lte=datetime.now(timezone.utc), deadline__gte=datetime.now(timezone.utc)).values('date').order_by('date').distinct()
        print(all_dates)
        context['dates'] = []
        context['deadline_dates'] = []
        context['tags'] = Tag.objects.all()
        context['months'] = diff_dates(
            all_dates[0].get('date').strftime('%Y-%m-%d'), 
            event_last_day.strftime('%Y-%m-%d')
        )
        
        for date in all_dates:
            for value in date.values():
                context['dates'].append(ajax_renderer_date(value.strftime('%Y-%m-%d')))
        for date in deadline_dates:
            for value in date.values():
                context['deadline_dates'].append(ajax_renderer_date(value.strftime('%Y-%m-%d')))
        
        print(all_dates, deadline_dates)
        return context


class AjaxTagsRender(View):
    def get(self, request):
        if request.is_ajax():
            tags = request.GET.get('tags').strip().split(',')
            js_render_string = ''
            if 'KYC' in tags:
                event = Event.objects.filter(tag__name__in=tags, have_kyc=True, date__gte=datetime.now(timezone.utc)).values('date').order_by('date').distinct()
                if len(event) == 0:
                    event = Event.objects.filter(have_kyc=True, date__gte=datetime.now(timezone.utc)).values('date').order_by('date').distinct()
            else:
                event = Event.objects.filter(tag__name__in=tags, date__gte=datetime.now(timezone.utc)).values('date').order_by('date').distinct()
            for date in event:
                js_render_string += f"{ajax_renderer_date(date['date'].strftime('%Y-%m-%d'))},"
            print(js_render_string)
            return JsonResponse({'tags': js_render_string}, status=200)

        return render(request, 'store/calendar_month.html')


class CalendarDayView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        year, month, day = list(kwargs.values())
        events = Event.objects.filter(date__year=year, date__month=month, date__day=day)
        tags_queryset = [event.tag.all() for event in events]
        tags = []
        
        for tag in tags_queryset:
            for t in tag:
                if not t.name in tags:
                    tags.append(t.name)
        
        context = {
            'events': events,
            'tags': tags,
            'month': datetime(year, month, day),
            'event_counts': len(events)
        }
        return render(request, 'store/calendar_day.html', context)

        
class ArticleCategoryView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'store/articles_cat.html')


