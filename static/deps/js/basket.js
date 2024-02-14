let cart = [];

function addToCart(productId) {
  cart.push(productId);
  renderCart();
}

function removeFromCart(index) {
  cart.splice(index, 1);
  renderCart();
}

function checkoutItem(productId) {
  // Логика оплаты отдельного товара
  console.log(`Оплата товара ${productId}`);
}

function checkoutAll() {
  // Логика оплаты всех товаров
  console.log('Оплата всех товаров');
}

function renderCart() {
  const cartItems = document.getElementById('cart-items');
  cartItems.innerHTML = '';

  cart.forEach((item, index) => {
    const li = document.createElement('li');
    li.textContent = `Товар ${item}`;
    
    const payButton = document.createElement('button');
    payButton.textContent = 'Оплатить';
    payButton.onclick = () => checkoutItem(item);
    
    const removeButton = document.createElement('button');
    removeButton.textContent = 'Удалить';
    removeButton.onclick = () => removeFromCart(index);
    
    li.appendChild(payButton);
    li.appendChild(removeButton);
    cartItems.appendChild(li);
  });
}
