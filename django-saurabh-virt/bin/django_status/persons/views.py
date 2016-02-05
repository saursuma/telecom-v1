from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from persons.models import Persons
from forms import PersonForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.template import RequestContext

# Create your views here.

def persons(request):
	language = 'en-gb'
	session_language = 'en-gb'
	
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']

	return render_to_response('persons.html',{'persons': Persons.objects.all(),'language' : language,'session_language' : session_language})

def person(request, person_id=1):
	return render_to_response('person.html',{'person': Persons.objects.get(id=person_id) })

def language(request, language='en-gb'):
	response = HttpResponse("settings language to %s" % language)

	response.set_cookie('lang', language)

	request.session['lang'] = language
	return response

def create(request):
	#if request.POST:
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()
				
			return HttpResponseRedirect('/persons/all')
	
		else:
			raise Http404
		#else:
		#form = PersonForm()
                
	args = {}
	args.update(csrf(request))
	
	args['form'] = PersonForm()
	print args
	return render_to_response('create_person.html', args)



#def persons(request):
#	name = "Mike"
#	html = "<html> <body> Hi %s, this seems to have worked ! </body></html> " % name 
#	return HttpResponse(html)


#def hello_template(request):
#	name = 'Saurabh'
#	t = get_template('hello.html')
#	html = t.render(Context({'name' : name}))
#	return HttpResponse(html)

#def hello_template_simple(request):
#	name = 'SaurabhSuman'
#	return render_to_response('hello.html' , {'name' : name})

#class HelloTemplate(TemplateView):
	
#	template_name = 'hello_class.html'
	
#	def get_context_data(self, **kwargs):
#		context = super(HelloTemplate, self).get_context_data(**kwargs)
#		context['name'] = 'Mike'
#		return context


