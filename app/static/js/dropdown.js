// Code from W3Schools: https://www.w3schools.com/howto/howto_js_dropdown.asp


/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function toggleDropdown(dropdownID) {
    
    if (dropdownID == facultyDropdown) {
        document.getElementById("facultyDropdown").classList.toggle("show-block")
    }
    else if (dropdownID == principalDropdown) {
        document.getElementById("principalDropdown").classList.toggle("show")
    }
    else if (dropdownID == leadershipTeamDropdown) {
        document.getElementById("leadershipTeamDropdown").classList.toggle("show")
    }
    else if (dropdownID == deansDropdown) {
        document.getElementById("deansDropdown").classList.toggle("show")
    }
    else if (dropdownID == counsellorsDropdown) {
        document.getElementById("counsellorsDropdown").classList.toggle("show")
    }
    
    if (dropdownID == accountDropdown) {
        document.getElementById("accountDropdown").classList.toggle("show-block")
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
            else if (openDropdown.classList.contains('show-block')) {
                openDropdown.classList.remove('show-block');
            }
        }
    }
    
}
