document.addEventListener('DOMContentLoaded',function () {
    carousel_ids = randomNum(1,17)
    fetch(`https://api.escuelajs.co/api/v1/products?offset=0&limit=3`)
            .then(res=>res.json())
            .then(items => {
                items.forEach(function(item){
                     console.log(item,carousel_ids)
                carousel_div = document.createElement('div')
                carousel_div.className = 'carousel_container'
                carousel_div.innerHTML = `<a >
                <img src="${item.images[0]}" alt="" class="col-md"id="carousel_image" ><br>
                ${item.title}
                <br> Starting price:${item.price} 
            </a>`
/*         document.querySelector('#carousel').appendChild(carousel_div)
 */                })
               
    
 
        

                
                
        })
    fetch('https://api.escuelajs.co/api/v1/products?offset=0&limit=20')
    .then(res=>res.json())
    .then(products => {
        //for each product in products display picture, title, and price 
        products.forEach( function (product){
            product_container = document.createElement('div')
            product_container.id='listing'
            product_container.className = 'listings'
            product_container.innerHTML = `<a >
            <img src="${product.images[1]}" alt="" id="product_image" ><br>
           ${product.title}
            <br> Starting price:$${product.price} 
        </a>`
        document.querySelector('#products').appendChild(product_container)
        

        })

        var elements = document.querySelectorAll('#product_image');
        elements.forEach(function(element) {
            element.classList.add('mb-3','img-fluid',); //add class
        });

        var elements = document.querySelectorAll('.listings');
        elements.forEach(function(element) {
            element.classList.add('card','text-center',); //add class
        });


    } )
    

})

function randomNum(min, max) { 
    var n = []; 
    for(var i=0;i<1;i++){ 
    n.push(Math.floor(Math.random() * max) + min); 
    } 
    return n; 
    } 
