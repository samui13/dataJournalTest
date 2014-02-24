userUI = {};
userUI.beforeButton = function(){
    $('#mapData').html('');
};
userUI.getAround = function(){
    userUI.beforeButton();
    var t = $.fn.deferrAjax('./json/radius?r=10');
    return userUI.setHtml(t);
};
userUI.getAll = function(offset,limit){
    userUI.beforeButton();
    var t = $.fn.deferrAjax('./json/all?l10');
    return userUI.setHtml(t);
};

userUI.__viewTemplate = '\
<h2>{{data.name}}</h2>\n\
<p>{{data.comment}}</p>\n\
<p>{{data.lat}},{{data.lng}}</p>\n\
';

userUI.setHtml = function(obj){
    return $.when(obj).done(function(){
	console.log(obj.data);
	for(var key in obj.data){
	    var data = obj.data[key];
	    var html = $('<div>');
	    html.html(Mustache.render(userUI.__viewTemplate,{
		data:data,
	    }));
	    html.appendTo($('#mapData'));
	    console.log(html.html());
	}
    });
};

(function($){
//    userUI.getAround();  
})(jQuery);
