

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
    var current_date = new Date();
    var y = current_date.getFullYear();
    var n = current_date.getMonth() + 1;
    var d = current_date.getDate();
    var h = current_date.getHours();
    var m = current_date.getMinutes();
    var s = current_date.getSeconds();
    h = formatTime(h);
    m = formatTime(m);
    s = formatTime(s);
    var time_now = h + ':' + m + ':' + s;
    var date_now = d + '-' + n + '-' + y;
    document.getElementById("currentTime").innerHTML = time_now;
    document.getElementById("currentDate").innerHTML = date_now;
    var t = setTimeout(currentTime, 500);
}

function formatTime(i) {
    if (i < 10) {i = "0" + i};
    return i;
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
