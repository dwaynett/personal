class MySerializer(serializers.Serializer):
    result = serializers.CharField(max_length=256)
    
    def create(self, validated_data):
        return ComputeClass(id=None, **validated_data)
        
    def update(self, instance, validated_data)
        setattr(instance, field, value)
        return instance
