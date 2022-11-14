if (!localStorage.getItem('Watchlist')){
    localStorage.setItem('Watchlist',[]);
}        




document.addEventListener('DOMContentLoaded',function () {
    let Watchlist = localStorage.getItem('Watchlist');

    const button =document.querySelector('#Watchlist');
    button.onclick = function() {
        if (button.innerHTML === 'Add to Watchlist'){
            Watchlist.push();
            localStorage.setItem('Watchlist',Watchlist)
            button.innerHTML = 'Remove from Watchlist'
            alert('Item has been added to Watchlist')

        } else{
            button.innerHTML = 'Add to Watchlist'
            Watchlist.pop();
            localStorage.setItem('Watchlist',Watchlist);
            alert('Item has been removed from Watchlist')

        }
        
    }
})