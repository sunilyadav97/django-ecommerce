


let btns=document.querySelectorAll('.add-to-cart')

btns.forEach(btn=>{
    btn.addEventListener('click',function(e){
        let product_id=e.target.dataset.product
        let action=e.target.dataset.action
        if (user=='AnonymousUser')
        {
            console.log('You are not signed in.')
        }else{
                addToCart(product_id,action)
        }
    })
})



function addToCart(p_id,act)
{

const data = { product_id:p_id,action:act };
const url='/update-cart'
fetch(url, {
  method: 'POST', 
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken
  },
  body: JSON.stringify(data),
})
.then(response => response.json())
.then(data => {
    document.getElementById('cart').innerHTML=`${data.quantity}`
  console.log('Success:', data);
})
.catch((error) => {
  console.error('Error:', error);
});
}