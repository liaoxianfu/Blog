from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user_name', 'user_type', 'user_email', 'user_register_time'
    )
    # fk_fields = ('user_type', 'user_group')
    list_display_links = ('id', 'user_name', 'user_type',)
    list_filter = ('user_type', 'user_register_time')  # 过滤器
    # search_fields = ('user_name', 'user_group__group_name',)  # 搜索字段 外键字段需要使用双下线
    date_hierarchy = 'user_register_time'
    list_per_page = 20  # 每页显示的最大条数


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'tag',
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author', 'type', 'tag', 'create_date', 'update_date',
    )
    list_display_links = (
        'title', 'author', 'type', 'tag',
    )
    list_filter = (
        'author', 'type', 'tag',
    )
    search_fields = (
        'title', 'author', 'type', 'tag',
    )
    date_hierarchy = 'update_date'
    list_per_page = 20


@admin.register(FootInfo)
class FootInfo(admin.ModelAdmin):
    list_display = (
        'powerby', 'Register_Id', 'Design_By'
    )


class SecondNavigationBarInline(admin.StackedInline):
    model = SecondNavigationBar
    list_display = (
        'id', 'second_title', 'second_link',
    )


@admin.register(NavigationBar)
class NavigationBarAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'link', 'have_second_bar',
    )
    list_display_links = (
        'id', 'title', 'link', 'have_second_bar',
    )

    inlines = [SecondNavigationBarInline]


