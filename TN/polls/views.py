import json

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse , reverse_lazy
from django.views import generic
from django.utils import timezone
from django.views.generic import CreateView
from .get_schedule import connect_schedule
from .get_place import place
from .get_country import get_country_code
from .models import Choice, Question , Schedule
from django.views.generic import UpdateView
from .forms import ScheduleForm


def login(request):
    country = ''
    z = ''
    print('login')
    if request.method == "POST":
        # Get the posted form
        MyLoginForm = ScheduleForm(request.POST)

        if MyLoginForm.is_valid():
            country = MyLoginForm.cleaned_data['country']
            originplace = MyLoginForm.cleaned_data['originplace']
            outboundpartialdate = MyLoginForm.cleaned_data['outboundpartialdate']
            destinationplace = MyLoginForm.cleaned_data['destinationplace']
            inboundpartialdate = MyLoginForm.cleaned_data['inboundpartialdate']
            print(country,originplace,outboundpartialdate,destinationplace,inboundpartialdate)
            pl  = place(originplace)
            op = ''
            dp = ''
            for i in pl['Places']:
                op = i['PlaceId']
            pl2  = place(destinationplace)
            for i in pl2['Places']:
                dp = i['PlaceId']

            gcc_f = get_country_code(country)
            print(op,dp,gcc_f)
            z = connect_schedule(gcc_f,op,outboundpartialdate,dp,inboundpartialdate)

    else:
        MyLoginForm = ScheduleForm()

    return render(request, 'polls/schedule_form_update.html', z)

class ScheduleListView(generic.ListView):
    model = Schedule
    context_object_name = 'polls'


class ScheduleCreateView(CreateView):
    model = Schedule
    fields = ('country', 'originplace', 'outboundpartialdate', 'destinationplace', 'inboundpartialdate')
    success_url = reverse_lazy('schedule_list')


    def get_success_url(self):
        print('ScheduleCreateView')
        return reverse('polls:schedule')

class ScheduleUpdateView(UpdateView):
    model = Schedule
    form_class = ScheduleForm
    template_name = 'polls/schedule_form_update.html'

    def get_success_url(self):
        return reverse('polls:schedule')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

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