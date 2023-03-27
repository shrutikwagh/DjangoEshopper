
$('#paynow_btn').click(function(e){

    bill_id=document.getElementById("bill_id").value;
    cust_id=document.getElementById("cust_id").value;
    total_amt=document.getElementById("total_amt").value;
    console.log(bill_id,cust_id,total_amt,'total_amttotal_amt')
    formData1=document.getElementById("formData1")
    const formData = new FormData(formData1);

                $.ajax({
                   type: "POST",
                    dataType: "json",

                    data: JSON.stringify({total_amt: total_amt,}),
                    url: "/intiate_payment/",
                      headers: {
                    "X-Requested-With": "XMLHttpRequest",
                     "X-CSRFToken": csrftoken,  // don't forget to include the 'getCookie' function
                    },
                                    // on success
                    success: function (response) {
                        if (response.code == 200) {
                            console.log(response,'res')
//                            window.location.href = "/Payment_pagw/";

                   $.ajax({
                   type: "POST",
                    dataType: "json",

                    data: response.context,
                    url: "/Payment_pagw/",
                      headers: {
                    "X-Requested-With": "XMLHttpRequest",
                     "X-CSRFToken": csrftoken,  // don't forget to include the 'getCookie' function
                    },
                    })



                        }
                        else {
                        console.log(response,'error res')



                        }

                    },
                    // on error
                    error: function (response) {
                        // alert the error if any error occured
                        console.log("response error")
                    }
                });

            });
