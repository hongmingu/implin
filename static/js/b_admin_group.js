$(function () {
    $.ajax({
        url: '/re/group/list/',
        type: 'post',
        dataType: 'json',
        cache: false,
        data: {
            last_pk: $('#last_pk').html(),
        },
        success: function (data) {
            console.log(data)
            if (data.res === 1) {
                $.each(data.output, function (key, value) {
                    $('#obj_list').append('<div><span class="h4">' + value.name + '</span><span class="h5">' + value.desc + '</span></div><div>' + value.id + '</div><a href="/b/admin/group/edit/' + value.id + '/"><div>link</div></a>')
                })
                $('#last_pk').html(data.last_pk)
            }
        }
    });
    $('#more_load').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/group/list/',
            type: 'post',
            dataType: 'json',
            cache: false,
            data: {
                last_pk: $('#last_pk').html(),
            },
            success: function (data) {
                if (data.res === 1) {
                    $.each(data.output, function (key, value) {
                        $('#obj_list').append('<div><span class="h4">' + value.name + '</span><span class="h5">' + value.desc + '</span></div><div>' + value.id + '</div><a href="/b/admin/group/edit/' + value.id + '/"><div>link</div></a>')
                    })
                    $('#last_pk').html(data.last_pk)
                }
            }
        });
    })

    $('#register').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/group/register/',
            type: 'post',
            dataType: 'json',
            cache: false,
            data: {
                name: $('#name_input').val(),
                desc: $('#desc_input').val(),
            },
            success: function (data) {
                if (data.res === 1) {
                    location.reload()
                }
            }
        });
    })
    $('#id_delete').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/b/admin/group/delete/',
            type: 'post',
            dataType: 'json',
            cache: false,
            data: {
                id: $('#id_delete_input').val(),
            },
            success: function (data) {
                if (data.res === 1) {
                    location.reload()
                }
            }
        });
    })
})