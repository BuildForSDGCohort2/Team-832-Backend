from django.http import HttpResponse
from django.conf import settings
#from django.core.mail import send_mail

from courses.models import Course,  Topic
from .serializers import CourseSerializer, TopicSerializer

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

class CourseListView(ListAPIView):
        permission_classes = ([AllowAny])
        queryset = Course.objects.all()
        serializer_class = CourseSerializer

class TopicListView(ListAPIView):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('topic', 'course__title')

	
class CourseCreateAPIView(CreateAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer                

class TopicCreateAPIView(CreateAPIView):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer

class TopicRetrieveAPIView(RetrieveAPIView):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	print()

class CourseRetrieveAPIView(RetrieveAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer


@api_view(['GET', ])
def CourseTopic(request, pk):

	try:
		course = Course.objects.get(pk=pk)
	except Course.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	title = course.title
	print("title")

	for topic in course.topic_set.all():
		print(topic)

class TopicSearchListView(ListAPIView):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	filter_backends = (SearchFilter, OrderingFilter)
	search_fields = ('topic', 'course')

