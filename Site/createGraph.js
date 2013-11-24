var categories = {};
var arrOfFiles = [];

$(document).ready(function (e) {
    var req="/getData";
    console.log("asked data");
    $.getJSON(req,
        function (data) {
            console.log("received");
            console.log(data);
            arrGraph=[];
            index=1;
            for (el in data.elements) {
                console.log(data.elements[el]);
                arrGraph.push({"index":index,"name":data.elements[el].label, "value":data.elements[el].value});
                index+=1;
            }
            console.log(arrGraph);
            $("#todayGraph").height(480);
            $("#todayGraph").width(480);
             ay.pie_chart ('todayPie', arrGraph, {value: true});
             $(".todayPie").height("100%");
             $(".todayPie").width("100%");
        }
    );
});

