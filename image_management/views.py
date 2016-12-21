from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from serializers import PhotoSerializer,PhotoDeleteSerializer
from rest_framework.response import Response
from models import Photo
from time import gmtime, strftime

class PhotoUpload(APIView):
	queryset = Photo.objects.all()
	serializer_class = PhotoSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	def get_object(self, file_name):
		try:
			return Photo.objects.get(file_name=file_name)
		except Photo.DoesNotExist:
			return None

	def check_if_exist(self, image_name):
		#import pdb; pdb.set_trace()
		for photo in Photo.objects.all():
			if image_name == photo.image.name.split("/",1)[1]:
				return photo
		return None

	def get(self, request, *args, **kwargs):
		#import pdb; pdb.set_trace()
		fname = kwargs.get('file_name','')
		if fname:
			photo = self.get_object(kwargs.get('file_name',''))
			if photo:
				serializer = PhotoSerializer(photo)
				data = serializer.data
				data['image'] = "http://"+request.META['HTTP_HOST']+data['image']
				return Response(data, status=status.HTTP_200_OK)
			return Response(status=status.HTTP_404_NOT_FOUND)
		return Response(status=status.HTTP_200_OK)


	def post(self, request, *args, **kwargs):
		import pdb; pdb.set_trace()
	 	fname = "photo_"+strftime("%Y%m%d_%H%M", gmtime())

	 	photo = self.check_if_exist(request.data['image'].name)

	 	serializer = PhotoSerializer(data = request.data)

	 	data = dict()
	 	data['file_name'] = fname
	 	
	 	if not photo:
		 	if serializer.is_valid():
		 		data['already_exist'] = 0
		 		if request.data['image'].size < 25000000:
		 			photo = serializer.save(file_name = fname)
		 			data['url'] = "http://"+request.META['HTTP_HOST'] + photo.image.url
		 			return Response(data,status=status.HTTP_201_CREATED)
		 		return Response({'message':'File too large'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
		else:
			data['url']="http://"+request.META['HTTP_HOST'] + photo.image.url
			data['file_name'] = photo.file_name
			data['already_exist'] = 1
			return Response(data,status=status.HTTP_202_ACCEPTED)
		

	def put(self, request, *args, **kwargs):
		#import pdb; pdb.set_trace()
		photo = self.get_object(kwargs['file_name'])
		serializer = PhotoSerializer(photo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		


	def delete(self, request, file_name=None):
		#import pdb; pdb.set_trace()
		
		if file_name is not None:
			photo = self.get_object(file_name)
			photo.delete()
			return Response({'message':'Deleted Successfully',},status=status.HTTP_204_NO_CONTENT)
		else:
			return Response({'message':'File Name not mentioned',},status=status.HTTP_204_NO_CONTENT)

# class PhotoDelete(generics.CreateAPIView):
# 	queryset = Photo.objects.all()
# 	serializer_class = PhotoSerializer