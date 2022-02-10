
var mode = 'dark'

function changeMode() {
    switch(mode) {
        case 'light':
            document.body.style.backgroundColor = "white";
            document.body.style.color = "black";
            var links = document.getElementsByTagName("a");
            for(var i=0;i<links.length;i++) { links[i].style.color = "black"; }
            mode = 'dark'
            break;
        case 'dark':
            document.body.style.backgroundColor = "black";
            document.body.style.color = "grey";
            var links = document.getElementsByTagName("a");
            for(var i=0;i<links.length;i++) { links[i].style.color = "grey"; }
            mode = 'light'
            break;
        default:
            document.body.style.backgroundColor = "white";
            document.body.style.color = "black";
            var links = document.getElementsByTagName("a");
            for(var i=0;i<links.length;i++) { links[i].style.color = "black"; }
    }
}

function currentTime() {
    var current_date_time = new Date();
    var date_now = current_date_time.toLocaleString(navigator.language, {day: '2-digit', month: '2-digit', year: 'numeric'});
    var weekday = current_date_time.toLocaleString(navigator.language, {weekday:'long'});
    var time_now = current_date_time.toLocaleString(navigator.language, {hour: '2-digit', minute:'2-digit', second:'2-digit'});
    document.getElementById("currentTime").innerHTML = time_now;
    document.getElementById("currentWeekday").innerHTML = weekday;
    document.getElementById("currentDate").innerHTML = date_now;
    var t = setTimeout(currentTime, 1000);
}

function tellTime() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/time/", true);
    xhttp.send();
}

function readWiki() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/speak/");
    xhttp.setRequestHeader(
        "Content-Type",
        "application/json;charset=UTF-8");
    /*title = document.getElementById("w_title").innerHTML */
    summary = document.getElementById("w_summary").innerHTML
    xhttp.send(JSON.stringify({"string": summary } ));
}

function bodyLoaded() {
    currentTime();
}
