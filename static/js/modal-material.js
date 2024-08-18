document.addEventListener('DOMContentLoaded', function() {
    // Mostrar el modal de perfil
    document.querySelector('.descripcion-m-c-editar').addEventListener('click', function() {
        const modalMaterial = document.querySelector('.modal-material-contenido');
        if (modalMaterial) modalMaterial.style.display = 'block';
        document.querySelector('.modal-material').style.display = 'block';
    });

    // Cerrar el modal al hacer clic fuera
    document.querySelector('.modal-material').addEventListener('click', function(event) {
        if (event.target === this) {
            this.style.display = 'none';
            const modalMaterial = document.querySelector('.modal-material-contenido');
            if (modalMaterial) modalMaterial.style.display = 'none';
        }
    });
});