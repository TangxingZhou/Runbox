from django.db import models

# Create your models here.


class Execution(models.Model):

    taskid = models.CharField(max_length=50, unique=True)
    generator = models.CharField(max_length=100)
    generated = models.CharField(max_length=21)
    rpa = models.CharField(max_length=5)

    class Meta:
        db_table = 'executions'


class ExecutionError(models.Model):

    execution = models.ForeignKey(Execution, on_delete=models.CASCADE)
    level = models.CharField(max_length=10)
    timestamp = models.CharField(max_length=21)
    text = models.TextField()

    class Meta:
        db_table = 'execution_errors'


class SuiteStatistics(models.Model):

    execution = models.ForeignKey(Execution, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    _pass = models.CharField(max_length=10)
    _fail = models.CharField(max_length=10)
    name = models.TextField()
    text = models.TextField()
    elapsed = models.IntegerField(null=True)

    class Meta:
        db_table = 'suite_statistics'


class TestStatistics(models.Model):

    execution = models.ForeignKey(Execution, on_delete=models.CASCADE)
    _pass = models.CharField(max_length=10)
    _fail = models.CharField(max_length=10)
    text = models.TextField()
    elapsed = models.IntegerField(null=True)

    class Meta:
        db_table = 'test_statistics'


class TagStatistics(models.Model):

    execution = models.ForeignKey(Execution, on_delete=models.CASCADE)
    _pass = models.CharField(max_length=10)
    _fail = models.CharField(max_length=10)
    text = models.TextField()
    elapsed = models.IntegerField(null=True)

    class Meta:
        db_table = 'tag_statistics'


class Suite(models.Model):

    execution = models.ForeignKey(Execution, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    name = models.TextField()
    source = models.TextField(null=True)
    doc = models.TextField(null=True)
    msg = models.TextField(null=True)
    parent_id = models.IntegerField(null=True)
    status = models.CharField(max_length=10)
    starttime = models.CharField(max_length=21)
    endtime = models.CharField(max_length=21)
    elapsed = models.IntegerField(null=True)

    class Meta:
        db_table = 'suites'


class Test(models.Model):

    suite = models.ForeignKey(Suite, on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    name = models.TextField()
    doc = models.TextField(null=True)
    msg = models.TextField(null=True)
    timeout = models.TextField(null=True)
    status = models.CharField(max_length=10)
    starttime = models.CharField(max_length=21)
    endtime = models.CharField(max_length=21)
    elapsed = models.IntegerField(null=True)
    critical = models.CharField(max_length=5)

    class Meta:
        db_table = 'tests'


class TestTag(models.Model):

    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    tag = models.TextField()

    class Meta:
        db_table = 'test_tags'


class Keyword(models.Model):

    suite = models.ForeignKey(Suite, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    name = models.TextField()
    library = models.TextField(null=True)
    type = models.CharField(max_length=20, null=True)
    doc = models.TextField(null=True)
    parent_id = models.IntegerField(null=True)
    timeout = models.TextField(null=True)
    status = models.CharField(max_length=10)
    starttime = models.CharField(max_length=21)
    endtime = models.CharField(max_length=21)
    elapsed = models.IntegerField(null=True)

    class Meta:
        db_table = 'keywords'


class KeywordTag(models.Model):

    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    tag = models.TextField()

    class Meta:
        db_table = 'keyword_tags'


class Argument(models.Model):

    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    arg = models.TextField()

    class Meta:
        db_table = 'keyword_arguments'


class Assign(models.Model):

    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    var = models.TextField()

    class Meta:
        db_table = 'keyword_assigns'


class Message(models.Model):

    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=21)
    level = models.CharField(max_length=10)
    text = models.TextField()

    class Meta:
        db_table = 'keyword_messages'
