
var modalLoadWork = document.getElementById("modalLoadWork");
var myDiagramDiv = document.getElementById('myDiagramDiv');

function openModalLoadWork() {
    modalLoadWork.style.display = "block";
    myDiagramDiv.style.zIndex = -1;
    listWorks()
}

function createWorksTableList(dataTableList) {
    let bodyModalLoadWork = document.getElementById("bodyModalLoadWork")
    bodyModalLoadWork.innerHTML = null

    dataTableList.forEach(e => {
        let tr = document.createElement("tr")
        let tdId = document.createElement("td")
        let tdName = document.createElement("td")
        let tdDescription = document.createElement("td")
        let tdBtn = document.createElement("td")

        tdId.textContent = e["id"]
        tdName.textContent = e["name"]
        tdDescription.textContent = e["description"]

        let btnSelect = document.createElement("button")
        btnSelect.className = "btn btn-primary"
        btnSelect.textContent = "Select"
        btnSelect.onclick = function () {
            document.getElementById("inpWorkId").value = e["id"]
            document.getElementById("h2WorkTitle").textContent = e["name"]
            loadWorks(e["id"])
            closeModalLoadWork()
        }
        tdBtn.append(btnSelect)

        let btnDelete = document.createElement("button")
        btnDelete.className = "btn btn-danger"
        btnDelete.textContent = "Delete"
        btnDelete.onclick = function () {
            if (confirm("Do you really want to delete?")) {
                deleteWork(e["id"])
                closeModalLoadWork()
            }
        }
        tdBtn.append(btnDelete)

        tr.append(tdId)
        tr.append(tdName)
        tr.append(tdDescription)
        tr.append(tdBtn)

        bodyModalLoadWork.append(tr)
    });
}

function listWorks() {
    var get = new XMLHttpRequest()
    get.open("GET", "/work/list", true)
    get.send()
    get.onreadystatechange = function () {
        if (get.readyState == 4 && get.status == 200) {
            let response = JSON.parse(get.responseText)
            createWorksTableList(response)
        }
    }
}

function deleteWork(idWork) {
    var post = new XMLHttpRequest()
    post.open("POST", "/work/delete", true)
    post.setRequestHeader("Content-Type", "application/json");
    post.send(JSON.stringify({
        "id": idWork
    }))
    post.onreadystatechange = function () {
        if (post.readyState == 4 && post.status == 200) {
            // JSON.parse(post.responseText)
            alert("Deleted")
        }
        else if (post.readyState == 4 && post.status == 400) {
            // JSON.parse(post.responseText)
            alert("Error!")
        }
    }
}

function loadWorks(idWork) {
    var get = new XMLHttpRequest()
    get.open("GET", "/work/load/" + idWork, true)
    get.send()
    get.onreadystatechange = function () {
        if (get.readyState == 4 && get.status == 200) {
            dataContent = JSON.parse(get.responseText)

            document.getElementById('iptNameSaveWork').value = dataContent.name
            document.getElementById('iptDescriptionSaveWork').value = dataContent.description

            myDiagram.model = new go.GraphLinksModel(dataContent['data']);
        }
    }
}

function closeModalLoadWork() {
    modalLoadWork.style.display = "none";
    myDiagramDiv.style.zIndex = 0;
}
