
var modalSaveWork = document.getElementById("modalSaveWork");
var myDiagramDiv = document.getElementById('myDiagramDiv');

function saveWork() {
    let post = new XMLHttpRequest()
    let body = JSON.stringify({
        "name": document.getElementById('iptNameSaveWork').value,
        "description": document.getElementById('iptDescriptionSaveWork').value,
        "data": myDiagram.model.toJson()
    })
    post.open("POST", "/work/save", true)
    post.setRequestHeader("Content-Type", "application/json");
    post.send(body)
    post.onreadystatechange = function () {
        if (post.readyState == 4 && post.status == 200) {
            myDiagram.model = new go.GraphLinksModel(JSON.parse(post.responseText));
            closeModalSaveWork()
        }
    }
}

function openModalSaveWork() {
    modalSaveWork.style.display = "block";
    myDiagramDiv.style.zIndex = -1;
}

function closeModalSaveWork() {
    modalSaveWork.style.display = "none";
    myDiagramDiv.style.zIndex = 0;
}
