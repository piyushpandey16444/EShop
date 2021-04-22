$(document).ready(() => {
    $(".ap_customer_uname").click(function(e) {
        e.preventDefault();
        $(".ap_customer_uname").css("box-shadow", "0px 0px 5px 2px #f09f26");
        $(".ap_customer_uname").css("outline-color", "#c97800");
    });
});