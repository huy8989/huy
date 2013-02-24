from forms import TargetForm
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext 
from models import Target
import logging

def addTargetForm(request):
	return render_to_response('add_target.htm',context_instance=RequestContext(request))
@csrf_protect
def addTarget(request):
	if request.method=='POST':
		form = TargetForm(request.POST)
		if form.is_valid():
			tf = form.cleaned_data
			target = Target(name=tf['name'],time_allownace = tf['time_allownace'],
							comment=tf['comment'],user=request.user.get_full_name())
			target.save(force_insert=True )
			logging.debug(target)
		return HttpResponseRedirect('/result/')
	else:
		form = TargetForm()
	return render_to_response('add_target.htm',{'form':form})
	
	
def result(request):
	return render_to_response('success.htm')

def deleteTarget(request,id):
	target = Target.objects.get(id=id)
	target.delete()
	return HttpResponseRedirect('/myTargets/')

def showMyTargets(request):
	if request.user.is_authenticated():
		username = request.get_full_name()
		targets = Target.objects.filter(name=username)
		return render_to_response('targetList.htm',{'targets':targets})
		
	else:
		return HttpResponseRedirect('/login/')

