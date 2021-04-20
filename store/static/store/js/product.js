$(document).ready(() => {
    document;
    $("#filter__l2h").click(function(e) {
        e.preventDefault();
        // low to high clicked check for category
        const obtaniedURL = window.location.href;


        // making ajax call
        // $.ajax({
        //     type: "GET",
        //     url: "/",
        //     data: "data",
        //     dataType: "dataType",
        //     success: function(response) {

        //     }
        // });
    });
});
// $(document).ready(() => {
//     $(".list__filter").click(function(e) {
//         e.preventDefault();
//         const categoryId = this.id;
//         console.log("data found: making ajax call !", categoryId);
//         var output = "";

//         // making ajax call
//         $.ajax({
//             type: "get",
//             url: "/",
//             data: {
//                 category_id: categoryId,
//             },
//             dataType: "json",
//             success: function(response) {
//                 const allUseRecords = JSON.parse(response);
//                 console.log(allUseRecords);
//                 for (record in allUseRecords) {
//                     output +=
//                         "<div class='to_remove border border-danger'>" + "Like" + "</div>";
//                     // "<div class='product__display col-lg-10 p-0 m-0 border border-info to_remove container-fluid p-0 m-0 border border-danger'>" +
//                     // "<div class='row'>" +
//                     // "<div class='card mb-3' style ='width: 18rem;'>" +
//                     // "<img src=" +
//                     // "http://localhost:8000/images/" +
//                     // allUseRecords[record]["image"] +
//                     // " class='card-img-top' alt='...' style='width: 100%; height: 20rem;'>" +
//                     // "<div class='card-body'>" +
//                     // "<h5 class='card-title'>" +
//                     // allUseRecords[record]["name"] +
//                     // "</h5><p class='card-text' style='width: 100%; height: 4rem;'>" +
//                     // allUseRecords[record]["price"] +
//                     // "<br>" +
//                     // allUseRecords[record]["description"] +
//                     // "</p></div><a href='#' class='btn btn-outline-secondary btn-lg'>" +
//                     // "Add to Cart" +
//                     // "</a></div></div></div>";
//                 }
//                 $(".to_remove").replaceWith(output);
//             },
//         });
//     });
// });