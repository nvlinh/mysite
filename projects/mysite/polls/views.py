from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . models import Question, Choice
from django.shortcuts import render, get_object_or_404


def index(request):
    lasted_questions = Question.objects.order_by('pub_date')[:5]
    context = {'lasted_questions': lasted_questions}
    return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    model = Question
    template_name = 'polls/detail.html'
    return render(request, template_name, {'question': get_object_or_404(Question, pk=question_id)})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
