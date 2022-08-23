from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Choice, Question

'''
在我们的投票应用程序中，我们将有以下四个视图：

问题“索引”页面——显示最近的几个问题。
问题“详细信息”页面 - 显示问题文本，没有结果，但有投票表格。
问题“结果”页面 – 显示特定问题的结果。
投票操作 - 处理对特定问题中特定选项的投票。
'''


# def index(request): # 教学写法
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     template = loader.get_template('firstlink/index.html')  # 读取模板文件
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):  # 使用render()的最优写法
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'firstlink/index.html', context)


class IndexView(generic.ListView):
    template_name = 'firstlink/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'firstlink/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'firstlink/results.html'


# Leave the rest of the views (detail, results, vote) unchanged


# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)
#     try:  # 引发404错误写法
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'firstlink/detail.html', {'question': question})


def detail(request, question_id):  # 使用get_object_or_404()最优写法
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'firstlink/detail.html', {'question': question})


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'firstlink/results.html', {'question': question})


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'firstlink/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1  # 数据库字段累计+1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('firstlink:results', args=(question.id,)))  # 重定向
