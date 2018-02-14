from django.shortcuts import render, get_object_or_404
from . import models


def header_info():
    navigation_bars = models.NavigationBar.objects.all().order_by('id')
    return navigation_bars


def foot_info():
    info = models.FootInfo.objects.first()
    return info


def page_list(id, articles_list, articles_list_count):
    """

    :param id: 网页ud
    :param articles_list:orm拿到的文章集合
    :return: id, page, have_pre, have_next, articles_list
    """

    have_pre = True
    have_next = True
    if articles_list_count % 6 != 0:
        page = articles_list_count // 6 + 1
    else:
        page = articles_list_count // 6

    if not id:
        id = 1
    id = int(id)
    if id <= 1:
        have_pre = False
    if id >= page:
        have_next = False
    if id < 1:
        id = 1
    if id <= page:
        articles_list = articles_list[6 * (int(id) - 1):6 * int(id)]
    else:
        articles_list = articles_list[6 * (int(page) - 1):6 * int(page)]
        id = page
    return id, page, have_pre, have_next, articles_list


def index(request, id):
    """
    index首页页面
    :param request:
    :param id:
    :return:
    """
    articles_list = models.Article.objects.all().order_by('-update_date')
    articles_list_count = models.Article.objects.all().count()
    hot_articles = models.Article.objects.all().order_by('-views')[:10]
    id, page, have_pre, have_next, articles_list = page_list(id=id, articles_list=articles_list,
                                                             articles_list_count=articles_list_count)
    # print(id)
    info = foot_info()
    img = ['img_1.jpg', 'img_2.jpg', 'img_3.jpg', 'img_4.jpg', 'img_5.jpg', 'img_6.jpg', ]
    context = {'articles_list': articles_list,
               'hot_articles': hot_articles,
               'page': page, 'id': id,
               'have_pre': have_pre,
               'have_next': have_next,
               'foot_info': info,
               'navigation_bar': header_info(),
               'img':img,
               'time': 1,
               }
    return render(request, 'gufeng/index/index.html', context=context)


# def articles(request):
#     return render(request, 'gufeng/articles/articles.html')


def article_detail(request, id):
    article = get_object_or_404(models.Article, pk=id)
    article.increase_views()

    pre_title = models.Article.objects.filter(id=str(int(id) + 1)).first()

    next_title = models.Article.objects.filter(id=str(int(id) - 1)).first()
    info = foot_info()
    context = {
        'article': article,
        'pre_title': pre_title,
        'next_title': next_title,
        'foot_info': info,
        'navigation_bar': header_info(),

    }
    return render(request, 'gufeng/article_content/detail.html', context=context)


def article_category(request, name, id):
    articles_list = models.Article.objects.filter(tag__tag=name).order_by('-update_date')
    articles_list_count = models.Article.objects.filter(tag__tag=name).order_by('-update_date').count()
    id, page, have_pre, have_next, articles_list = page_list(id=id, articles_list=articles_list,
                                                             articles_list_count=articles_list_count)

    info = foot_info()
    context = {
        'articles_list': articles_list,
        'name': name,
        'page': page,
        'id': id,
        'have_pre': have_pre,
        'have_next': have_next,
        'foot_info': info,
        'navigation_bar': header_info(),
    }
    return render(request, 'gufeng/articles/articles.html', context=context)
