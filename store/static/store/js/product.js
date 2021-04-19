$(document).ready(() => {
    $(".list__filter").click(function(e) {
        e.preventDefault();
        const categoryId = this.id;
        $.ajax({
            type: "get",
            url: "/",
            data: {
                category_id: categoryId,
            },
            dataType: "json",
            success: function(response) {
                console.log("response is : ", response);
                $(".product__display").replaceWith(
                    "<h1>Here is the required data !" + response + " </h1>"
                );
            },
        });
    });
});