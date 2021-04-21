$(document).ready(() => {
    $("#filter__l2h").click(function(e) {
        e.preventDefault();
        const filter = "l2h";
        var output = "";

        // making ajax call
        $.ajax({
            type: "GET",
            url: "/",
            data: {
                get_filter: filter,
            },
            dataType: "json",
            success: function(response) {
                const allUseRecords = response;
                console.log("response is: ", allUseRecords);
                for (record in allUseRecords) {
                    output +=
                        "<div class='row mx-auto'>" +
                        "<div class='card shadow p-3 mb-5 bg-white rounded mx-auto mb-3' style='width: 18rem;'>" +
                        "<img class='card-img-top' style='width: 100%; height: 20rem;' " +
                        "src = 'http://localhost:8000/images/" +
                        allUseRecords[record]["image"] +
                        "'/> " +
                        "<div class='card-body'>" +
                        "<h5 class='card-title'></h5>" +
                        "<p class='card-text' style='width: 100%; height: 4rem;'><br></p></div>" +
                        "<a href='#' class='btn btn-outline-secondary btn-lg'>" +
                        "Add To Cart" +
                        "</a>" +
                        "</div></div>";
                }

                $(".product__body").html(output);
            },
        });
    });
});