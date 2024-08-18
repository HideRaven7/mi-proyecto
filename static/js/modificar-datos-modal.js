// Obtener el modal
var modal = document.getElementById("registro-modal");

// Obtener todos los botones de "Editar"
var btnEditores = document.querySelectorAll(".btn-editar");

// Obtener el elemento <span> que cierra el modal
var span = document.querySelector("#registro-modal .close");

// Función para abrir el modal con los datos del estudiante
function abrirModal(estudianteId) {
    // Aquí cargarías los datos del estudiante en los campos del formulario
    // Por ahora, simplemente mostraremos el modal
    modal.style.display = "block";
}

// Función para cerrar el modal
function cerrarModal() {
    modal.style.display = "none";
}

// Asignar eventos a los botones de "Editar"
btnEditores.forEach(function(btn) {
    btn.addEventListener("click", function() {
        var estudianteId = btn.getAttribute("data-estudiante-id");
        abrirModal(estudianteId);
    });
});

// Evento para cerrar el modal al hacer clic en <span> (x)
span.addEventListener("click", function() {
    cerrarModal();
});

// Evento para cerrar el modal al hacer clic fuera del modal
window.addEventListener("click", function(event) {
    if (event.target == modal) {
        cerrarModal();
    }
});

// Evento para guardar los cambios
var btnGuardarCambios = document.querySelector("#registro-modal .btn-guardar-cambios");
btnGuardarCambios.addEventListener("click", function() {
    // Aquí puedes implementar la lógica para guardar los cambios
    // Puedes obtener los valores de los campos y realizar una petición AJAX, por ejemplo
    cerrarModal();
});