document.getElementById("filterSelect").onchange = changeListener;

function changeListener(){
    var value = this.value

    if (value == "fname"){
        document.getElementById("fnameSorted").style.display = "none";
    } else if (value == "lname"){
        document.getElementById("lnameSorted").style.display = "none";
    }

}