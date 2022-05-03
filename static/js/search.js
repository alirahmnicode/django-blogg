$('.closebtn').css('display', 'none')
$(document).ready(function () {
    $('#search').keyup(function () {
        var q = $('#search').val()
        var box = ''
        $('.search-result').text('')
        $('.search-box').css('display', 'block')
        $('.closebtn').css('display', 'block')
        $('.ali').text('')
        if (q.length > 0) {
            var url = `${window.location.origin}/blog/search/?q=${q}`
            $.ajax(
                {
                    type: "GET",
                    url: url,
                    success: function (response) {
                        for (let i = 0; i < response.articles.length; i++) {
                            box += `<a href="articles/detail/${response.articles[i].slug}/${response.articles[i].pk}/">
                                        <div class="search-article">
                                            <div>
                                                <h4>${response.articles[i].title}</h4>
                                                <p>${response.articles[i].user}</p>
                                            </div>
                                            <div>
                                                <img src="${response.articles[i].image}" alt="">
                                            </div>
                                        </div>
                                    </a>`
                            $('.search-result').append(box)
                        }
                    }
                }
            )
        }
    })
})