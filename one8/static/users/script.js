document.addEventListener("DOMContentLoaded", function() {
    const password1Field = document.getElementById("id_password1");
    const password2Field = document.getElementById("id_password2");

    password2Field.addEventListener("input", function() {
        if (password1Field.value !== password2Field.value) {
            password2Field.setCustomValidity("Passwords do not match");
        } else {
            password2Field.setCustomValidity("");
        }
    });

    const signupForm = document.getElementById("signupForm");

    signupForm.addEventListener("submit", function(event) {
        if (!signupForm.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }

        signupForm.classList.add("was-validated");
    });
});
