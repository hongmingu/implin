$(function () {
    var obj_type = $('#obj_type').html()
    $.ajax({
        url: '/re/' + obj_type + '/posts/', type: 'post', dataType: 'json', cache: false,
        data: {
            obj_id: $('#obj_id').html(),
            end_id: $('#end_id').html()
        },
        success: function (data) {
            if (data.res === 1) {
                $.each(data.output, function (index, value) {
                    var appender = '<div class="row div_base" id="post_wrapper_' + value + '">' +
                        '<script defer>' +
                        '    obj_post_populate("' + value + '", "' + obj_type + '")' +
                        '<' + '/script>' +
                        '</div>'
                    $('#post_list').append(appender)
                })


                if (data.end === null) {
                    $('#more_load').addClass('hidden')
                    $('#end_id').html('')
                } else {
                    $('#more_load').removeClass('hidden')
                    $('#end_id').html(data.end)
                }
            }
        }
    })

    $('#more_load').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/' + obj_type + '/posts/', type: 'post', dataType: 'json', cache: false,
            data: {
                obj_id: $('#obj_id').html(),
                end_id: $('#end_id').html()
            },
            success: function (data) {
                if (data.res === 1) {
                    $.each(data.output, function (index, value) {
                        var appender = '<div class="row div_base" id="post_wrapper_' + value + '">' +
                            '<script defer>' +
                            '    obj_post_populate("' + value + '", "' + obj_type + '")' +
                            '<' + '/script>' +
                            '</div>'
                        $('#post_list').append(appender)
                    })


                    if (data.end === null) {
                        $('#more_load').addClass('hidden')
                        $('#end_id').html('')
                    } else {
                        $('#more_load').removeClass('hidden')
                        $('#end_id').html(data.end)
                    }
                }
            }
        })

    })
})