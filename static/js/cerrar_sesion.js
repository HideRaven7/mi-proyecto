async function confirmarOperacion() {
    // Utilizamos un Promise para manejar la operación asíncrona
    return new Promise((resolver) => {
        // Mostramos el cuadro de diálogo de SweetAlert2
        Swal.fire({
            html: '<span class="white">"Est&aacute; seguro que quiere cerrar sesion?"</span',
            backdrop: true,
            customClass: {
                popup: 'emergente-class',
                confirmButton: 'confirm-eme',
                container: 'container-eme',
            },
            imageUrl: './imagenes/recursos/logo-jes.png',
            imageWidth: '140px',
            imageHeight: '120px',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, continuar',
            cancelButtonText: 'Cancelar'
        }).then((resultado) => {
            // Resolvemos el Promise con el valor de la acción del usuario
            resolver(resultado.isConfirmed);
        });
    });
}

// Ejemplo de uso
async function cerrarSesion() {
    // Esperamos la confirmación del usuario
    const confirmado = await confirmarOperacion();

    // si el resultado es true (confirmar) entonces mandara al index.html
    if (confirmado) {
        window.location = 'index.html';
    }
}

// Llamamos a la función cerrar sesion
cerrarSesion();
