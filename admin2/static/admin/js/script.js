// Get modal and buttons
const modal = document.getElementById("modal");
const openModalBtn = document.getElementById("open-modal-btn");
const closeModalBtn = document.getElementById("close-modal-btn");

// Open modal
openModalBtn.addEventListener("click", () => {
  modal.classList.add("show");
});

// Close modal
closeModalBtn.addEventListener("click", () => {
  modal.classList.remove("show");
});

// Optional: Close modal when clicking outside the modal content
window.addEventListener("click", (e) => {
  if (e.target === modal) {
    modal.classList.remove("show");
  }
});

// ===========================================================
// Selectors for the update modal and form fields
const updateModal = document.getElementById("modal-update");
const updateNameInput = document.getElementById("book-update-name");
const updateLevelInput = document.getElementById("book-update-level");
const closeUpdateModalBtn = updateModal.querySelector(".cancel-btn");
let currentUpdateForm; // To hold the dynamic form action URL for updating

// Function to open the Update Modal with pre-filled data
document.querySelectorAll(".edit").forEach((editButton) => {
  editButton.addEventListener("click", (event) => {
    const row = event.target.closest(".table-row");
    const bookId = row.querySelector(".column").textContent.trim();
    const bookName = row.querySelector(".column[data-title]").dataset.title;
    const bookLevel = row.querySelector(".column[data-title]").nextElementSibling.dataset.title;

    // Set form fields with current book data
    updateNameInput.value = bookName;
    updateLevelInput.value = bookLevel;

    // Set the form action dynamically
    currentUpdateForm = updateModal.querySelector("form");
    currentUpdateForm.action = `/admin2/panel/book/update/${bookId}`;

    // Open the modal
    updateModal.style.display = "block";
  });
});

// Close the update modal
closeUpdateModalBtn.addEventListener("click", () => {
  updateModal.style.display = "none";
});

// =====================================================================================
