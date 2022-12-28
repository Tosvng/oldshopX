function toggleForm() {
  document.getElementById("userForm").classList.toggle("d-none");
}

const multiStepForm = document.querySelector("[data-multi-step]");
console.log(multiStepForm);
const formSteps = [...multiStepForm.querySelectorAll("[data-step]")];

let currentStep = formSteps.findIndex((step) => {
  return step.classList.contains("active");
});

if (currentStep < 0) {
  currentStep = 0;
  showCurrentStep();
}

multiStepForm.addEventListener("click", (e) => {
  let increment;
  if (e.target.matches("[data-next]")) {
    increment = 1;
  } else if (e.target.matches("[data-previous]")) {
    increment = -1;
  }
  if (increment == null) return;

  const inputs = [...formSteps[currentStep].querySelectorAll("input")];
  const allValid = inputs.every((input) => input.reportValidity());
  if (allValid) {
    currentStep += increment;
    showCurrentStep();
  }
});

formSteps.forEach((step) => {
  step.addEventListener("animationend", (e) => {
    formSteps[currentStep].classList.remove("hide");
    e.target.classList.toggle("hide", !e.target.classList.contains("active"));
  });
});

function showCurrentStep() {
  formSteps.forEach((step, index) => {
    step.classList.toggle("active", index === currentStep);
  });
}

// COLLAPSING A DIV
const btn = document.getElementById("collapse-btn");
btn.addEventListener("click", () => {
  const targetDiv = document.getElementById("selector-panel");
  console.log(targetDiv);
  targetDiv.classList.toggle("collapsed");
});

// Handle viewing the image that the user hovers over
const hoverHandler = (image) => {
  const panel = document.getElementById("view-panel");
  panel.src = image.src;
};
