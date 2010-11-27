from django import forms
from cab.models import Snippet

class SnippetForm(forms.ModelForm):

#	language = forms.ChoiceField(
#		choices=LEXER_LIST_ALL,
#		initial=LEXER_DEFAULT,
#	)
	
	class Meta:
		model = Snippet
#		fields = (
#			'title',
#			'code',
#			'language_code',
#		)
		exclude = [
			'author',
		]