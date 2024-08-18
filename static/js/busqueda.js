document.getElementById('buscar-estudiantes').addEventListener('input', function() {
    const query = this.value.toLowerCase();
    const rows = document.querySelectorAll('#tbody-estudiantes tr');

    rows.forEach(row => {
        const cells = row.getElementsByTagName('td');
        let match = false;
        for (let i = 0; i < cells.length; i++) {
            if (cells[i].textContent.toLowerCase().includes(query)) {
                match = true;
                break;
            }
        }
        row.style.display = match ? '' : 'none';
    });
});

// Función de búsqueda para profesores
document.getElementById('buscar-profesores').addEventListener('input', function() {
    const query = this.value.toLowerCase();
    const rows = document.querySelectorAll('#tbody-profesores tr');

    rows.forEach(row => {
        const cells = row.getElementsByTagName('td');
        let match = false;
        for (let i = 0; i < cells.length; i++) {
            if (cells[i].textContent.toLowerCase().includes(query)) {
                match = true;
                break;
            }
        }
        row.style.display = match ? '' : 'none';
    });
});