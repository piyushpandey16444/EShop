$(document).ready(() => {
    // code for low-to-high price btn click handle
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
                console.log("response is: ", allUseRecords["response"]);
                for (record in allUseRecords["response"]) {
                    output +=
                        "<div class='d-inline-flex'><div class='no-gutters'>" +
                        "<div class='card shadow p-3 mb-5 bg-white rounded ml-3' style='width: 18rem;'>" +
                        "<img class='card-img-top' style='width: 100%; height: 20rem;' " +
                        "src = 'http://localhost:8000/images/" +
                        allUseRecords["response"][record]["image"] +
                        "'/> " +
                        "<div class='card-body'>" +
                        "<h5 class='card-title'>" +
                        allUseRecords["response"][record]["name"] +
                        "</h5>" +
                        "<p class='card-text' style='width: 100%; height: 4rem;'>" +
                        allUseRecords["response"][record]["price"] +
                        "<br>" +
                        allUseRecords["response"][record]["description"] +
                        "</p></div>" +
                        "<a href='#' class='btn btn-outline-secondary btn-lg'>" +
                        "Add To Cart" +
                        "</a>" +
                        "</div></div></div>";
                }

                $(".product__body").html(output);
            },
        });
    });

    // code for high-to-low price btn click handle
    $("#filter__h2l").click(function(e) {
        e.preventDefault();
        const filter = "h2l";
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
                for (record in allUseRecords["response"]) {
                    output +=
                        "<div class='d-inline-flex'><div class='no-gutters'>" +
                        "<div class='card shadow p-3 mb-5 bg-white rounded ml-3' style='width: 18rem;'>" +
                        "<img class='card-img-top' style='width: 100%; height: 20rem;' " +
                        "src = 'http://localhost:8000/images/" +
                        allUseRecords["response"][record]["image"] +
                        "'/> " +
                        "<div class='card-body'>" +
                        "<h5 class='card-title'>" +
                        allUseRecords["response"][record]["name"] +
                        "</h5>" +
                        "<p class='card-text' style='width: 100%; height: 4rem;'>" +
                        allUseRecords["response"][record]["price"] +
                        "<br>" +
                        allUseRecords["response"][record]["description"] +
                        "</p></div>" +
                        "<a href='#' class='btn btn-outline-secondary btn-lg'>" +
                        "Add To Cart" +
                        "</a>" +
                        "</div></div></div>";
                }

                $(".product__body").html(output);
            },
        });
    });
});