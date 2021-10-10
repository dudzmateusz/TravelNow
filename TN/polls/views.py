import json
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse , reverse_lazy
from django.views import generic
from django.utils import timezone
from django.views.generic import CreateView
from .get_schedule import connect_schedule
from .get_place import place,test
from .get_weather import weather
from .models import Choice, Question , Schedule
from django.views.generic import UpdateView
from .forms import ScheduleForm
from .map import generate_map




class ScheduleListView(generic.ListView):
    model = Schedule
    context_object_name = 'polls'

class ScheduleCreateView(CreateView):
    model = Schedule
    form_class = ScheduleForm
    success_url = reverse_lazy('schedule_list')


    def login(request):
        z = ''
        if request.method == "POST":
            # Get the posted form
            MyLoginForm = ScheduleForm(request.POST)

            if MyLoginForm.is_valid():
                originplace = MyLoginForm.cleaned_data['originplace']
                outboundpartialdate = MyLoginForm.cleaned_data['outboundpartialdate']
                destinationplace = MyLoginForm.cleaned_data['destinationplace']
                inboundpartialdate = MyLoginForm.cleaned_data['inboundpartialdate']
                telephone = MyLoginForm.cleaned_data['telephone']
                adults = MyLoginForm.cleaned_data['adults']
                pl = place(originplace)
                op = ''
                dp = ''
                for i in pl['Places']:
                    if originplace in i['PlaceName']:
                        op = i['PlaceId']
                pl2 = place(destinationplace)
                for i in pl2['Places']:
                    if destinationplace in i['PlaceName']:
                        dp = i['PlaceId']
                z = connect_schedule(op, str(outboundpartialdate), dp, str(inboundpartialdate))
                iat = []
                for i in z['Places']:
                    if originplace in i['Name'] or originplace in i['CityName']:
                        iat.append(i['IataCode'])
                    if destinationplace in i['Name'] or destinationplace in i['CityName']:
                        iat.append(i['IataCode'])
                zx = test(iat)
                check_weather = weather(destinationplace)
                generate_map(destinationplace,inboundpartialdate,outboundpartialdate,adults)



        else:
            MyLoginForm = ScheduleForm()

        c = {'z':z,
            'zx':zx,
            'zw':check_weather,
             }
        return render(request, 'polls/schedule_form_update.html', context=c)

    def testa(request):
        return render(request, 'polls/list_of_hotels.html')

    def form_valid(self, form):
        form.save()
        super(ScheduleCreateView,self).form_valid(form)
        return ScheduleCreateView.login(self.request)

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