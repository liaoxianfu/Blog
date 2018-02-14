from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class User(models.Model):
    sex_choice = (
        (0, r'男'),
        (1, r'女'),
    )
    type_choice = (
        (0, r'普通用户'),
        (1, r'管理员'),
        (2, r'超级管理员'),
        (3, r'站长'),
    )
    user_name = models.CharField(max_length=30, verbose_name='用户名')
    user_email = models.EmailField(max_length=30, verbose_name='邮箱')
    user_password = models.CharField(max_length=12, verbose_name='用户密码')
    user_type = models.IntegerField(choices=type_choice, default=0)
    user_register_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['id']


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
        ordering = ['id']


class Article(models.Model):
    type_choice = (
        (0, r'原创'),
        (1, r'转载'),
        (2, r'翻译'),
        (3, r'其他'),
    )
    title = models.CharField(max_length=200, verbose_name='标题')
    type = models.IntegerField(choices=type_choice, verbose_name='类型')
    article = RichTextUploadingField(max_length=5000, verbose_name='正文')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='最后一次更新')
    author = models.ForeignKey(User, verbose_name='作者')
    tag = models.ForeignKey(Tag, verbose_name='标签')
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        verbose_name = '博文'
        verbose_name_plural = '博文'
        ordering = ['-update_date']


class FootInfo(models.Model):
    powerby = models.CharField(max_length=100, default=u'过不去的过去', verbose_name='版权')
    Register_Id = models.CharField(max_length=100, default=u'豫ICP备17028946号', verbose_name='备案号')
    Design_By = models.CharField(max_length=100, default=u'过不去的过去', verbose_name='设计者')

    class Meta:
        verbose_name = '版权'
        verbose_name_plural = '版权'
        ordering = ['-id']


class NavigationBar(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    link = models.CharField(max_length=200, verbose_name='链接')
    have_second_bar = models.BooleanField(default=False, verbose_name='是否有二级菜单')

    class Meta:
        verbose_name = '导航栏设置'
        verbose_name_plural = '导航栏设置'


class SecondNavigationBar(models.Model):

    second_title = models.CharField(max_length=30, verbose_name='二级标题', blank=True, null=True)
    second_link = models.CharField(max_length=200, verbose_name='二级链接', blank=True, null=True)
    NavigationBar = models.ForeignKey(NavigationBar)

    class Meta:
        verbose_name = '二级导航栏设置'
        verbose_name_plural = '二级导航栏设置'
