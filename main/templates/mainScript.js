const $ = go.GraphObject.make;

const myDiagram =
    new go.Diagram("myDiagramDiv", { "undoManager.isEnabled": true });

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

// myDiagram.model = new go.TreeModel([
//     { key: 1, text: "Alpha", color: "lightblue" },
//     { key: 2, text: "Beta", color: "orange" },
//     { key: 3, text: "Gamma", color: "lightgreen" },
//     { key: 4, text: "Delta", color: "pink" }
// ]);

var mpopup = document.getElementById("mpopupBox");
var myDiagramDiv = document.getElementById('myDiagramDiv');

function saveWork() {

}

function loadWork() {

}

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
    }

    if (nodeType == "postRequest") {
        document.getElementById("dvTypePost").style.display = ""
        document.getElementById("dvTypeGet").style.display = "none"
    }

    if (nodeType == "parserData") {

    }
}

function run() {
    console.log(myDiagram.model.toJson())
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
        this.nodeType = document.getElementById("slcNodeType").value
        this.url = document.getElementById("inpUrlPost").value
        this.body = JSON.parse(document.getElementById("inpBodyPost").value)
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
        this.nodeType = document.getElementById("slcNodeType").value
    }
}
