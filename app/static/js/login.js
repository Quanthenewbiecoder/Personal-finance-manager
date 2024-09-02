// Toggle the visibility of the password
document.getElementById('showPassword').addEventListener('click', function() {
    var passwordInput = document.getElementById('password');
    if (this.checked) {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
});

// Handle the login form submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    var formData = new FormData(this);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', this.action, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('Accept', 'application/json'); // Expect JSON response

    xhr.onload = function() {
        if (xhr.status === 200) {
            try {
                var response = JSON.parse(xhr.responseText);
                if (response.success) {
                    Swal.fire({
                        title: 'Success!',
                        text: response.message,
                        icon: 'success',
                        confirmButtonText: 'OK'
                    }).then(() => {
                        window.location.href = response.redirect_url;
                    });
                } else {
                    Swal.fire({
                        title: 'Error!',
                        text: response.message,
                        icon: 'error',
                        confirmButtonText: 'OK'
                    });
                }
            } catch (e) {
                console.error('Failed to parse JSON response:', e);
                Swal.fire({
                    title: 'Error!',
                    text: 'An error occurred while processing the response.',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            }
        } else {
            Swal.fire({
                title: 'Error!',
                text: 'An error occurred. Please try again.',
                icon: 'error',
                confirmButtonText: 'OK'
            });
        }
    };

    xhr.onerror = function() {
        Swal.fire({
            title: 'Error!',
            text: 'Network error. Please check your connection and try again.',
            icon: 'error',
            confirmButtonText: 'OK'
        });
    };

    xhr.send(formData);
});
