from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$',
        TemplateView.as_view(template_name='demo/index.html'),
        name='index'),

    url(r'^page0$',
        TemplateView.as_view(template_name='demo/page0.html'),
        name='page0'),

    url(r'^page0/tab0$',
        TemplateView.as_view(template_name='demo/page0_tab0.html'),
        name='page0_tab0'),

    url(r'^page0/tab1$',
        TemplateView.as_view(template_name='demo/page0_tab1.html'),
        name='page0_tab1'),

    url(r'^page1$',
        TemplateView.as_view(template_name='demo/page1.html'),
        name='page1'),

    url(r'^page2$',
        TemplateView.as_view(template_name='demo/page2.html'),
        name='page2'),
)