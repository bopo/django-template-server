var us = navigator.userAgent.toLowerCase();

$(function(){
	if((us.indexOf('android') > -1 || us.indexOf('linux') > -1) || navigator.platform.toLowerCase().indexOf('linux') != -1 || us.indexOf('iphone') > -1 || us.indexOf('ipad') > -1){
   		window.location.href="h5/"; 	
    }
	$('#ios').click(function(){
		$('.mask').show();
		setTimeout(function(){
			$('.mask').hide();
		},3000)
	})
})
   
    


