$(document).on('keydown', 'input[pattern]', function (e) {
    var input = $(this);
    var oldVal = input.val();
    var regex = new RegExp(input.attr('pattern'), 'g');

    setTimeout(function () {
        var newVal = input.val();
        if (!regex.test(newVal)) {
            input.val(oldVal);
        }
    }, 0);
});
$(function () {
    $('#check_server_time').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/create/check/server/time/', type: 'post', dataType: 'json', cache: false,
            data: {},
            success: function (data) {
                if (data.res === 1) {
                    var cal_value = data.time
                    var year, month, day, hour, min, sec
                    [day, time] = cal_value.split("T");
                    [year, month, day] = day.split("-");
                    [hour, min, sec] = time.split(".")[0].split(":");
                    var made_str = year + '-' + month + '-' + day + ' ' + hour + ':' + min + ':' + sec
                    $('#server_time').html(made_str)
                }
            }
        });
    })
    var obj_type = $('#obj_type').html()
    $('#create_post_complete').click(function (e) {
        e.preventDefault()
        var get_value = $('#create_post_input').val()
        if (get_value.replace(/ /g, '') === '') {
            $('#create_post_note').html('minimum: 1.00')
            return false
        }

        var get_fixed = Number(get_value).toFixed(2)
        var current_value = $('#create_post_current_wallet').html()
        var current_fixed = Number(current_value).toFixed(2)
        $('#create_post_note').html('')
        if (parseFloat(get_fixed) > parseFloat(current_fixed)) {
            $('#create_post_note').html('more than what you have')
            return false;
        }
        if (parseFloat(get_fixed) < 1) {
            $('#create_post_note').html('minimum: 1.00')
            return false;
        }
        $.ajax({
            url: '/re/create/' + obj_type + '/post/complete/', type: 'post', dataType: 'json', cache: false,
            data: {
                obj_id: $('#obj_id').html(),
                gross: get_fixed,
                text: $.trim($('#create_post_textarea').val())
            },
            success: function (data) {
                if (data.res === 1) {
                    var scheme = window.location.protocol == "https:" ? "https://" : "http://";
                    var path = scheme + window.location.host + "/"+$('#user_username').html()+"/";
                    location.href = path
                }
            }
        });

    })
    $.ajax({
        url: '/re/create/' + obj_type + '/post/', type: 'post', dataType: 'json', cache: false,
        data: {
            obj_id: $('#obj_id').html(),
        },
        success: function (data) {
            if (data.res === 1) {
                $('#create_post_img').attr('src', data.output.main_photo)
                $('#create_post_name').html(data.output.main_name)
                $('#create_post_current_wallet').html(data.output.wallet)
            }
        }
    });

});