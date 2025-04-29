$(document).ready(function () {
	$('.ask_question').textillate({
		in:{
			effect: "fadeInUp"
		},

		out:{
			effect: "fadeOutDown"
		},

		loop: true
	});
});

$(document).ready(function () {
	$('.siriMsg').textillate({
		in:{
			effect: "fadeInUp"
		},

		out:{
			effect: "fadeOutDown"
		},

		loop: true
	});
});


// video 5

if (jQuery) {
    console.log("jquery is loaded");
} else {
    console.log("Not loaded");
}

$("#micBtn").click( function () { 
	eel.soundAssistant();
	$("#oval").attr("hidden", true); 
	$("#SiriWave").attr("hidden", false);
	eel.takeAllCommand();
});