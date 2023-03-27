let cart = []
// Function to stringify and set items in local storage.
function saveCart() {
    localStorage.setItem("cart",
        JSON.stringify(cart)
    )
}

function addCart(name, image, price) {
    // Looping through products in order to add or increase products.
    for (let i = 0; i < cart.length; i++) {
        if (cart[i].name === name) {
            cart[i].count += 1
            saveCart()
            return
        }
    }

    let plant = new Plant(name, image, price)
    cart.push(plant)
    saveCart()
}

// Created function to show the amount of items in the navigation bar on the cart icon.
function countInCart() {
  let productNumbers = document.getElementById("lblCartCount");
  if (productNumbers) {
    productNumbers.innerHTML = countCart();
  }
}
countInCart();


