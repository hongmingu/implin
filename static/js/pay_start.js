$(function () {
    $('#charge').click(function (e) {
        e.preventDefault()
        var get_unit = $('#unit_input').val()
        if (get_unit.length === 0) {
            $('#charge_note').html('cannot charge 0$')
            return false
        }

        if (isNaN(Number(get_unit))) {
            $('#charge_note').html('check your input, only digit is working')
            return false
        }
        $('#charge_note').html('')
        var str_unit = get_unit.toString()
        var height = 'height=' + window.innerHeight
        window.open('/pay/charge/?q=' + str_unit, '',
            'toolbar=no, location=no, status=no, menubar=no, scrollbars=yes, resizable=yes, fullscreen=yes, width=768,' + height);
        return false;
    })

})
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