class ComputeViewSet(viewsets.Viewset)
    serializer_class = serializers.MySerializer
    
    def list(self, request):
        serializer = serializers.MySerializer(
            instance = compute.values)
