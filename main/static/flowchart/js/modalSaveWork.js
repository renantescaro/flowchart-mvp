
var modalSaveWork = document.getElementById("modalSaveWork");
var myDiagramDiv = document.getElementById('myDiagramDiv');

function saveWork() {
    let workId = document.getElementById("inpWorkId").value
    let endpoint = "/work/save"
    if (workId) {
        endpoint += `/${workId}`
    }

    let post = new XMLHttpRequest()
    let body = JSON.stringify({
        "name": document.getElementById('iptNameSaveWork').value,
        "description": document.getElementById('iptDescriptionSaveWork').value,
        "data": myDiagram.model.toJson()
    })
    post.open("POST", endpoint, true)
    post.setRequestHeader("Content-Type", "application/json");
    post.send(body)
    post.onreadystatechange = function () {
        if (post.readyState == 4 && post.status == 200) {
            closeModalSaveWork()
        }
        else if (post.readyState == 4 && post.status == 400) {
            closeModalSaveWork()
            alert("Error to save!")
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
