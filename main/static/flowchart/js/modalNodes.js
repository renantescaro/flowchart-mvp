
var mpopup = document.getElementById("mpopupBox");
var myDiagramDiv = document.getElementById('myDiagramDiv');

function openModal() {
    mpopup.style.display = "block";
    myDiagramDiv.style.zIndex = -1;
}

function closeModal() {
    mpopup.style.display = "none";
    myDiagramDiv.style.zIndex = 0;
}

function changeNodeTypeModal() {
    let nodeType = document.getElementById("slcNodeType").value

    if (nodeType == "getRequest") {
        document.getElementById("dvTypeGet").style.display = ""
        document.getElementById("dvTypePost").style.display = "none"
        document.getElementById("dvTypeParser").style.display = "none"
    }

    if (nodeType == "postRequest") {
        document.getElementById("dvTypePost").style.display = ""
        document.getElementById("dvTypeGet").style.display = "none"
        document.getElementById("dvTypeParser").style.display = "none"
    }

    if (nodeType == "parserData") {
        document.getElementById("dvTypeParser").style.display = ""
        document.getElementById("dvTypePost").style.display = "none"
        document.getElementById("dvTypeGet").style.display = "none"

    }
}
