document
  .getElementById("ollamaapiinputEnter")
  .addEventListener("click", getollamaapivalue);

function startollamaapiConnection() {
  // add fetch/get/post stuff
}

function getollamaapivalue() {
  document.getElementsByClassName("ollamaapiinput");
  const ollamaapiinput = document.getElementsByClassName("ollamaapiinput");
  let ollamaapivalue = ollamaapiinput.value;

  console.log(`Ollama API is set to ${ollamaapivalue}`);
  startollamaapiConnection();
}
