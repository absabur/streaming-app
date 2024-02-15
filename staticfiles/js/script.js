window.addEventListener("DOMContentLoaded", () => {
  var elementWidth = document.querySelector(".video-section");
  if (elementWidth) {
    elementWidth.style.height = `${parseInt(
      elementWidth.clientWidth / 1.78
    )}px`;
  }

  let cross = document.querySelector(".cross");
  if (cross) {
    cross.addEventListener("click", () => {
      cross.previousElementSibling.value = "";
    });
  }

  let see_toggle = document.querySelector(".see-toggle");
  let short = document.querySelector(".short");
  let full = document.querySelector(".full");
  if (see_toggle) {
    short.style.display = "block";
    full.style.display = "none";
    see_toggle.addEventListener("click", () => {
      if (see_toggle?.textContent == "See Full") {
        see_toggle.textContent = "See Less";
        short.style.display = "none";
        full.style.display = "block";
      } else {
        see_toggle.textContent = "See Full";
        short.style.display = "block";
        full.style.display = "none";
      }
    });
  }
});
