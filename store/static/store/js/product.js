$(document).ready(() => {
    $(".list__filter").click(function(e) {
        e.preventDefault();
        output = "";
        const categoryId = this.id;
        console.log("data found: making ajax call !", categoryId);

        // making ajax call
        $.ajax({
            type: "get",
            url: "/",
            data: {
                category_id: categoryId,
            },
            dataType: "json",
            success: function(response) {
                const allUseRecords = JSON.parse(response);
                console.log(allUseRecords);
                for (record in allUseRecords) {
                    output +=
                        "<div class='product__display container-fluid col-lg-10' >" +
                        "<div class='row mx-auto'>" +
                        "<div class='card mx-auto mb-3' style ='width: 18rem;'>" +
                        "<img src =" +
                        allUseRecords[record]["image"] +
                        "class='card-img-top' alt='...' style='width: 100%; height: 20rem;'>" +
                        "<div class='card-body'>" +
                        "<h5 class='card-title'>" +
                        allUseRecords[record]["name"] +
                        "</h5><p class='card-text' style='width: 100%; height: 4rem;'>" +
                        allUseRecords[record]["price"] +
                        "<br>" +
                        allUseRecords[record]["description"] +
                        "</p></div><a href='#' class='btn btn-outline-secondary btn-lg'>" +
                        "Add to Cart" +
                        "</a></div></div></div>";
                }
                $(".product__display").replaceWith(output);
            },
        });
    });
});