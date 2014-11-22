$(document).ready(function(){
    $("#uploadbutton").click(function(){
        $("#mainupload").addClass("showdialog");
        console.log("added class ...");


    });
    $("#upload2").click(function(){
        $("#mainupload").removeClass("showdialog");
        console.log("removed class");
    });

});
