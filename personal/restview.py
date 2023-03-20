from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from personal.compute import ComputeClass


class MyRESTView(APIView):

    def get(self, request, *args, **kw):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        get_arg1 = request.GET.get('arg1', None)
        
        # Any URL parameters get passed in **kw
        myClass = ComputeClass()
        result = myClass.do_work(get_arg1)
        response = Response(result, status=status.HTTP_200_OK)
        return response
