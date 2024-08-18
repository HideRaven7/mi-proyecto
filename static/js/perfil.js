document.addEventListener('DOMContentLoaded', function() {
    const modalsContainer = document.querySelector('.modals-container');

    modalsContainer.addEventListener('click', function(event) {
        if (event.target === modalsContainer) {
            window.history.back();
        }
    });

    const modalPerfil = document.querySelector('.modal-perfil');

    modalPerfil.addEventListener('click', function(event) {
        event.stopPropagation();
    });
});