document.addEventListener('DOMContentLoaded', function() {
    const modalsContainer = document.querySelector('.agregar-material-section');

    modalsContainer.addEventListener('click', function(event) {
        if (event.target === modalsContainer) {
            window.history.back();
        }
    });

    const modalAggMaterial = document.querySelector('.agregar-material-fieldset');

    modalAggMaterial.addEventListener('click', function(event) {
        event.stopPropagation();
    });
});