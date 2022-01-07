window.addEventListener('load', function () {
    const btnDelete = document.querySelectorAll('.btnDelete');
    btnDelete.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        })
    })
})