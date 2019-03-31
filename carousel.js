$(document).ready(function() {
		   
	var slider = $("#image_list");                    
	var leftProperty, newleftProperty;
					
	$("#right_button").click(function() { 
		
		leftProperty = parseInt(slider.css("left"));
		
		if (leftProperty - 100 <= -900) {
			newLeftProperty = 0; }
		else {
			newLeftProperty = leftProperty - 100; }
		
		slider.animate( {left: newLeftProperty}, 1000);
		
	});  
	
	$("#left_button").click(function() {
		
		leftProperty = parseInt(slider.css("left"));
		

		if (leftProperty < 0) {
			newLeftProperty = leftProperty + 100;
		}
		else {
			newLeftProperty = -800;
		}
		
		slider.animate( {left: newLeftProperty}, 1000);
						
	}); 		
}); 