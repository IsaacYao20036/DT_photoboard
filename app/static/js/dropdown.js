// Code from W3Schools: https://www.w3schools.com/howto/howto_js_dropdown.asp

// Show and hide nav dropdowns
function toggleDropdown(dropdownID) {

    if (dropdownID == facultyDropdown) {
        document.getElementById("facultyDropdown").classList.toggle("show")
    }
    if (dropdownID == accountDropdown) {
        document.getElementById("accountDropdown").classList.toggle("show")
    }

}


// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
    
}
