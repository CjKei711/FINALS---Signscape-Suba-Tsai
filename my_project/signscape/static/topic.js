document.addEventListener('DOMContentLoaded', function() {
    const topicBoxes = document.querySelectorAll('.topic-box');
    topicBoxes.forEach(box => {
        box.addEventListener('click', function(event) {
            event.preventDefault();
            window.location.href = this.getAttribute('href');
        });
    });
});