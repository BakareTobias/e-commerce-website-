document.addEventListener('DOMContentLoaded',function () {
    const button= document.querySelector('#Watchlist')

    if (watchlist.includes(listing_name)){
        button.innerHTML = 'Remove from Watchlist'
    } else{
        button.innerHTML = 'Add to Watchlist'
    }

    button.onclick = function() {
        if (button.innerHTML === 'Add to Watchlist'){
            button.innerHTML = 'Remove from Watchlist'
            window.location.replace(`http://127.0.0.1:8000/watchlist_add/${listing_id}`);
            alert('Item has been added to Watchlist');

        } else{
            button.innerHTML = 'Add to Watchlist'
            window.location.replace(`http://127.0.0.1:8000/watchlist_remove/${listing_id}`);
            alert('Item has been removed from Watchlist');

        }
        
    }
})