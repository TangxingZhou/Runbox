from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Execution, ExecutionError, SuiteStatistics, TestStatistics, TagStatistics, Suite, Test, TestTag, \
    Keyword, KeywordTag, Argument, Assign, Message


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ExecutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Execution
        fields = ['id', 'taskid', 'generator', 'generated', 'rpa']


class ExecutionErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionError
        fields = ['id', 'execution_id', 'level', 'timestamp', 'text']


class SuiteStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuiteStatistics
        fields = ['id', 'execution_id', 'key', '_pass', '_fail', 'name', 'text', 'elapsed']


class TestStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestStatistics
        fields = ['id', 'execution_id', '_pass', '_fail', 'text', 'elapsed']


class TagStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagStatistics
        fields = ['id', 'execution_id', '_pass', '_fail', 'text', 'elapsed']


class SuiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suite
        fields = [
            'id', 'execution_id', 'key', 'name', 'source', 'doc', 'msg', 'parent_id', 'status',
            'starttime', 'endtime', 'elapsed'
        ]


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = [
            'id', 'suite_id', 'key', 'name', 'doc', 'msg', 'timeout', 'status',
            'starttime', 'endtime', 'elapsed', 'critical'
        ]


class TestTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTag
        fields = ['id', 'test_id', 'tag']


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = [
            'id', 'suite_id', 'test_id', 'name', 'library', 'type', 'doc', 'parent_id', 'timeout', 'status',
            'starttime', 'endtime', 'elapsed'
        ]


class KeywordTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordTag
        fields = ['id', 'keyword_id', 'tag']


class ArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Argument
        fields = ['id', 'keyword_id', 'arg']


class AssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assign
        fields = ['id', 'keyword_id', 'var']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'keyword_id', 'timestamp', 'level', 'text']
