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
                const allUseRecords = response;
                for (record in allUseRecords) {
                    console.log(record);
                    output += "<h1>" + record + "</h1>";
                }

                $(".product__display").html(output);
            },
        });
    });
});