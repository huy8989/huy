from forms import TargetForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from models import Target
import logging


def addTargetForm(request):
    return render_to_response('add_target.htm', context_instance=RequestContext(request))


@csrf_protect
def addTarget(request):
    if request.method == 'POST':
        form = TargetForm(request.POST)
        if form.is_valid():
            tf = form.cleaned_data
            target = Target(
                name=tf['name'], time_allownace=tf['time_allownace'],
                comment=tf['comment'], user=request.user.username)
            target.save(force_insert=True)
            logging.debug(target)
        return HttpResponseRedirect('/result/')
    else:
        form = TargetForm()
    return render(request, 'add_target.htm')


def result(request):
    return render_to_response('success.htm')


def deleteTarget(request, id):
    target = Target.objects.get(id=id)
    target.delete()
    return HttpResponseRedirect('/myTargets/')


def showMyTargets(request):
    if request.user.is_authenticated():
        username = request.user.username
        targets = Target.objects.filter(user=username)

        # return
        # render_to_response('targetList.htm',{'targets':targets},context_instance=RequestContext(request))
        return render(request, 'targetList.htm', {'targets': targets})

    else:
        return HttpResponseRedirect('/login/')
