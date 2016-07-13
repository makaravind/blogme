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
    
    $(".mine").click(function (event) {

        // make all disappear
        // $('.posts-container').remove();
        $('.thumbnail').addClass('hidden');
        // $('.thumbnail').removeClass('hidden');
        // retrive required data
        console.log('making ajax call now');
        flag = $('.mine').attr('value');
        if(flag == 'show only mine'){
            display_my_posts();
        }
        else{
            $('.thumbnail .me').addClass('hidden');
            $('.thumbnail').removeClass('hidden');
             $('.mine').val('show only mine');
        }
    });

    function display_my_posts(){
        $.ajax({
           type: 'GET',
            url: '/posts/api/view/'+$(".mine").attr('author'),

            success: function (json) {
                console.log(json);

                // place the elemets now
                $.each(json, function (index, element) {
                   $('body .row').append(
                       '<div class="posts-container col-sm-offset-1 col-sm-6 col-md-4"> ' +
                       '<div class="thumbnail me"> ' +
                       '<div class="caption"> ' +
                       '<h3>'+ element.title+ '</h3>' +
                           + '<p>'+ element.content +'</p>' +
                       '<p><a href="/posts/update/'+element.id+ '"' + ' class="update btn btn-primary" role="button">update</a></p>'+
                           +'<p style="color:rgba(6,7,8,0.40)">'+element.timestamp+'</p>'

                   );
                });
            },

            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>" +
                    "Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");
                console.log(xhr.status + ": " + xhr.responseText);
            }

        });
        
        flag = $('.mine').attr('value');
        if(flag == 'show only mine') {
            $('.mine').val('show all');
        }
        else{
            $('.mine').val('show only mine');
        }

    }

});