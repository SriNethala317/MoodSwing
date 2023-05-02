const username = document.querySelector(".username")
const password = document.querySelector(".password")
const loginSubmit = document.querySelector(".loginSubmit")

loginSubmit.addEventListener("click", login)

function login() {

  let data = new FormData();
  data.usern = String(username.value);
  data.pass = String(password.value);
  fetch("/loginProcess", {

    method: "POST",
    headers: new Headers({
      "Content-Type": "application/json"
    }),
    body: JSON.stringify(data)

  })
    .then(response => response.json()).then(data => location.href = data)
}


