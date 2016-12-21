from rest_framework import serializers
from models import Photo

# class PhotoSerializer(serializers.Serializer):
# 	image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

class PhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Photo
		fields = ('file_name','image',)
		read_only_fields = ('file_name',)

