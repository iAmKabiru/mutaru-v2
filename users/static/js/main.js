/*
if("serviceWorker" in navigator){
    navigator.serviceWorker.register('sw.js')
    .then(()=>{
       console.log('SW registered'); 
    })
}
*/


/*
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */ 
/*
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
*/



function openNav() {
    var x = document.getElementById("mySidenav");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }