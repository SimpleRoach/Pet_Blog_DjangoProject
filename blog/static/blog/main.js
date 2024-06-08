document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        var messages = document.querySelectorAll('.message');
        messages.forEach(function (message) {
            message.classList.add('fade-out');
        });
    }, 1000);
});