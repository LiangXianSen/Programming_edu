function Register() {
    var input_dict = {};
    $('div#register_form :input').each(function () {
       var v = $(this).val();
        var n = $(this).attr('name');
        input_dict[n] = v;
    });
    console.log(input_dict);
    $('.error-msg').remove();  //在每次提交(验证)之前把之前的错误信息先删除掉
    $.ajax({
        url: '/register/',
        type: 'POST',
        data: input_dict,
        dataType: 'json',
        success: function (result) {
            console.log(result);
            if(result.status){
                location.href = '/'
            }else {
                $.each(result.message, function (k, v) {
                    console.log(k,v[0].message);
                    var tag = document.createElement('span');
                    tag.className = 'error-msg';
                    tag.innerText = v[0].message;
                    $('input[name="' + k + '"]').after(tag);
                })
            }
        },
        error: function () {
        }
    })
}

function Login() {
    var input_dict = {};
    $('div#login_form :input').each(function () {
       var v = $(this).val();
        var n = $(this).attr('name');
        input_dict[n] = v;
    });
    console.log(input_dict);
    $('.error-msg').remove();  //在每次提交(验证)之前把之前的错误信息先删除掉
    $.ajax({
        url: '/login/',
        type: 'POST',
        data: input_dict,
        dataType: 'json',
        success: function (result) {
            console.log(result);
            if(result.status){
                location.href = '/'
            }else {
                $.each(result.message, function (k, v) {
                    console.log(k,v[0].message);
                    var tag = document.createElement('span');
                    tag.className = 'error-msg';
                    tag.innerText = v[0].message;
                    $('input[name="' + k + '"]').after(tag);
                })
            }
        },
        error: function () {
        }
    })
}