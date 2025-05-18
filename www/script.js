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

function playAssistant(message){
	if(message != ""){
		$("#oval").attr("hidden", true); 
		$("#SiriWave").attr("hidden", false);
		
		eel.takeAllCommand(message)

		$("#chatBox").val("")
		$("#micBtn").attr("hidden", false)
		$("#sendBtn").attr("hidden", true)
	}
}

function showHideSendBtn(message){
	if(message.length == 0){
		$("#micBtn").attr("hidden",false)
		$("#sendBtn").attr("hidden", true)
	}
	else{
		$("#micBtn").attr("hidden", true)
		$("#sendBtn").attr("hidden", false)
	}
}

$("#chatBox").keyup(function () {
	let message = $("#chatBox").val()
	showHideSendBtn(message)
})

$("#chatBox").keypress(function (e) {
	if(e.which == 13){//code for enter key
		let message = $("#chatBox").val()
		playAssistant(message)
	}
})

$("#sendBtn").click(function () {
	let message = $("#chatBox").val()
	playAssistant(message)
})