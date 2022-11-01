from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from board.models import Blog


# Create your views here.
def main(request):
    return render(request, 'index.html')


class Create(View):
    def get(self, request):
        return render(request, 'create-board.html')

    def post(self, request):
        Blog(
            title=request.POST.get('title'),
            content=request.POST.get('content')
        ).save()
        return HttpResponseRedirect('/items/')


def find_all(request):
    boards = Blog.objects.values()
    ls = []
    for item in boards:
        d = dict()
        add_dic(d, item, ['id', 'title'])
        ls.append(d)
    return render(request, 'list-board.html', {'list': ls})


def add_dic(dic1, dic2, key):
    for k in key:
        dic1[k] = dic2[k]


class FindOne(View):
    def post(self, request, board_id):
        b = Blog(
            title=request.POST.get('title'),
            content=request.POST.get('content')
        )
        b.pk = board_id
        b.save()
        return HttpResponseRedirect('/items/')

    def get(self, request, board_id):
        board = get_object_or_404(Blog, pk=board_id)
        b = {'title': board.title, 'content': board.content}
        return render(request, 'item-board.html', b)


class Delete(View):
    def post(self, request, board_id):
        board = get_object_or_404(Blog, pk=board_id)
        Blog.delete(board)
        return HttpResponseRedirect('/items/')
