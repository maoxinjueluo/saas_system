from product.models import GoodsUnit
from django.http import JsonResponse
import json
from django.views.generic import View

# Create your views here.


class AddUnit(View):
    """
    add unit
    """
    def post(self, request):
        data = json.loads(request.body)
        mch_id = data.get('mch_id', 0)
        store_id = data.get('store_id', 0)
        unit = data.get('unit')

        if not unit:
            response = {
                'msg': 'unit is None',
            }
            return JsonResponse({'state': 400, 'data': response})

        O_unit = GoodsUnit()
        O_unit.mch_id = int(mch_id)
        O_unit.store_id = int(store_id)
        O_unit.unit = unit
        O_unit.state = 1
        O_unit.save()

        response = {
            'msg': 'create success'
        }
        return JsonResponse({'state': 200, 'data': response})

