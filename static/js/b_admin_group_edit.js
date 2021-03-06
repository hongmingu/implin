$(function () {
    $('#default_register').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/b/admin/group/edit/default/register/',
            type: 'post',
            dataType: 'json',
            cache: false,
            data: {
                id: $('#id').html(),
                name: $('#default_name_input').val(),
                desc: $('#default_desc_input').val(),
            },
            success: function (data) {
                if (data.res === 1) {
                    location.reload()
                }
            }
        });
    })
    $('#photo_main_register').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/b/admin/group/edit/main/photo/register/',
            type: 'post',
            dataType: 'json',
            cache: false,
            data: {
                id: $('#id').html(),
                photo_id: $('#photo_main_input').val(),
            },
            success: function (data) {
                if (data.res === 1) {
                    location.reload()
                }
            }
        });
    })
    $('#photo_delete').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/b/admin/group/edit/photo/delete/',
            type: 'post',
            dataType: 'json',
            cache: false,
            data: {
                id: $('#id').html(),
                photo_id: $('#photo_delete_input').val(),
            },
            success: function (data) {
                if (data.res === 1) {
                    location.reload()
                }
            }
        });
    })
    $('#name_delete').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/b/admin/group/edit/name/delete/',
            type: 'post',
            dataType: 'json',
            cache: false,
            data: {
                id: $('#id').html(),
                name: $('#name_delete_input').val(),
            },
            success: function (data) {
                if (data.res === 1) {
                    location.reload()
                }
            }
        });
    })

    $('#name_register').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/b/admin/group/edit/name/register/',
            type: 'post',
            dataType: 'json',
            cache: false,
            data: {
                id: $('#id').html(),
                name: $('#name_input').val(),
            },
            success: function (data) {
                if (data.res === 1) {
                    location.reload()
                }
            }
        });
    })
    $.ajax({
        url: '/re/b/admin/group/edit/',
        type: 'post',
        dataType: 'json',
        cache: false,
        data: {
            id: $('#id').html(),
        },
        success: function (data) {
            if (data.res === 1) {
                $('#default_name').html(data.default_name)
                $('#default_desc').html(data.default_desc)
                $('#main_name').html(data.main_name)
                $('#img_300').attr('src', data.main_photo)
                $.each(data.name_output, function (key, value) {
                    $('#name_list').append('<div class="h5">' + value.name + '</div>')
                })
                $.each(data.photo_output, function (key, value) {
                    $('#photo_list').append('<div><img class="img_300_300" src="' + value.photo + '"></div><div>' + value.id + '</div>')
                })

                $.each(data.member_solo_output, function (key, value) {
                    $('#member_list').append('<div class="h4">' + value.name + '</div><div class="h5">' + value.id + '</div>')
                })
            }
        }
    });
    $('#main_name_register').click(function (e) {
        e.preventDefault()
        $.ajax({
            url: '/re/b/admin/group/edit/main/name/',
            type: 'post',
            dataType: 'json',
            cache: false,
            data: {
                id: $('#id').html(),
                main_name: $('#main_name_input').val()
            },
            success: function (data) {
                if (data.res === 1) {
                    location.reload()
                } else {
                    alert('failed')
                }
            }
        });
    })

    $('#span_change_photo').click(function (e) {
        e.preventDefault();
        $('#input_file').click()
    });
    $('#input_file').change(function () {
        if (this.files && this.files[0]) {
            if (this.files[0].size > (1048576 * 10)) {
                var agent = navigator.userAgent.toLowerCase();

                if ((navigator.appName == 'Netscape' && navigator.userAgent.search('Trident') != -1) || (agent.indexOf("msie") != -1)) {
                    // ie 일때 input[type=file] init.
                    $('#input_file').replaceWith($('#input_file').clone(true));
                } else {
                    //other browser 일때 input[type=file] init.
                    $('#input_file').val("");
                }
                alert('File size can\'t exceed 10m');
                return;
            }
            var reader = new FileReader();
            reader.onload = function (e) {
                $("#img_crop").attr("src", e.target.result);
                $("#modal_crop").modal("show");
            };
            reader.readAsDataURL(this.files[0]);
        }
    });

    /* SCRIPTS TO HANDLE THE CROPPER BOX */
    var image;
    var cropper;
    $("#modal_crop").on("shown.bs.modal", function () {
        image = document.getElementById('img_crop');
        cropper = new Cropper(image, {
            viewMode: 2,
            minCropBoxWidth: 300,
            minCropBoxHeight: 300,
            aspectRatio: 1 / 1,
        });

    }).on("hidden.bs.modal", function () {
        cropper.destroy();
        var agent = navigator.userAgent.toLowerCase();

        if ((navigator.appName == 'Netscape' && navigator.userAgent.search('Trident') != -1) || (agent.indexOf("msie") != -1)) {
            // ie 일때 input[type=file] init.
            $('#input_file').replaceWith($('#input_file').clone(true));
        } else {
            //other browser 일때 input[type=file] init.
            $('#input_file').val("");
        }
    });

    $(".js-zoom-in").click(function () {
        cropper.zoom(0.1);
    });

    $(".js-zoom-out").click(function () {
        cropper.zoom(-0.1);

    });

    $(".js-crop-and-upload").click(function () {
        var cropData = cropper.getData();

        var form_file = $('#form_upload')[0];
        var form_data = new FormData(form_file);
        form_data.append('x', cropData["x"]);
        form_data.append('y', cropData["y"]);
        form_data.append('height', cropData["height"]);
        form_data.append('width', cropData["width"]);
        form_data.append('rotate', cropData["rotate"]);
        form_data.append('id', $('#id').html())

        $.ajax({
            url: '/re/b/admin/group/upload/photo/',
            type: 'post',
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            data: form_data,
            success: function (data) {
                console.log(data)
                $("#modal_crop").modal("hide");
                if (data.res === 1) {
                    location.reload()

                }
            }
        });
    });
})