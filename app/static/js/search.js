document.getElementById("filterSelect").onchange = changeListener;

function changeListener(){
    var value = this.value

    if (value == "fname"){
        document.getElementById("fnameSorted").style.display = "grid";
        document.getElementById("lnameSorted").style.display = "none";
    } else if (value == "lname"){
        document.getElementById("lnameSorted").style.display = "grid";
        document.getElementById("fnameSorted").style.display = "none";
    }

}