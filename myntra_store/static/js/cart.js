$( document ).ready(function() {
var list_i=[]
    $( ".total_price_span" ).each(function() {
    list_items=Number($(this).val())
    list_i.push(list_items);

console.log(list_items);
console.log(list_i);

});
const values = Object.values(list_i);
console.log(values,typeof(values),'valuesvalues');
const sum = values.reduce((accumulator, value) => {
  return accumulator + value;
}, 0);

console.log(sum);
Total=100+sum
$("#Subtotal").html(sum);
$("#Total").html(Total);
//total=0
//total += parseInt($(this).val(), 10);
//console.log(total,'total==',typeof(total),'total type');
//


});






var updateBtns = document.getElementsByClassName('update_cart')

for (var i = 0; i <= updateBtns.length; i++) {




    updateBtns[i].addEventListener('click', function() {

        var productId = this.dataset.product
        var action = this.dataset.action
        console.log(productId, action, '****')
        console.log(typeof(user), 'uuuuuu', '|', user, '|')
        if (user =='0') {
            console.log("USer is not logged in")

                        Swal.fire({
                          icon: 'error',
                      title: 'You can"t add items in cart...',
              title: 'You are not Logged In',
              showDenyButton: false,
              showCancelButton: true,
              confirmButtonText: 'Login',
            }).then((result) => {
              /* Read more about isConfirmed, isDenied below */
              if (result.isConfirmed) {

                  window.location.href = "/login_page/";

              }

            })

        }
        else if (user !='0' & action=="delete")
        {
        Swal.fire({
  title: 'Are you sure?',
  text: "You won't be able to revert this!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Yes, delete it!'
})

.then((result) => {
  if (result.isConfirmed) {

  DeleteCartItem(productId, action)

  }
})

        }

        else if (user !='0' & action=="add") {
            updateUserOrder(productId, action)
        }
    })
}




function updateUserOrder(productId, action) {

    console.log(productId, action,'productId, action')
    var url = '/UpdateItem/'

    fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'

            },
            body: JSON.stringify({ 'productId': productId, 'action': action })

        })
        .then((response) => {
            return response.json()
        })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })

}


function DeleteCartItem(productId, action) {

    console.log(productId, action,'productId, action')
    var url = '/delete_view/'

    fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'

            },
            body: JSON.stringify({ 'productId': productId, 'action': action })

        })
        .then((response) => {
        console.log(response,'response')
            return response.json()
        })

    .then((data) => {

    if (data){
    console.log('data:', data)

    location.reload()

    }
    else{
    Swal.fire('Items are not deleted', '', 'info')


    }


        location.reload()
    })

}


$('#place_order_btn').click(function(e){

console.log('place_order_btn $$$$$$')

 e.preventDefault();

cart_id = $(this).attr("data-cart_id");
console.log(cart_id,'cart_id $$$$$$')

                $.ajax({
                   type: "POST",
                    dataType: "json",

                    data: JSON.stringify({total_amt: total_amt,}),
                    url: "/delete_view1/",
                      headers: {
                    "X-Requested-With": "XMLHttpRequest",
                     "X-CSRFToken": csrftoken,  // don't forget to include the 'getCookie' function
                    },
                                    // on success
                    success: function (context) {
                        if (context.msg == "success") {
                            console.log(context,'res')
//                            window.location.href = "/Payment_pagw/";

                        }
                        else {
                        console.log(context,'error res')



                        }

                    },
                    // on error
                    error: function (context) {
                        // alert the error if any error occured
                        console.log("context error")
                    }
                });

            });

