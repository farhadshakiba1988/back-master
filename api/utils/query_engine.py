from django.db import models
from django.http import HttpRequest
from django.db.models import Q


class QueryEngine:
    def __init__(self, query: models.Model, request: HttpRequest):
        self.query = query
        self.request = request.GET
        self.pageSize = request.GET['pageSize'] if 'pageSize' in request.GET else 10
        self.currentPage = request.GET['currentPage'] if 'currentPage' in request.GET else 1

    t = 10

    def run(self):
        q = self.query.objects
        if self.request.__contains__('global'):
            q = q.filter(Q(name__icontains=self.request['global']))

        if self.request.__contains__('name'):
            q = q.filter(Q(name__icontains=self.request['name']))

        if self.request.__contains__('status') and self.request['status'] != '':
            q = q.filter(Q(status__in=self.request['status'].split(',')))

        if self.request.__contains__('sorter') and self.request['sorter'] != '':
            order = '-' if self.request['sorter'].endswith('descend') else ''
            splt = self.request['sorter'].split('_')
            splt.pop()
            order += '_'.join(splt)
        else:
            order = 'id'

        count = q.count()
        q = q.order_by(order)[int(self.currentPage):int(self.currentPage) + int(self.pageSize)].values()

        list_result = [entry for entry in q]
        return {'list': list_result,
                'pagination': {'current': int(self.currentPage), 'pageSize': int(self.pageSize), 'total': count}}
