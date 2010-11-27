// http://www.learningjquery.com/2007/10/a-plugin-development-pattern

;(function($){
	
	var PROTOCOL = 'http://';
	var DOMAIN = 'hulse.me';
	
	$.fn.embed = function($_options) {
		
		if (this.length > 0) {
			
			// Build main options before element iteration:
			var $settings = $.extend({}, $.fn.embed.defaults, $_options);
			
			return this.each(function() {
					
					var $this = $(this);
					new $.embed($this, $settings);
				
			});
			
		}
		
	};
	
	$.embed = function($_this, $_settings) {
		
		var css = $_settings.css || PROTOCOL + 'assets.' + DOMAIN + '/apps/code/css/embed.css';
		
		if ($('link[title="embed"]').length <= 0) {
			$('<link title="embed" rel="stylesheet" type="text/css" href="' + css + '">').appendTo('head');
		}
		
		var t_sid = $_this.attr('id').substring(4); // Everything after "sid_".
		
		$.getJSON(PROTOCOL + 'code.' + DOMAIN + '/' + t_sid + '.json?callback=?', function(d) {
			
			var $x = d.data;
			var code_splitted = $.trim($x.code_highlighted).split(/\n/);
			var numbers = '';
			var lines = '';
			var str = '';
			
			for (var i = 1, j = code_splitted.length; i <= j; i++) {
				numbers += '<a class="number" href="#l' + i + '">' + i + '</a>';
				lines += '<span class="line" id="l' + i + '">' + (code_splitted[i-1] || '&nbsp;') + '</span>';
			}
			
			str += '<div class="embed">';
				str += '<ul><li><a href="' + PROTOCOL + 'code.' + DOMAIN + '/' + t_sid + '.txt">Raw</a></li><li><a href="' + PROTOCOL + 'code.' + DOMAIN + '/' + t_sid + '.embed">Embed</a></li></ul>';
				str += '<table cellpadding="0" cellspacing="0"><tr><th><pre>' + numbers + '</pre></th><td><pre>' + lines + '</pre></td></tr></table>';
			str += '</div>';
			
			$_this.html(str);
			
			_call_back($_settings.on_loaded, $_this);
			
		});
		
	};
	
	function _call_back($_fun, $_obj) {
		
		if ($.isFunction($_fun)) {
			$_fun.call($_obj);
		}
		
	};
	
	$.fn.embed.defaults = {
		
		css: '',                // Override default css.
		on_loaded: function(){} // Callback when everything is ready to show.
		
	};
	
})(jQuery);