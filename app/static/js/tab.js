// Switch between tab content
function openTab(evt, tabName) {
    var i, tabContent, tabBtn;
  
    tabContent = document.getElementsByClassName("tabContent");
    for (i = 0; i < tabContent.length; i++) {
      tabContent[i].style.display = "none";
    }

    tabBtn = document.getElementsByClassName("tabBtn");
    for (i = 0; i < tabBtn.length; i++) {
      tabBtn[i].className = tabBtn[i].className.replace(" active", "");
    }

    document.getElementById(tabName).style.display = "grid";
    evt.currentTarget.className += " active";
}

// Open default tab
window.addEventListener('DOMContentLoaded', 
    function defaultOpen() { 
        document.getElementById("defaultOpen").click();
    }
)