document.addEventListener('DOMContentLoaded', function() {
    // Mostrar el modal de perfil
    document.querySelector('.ver-estudiante-p').addEventListener('click', function() {
        const modal_verEstudiante = document.querySelector('.modal-p-estudiantes');
        if (modal_verEstudiante) modal_verEstudiante.style.display = 'flex';
        document.querySelector('.modal-perfil').style.display = 'flex';
    });

    // Cerrar el modal al hacer clic fuera
    document.querySelector('.modal-p-estudiantes').addEventListener('click', function(event) {
        if (event.target === this) {
            this.style.display = 'none';
            const modal_verEstudiante = document.querySelector('.modal-p-estudiantes');
            if (modal_verEstudiante) modal_verEstudiante.style.display = 'none';
        }
    });
});