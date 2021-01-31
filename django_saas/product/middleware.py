from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
import json


class CheckIntValueMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        data = json.loads(request.body)
        mch_id = data.get('mch_id')
        store_id = data.get('store_id')

        if mch_id and type(mch_id) != 'int':
            response = {'msg': 'please check your mch_id'}
            return JsonResponse({'state': 400, 'data': response})
        if store_id and type(store_id) != 'int':
            response = {'msg': 'please check your store_id'}
            return JsonResponse({'state': 400, 'data': response})
