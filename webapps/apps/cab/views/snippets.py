#from django.http import HttpResponseRedirect, HttpResponseForbidden
#from django.forms import ModelForm
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from cab.models import Snippet
#from cab.forms import SnippetForm

"""
class SnippetForm(ModelForm):
	class Meta:
		model = Snippet
		exclude = [
			'author',
		]
"""

"""
def snippet_add(request):
	if request.method == 'POST':
		form = SnippetForm(data=request.POST)
		if form.is_valid():
			new_snippet = form.save(commit=False)
			new_snippet.author = request.user
			new_snippet.save()
			return HttpResponseRedirect(new_snippet.get_absolute_url())
	else:
		form = SnippetForm()
	return render_to_response(
		'cab/snippet_form.html',
		{ 'form': form, 'add': True },
		context_instance=RequestContext(request)
	)
snippet_add = login_required(snippet_add)
"""

"""
def snippet_edit(request, snippet_id):
	snippet = get_object_or_404(Snippet, sid=snippet_id)
	if request.user.id != snippet.author.id:
		return HttpResponseForbidden()
	if request.method == 'POST':
		form = SnippetForm(instance=snippet, data=request.POST)
		if form.is_valid():
			snippet = form.save()
			return HttpResponseRedirect(snippet.get_absolute_url())
	else:
		form = SnippetForm(instance=snippet)
	return render_to_response(
		'cab/snippet_form.html', { 'form': form, 'add': False }, context_instance=RequestContext(request))
snippet_edit = login_required(snippet_edit)
"""

def snippet_list(request, template_name='cab/snippet_list.html'):
	
	try:
		snippet_list = Snippet.live.all()
	except ValueError:
		snippet_list = None
	
	template_context = {
		'object_list': snippet_list,
	}
	
	return render_to_response(
		template_name,
		template_context,
		RequestContext(request)
	)

def snippet_detail(request, snippet_id, template_name='cab/snippet_detail.html', is_raw=False, is_js=False):
	
	snippet = get_object_or_404(Snippet, sid=snippet_id)
	
	template_context = {
		'object': snippet,
	}

	response = render_to_response(
		template_name,
		template_context,
		RequestContext(request)
	)

	if is_raw:
		response['Content-Type'] = 'text/plain'
	
	if is_js:
		response['Content-Type'] = 'text/javascript'
	
	return response