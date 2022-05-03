$(document).ready(function () {
    $('.username').keyup(function () {
        var username = $('.username').val()
        var message = ''
        if (username.length > 0) {
            var url = `${window.location.origin}/account/search/${username}/`
            $.ajax(
                {
                    type: "GET",
                    url: url,
                    // on success
                    success: function (response) {
                        if (response.access === true) {
                            message = 'this username is available'
                        } else {
                            message = 'this username is not available'
                        }
                        $('.alert').text(message)
                    }
                })
        } else {
            message = 'this username is not available'
            $('.alert').text(message)
        }

    })
    // check if password1 and password is math
    $('.password1').keyup(function () {
        password1 = $('.password1').val()
        if (password1.length < 6) {
            message = 'The password is too short.'
            $('.alert').text(message)
        } else {
            message = 'The password length is good.'
            $('.alert').text(message)
        }
    })
    $('.password2').keyup(function () {
        message = ''
        password1 = $('.password1')
        password2 = $('.password2')

        if (password1.val() === password2.val()) {
            message = 'password are matched'
        } else {
            message = 'password are not matched'
        }
        $('.alert').text(message)

    })
})