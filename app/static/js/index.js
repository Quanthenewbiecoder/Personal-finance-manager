document.addEventListener("DOMContentLoaded", () => {
    const headers = document.querySelectorAll(".month-header");

    headers.forEach(header => {
        header.addEventListener("click", () => {
            const tableContainer = header.nextElementSibling.nextElementSibling;
            if (tableContainer && tableContainer.classList.contains("month-table")) {
                tableContainer.classList.toggle("expanded");
            }
        });
    });
});
