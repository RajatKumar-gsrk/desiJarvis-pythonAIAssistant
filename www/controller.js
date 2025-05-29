

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


    eel.expose(userText);
    function userText(msg){{
        let chatHistoryBody = document.getElementById("chatHistoryBody")
        if(msg.trim() !== ""){
            chatHistoryBody.innerHTML += `<div class="row justify-content-end mb-4">
                <div class = "userMsg">${msg}</div>
            </div>`

            chatHistoryBody.scrollTop = chatHistoryBody.scrollHeight;
        }
    }}


    eel.expose(assistantText);
    function assistantText(msg){{
        let chatHistoryBody = document.getElementById("chatHistoryBody")
        if(msg.trim() !== ""){
            chatHistoryBody.innerHTML += `<div class="row justify-content-start mb-4">
                <div class = "assistantMsg">${msg}</div>
            </div>`

            chatHistoryBody.scrollTop = chatHistoryBody.scrollHeight;
        }
    }}

    
});
