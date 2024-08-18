const menu = document.querySelector('.menu');

menu.addEventListener('click',() => {
    Swal.fire({
        html: '<nav><ul class="ul-eme"><li class="li-eme"><a href="/estudiante/perfil/" class="a-eme">Perfil</a></li><li class="li-eme"><a href="/estudiante/refuerzo/libros" class="a-eme home-eme">Refuerzo de curso</a></li><li class="li-eme"><a href="/estudiante/material/" class="a-eme material-eme">Material de tareas</a></li><li class="li-eme"><a href="/" class="a-eme cerrar-eme">Cerrar Sesion</a></li></ul></nav>',
        backdrop: true,
        customClass: {
            popup: 'emergente-class classes-eme',
            confirmButton: 'confirm-eme',
            container: 'container-eme conta-eme'
        },
        buttonsStyling: false,
        showCloseButton: false,
        // closeButtonAriaLabel: "cerrar",
        allowOutsideClick: true,
        confirmButtonText: "Aceptar",
        showConfirmButton: false,
        position: 'top-right',
        // grow: 'column'
    });
});