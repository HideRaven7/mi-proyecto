document.addEventListener('DOMContentLoaded', function() {
    // Mostrar el modal de perfil
    document.querySelector('#material-p').addEventListener('click', function() {
        const recursoEstudio = document.querySelector('.modal-recurso-de-estudio');
        if (recursoEstudio) recursoEstudio.style.display = 'block';
        document.querySelector('.modal-recurso-de-estudio-container').style.display = 'block';
    });

    // Cerrar el modal al hacer clic fuera
    document.querySelector('.modal-recurso-de-estudio-container').addEventListener('click', function(event) {
        if (event.target === this) {
            this.style.display = 'none';
            const recursoEstudio = document.querySelector('.modal-recurso-de-estudio');
            if (recursoEstudio) recursoEstudio.style.display = 'none';
        }
    });
});