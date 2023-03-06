window.addEventListener("resize", function() {
    var width = window.innerWidth;
    var button = document.querySelector(".button");

    if (width < 600) {
        button.style.display = "block";
        button.style.margin = "0 auto";
        button.style.width = "100%";
    } else {
        if (button.classList.contains("next")) {
            button.style.float = "right";
        } else {
            button.style.float = "left";
        }

        button.style.display = "inline-block";
        button.style.margin = "";
        button.style.width = "";
    }
});

var button = document.querySelector(".button");

if (window.innerWidth < 600) {
    button.style.display = "block";
    button.style.margin = "0 auto";
    button.style.width = "100%";
} else {
    if (button.classList.contains("next")) {
        button.style.float = "right";
    } else {
        button.style.float = "left";
    }

    button.style.display = "inline-block";
    button.style.margin = "";
    button.style.width = "";
}




