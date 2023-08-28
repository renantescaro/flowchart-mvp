
var modalLoadWork = document.getElementById("modalLoadWork");
var myDiagramDiv = document.getElementById('myDiagramDiv');

function openModalLoadWork() {
    modalLoadWork.style.display = "block";
    myDiagramDiv.style.zIndex = -1;
    listWorks()
}

function listWorks() {
    var get = new XMLHttpRequest()
    get.open("GET", "/work/list", true)
    get.send()
    get.onreadystatechange = function () {
        if (get.readyState == 4 && get.status == 200) {
            let response = JSON.parse(get.responseText)

            let bodyModalLoadWork = document.getElementById("bodyModalLoadWork")
            response.forEach(e => {
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
                    loadWorks(e["id"])
                    closeModalLoadWork()
                }
                tdBtn.append(btnSelect)

                tr.append(tdId)
                tr.append(tdName)
                tr.append(tdDescription)
                tr.append(tdBtn)

                bodyModalLoadWork.append(tr)
            });
        }
    }
}

function loadWorks(idWork) {
    var get = new XMLHttpRequest()
    get.open("GET", "/work/load/" + idWork, true)
    get.send()
    get.onreadystatechange = function () {
        if (get.readyState == 4 && get.status == 200) {
            myDiagram.model = new go.GraphLinksModel(JSON.parse(get.responseText));
        }
    }
}

function closeModalLoadWork() {
    modalLoadWork.style.display = "none";
    myDiagramDiv.style.zIndex = 0;
}
