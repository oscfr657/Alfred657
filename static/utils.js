
let mode = 'dark'

function changeMode() {
    let links = document.getElementsByTagName("a");
    switch(mode) {
        case 'light':
            document.body.style.backgroundColor = "white";
            document.body.style.color = "black";
            for(let i=0;i<links.length;i++) { links[i].style.color = "black"; }
            mode = 'dark'
            break;
        case 'dark':
            document.body.style.backgroundColor = "black";
            document.body.style.color = "grey";
            for(let i=0;i<links.length;i++) { links[i].style.color = "grey"; }
            mode = 'light'
            break;
        default:
            document.body.style.backgroundColor = "white";
            document.body.style.color = "black";
            for(let i=0;i<links.length;i++) { links[i].style.color = "black"; }
    }
}

function currentTime() {
    let current_date_time = new Date();
    let date_now = current_date_time.toLocaleString('sv-SE', {day: '2-digit', month: '2-digit', year: 'numeric'});
    let weekday = current_date_time.toLocaleString(navigator.language, {weekday:'long'});
    let time_now = current_date_time.toLocaleString('sv-SE', {hour: '2-digit', minute:'2-digit', second:'2-digit'});
    document.getElementById("currentTime").innerHTML = time_now;
    document.getElementById("currentWeekday").innerHTML = weekday;
    document.getElementById("currentDate").innerHTML = date_now;
    checkAndReportTodo(current_date_time);
    let t = setTimeout(currentTime, 1000);
}

function tellTime() {
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/time/", true);
    xhttp.send();
}

function readWiki() {
    summary = document.getElementById("w_summary").innerHTML;
    readThis(summary);
}

function checkAndReportTodo(date_time) {
    let date_time_string = date_time.toLocaleString(
            'sv-SE', 
            { year: 'numeric', month: '2-digit', day: '2-digit', 
              hour: '2-digit', minute:'2-digit', second:'2-digit'
            });
    event_list = document.getElementById("cal_events").getElementsByTagName('p');
    for (let i=0, event; event = event_list[i]; i++) {
        if (event.dataset.datetime == date_time_string) {
            console.log(event.dataset.what);
            let timeFor = 'It is time for ' + event.dataset.what;
            readThis(timeFor);
            location.reload();
            break;
        }
    }
}

function readThis(text) {
    let xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/speak/");
    xhttp.setRequestHeader(
        "Content-Type",
        "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({"string": text } ));
}

function bodyLoaded() {
    currentTime();
}
