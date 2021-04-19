$(document).ready(() => {
    $(".list__filter").click(function(e) {
        console.log(this.id);
        e.preventDefault();
    });
});