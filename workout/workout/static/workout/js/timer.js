let playStopButton = document.getElementById("play-stop");
let workoutsList = document.getElementsByClassName("div-training");

var counter = 0;
plankComplete(counter)

let timer;
let trainingTime = Number(document.getElementsByClassName("p-time")[0].textContent);


function timerWorkout() {
    if (playStopButton.src.includes("play")) {
        playStopButton.src = "../../../media/icons/pause.png"
        setTimeout(countdown, 1000)
    }
    else {
        pause()
        playStopButton.src = "../../../media/icons/play.png"
    }
}

function countdown() {
    document.querySelector(".p-time").innerText = trainingTime
    trainingTime--;

    if (trainingTime < 0) {
        if (counter < workoutsList.length - 1) {
            workoutsList[counter].style.backgroundColor = "#B3EAB6";
            counter++;
            plankComplete()
            trainingTime = Number(document.querySelector(".p-time").innerText)
            countdown()
        }
        else {
            workoutsList[counter].style.backgroundColor = "#B3EAB6";
        }
    }
    else {
        timer = setTimeout(countdown, 1000);
    }
};

function pause() {
    clearTimeout(timer)
};

function forward() {
    pause()
    if (counter < workoutsList.length - 1) {
        counter++;
        plankComplete()
        workoutsList[counter - 1].style.backgroundColor = "#B3EAB6";
        trainingTime = Number(document.getElementsByClassName("p-time")[0].textContent)

    }
    else {
        counter = workoutsList.length - 1;
    }
};

function backward() {
    pause()
    if (counter > 0) {
        counter--;
        plankComplete()
        workoutsList[counter].style.backgroundColor = "whitesmoke";
        trainingTime = Number(document.getElementsByClassName("p-time")[0].textContent)
    }
    else {
        counter = 0;
    }
};

function plankComplete() {
    // Изображение
    document.getElementsByClassName("div-img-box")[0].children[0].src = document.getElementsByClassName("div-training")[counter].children[0].src
    // Заголовок
    document.getElementsByTagName("h2")[1].innerText = document.getElementsByClassName("div-training")[counter].getElementsByTagName("span")[0].innerText;
    // Время
    document.getElementsByClassName("p-time")[0].textContent = Number(document.getElementsByClassName("div-training")[counter].getElementsByTagName("span")[1].textContent.replace("s", ""));
};
