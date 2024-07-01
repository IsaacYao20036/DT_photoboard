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
    
    if (value == "fname") {
        originalAllCards = document.getElementById("allCards_l");
        console.log(originalAllCards)
    } else if (value == "lname") {
        originalAllCards = document.getElementById("allCards_f");
        console.log(originalAllCards)
    }

    // Move profile cards that are in the alphabet groups and back into their original div
    const allAlphabetDivs = [divA,divB,divC,divD,divE,divF,divG,divH,divI,divJ,divK,divL,divM,divN,divO,divP,divQ,divR,divS,divT,divU,divV,divW,divX,divY,divZ]
    for (i = 0; i < (allAlphabetDivs.length); i++) {
        let profileCard = allAlphabetDivs[i].getElementsByTagName("div")[0];
        console.log(profileCard)
        
        while (profileCard) {
            originalAllCards.appendChild(profileCard)
            console.log(originalAllCards)
            profileCard = allAlphabetDivs[i].getElementsByTagName("div")[0];
        }
    }

    // get p tags from one of the divs based on filter chosen
    let allCards
    
    if (value == "fname") {
        allCards = document.getElementById("allCards_f");
    } else if (value == "lname") {
        allCards = document.getElementById("allCards_l");
    }
    let p = allCards.getElementsByTagName("p");

    while (p.length != 0) {

        for (i = 0; i < (p.length); i++) {
            let firstLetter = p[i].className.charAt(0)
            
            // sort cards in alphabet groups and remove from their div
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
}
