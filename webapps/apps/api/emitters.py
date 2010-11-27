from django.utils import simplejson
from django.core.serializers.json import DateTimeAwareJSONEncoder

from piston.emitters import Emitter

class ExtJSONEmitter(Emitter):
	"""
	JSON emitter, understands timestamps, wraps result set in object literal
	for Ext JS compatibility
	"""
	def render(self, request):
		cb = request.GET.get('callback', 'oontz')
		ext_dict = {
			'success': True,
			'data': self.construct(),
			#'message': 'Something good happened on the server!'
		}
		seria = simplejson.dumps(ext_dict, cls=DateTimeAwareJSONEncoder, ensure_ascii=False, indent=4)

		# Callback
		if cb:
			return '%s(%s)' % (cb, seria)

		return seria
	
Emitter.register('json', ExtJSONEmitter, 'application/json; charset=utf-8')
