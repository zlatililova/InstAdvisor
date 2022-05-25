 function openSignUp(){
    var mod = document.getElementById('id02');
    if (mod.style.display == 'block') {
        mod.style.display = 'none';
    }
    var modal = document.getElementById('id01');
    if (modal.style.display == 'none') {
        modal.style.display = 'block';
    }

}

function openSignIn(){
    var mod = document.getElementById('id01');
    if (mod.style.display == 'block') {
        mod.style.display = 'none';
    }
    var modal = document.getElementById('id02');
    if (modal.style.display == 'none') {
        modal.style.display = 'block';
    }

}
{/* Get the modal */}
var modal = document.getElementById('id01');

{/* When the user clicks anywhere outside of the modal, close it */}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}