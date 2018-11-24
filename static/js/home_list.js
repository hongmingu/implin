$(function () {
    $.ajax({
        url: '/re/home/list/', type: 'post', dataType: 'json', cache: false,
        data: {
            day: $('#day').html(),
        },
        success: function (data) {
            console.log(data)
            if(data.res === 1){
                $.each(data.all_output, function (key, value) {
                    var rank = '<div class="home_rank_wrapper"><span class="home_rank_1">'+key+'</span></div>'
                    var obj = '<div class="home_obj_wrapper">' +
                        '<div class="home_obj_img_wrapper">' +
                        '<img class="home_obj_img" src="http://file.mk.co.kr/meet/neds/2018/07/image_readtop_2018_446394_15317027263389308.png">' +
                        '</div>' +
                        '<div>' +
                        '<div>' +
                        'BTS' +
                        '</div>' +
                        '<div align="right">' +
                        '50 $' +
                        '</div>' +
                        '</div>' +
                        '</div>'
                    var posts = ''
                    $.each(value.posts, function (key, value) {
                        posts = posts + '<div>' +
                            '<div>' +
                            '<div>'+value.username+'</div>' +
                            '<div>'+value.text+'</div>' +
                            '<div align="right">'+value.gross+'</div>' +
                            '</div>' +
                            '</div>'
                    })
                    posts = posts +
                        '<div align="right">go to bts 일단 가게 하고 옵젝트면 날짜별로 볼 수 있게 하고 날짜 지난 날이면 베스트 3 박제되게 한다.</div>'
                    var appender = '<div>\n' +
                        '\n' +
                        '                        </div>'
                })
                $.each(data.group_output, function (key, value) {

                })
                $.each(data.solo_output, function (key, value) {

                })
            }
        }
    })
})