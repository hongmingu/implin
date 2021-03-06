$(function () {
    var obj_type = $('#obj_type').html()
    var post_id = $('#id').html()
    $('#update_post_complete').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/update/' + obj_type + '/post/complete/', type: 'post', dataType: 'json', cache: false,
            data: {
                id: post_id,
                text: $.trim($('#update_post_textarea').val())
            },
            success: function (data) {
                if (data.res === 1) {
                    var scheme = window.location.protocol == "https:" ? "https://" : "http://";
                    var path = scheme + window.location.host + "/" + $('#user_username').html() + "/";
                    location.href = path
                }
            }
        });

    })
    $.ajax({
        url: '/re/update/' + obj_type + '/post/', type: 'post', dataType: 'json', cache: false,
        data: {
            id: post_id,
        },
        success: function (data) {
            if (data.res === 1) {
                $('#update_post_img').attr('src', data.output.main_photo)
                $('#update_post_name').html(data.output.main_name)
                $('#update_post_gross').html(data.output.gross)
                $('#server_date').html(data.output.date)
                $('#update_post_textarea').val(data.output.text)
            }
        }
    });


});

