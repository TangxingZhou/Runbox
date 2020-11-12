from django.urls import path
from .views import *

urlpatterns = [
    path('executions/', ExecutionList.as_view()),
    path('executions/<int:pk>/', ExecutionDetail.as_view()),
    path('execution-errors/', ExecutionErrorList.as_view()),
    path('execution-errors/<int:pk>/', ExecutionErrorDetail.as_view()),
    path('suite-statistics/', SuiteStatisticsList.as_view()),
    path('suite-statistics/<int:pk>/', SuiteStatisticsDetail.as_view()),
    path('test-statistics/', TestStatisticsList.as_view()),
    path('test-statistics/<int:pk>/', TestStatisticsDetail.as_view()),
    path('tag-statistics/', TagStatisticsList.as_view()),
    path('tag-statistics/<int:pk>/', TagStatisticsDetail.as_view()),
    path('suites/', SuiteList.as_view()),
    path('suites/<int:pk>/', SuiteDetail.as_view()),
    path('tests/', TestList.as_view()),
    path('tests/<int:pk>/', TestDetail.as_view()),
    path('test-tags/', TestTagList.as_view()),
    path('test-tags/<int:pk>/', TestTagDetail.as_view()),
    path('keywords/', KeywordList.as_view()),
    path('keywords/<int:pk>/', KeywordDetail.as_view()),
    path('keyword-tags/', KeywordTagList.as_view()),
    path('keyword-tags/<int:pk>/', KeywordTagDetail.as_view()),
    path('keyword-arguments/', ArgumentList.as_view()),
    path('keyword-arguments/<int:pk>/', ArgumentDetail.as_view()),
    path('keyword-assigns/', AssignList.as_view()),
    path('keyword-assigns/<int:pk>/', AssignDetail.as_view()),
    path('keyword-messages/', MessageList.as_view()),
    path('keyword-messages/<int:pk>/', MessageDetail.as_view()),
]