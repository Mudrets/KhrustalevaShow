$(document).ready(function(){
	$(".addition").slice(0, 3).show();
	var f = true;
	$("#moreAdditions").on('click', function(e){
		if(f){
			e.preventDefault();
			$(".addition:hidden").slideDown();
			f = false;
		}else{
			e.preventDefault();
			$(".addition").slice(3).slideUp();
			f = true;
		}
	})
})