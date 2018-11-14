var post_populate = function post_populate(id) {
    $(function () {
        $.ajax({
            url: '/re/post/populate/', type: 'post', dataType: 'json', cache: false,
            data: {
                post_id: id,
            },
            success: function (data) {

                if (data.res === 1) {
                    var text = ''
                    if (data.output.text === null){

                    }else {
                        text = '<div class="pop_text">'+value.output.text+'</div>'
                    }
                    var comment_more_load = '<a href=""><div id="post_comment_more_load hidden" align="center">more load</div></a>'
                    if (data.output.comment_count > 3){
                        comment_more_load = '<a href=""><div id="post_comment_more_load" align="center">more load</div></a>'
                    }

                    var comment_textarea = '<div align="center"><form><div class="input-group input-group-sm">' +
                        '<textarea class="form-control" id="pop_comment_textarea_'+id+'" placeholder="a comment"></textarea>' +
                        '<div class="input-group-btn">' +
                        '<button class="btn btn-default">' +
                        '<i class="glyphicon glyphicon-send"></i>' +
                        '</button></div>' +
                        '</div>' +
                        '</form>' +
                        '</div>'
                    var appender = $('<div id="pop_'+id+'">' +
                        '<div align="right"><a href=""><span class="glyphicon glyphicon-option-horizontal pop_menu"></span></a></div>' +
                        '<div><a href="/'+data.output.username+'/"><span class="pop_username">'+data.output.username+'</span></a></div>' +
                        text +
                        '<div align="right"><span class="pop_gross">'+data.output.gross+'</span><span class="pop_dollar">$</span></div>'+
                        '<div align="right">'+data.output.date+'</div>'+
                        '<div><div class="pop_like_count"></div><div class="pop_like" align="right"><span class="pop_heart"></span></div></div>'+
                        '<div><span class="pop_comment"></span><span class="pop_comment_count"></span></div>'+
                        '<div id="pop_comment_wrapper_'+id+'"></div>'+//여기서 이것의 차일드 중 마지막 값의 uuid 를 이용하여 이것 다음 코멘트를
                        comment_more_load +
                        '<div id="pop_new_comment_wrapper_'+id+'"></div>'+
                        comment_textarea+
                        '</div>')

                    '<div><input class="create_post_input" id="pop_comment_input" placeholder="leave a comment"/></div>'
                    appender.find('.pop_menu').on('click', function (e) {
                        e.preventDefault()
                        if ($('#user_id').html() === '') {
                            $('#modal_need_login').modal('show')
                            return false;
                        }
                        $('#modal_need_login').modal('show')
                    })


                    $('#post_wrapper_' + post_id_value).append(append_to)
                }
            }
        })
    })
}