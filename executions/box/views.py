from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from .serializers import *


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExecutionList(generics.ListCreateAPIView):
    queryset = Execution.objects.all()
    serializer_class = ExecutionSerializer


class ExecutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Execution.objects.all()
    serializer_class = ExecutionSerializer


class MyExecutionErrors(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    # def get_object(self, pk):
    #     try:
    #         return ExecutionError.objects.get(pk=pk)
    #     except ExecutionError.DoesNotExist:
    #         raise Http404

    def get(self, request, pk, format=None):
        """
        Return a list of all users.
        """
        error = SuiteStatistics.objects.filter(execution=Execution.objects.filter(id=pk))
        serializer = SuiteStatisticsSerializer(error, many=True)
        return Response(serializer.data)


class ExecutionErrorList(generics.ListCreateAPIView):
    queryset = ExecutionError.objects.filter(execution_id=1)
    serializer_class = ExecutionErrorSerializer


class ExecutionErrorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExecutionError.objects.all()
    serializer_class = ExecutionErrorSerializer


class SuiteStatisticsList(generics.ListCreateAPIView):
    queryset = SuiteStatistics.objects.all()
    serializer_class = SuiteStatisticsSerializer


class SuiteStatisticsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuiteStatistics.objects.all()
    serializer_class = SuiteStatisticsSerializer


class TestStatisticsList(generics.ListCreateAPIView):
    queryset = TestStatistics.objects.all()
    serializer_class = TestStatisticsSerializer


class TestStatisticsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestStatistics.objects.all()
    serializer_class = TestStatisticsSerializer


class TagStatisticsList(generics.ListCreateAPIView):
    queryset = TagStatistics.objects.all()
    serializer_class = TagStatisticsSerializer


class TagStatisticsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TagStatistics.objects.all()
    serializer_class = TagStatisticsSerializer


class SuiteList(generics.ListCreateAPIView):
    queryset = Suite.objects.all()
    serializer_class = SuiteSerializer


class SuiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Suite.objects.all()
    serializer_class = SuiteSerializer


class TestList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestTagList(generics.ListCreateAPIView):
    queryset = TestTag.objects.all()
    serializer_class = TestTagSerializer


class TestTagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestTag.objects.all()
    serializer_class = TestTagSerializer


class KeywordList(generics.ListCreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class KeywordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class KeywordTagList(generics.ListCreateAPIView):
    queryset = KeywordTag.objects.all()
    serializer_class = KeywordTagSerializer


class KeywordTagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KeywordTag.objects.all()
    serializer_class = KeywordTagSerializer


class ArgumentList(generics.ListCreateAPIView):
    queryset = Argument.objects.all()
    serializer_class = ArgumentSerializer


class ArgumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Argument.objects.all()
    serializer_class = ArgumentSerializer


class AssignList(generics.ListCreateAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer


class AssignDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assign.objects.all()
    serializer_class = AssignSerializer


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
