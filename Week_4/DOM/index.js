console.log("HELLO TANGO PLATOON!")
document.getElementById('Submit').addEventListener('click', function (event) {
    event.preventDefault()
})

function someFunction(){
    return Math.floor(Math.random()*100)+1
}
const randomNumber = someFunction();

function checkGuess(){
    let input = document.getElementById('num').value

    if (input < randomNumber) {
        let output=document.body.appendChild(document.createElement('p'));
        output.innerText=`${input} is too low`
    } else if (input > randomNumber) {
        let output=document.body.appendChild(document.createElement('p'));
        output.innerText=`${input} is too High`
    } else {
        let output=document.body.appendChild(document.createElement('p'));
        output.innerText=`Correct!`
    }
}

function refreshPage() {
    location.reload();
  }