// get client cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// create best article layout
var articles = document.getElementsByClassName('article best')
for (var i = 0; i < articles.length; i++) {
    if (i <= 1) {
        document.getElementsByClassName('left-box')[0].appendChild(articles[i])
    } else {
        document.getElementsByClassName('right-box')[0].appendChild(articles[i])
    }

}


// get url and objct pk for like
const url = window.location.href.split('/')
const pk = url[url.length-2]
// add like 
$(document).ready(function () {
    $('.like').click(function () {
        var url = `${window.location.origin}/articles/like/${pk}/`
        $.ajax(
            {
                type: "POST",
                url: url,
                headers: { 'X-CSRFToken': csrftoken },
                // on success
                success: function (response) {
                    $('.like-count').text(response.likes)
                }
            })
    });
});
