from __future__ import absolute_import, unicode_literals
from .zoomit_scraper import NewsScraper
from celery import shared_task
from .models import New
import json
import os


@shared_task
def update_news():
    # get new data
    start_url = 'https://www.zoomit.ir/archive/?sort=Newest&skip=20'
    
    scraper = NewsScraper(start_url)
    data = scraper.get_data()

    # add new data
    for d in reversed(data):
        obj = New(title=d['title'].replace('\u200c', ' '), 
                    content=[c.replace('\u200c', ' ') for c in d['content']], 
                    tags=d['tags'], 
                    source=d['source'])
        obj.save()