from django.http import JsonResponse
from api.models.rule import Rule
from api.models.user import User
from api.utils.query_engine import QueryEngine
from django.core import serializers
from django.http import HttpRequest

import random
import json


class RuleController:
    @staticmethod
    def index(request: HttpRequest):
        if request.method == 'POST':
            return JsonResponse(RuleController.create(request), safe=False)
        else:
            return JsonResponse(QueryEngine(Rule, request).run(), safe=False)

    @staticmethod
    def create(request):
        data = json.loads(request.body.decode())
        del data['method']
        Rule.objects.filter(id=data['id']).update(**data)
        return True

    @staticmethod
    def seed(request):
        avatar = [
            'images/eeHMaZBwmTvLdIwMfBpg.png',
            'images/udxAbMEhpwthVVcjLXik.png',
            'images/eeHMaZBwmTvLdIwMfBpg.png',
        ]
        fmaliy = [
            'توکلی',
            'تبریزی',
            'رازع',
            'روحانی',
            'رهنما',
            'سبزواری',
            'ساعی',
            'سیف',
            'سلامت',
            'اصفهانی',
            'اشتری',
            'خدایی',
            'شیرازی',
            'شیروانی',
            'صفوی',
            'بهادر',
            'بیگی',
            'بدخشانی',
            'رجایی',
            'رسولی',
            'عصار',
            'عبادی',
            'عاشوری',
            'موسوی',
        ]
        name = [
            'فاطمه',
            'زهرا',
            'یسنا',
            'ریحانه',
            'زینب',
            'باران',
            'رها',
            'کوثر',
            'مریم',
            'سارینا',
            'سارا',
            'هستی',
            'محیا',
            'ایلین',
            'مهسا',
            'نرگس',
            'معصومه',
            'حلما',
            'آوا',
            'الیا',
            'نیایش',
            'بهار',
            'امیر علی',
            'محمد طاها',
            'محمد',
            'عباس',
            'امیر حسین',
            'علی',
            'حسین',
            'امیر محمد',
            'امیر عباس',
            'محمد مهدی',
            'محمد رضا',
            'مهدی',
            'محمد حسین',
            'رضا',
            'ماهان',
            'یاسین',
            'پارسا',
            'کیان',
            'بنیامین',
        ]
        for x in range(1000):
            _name = random.choice(name)
            _family = random.choice(fmaliy)
            _callNo = random.randint(21000000, 219999999)
            _key = random.randint(1, 100000)
            _href = random.randint(1, 100000)
            _prg = random.randint(1, 100)
            _sts = random.randint(1, 3)
            user = Rule.objects.create(
                name=_name + ' ' + _family,
                avatar=random.choice(avatar),
                owner=random.choice(name) + '  ' + random.choice(fmaliy),
                desc=_name,
                disabled=False,
                href=_href,
                key=_key,
                callNo=_callNo,
                progress=_prg,
                status=_sts,
                title=_name
            )
        return JsonResponse(True, safe=False)
