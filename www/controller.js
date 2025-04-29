$(document).ready(function (){
    eel.expose(displayMessage);
    function displayMessage(msg){
        $(".siriMsg li:first").text(msg);
        $(".siriMsg").textillate("start");
    }

    eel.expose(displayMessageReset);
    function displayMessageReset(){
        $(".siriMsg li:first").text("Hello I am D.J! nice to meet you");
        $(".siriMsg").textillate("start");
    }

    eel.expose(displayOval);
    function displayOval(){
        $("#oval").attr("hidden", false); 
	    $("#SiriWave").attr("hidden", true);
    }
});
