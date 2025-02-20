document.querySelectorAll(".edit").forEach((editButton) => {
    editButton.addEventListener("click", (event) => {
        const unitId = event.target.dataset.id;
        const unitNum = event.target.dataset.unitNum;
        const bookId = event.target.dataset.bookId;

        // Check if unitId is valid
        if (!unitId) {
            console.error("Unit ID is missing.");
            return;
        }

        // Set the form action dynamically
        const updateForm = document.getElementById("update-unit-form");
        updateForm.action = `/admin2/panel/unit/update/${unitId}/`;

        // Set the form values
        document.getElementById("unit-num").value = unitNum;
        document.getElementById("book-select-update").value = bookId;

        // Open the modal
        updateModal.classList.add('show');
    });
});
