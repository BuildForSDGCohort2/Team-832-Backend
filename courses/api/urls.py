from django.urls import path, include
from .views import (
	CourseListView, 
	TopicListView, 
	CourseCreateAPIView, 
	TopicCreateAPIView, 
	CourseRetrieveAPIView, 
	TopicRetrieveAPIView,
	CourseTopic,
	TopicSearchListView
	)
#, OrderCreateAPIView, OrderDetailAPIView, ProductUpdateAPIView

urlpatterns = [
    path('course-list/', CourseListView.as_view(), name="course-list"),
    path('topic-list/', TopicListView.as_view(), name="topic-list"),
    path('course-create/', CourseCreateAPIView.as_view(), name="course-list"),
    path('topic-create/', TopicCreateAPIView.as_view(), name="topic-list"),
    path('topic/<pk>/', TopicRetrieveAPIView.as_view(), name="topic-detail"),
    path('course/<pk>/', CourseRetrieveAPIView.as_view(), name="course-detail"),
    path('course-topic/<pk>/', CourseRetrieveAPIView.as_view(), name="course-topic"),
    path('topic-search/', TopicSearchListView.as_view(), name="topic-search"),

]
