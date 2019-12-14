let searchBox = document.getElementById("searchBox")
let searchButton = document.getElementById("getButton")
let divElement = document.getElementById('removeElements')
let h1 = document.getElementById('h1Class')
function createData() {
    searchButton.addEventListener("click", function () {
        eel.getLinkFromSite(searchBox.value)
        divElement.innerHTML = "<div class='loader'></div>"
        setTimeout(function () {
            let jsonFile = [];
            updateMe(function (json) {
                document.getElementById('wrapper').style.display  =  'flex'
                const [model, name, pass] = document.querySelectorAll('#wrapper div');
                model.innerHTML+=`<p class="first"><strong>Model</strong></p>`
                name.innerHTML+=`<p class="first"><strong>Username</strong></p>`
                pass.innerHTML+=`<p class="first"><strong>Password</  strong></p>`
                Object.values(json).forEach(([entry]) => {
                    model.innerHTML+=`<p>${entry['Model']}</p>`
                    name.innerHTML+=`<p>${entry['Username']}</p>`
                    pass.innerHTML+=`<p>${entry['Password']}</p`
                })
              divElement.remove()
            })
            divElement.classList.toggle("newDisplay")
        }, 8000)

    });
}
function updateMe(callback) {
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', '../data.json', true);
    xobj.onreadystatechange = function () {
        if (xobj.readyState == 4 && xobj.status == "200") {
            callback(JSON.parse(xobj.responseText));
        }
    };
    xobj.send(null);
}
createData()