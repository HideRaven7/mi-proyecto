document.addEventListener('DOMContentLoaded', function() {
    // Mostrar el modal de perfil
    document.querySelector('.ver-recurso').addEventListener('click', function() {
        const verRecurso = document.querySelector('.modal-clases-enviada');
        if (verRecurso) verRecurso.style.display = 'block';
        document.querySelector('.modal-c-enviada-container').style.display = 'block';
    });

    // Cerrar el modal al hacer clic fuera
    document.querySelector('.modal-c-enviada-container').addEventListener('click', function(event) {
        if (event.target === this) {
            this.style.display = 'none';
            const verRecurso = document.querySelector('.modal-clases-enviada');
            if (verRecurso) verRecurso.style.display = 'none';
        }
    });
});