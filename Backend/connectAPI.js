function getollamaapivalue() {
    document.getElementsByClassName('ollamaapiinput')
    const ollamaapiinput =  document.getElementsByClassName('ollamaapiinput')
    let ollamaapivalue = ollamaapiinput.value 

    console.log(`Ollama API is set to ${ollamaapivalue}`);
}
