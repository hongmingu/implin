$(function () {
    $.ajax({
        url: '/re/home/rank/', type: 'post', dataType: 'json', cache: false,
        data: {
            day: $('#day').html(),
        },
        success: function (data) {
            console.log(data)
            if (data.res === 1) {
                $.each(data.all_output, function (key, value) {
                    var rank = '<div class="home_rank_wrapper" align="right"><span class="home_rank_' + (parseInt(key) + 1) + '">' + (parseInt(key) + 1) + '</span></div>'
                    var obj_path = '/' + value.obj_type + '/' + value.obj_id + '/'
                    var obj = '<a href="' + obj_path + '"><div class="home_obj_wrapper">' +
                        '<div class="home_obj_img_wrapper">' +
                        '<img class="home_obj_img" src="' + value.main_photo + '">' +
                        '</div>' +
                        '<div class="home_obj_content_wrapper">' +
                        '<div>' +
                        '<span class="home_obj_name">' + value.main_name + '</span>' +
                        '</div>' +
                        '<div align="right">' +
                        '<span class="home_obj_gross">' + value.gross + '</span>' +
                        '</div>' +
                        '</div>' + //home_obj_content_wrapper
                        '</div></a>'  //home_obj_wrapper
                    var posts = ''
                    $.each(value.posts, function (key, value) {
                        posts = posts + '<a href="/post/'+value.post_id+'/"><div class="home_post_wrapper clickable">' +
                            '<span class="home_post_username">' + value.username + '</span><span class="home_post_gross">' + value.gross + '</span>' +
                            '</div></a>'
                    })

                    var appender = '<div class="home_rank_obj_wrapper">' +
                        rank +
                        obj +
                        '</div>' +
                        '<div>' +
                        posts +
                        '</div>'
                    $('#all_list').append(appender)
                    // 일단 가게 하고 옵젝트면 날짜별로 볼 수 있게 하고 날짜 지난 날이면 베스트 3 박제되게 한다.
                })
                $.each(data.group_output, function (key, value) {
                    var rank = '<div class="home_rank_wrapper" align="right"><span class="home_rank_' + (parseInt(key) + 1) + '">' + (parseInt(key) + 1) + '</span></div>'
                    var obj_path = '/' + value.obj_type + '/' + value.obj_id + '/'

                    var obj = '<a href="'+obj_path+'"><div class="home_obj_wrapper">' +
                        '<div class="home_obj_img_wrapper">' +
                        '<img class="home_obj_img" src="' + value.main_photo + '">' +
                        '</div>' +
                        '<div class="home_obj_content_wrapper">' +
                        '<div>' +
                        '<span class="home_obj_name">' + value.main_name + '</span>' +
                        '</div>' +
                        '<div align="right">' +
                        '<span class="home_obj_gross">' + value.gross + '</span>' +
                        '</div>' +
                        '</div>' + //home_obj_content_wrapper
                        '</div></a>'  //home_obj_wrapper
                    var posts = ''
                    $.each(value.posts, function (key, value) {
                        posts = posts + '<a href="/post/'+value.post_id+'/"><div class="home_post_wrapper clickable">' +
                            '<span class="home_post_username">' + value.username + '</span><span class="home_post_gross">' + value.gross + '</span>' +
                            '</div></a>'
                    })

                    var appender = '<div class="home_rank_obj_wrapper">' +
                        rank +
                        obj +
                        '</div>' +
                        '<div>' +
                        posts +
                        '</div>'
                    $('#group_list').append(appender)

                })
                $.each(data.solo_output, function (key, value) {
                    var rank = '<div class="home_rank_wrapper" align="right"><span class="home_rank_' + (parseInt(key) + 1) + '">' + (parseInt(key) + 1) + '</span></div>'
                    var obj_path = '/' + value.obj_type + '/' + value.obj_id + '/'

                    var obj = '<a href="'+obj_path+'"><div class="home_obj_wrapper">' +
                        '<div class="home_obj_img_wrapper">' +
                        '<img class="home_obj_img" src="' + value.main_photo + '">' +
                        '</div>' +
                        '<div class="home_obj_content_wrapper">' +
                        '<div>' +
                        '<span class="home_obj_name">' + value.main_name + '</span>' +
                        '</div>' +
                        '<div align="right">' +
                        '<span class="home_obj_gross">' + value.gross + '</span>' +
                        '</div>' +
                        '</div>' + //home_obj_content_wrapper
                        '</div></a>'  //home_obj_wrapper
                    var posts = ''
                    $.each(value.posts, function (key, value) {
                        posts = posts + '<a href="/post/'+value.post_id+'/"><div class="home_post_wrapper clickable">' +
                            '<span class="home_post_username">' + value.username + '</span><span class="home_post_gross">' + value.gross + '</span>' +
                            '</div></a>'
                    })

                    var appender = '<div class="home_rank_obj_wrapper">' +
                        rank +
                        obj +
                        '</div>' +
                        '<div>' +
                        posts +
                        '</div>'
                    $('#solo_list').append(appender)
                })
            }
        }
    })
})