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
            workoutsList[counter].style.backgroundColor = "#41DB00";
            counter++;
            plankComplete()
            trainingTime = Number(document.querySelector(".p-time").innerText)
            countdown()
        }
        else {
            workoutsList[counter].style.backgroundColor = "#41DB00";
        }
    }
    else {
        timer = setTimeout(countdown, 1000);
    }
};

function pause() {
    clearTimeout(timer)
};

// function forward() {
//     counter++;
//     console.log(counter)
//     pause()
//     if (counter <= workoutsList.length - 1) {
//         plankComplete()
//     }
//     else {
//         counter = 5;
//     }
// };

// function backward() {
//     counter--;
//     console.log(counter)
//     pause()
//     if (counter >= 0) {
//         plankComplete()
//         workoutsList[counter].style.backgroundColor = "whitesmoke";
//     }
//     else {
//         counter = 1;
//     }
// };

function plankComplete() {
    // Изображение
    document.getElementsByClassName("div-img-box")[0].children[0].src = document.getElementsByClassName("div-training")[counter].children[0].src
    // Заголовок
    document.getElementsByTagName("h2")[1].innerText = document.getElementsByClassName("div-training")[counter].getElementsByTagName("span")[0].innerText;
    // Время
    document.getElementsByClassName("p-time")[0].textContent = Number(document.getElementsByClassName("div-training")[counter].getElementsByTagName("span")[1].textContent.replace("s", ""));
};
