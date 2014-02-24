
if (jQuery.when.once === undefined){
    jQuery.when.once = function(func) {
	var ran = false, memo;
	return function() {
	    if (ran) return memo;
	    ran = true;
	    return memo = func.apply(this, arguments);
	};
    }
}
if (jQuery.when.all===undefined) {
    jQuery.when.all = function(deferreds) {
        var deferred = new jQuery.Deferred();
        $.when.apply(jQuery, deferreds).then(
            function() {
                deferred.resolve(Array.prototype.slice.call(arguments));
            },
            function() {
                deferred.fail(Array.prototype.slice.call(arguments));
            });

        return deferred;
    }
}

jQuery.fn.getParamURL = function(url){
    if(typeof url  == 'undefined')
	var url = window.location.href;
    //var params = URL.split("?");
    //paramms   = params[1].split("&");
};

jQuery.fn.deferrAjax = function(url,param){
    // TODO
        /*
      if you use json url then params = {}
      if use jsonp url then 
      params = {
       dataType:'jsonp',
       jsonp: 'jsoncallback',
      } 
     */

    if(typeof params === 'undefined')
	params = {}
    if(!(typeof __callback  == 'function')){
	__callback = function(){};
    }

    var obj = {
	data:'',
	url:url,
	ajaxparam:{
	    type:'GET',
	    url: url,
	    dataType:'json',
	},
	__callback:__callback,
    };
    if(typeof params.ajaxparam === 'undefined'){
	var param = params;
    }else{
	var param = params.ajaxparam;
	for(var key in params){
	    if( typeof params[key] == 'object')
		continue;
	    obj.key = params[key];
	}
    }
    for(var key in param){
	obj.ajaxparam[key] = param[key];
    }
    obj.defer = $.Deferred();
    obj.ajax = $.ajax(obj.ajaxparam);
    obj.ajax.success(function(data){
	obj.data = data;
    });
    obj.ajax.error(function(){
	obj.defer.reject();
    });
    obj.setdone = function(__callback){
	obj.__callback = __callback;
    };
    obj.ajax.done(function(){
	obj.__callback();
	obj.defer.resolve();
    });
    obj.promise = function(){
	return this.defer.promise();
    };
    return obj;

};
jQuery.fn.ajaxRaw = function(url){
    //http://www.qript.co.jp/blog/technique/215/
    var obj = {
	data:{},
	url:url,
    };
    obj.defer = new $.Deferred;
    obj.xhr = new XMLHttpRequest();
    obj.xhr.open('GET',obj.url,true);
    obj.xhr.responseType = "arraybuffer";
    obj.xhr.onload = function() {
	var bytes = new Uint8Array(this.response);
	var binaryData = "";
	for (var i = 0, len = bytes.byteLength; i < len; i++) {
	    binaryData += String.fromCharCode(bytes[i]);
	}
	var bytes = new Uint8Array(this.response);
	if (bytes[0] === 0xff && bytes[1] === 0xd8 && bytes[bytes.byteLength-2] === 0xff && bytes[bytes.byteLength-1] === 0xd9) {
	    imgSrc = "data:image/jpeg;base64,";
	}
	else if (bytes[0] === 0x89 && bytes[1] === 0x50 && bytes[2] === 0x4e && bytes[3] === 0x47) {
	    imgSrc = "data:image/png;base64,";
	}
	else if (bytes[0] === 0x47 && bytes[1] === 0x49 && bytes[2] === 0x46 && bytes[3] === 0x38) {
	    imgSrc = "data:image/gif;base64,";
	}
	else if (bytes[0] === 0x42 && bytes[1] === 0x4d) {
	    imgSrc = "data:image/bmp;base64,";
	}
	else {
	    imgSrc = "data:image/unknown;base64,";
	}
	obj.imgRaw = imgSrc + window.btoa(binaryData);
	obj.defer.resolve();
    };
    obj.promise = function(){
	return obj.defer.promise();
    };
    obj.xhr.send();
    return obj;
};

(function(){
    var once_test = $.when.once(function(){
	console.log("TEST");
    });
    var two_test = $.when.once(function(){
	console.log("TEst2");
    });
    $(document).ready(function(){
	//once_test();
	//once_test();
	//two_test();
	//two_test();
    });
})();
