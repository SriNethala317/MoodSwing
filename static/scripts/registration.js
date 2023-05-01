const username = document.querySelector(".username")
const password = document.querySelector(".password")
const registrationSubmit = document.querySelector(".registrationSubmit")

registrationSubmit.addEventListener("click", register)

function register() {

  let data = new FormData();
  data.usern = String(username.value)
  data.pass = String(password.value)
  fetch("/registrationProcess", {
    method: "POST",
    headers: new Headers({
      "Content-Type": "application/json"
    }),
    body: JSON.stringify(data)

  })
    .then(response => response.json()).then(data => location.href = data)
}









