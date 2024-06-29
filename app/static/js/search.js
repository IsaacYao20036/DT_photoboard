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

            let firstLetter
            if (value == "fname") {
                firstLetter = p[i].classList[0].charAt(0)
            } else if (value == "lname") {
                firstLetter = p[i].classList[1].charAt(0)
            }
            

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
