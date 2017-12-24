var us = navigator.userAgent.toLowerCase();
var android ='http://apkcdn.kxtop.com/mm/mmpic_v1.1.9.apk';
var ios = '#';

$(function(){
	if((us.indexOf('android') > -1 || us.indexOf('linux') > -1) || navigator.platform.toLowerCase().indexOf('linux') != -1 || us.indexOf('iphone') > -1 || us.indexOf('ipad') > -1){}else{window.location.href="../";}
	$('#downBtn').click(function(){
		down();
	})
})
function down(){    
    if ((us.indexOf('android') > -1 || us.indexOf('linux') > -1) || navigator.platform.toLowerCase().indexOf('linux') != -1) {
    	if (us.indexOf('micromessenger') > -1){
    		$('#wechat').show();
    	}
    	
        //安卓地址跳转
        location.href=android;
        return false;
        console.log(android)
    }
    else if (us.indexOf('iphone') > -1 || us.indexOf('ipad') > -1) {
    	//IOS地址跳转
        location.href=ios;
        return false;
        console.log(ios)
    }
}

