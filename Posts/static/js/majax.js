$(document).ready(function(){

    $("#complete_btn").click(function () {
        
    var completeId;
    completeId = $(this).attr('complete-btn-id');
    $.get('updatecomplete', {completed_btn_id :completeId}, function () {
        // make the changes that have to happen when control comes back after processing the view
        complete_label = $("#completed-label-"+completeId).html();
        completed = "completed";
       $("#completed-label-"+completeId).addClass("label label-danger");
       $("#completed-label-"+completeId).html(completed);
    })
});

});

