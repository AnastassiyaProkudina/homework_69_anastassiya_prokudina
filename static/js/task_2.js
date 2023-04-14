BASEURL = 'http://127.0.0.1:8000/add/'
const button = document.getElementById("add");
const numberA = document.getElementById("a").value;
const numberB = document.getElementById("b").value;
let result = document.getElementById("result");
const answer = {"A": parseInt(numberA), "B": parseInt(numberB)};
const settings = {
    method: 'POST',
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        body: JSON.stringify(answer)
    }
}

async function aMakeRequest(url, settings) {
    let response = await fetch(url, settings);
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function getData(event) {
    event.preventDefault();
    try {
        const headers= {
              "Content-Type": "application/json",
              "X-CSRFToken": document.cookie.split('=')[1]
            }
        let data = await aMakeRequest(BASEURL, settings)
        console.log(data)
        result.innerText = data

    } catch (error) {
        console.log(error)
    }
}

button.addEventListener('click', getData)