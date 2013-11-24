var fs=require("fs");
var host = "127.0.0.1";
var port = 8085;
var express=require("express");

var app=express();

//give default directory to public
app.use(express.static(__dirname+"/public"));


app.get("/", function (request, response) {
    fs.readFile("content.html", function(err,data){response.send(data.toString())});
});
app.get("/d3.ay-pie-chart.js", function (request, response) {
        fs.readFile("d3.ay-pie-chart.js", function(err,data){response.send(data.toString())});
});
app.get("/d3.v2.js", function (request, response) {
            fs.readFile("d3.v2.js", function(err,data){response.send(data.toString())});
});

app.get("/jquery.js", function (request, response) {
                fs.readFile("jquery.js", function(err,data){response.send(data.toString())});
});

//get everything coming after hello/ and use it as a variable
app.get("/createGraph.js", function (request, response) {
    fs.readFile("createGraph.js", function(err,data){response.send(data.toString())});
});

app.get("/getData", function (request, response) {
    fs.readFile("2ndStage.json", function(err,data){data=JSON.parse(data);response.send(data)});
});

console.log("created");
app.listen(port);
console.log("listening..");
