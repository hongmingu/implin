$(function () {
    var rank_kind = $('#rank_kind').html()
    $.ajax({
        url: '/re/'+rank_kind+'/rank/', type: 'post', dataType: 'json', cache: false,
        data: {
            day: $('#day').html(),
        },
        success: function (data) {
            console.log(data)
            if (data.res === 1) {
                $.each(data.output, function (key, value) {
                    var rank = ''
                    if((parseInt(key)<3)){
                        rank = '<div class="gen_rank_wrapper" align="right"><span class="gen_rank_' + (parseInt(key) + 1) + '">' + (parseInt(key) + 1) + '</span></div>'
                    } else {
                        rank = '<div class="gen_rank_wrapper" align="right"><span class="gen_rank_other">' + (parseInt(key) + 1) + '</span></div>'
                    }
                    var obj_path = '/' + value.obj_type + '/' + value.obj_id + '/'

                    var obj = '<a href="'+obj_path+'"><div class="gen_obj_wrapper">' +
                        '<div class="gen_obj_img_wrapper">' +
                        '<img class="gen_obj_img" src="' + value.main_photo + '">' +
                        '</div>' +
                        '<div class="gen_obj_content_wrapper">' +
                        '<div>' +
                        '<span class="gen_obj_name">' + value.main_name + '</span>' +
                        '</div>' +
                        '<div align="right">' +
                        '<span class="gen_obj_gross">' + value.gross + '</span>' +
                        '</div>' +
                        '</div>' + //gen_obj_content_wrapper
                        '</div></a>'  //gen_obj_wrapper
                    var posts = ''
                    $.each(value.posts, function (key, value) {
                        posts = posts + '<a href="/post/'+value.post_id+'/"><div class="gen_post_wrapper clickable">' +
                            '<span class="gen_post_username">' + value.username + '</span><span class="gen_post_gross">' + value.gross + '</span>' +
                            '</div></a>'
                    })

                    var appender = '<div class="gen_rank_obj_wrapper">' +
                        rank +
                        obj +
                        '</div>' +
                        '<div>' +
                        posts +
                        '</div>'
                    $('#list').append(appender)
                    // 일단 가게 하고 옵젝트면 날짜별로 볼 수 있게 하고 날짜 지난 날이면 베스트 3 박제되게 한다.
                })

            }
        }
    })
})