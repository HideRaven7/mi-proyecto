// modales_asistir_cali.js

// Función para abrir un modal
function openModal(modalId) {
    var modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "block";
    }
}

// Función para cerrar todos los modales
function closeAllModals() {
    var modals = document.querySelectorAll('.modal');
    modals.forEach(function(modal) {
        modal.style.display = "none";
    });
}

// Agregar eventos a los botones de cerrar
document.querySelectorAll('.modal .close').forEach(function(closeButton) {
    closeButton.addEventListener('click', function() {
        closeAllModals();
    });
});

// Agregar eventos a los enlaces que abren los modales
document.querySelectorAll('a[href^="#modal-"]').forEach(function(link) {
    link.addEventListener('click', function(event) {
        event.preventDefault(); // Evitar el comportamiento por defecto del enlace
        var modalId = this.getAttribute('href').substring(1); // Obtener el ID del modal
        openModal(modalId);
    });
});

// Agregar evento de clic fuera del modal para cerrarlo
window.addEventListener('click', function(event) {
    var modals = document.querySelectorAll('.modal');
    modals.forEach(function(modal) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
