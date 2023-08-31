
var mpopup = document.getElementById("mpopupBox");
var myDiagramDiv = document.getElementById('myDiagramDiv');

function openModal() {
    mpopup.style.display = "block";
    myDiagramDiv.style.zIndex = -1;
}

function openAddModal() {
    // hide NodeKey, because is a new node
    document.getElementById("dvNodeKey").style.display = "none"

    // change button from 'edit' to 'new'
    document.getElementById("btnModalNodesNew").style.display = ""
    document.getElementById("btnModalNodesEdit").style.display = "none"

    // clean inputs
    document.getElementById("inpNodeName").value = null
    document.getElementById("inpNodeColor").value = null
    document.getElementById("inpBodyPost").value = null
    document.getElementById("inpHeadersPost").value = null
    document.getElementById("inpUrlPost").value = null
    document.getElementById("inpUrlGet").value = null
    document.getElementById("inpParamsGet").value = null
    document.getElementById("inpDataInputParser").value = null
    document.getElementById("inpDataExitParser").value = null

    openModal()
}

function openEditModal(data) {
    console.log(data)

    document.getElementById("btnModalNodesNew").style.display = "none"
    document.getElementById("btnModalNodesEdit").style.display = ""

    // show NodeKey
    document.getElementById("dvNodeKey").style.display = ""

    // set values
    document.getElementById("inpNodeKey").value = data.key
    document.getElementById("slcNodeType").value = data.dataContent.nodeType
    document.getElementById("inpNodeName").value = data.text
    document.getElementById("inpNodeColor").value = data.color

    if (data.dataContent.nodeType == "postRequest") {
        document.getElementById("inpBodyPost").value = JSON.stringify(data.dataContent.body)
        document.getElementById("inpHeadersPost").value = JSON.stringify(data.dataContent.headers)
        document.getElementById("inpUrlPost").value = data.dataContent.url
    }

    if (data.dataContent.nodeType == "getRequest") {
        document.getElementById("inpUrlGet").value = data.dataContent.url
        document.getElementById("inpParamsGet").value = data.dataContent.params
    }

    if (data.dataContent.nodeType == "parserData") {
        document.getElementById("inpDataInputParser").value = JSON.stringify(data.dataContent.dataInput)
        document.getElementById("inpDataExitParser").value = JSON.stringify(data.dataContent.dataExit)
    }

    changeNodeTypeModal()
    openModal()
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
