document.getElementById("filterSelect").onchange = changeListener;

function changeListener() {
    let value = this.value

    if (value == "fname") {
        myFunction(value)
    } else if (value == "lname") {
        myFunction(value)
    }
}


function myFunction(value) {

    // Remove cards that are in the alphabet groups and add back into allCards div
    const allAlphabetDivs = [divA,divB,divC,divD,divE,divF,divG,divH,divI,divJ,divK,divL,divM,divN,divO,divP,divQ,divR,divS,divT,divU,divV,divW,divX,divY,divZ]
    for (i = 0; i < (allAlphabetDivs.length); i++) {

        let profileCard = allAlphabetDivs[i].getElementsByTagName("div")[0];
        let allCards = document.getElementById("allCards");
        while (profileCard) {
            allCards.appendChild(profileCard)
            profileCard = allAlphabetDivs[i].getElementsByTagName("div")[0];
        }
    }

    let allCards = document.getElementById("allCards");
    let p = allCards.getElementsByTagName("p");

    while (p.length != 0) {

        for (i = 0; i < (p.length); i++) {

            // sorting based on filter chosen
            let firstLetter
            if (value == "fname") {
                firstLetter = p[i].classList[0].charAt(0)
            } else if (value == "lname") {
                firstLetter = p[i].classList[1].charAt(0)
            }
            
            // sort cards in alphabet groups and remove from allCards div
            if (firstLetter == "A") {
                divA.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "B") {
                divB.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "C") {
                divC.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "D") {
                divD.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "E") {
                divE.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "F") {
                divF.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "G") {
                divG.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "H") {
                divH.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "I") {
                divI.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "J") {
                divJ.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "K") {
                divK.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "L") {
                divL.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "M") {
                divM.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "N") {
                divN.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "O") {
                divO.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "P") {
                divP.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "R") {
                divR.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "S") {
                divS.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "T") {
                divT.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "U") {
                divU.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "V") {
                divV.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "W") {
                divW.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "X") {
                divX.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "Y") {
                divY.appendChild(p[i].parentNode.parentNode)
            } else if (firstLetter == "Z") {
                divZ.appendChild(p[i].parentNode.parentNode)
            }
        }
    }

    // for (i = 0; i < (allAlphabetDivs.length); i++) {

    //     let switching, shouldSwitch;
    //     switching = true;
    //     p = allAlphabetDivs[i].getElementsByTagName("p")

    //     /* Make a loop that will continue until
    //     no switching has been done: */
    //     while (switching) {
    //         // Start by saying: no switching is done:
    //         switching = false;

    //         // Loop through all list items:
    //         compareloop: for (j = 0; j < (p.length - 1); j++) {
    //             // Start by saying there should be no switching:
    //             shouldSwitch = false;

    //             /* Check if the next item should
    //             switch place with the current item: */
    //             if (value == "fname") {
    //                 console.log("fname")

    //                 if (p[j].classList[0] > p[j + 1].classList[0]) {
    //                     /* If next item is alphabetically lower than current item,
    //                     mark as a switch and break the loop: */
    //                     shouldSwitch = true;
    //                     break compareloop;
    //                 }
    //             } else if (value == "lname") {
    //                 console.log("lname")

    //                 if (p[j].classList[1] > p[j + 1].classList[1]) {
    //                     /* If next item is alphabetically lower than current item,
    //                     mark as a switch and break the loop: */
    //                     shouldSwitch = true;
    //                     break compareloop;
    //                 }
    //             }
                
    //         }
    //     }

    //     if (shouldSwitch) {
    //         /* If a switch has been marked, make the switch
    //         and mark the switch as done: */
    //         allAlphabetDivs[i].insertBefore(p[j + 1].parentNode.parentNode, p[j].parentNode.parentNode);
    //         switching = true;

    //         console.log([p[j], p[j+1]])
    //     }
    // }

}
