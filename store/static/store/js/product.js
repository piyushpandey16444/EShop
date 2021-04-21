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
                    // output +=
                }
                $(".to_remove").replaceWith(output);
            },
        });
    });
});