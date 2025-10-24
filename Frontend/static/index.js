document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.querySelector(".toggle-sidebar");
  const sidebar = document.getElementById("sidebar");

  toggleBtn.addEventListener("click", function () {
    sidebar.classList.toggle("collapsed");
  });
});

const block3button = document.getElementsByClassName("block3button");
block3button.onclick = function viewusage() {
  window.open("../templates/usage.html", "_self");
};
