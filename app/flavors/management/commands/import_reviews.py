# -*- coding: utf-8 -*-
import requests
from django.core.management.base import BaseCommand
from progressbar import ProgressBar
from progressbar.widgets import *
from app.flavors.models import Flavor, Review


FEED_URL = 'http://kpwk.pw/debug'
_table = {}


def _get_review_user(item):
    user_row = 5
    user_col = item['col'] - 1
    return _table.get(user_row, {}).get(user_col, {})


def _get_review_flavor(item):
    _row = item['row']
    _col = 1
    return _table.get(_row, {}).get(_col, {})


def _get_percentage(item):
    _col = item['col'] - 1
    _row = item['row']
    return _table.get(_row, {}).get(_col, {}).get('value')


def _handle_user(item):
    pass


def _handle_flavor(item):
    flavor, _ = Flavor.objects.get_or_create(
        name=item.get('value'),
        manufacturer_id=1
    )
    flavor.save()
    item['_obj'] = flavor


def _handle_review(item):
    user_item = _get_review_user(item)
    flavor_item = _get_review_flavor(item)
    if not flavor_item.get('_obj'):
        print item
    review, _ = Review.objects.get_or_create(
        flavor=flavor_item.get('_obj'),
        author_name=user_item.get('value'),
        defaults={
            'content': item.get('value'),
            'favorite_percentage': _get_percentage(item)
        }
    )
    review.save()
    item['_obj'] = review


PARSE_RULES = [
    {
        'range': lambda (row, col): row == 5 and col > 2,
        'type': 'username',
        'handle': _handle_user
    },
    {
        'range': lambda (row, col): row > 6 and col == 1,
        'type': 'flavor',
        'handle': _handle_flavor
    },
    {
        'range': lambda (row, col): row > 6 and col % 2 == 0 and col > 3,
        'type': 'review',
        'handle': _handle_review
    },
]

class Command(BaseCommand):
    args = ''
    help = 'Performs initial loading from kpwk.pw/debug.'

    def handle(self, *args, **options):

        resp = requests.get(FEED_URL)
        if resp.status_code != 200:
            print('Cannot open URL')
            return

        json = resp.json()

        # Processing product prices reindex
        _num, _processed = len(json), 0
        # Intializing progress bar.
        print ''
        progress = ProgressBar(maxval=_num,
                               widgets=['  Importing reviews: ', Counter(), ' of %i' % _num, ' ', Bar(),
                                        ' ', ETA()])
        progress.start()

        for item in json:
            if not item.get('row') or not item.get('col'):
                continue
            if not _table.get(item['row']):
                _table[item['row']] = {}
            _table[item['row']][item['col']] = item

            for rule in PARSE_RULES:
                if rule['range']((item['row'], item['col'])):
                    rule['handle'](item)
                    break
            _processed += 1
            progress.update(_processed)

        progress.finish()
