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


$('document').ready(function () {
    $('.like-comment').on('click', function () {
        let id=$(this).attr('id');
        let current_id = id.split('-')[1];
        $.ajax({
            url:`/shop/add_like2comment_ajax/${current_id}`,
            header: {"X-CSRFToken": csrftoken},
            method: "PUT",
            success: function (data) {
                $(`#${id}`).html(`Likes: ${data['likes']}`);
            }
        })
    });

    $('.delete-comment').on('click', function () {
        let id=$(this).attr('id');
        $.ajax({
               url:`/shop/add_like2comment_ajax/${current_id}`,
            header: {"X-CSRFToken": csrftoken},
            method: "DELETE",
            success: function (data) {
                $(`#${id}`).remove()
            }
        })
    })

    $('.delete-book').on('click', function () {
        let id=$(this).attr('id');
        $.ajax({
            url: "/shop/delete_book_ajax",
            data: {"book_id": id.split("-")[2]},
            method: "GET",
            success: function (data) {
                $(`#${id}`).remove()
            }
        })
    })

});