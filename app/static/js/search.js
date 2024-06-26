sortFirstName()

document.getElementById("filterSelect").onchange = changeListener;

function changeListener(){
    var value = this.value

    if (value == "fname"){
        sortFirstName();
    } else if (value == "lname"){
        sortLastName();
    }

}


// Sort List code from W3Schools, it has been modified

function sortFirstName() {
    var div, i, switching, p, shouldSwitch;
    div = document.getElementById("allCards");
    switching = true;
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        p = div.getElementsByTagName("p");
        // Loop through all list items:
        for (i = 0; i < (p.length - 1); i++) {
            // Start by saying there should be no switching:
            shouldSwitch = false;
            /* Check if the next item should
            switch place with the current item: */
            if (p[i].innerHTML.toLowerCase() > p[i + 1].innerHTML.toLowerCase()) {
                /* If next item is alphabetically lower than current item,
                mark as a switch and break the loop: */
                shouldSwitch = true;
                
                break;
            }
        }
        if (shouldSwitch) {
            /* If a switch has been marked, make the switch
            and mark the switch as done: */
            // p[i].parentNode.parentNode.insertBefore(p[i + 1].parentNode, p[i].parentNode);
            div.insertBefore(p[i + 1].parentNode.parentNode, p[i].parentNode.parentNode);
            switching = true;
        }
    }
}


function sortLastName() {
    var div, i, switching, p, shouldSwitch, firstLetter, divA;
    div = document.getElementById("allCards");
    switching = true;
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        p = div.getElementsByTagName("p");
        // o_O     :>     B)     \o/     (^-.-^)     (._. )     (*˘︶˘*)     ❀◕ ‿ ◕❀     (◍•ᴗ•◍)❤     ₍՞◌′ᵕ‵ू◌₎♡     (๑꒪▿꒪)*     ⁄(⁄ ⁄•⁄-⁄•⁄ ⁄)⁄      :P    D:     :?
        // Loop through all list items:
        for (i = 0; i < (p.length - 1); i++) {
            // Start by saying there should be no switching:
            shouldSwitch = false;
            /* Check if the next item should
            switch place with the current item: */
            if (p[i].className.toLowerCase() > p[i + 1].className.toLowerCase()) {
                /* If next item is alphabetically lower than current item,
                mark as a switch and break the loop: */
                shouldSwitch = true;
                
                break;
            }
        }
        if (shouldSwitch) {
            /* If a switch has been marked, make the switch
            and mark the switch as done: */
            div.insertBefore(p[i + 1].parentNode.parentNode, p[i].parentNode.parentNode);
            switching = true;
        }
    }

    // divA = document.getElementById("divA")
    // for (i = 0; i < (p.length); i++) {
    //     firstLetter = p[i].className.charAt(0)
    //     p[i].classList.add(firstLetter)
    //     if (p[i].classList[1] == "A") {
    //         divA.appendChild(p[i].parentNode)
    //         console.log(p[i].className)
    //     }
    // }
}


function myFunction() {

    var div, i, switching, p, shouldSwitch;
    div = document.getElementById("allCards");
    switching = true;
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        p = div.getElementsByTagName("p");
        // Loop through all list items:
        for (i = 0; i < (p.length-1); i++) {
            // Start by saying there should be no switching:
            shouldSwitch = false;

            firstLetter = p[i].className.charAt(0)
            p[i].classList.add(firstLetter) 
            // console.log(p[i].className)

            /* Check if the next item should
            switch place with the current item: */
            if (p[i].classList[1] > p[i + 1].classList[1]) {
                /* If next item is alphabetically lower than current item,
                mark as a switch and break the loop: */
                console.log(p[i].classList[1])
                shouldSwitch = true;
                
                break;
            }
        }
        if (shouldSwitch) {
            /* If a switch has been marked, make the switch
            and mark the switch as done: */
            div.insertBefore(p[i + 1].parentNode.parentNode, p[i].parentNode.parentNode);
            switching = true;
        }
    }
}