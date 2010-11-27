from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound
from pygments import highlight

LEXER_ALL = sorted([(i[0], i[0]) for i in get_all_lexers() if len(i[0]) > 0])
LEXER_CODE = sorted([(i[1][0], i[1][0]) for i in get_all_lexers() if len(i[1]) > 0])

class NakedHtmlFormatter(HtmlFormatter):
	def wrap(self, source, outfile):
		return self._wrap_code(source)
	def _wrap_code(self, source):
#		yield 0, '<pre>'
		for i, t in source:
			yield i, t
#		yield 0, '</pre>'

def pygmentize(code_string, lexer_name='text'):
	return highlight(
		code_string,
		get_lexer_by_name(lexer_name, encoding='utf-8'),
		NakedHtmlFormatter(
			#linenos='inline',
			#noclasses=True,
			style='native',
			#lineanchors='lineno',
			#anchorlinenos=True,
			encoding='utf-8',
		)
	)
