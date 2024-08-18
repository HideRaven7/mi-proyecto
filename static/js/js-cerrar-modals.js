

document.addEventListener("DOMContentLoaded", function() {
    const modalsContainer = document.querySelector('.modals-container');

    if (modalsContainer) {
        modalsContainer.addEventListener('click', function(event) {
            // Verificar que el clic haya ocurrido en el contenedor principal
            if (event.target === modalsContainer) {
                // Evitar que el evento se propague
                event.stopPropagation();

                // Realizar history.back() al hacer clic en modals-container
                history.back();
            }
        });
    }
});


