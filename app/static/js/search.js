document.getElementById("filterSelect").onchange = changeListener;

function changeListener() {
    let value = this.value

    if (value == "fname") {
        document.getElementById("alphabetLinks_f").style.display = "block"
        document.getElementById("alphabetLinks_l").style.display = "none"
        document.getElementById("allCards_f").style.display = "block"
        document.getElementById("allCards_l").style.display = "none"
    } else if (value == "lname") {
        document.getElementById("alphabetLinks_f").style.display = "none"
        document.getElementById("alphabetLinks_l").style.display = "block"
        document.getElementById("allCards_f").style.display = "none"
        document.getElementById("allCards_l").style.display = "block"
    }
}
