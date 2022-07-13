$(document).ready(function () {

	function scroll_to($source_element, $target_element, speed) { 
	    $source_element.animate({
	        scrollTop:  $source_element.scrollTop() - $source_element.offset().top + $target_element.offset().top 
	    }, 
	    speed == undefined ? 1000 : speed); 
	}

	function create_message_div($original_word, $dictionary_word){
		$div = $('<div/>');
		
		$username_element = $('<h5/>')
		.addClass("title_case d-inline")
		.text($original_word)
		.appendTo($div);
		$time_element = $('<small/>')
		.addClass("pull-right text-muted")
		.html('<p><small>Nguồn<a href="https://tracau.vn/" target="_blank">  https://tracau.vn</a></small></p>')
		.appendTo($div);

		$value_element = $('<p/>')
		.html($dictionary_word)
		.appendTo($div);
		return $div;
	}

    
	function search_word(){
		$search_word_value = $("#search_word_text").val();
		$search_word_value = $.trim($search_word_value);
		if($search_word_value == ""){
			return;
		}
		$("#search_word_text").val("");
		$.ajax({
			url: '/words',
			data: {
				"word" : $search_word_value,
			},
			type: 'POST',
			success: function(response) {
				$new_div = create_message_div($search_word_value, response);
				$new_div.prependTo($("#message_area"));
				
			},
			error: function(error) {
				$new_div = create_message_div($search_word_value, false);
				$new_div.prependTo($("#message_area"));
			}
		});
		try{
			scroll_to($("#message_area"), $("#message_area>div"), 1500);
		}
		catch(err){

		}
	}



	$("#search_btn").on("click", function () {
		search_word();
	});
	$('#search_word_text').on('keypress', function (e) {
		if(e.which === 13){
			search_word();
		}
	});
	$("#clear_btn").on("click", function () {
		$("#message_area").html("");
	});			
})
