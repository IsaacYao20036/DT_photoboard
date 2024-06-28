document.getElementById("filterSelect").onchange = changeListener;

function changeListener() {
    var value = this.value

    if (value == "fname") {
        document.getElementById("fnameSorted").style.display = "grid";
        document.getElementById("lnameSorted").style.display = "none";
        console.log(document.getElementById("lnameSorted").style.display);
    } else if (value == "lname") {
        document.getElementById("lnameSorted").style.display = "grid";
        document.getElementById("fnameSorted").style.display = "none";
        console.log(document.getElementById("lnameSorted").style.display);
    }

    myFunction()
}


function myFunction() {
    const allAlphabetDivs = [divA,divB,divC,divD,divE,divF,divG,divH,divI,divJ,divK,divL,divM,divN,divO,divP,divQ,divR,divS,divT,divU,divV,divW,divX,divY,divZ]
    for (i = 0; i < (allAlphabetDivs.length); i++) {
        allAlphabetDivs[i] = document.getElementById(allAlphabetDivs[i])
    }

    if (document.getElementById("lnameSorted").style.display == "grid") {
        divLname = document.getElementById("lnameSorted");
        p = divLname.getElementsByTagName("p");

        while (p.length != 0) {
            for (i = 0; i < (p.length); i++) {
            firstLetter = p[i].className.charAt(0)

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
        
        // if (p.length != 0) {
        //     console.log("Still not empty")
        //     console.log(p)
        // } else if (p.length == 0) {
        //     console.log("Empty")
        //     console.log(p)
        // } else {
        //     console.log("It did not work")
        // }
    }
}
    