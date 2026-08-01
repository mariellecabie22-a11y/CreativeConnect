document.addEventListener("DOMContentLoaded", () => {
    setupWhitespaceValidation();
    setupCharacterCounters();
    setupDeleteConfirmations();
    setupAutoDismissAlerts();
});


function setupWhitespaceValidation() {
    const forms = document.querySelectorAll(".js-validate-form");

    forms.forEach((form) => {
        form.addEventListener("submit", (event) => {
            let isValid = true;

            const fields = form.querySelectorAll(
                "input[type='text'][required], textarea[required]"
            );

            fields.forEach((field) => {
                const value = field.value.trim();

                if (value.length === 0) {
                    field.classList.add("is-invalid");
                    isValid = false;
                } else {
                    field.classList.remove("is-invalid");
                }
            });

            if (!isValid) {
                event.preventDefault();
            }
        });
    });
}


function setupCharacterCounters() {
    const fields = document.querySelectorAll("[data-character-counter]");

    fields.forEach((field) => {
        const counterId = field.dataset.characterCounter;
        const counter = document.getElementById(counterId);

        if (!counter) {
            return;
        }

        const updateCounter = () => {
            const currentLength = field.value.length;
            const maximumLength = field.maxLength;

            counter.textContent = `${currentLength}/${maximumLength}`;
        };

        field.addEventListener("input", updateCounter);
        updateCounter();
    });
}


function setupDeleteConfirmations() {
    const deleteForms = document.querySelectorAll(".js-confirm-delete");

    deleteForms.forEach((form) => {
        form.addEventListener("submit", (event) => {
            const itemName =
                form.dataset.itemName || "this item";

            const confirmed = window.confirm(
                `Are you sure you want to delete ${itemName}?`
            );

            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
}


function setupAutoDismissAlerts() {
    const alerts = document.querySelectorAll(
        ".alert[data-auto-dismiss='true']"
    );

    alerts.forEach((alert) => {
        window.setTimeout(() => {
            const bootstrapAlert =
                bootstrap.Alert.getOrCreateInstance(alert);

            bootstrapAlert.close();
        }, 5000);
    });
}