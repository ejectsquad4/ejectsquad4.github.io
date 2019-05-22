// getting modal OPEN buttons:
var modalBtns = document.querySelectorAll(".modal-open");

//ABRINDO Modais ao clicar nos botoes
modalBtns.forEach(function (btn) {
    btn.onclick = function () {
        var modal = btn.getAttribute("data-modal");
        document.getElementById(modal).style.display = "block";
    };
});

// getting modal CLOSE buttons:
var closeBtns = document.querySelectorAll(".modal-close");

//FECHANDO Modais
closeBtns.forEach(function (btn) {
    btn.onclick = function () {
        var modal = (btn.closest(".modal").style.display = "none");
    };
})

window.onclick = function (e) {
    if (e.target.className === "modal") {
        e.target.style.display = "none"
    }
}