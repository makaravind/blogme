$(document).ready(function() {
    $("#create_btn").click( function(event) {
           window.location.href = '/posts/add'; // this is similar to clicking
           // window.location.replace('/posts/add'); // this is similar to redirect
    });

    $('.thumbnail').hover(function(){
        $(this).css("background-color", "#bf3e11");
        }, function(){
        $(this).css("background-color", "transparent");
    });
    
    $("#create_form").submit(function (event) {
            event.preventDefault();
            create_post();
    });

    function create_post() {
        console.log('create post ajax lives here');
        $.ajax({
           type: 'POST',
            url: '/posts/create/',

            data:{
                title: $('#title').val(),
                content: $('#id_content').val(),
                author: $('#id_author').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },

            success: function (json) {
                console.log("success");
                console.log('hreffing');
                window.location.href = '/posts/view';
            },

            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>" +
                    "Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

});