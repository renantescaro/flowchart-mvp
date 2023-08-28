const $ = go.GraphObject.make;
const myDiagram = new go.Diagram("myDiagramDiv", { "undoManager.isEnabled": true });


myDiagram.nodeTemplate = $(go.Node, "Auto",
    $(go.Shape, "Rectangle",
        {
            stroke: null,
            portId: "",
            cursor: "pointer",
            fromLinkable: true,
            fromLinkableSelfNode: true,
            fromLinkableDuplicates: true,
            toLinkable: true,
            toLinkableSelfNode: true,
            toLinkableDuplicates: true
        },
        new go.Binding("fill", "color")),
    $(go.TextBlock,
        { margin: 6, font: "18px sans-serif" },
        new go.Binding("text"))
);

function newFlowchart() {
    myDiagram.model = new go.GraphLinksModel();
}

function saveWorkBtn() {
    openModalSaveWork()
}

function loadWorkBtn() {
    openModalLoadWork()
}

function run() {
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "run");
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
    const body = myDiagram.model.toJson()
    console.log(body)

    xhr.onload = () => {
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log(JSON.parse(xhr.responseText));
        } else {
            console.log(`Error: ${xhr.status}`);
        }
    };
    xhr.send(body);
}

function createNewNode() {
    closeModal()

    let nodeName = document.getElementById("inpNodeName").value
    let nodeColor = document.getElementById("inpNodeColor").value

    let dataContent = getdata()

    const data = { text: nodeName, color: nodeColor, dataContent: dataContent };
    myDiagram.model.addNodeData(data);
    const node = myDiagram.findPartForData(data);

    node.location = myDiagram.lastInput.documentPoint;
    console.log(node.location)
}

function getdata() {
    let nodeType = document.getElementById("slcNodeType").value

    if (nodeType == "getRequest") {
        return new GetRequest()
    }

    if (nodeType == "postRequest") {
        return new PostRequest()
    }

    if (nodeType == "parserData") {
        return new Parser()
    }
}

class PostRequest {
    constructor() {
        let bodyPost = document.getElementById("inpBodyPost").value
        let headersPost = document.getElementById("inpHeadersPost").value

        this.nodeType = document.getElementById("slcNodeType").value
        this.url = document.getElementById("inpUrlPost").value
        this.body = bodyPost ? JSON.parse(bodyPost) : {}
        this.headers = headersPost ? JSON.parse(headersPost) : {}
    }
}

class GetRequest {
    constructor() {
        this.nodeType = document.getElementById("slcNodeType").value
        this.url = document.getElementById("inpUrlGet").value
        this.params = document.getElementById("inpParamsGet").value
    }
}

class Parser {
    constructor() {
        let dataInputParser = document.getElementById("inpDataInputParser").value
        let dataExitParser = document.getElementById("inpDataExitParser").value

        this.nodeType = document.getElementById("slcNodeType").value
        this.dataInput = dataInputParser ? JSON.parse(dataInputParser) : {}
        this.dataExit = dataExitParser ? JSON.parse(dataExitParser) : {}
    }
}
