$(function () {
    $.ajax({
        url: '/re/home/list/', type: 'post', dataType: 'json', cache: false,
        data: {
            day: $('#day').html(),
        },
        success: function (data) {
            console.log(data)
            if(data.res === 1){

            }
        }
    })
})