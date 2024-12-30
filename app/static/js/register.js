// Toggle the visibility of the password and confirm password fields
document.getElementById('showPassword').addEventListener('click', function() {
    var passwordInput = document.getElementById('password');
    if (this.checked) {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
});

document.getElementById('showConfirmPassword').addEventListener('click', function() {
    var confirmPasswordInput = document.getElementById('confirm_password');
    if (this.checked) {
        confirmPasswordInput.type = 'text';
    } else {
        confirmPasswordInput.type = 'password';
    }
});

document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    var formData = new FormData(this);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', this.action, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('Accept', 'application/json'); // Expect JSON response

    xhr.onload = function() {
        try {
            // Check if the response is not empty before parsing
            if (xhr.responseText) {
                var response = JSON.parse(xhr.responseText);

                if (xhr.status === 200) {
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
                } else if (xhr.status === 401) {
                    // Handle unauthorized error specifically
                    Swal.fire({
                        title: 'Unauthorized!',
                        text: 'You are not authorized to perform this action.',
                        icon: 'warning',
                        confirmButtonText: 'OK'
                    });
                } else {
                    // Handle other server errors
                    Swal.fire({
                        title: 'Error!',
                        text: response.message || 'An error occurred. Please try again.',
                        icon: 'error',
                        confirmButtonText: 'OK'
                    });
                }
            } else {
                // Handle empty or invalid JSON response
                Swal.fire({
                    title: 'Error!',
                    text: 'Empty response from the server.',
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
