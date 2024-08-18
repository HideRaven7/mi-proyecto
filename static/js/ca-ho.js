const btnHorario = document.querySelector('.btn-horario');
const btnCalificacion = document.querySelector('.btn-calificaciones');
const tablaCalificacion = document.querySelector('.tabla-calificacion');
const tablaHorario = document.querySelector('.tabla-horario');
const ch_scroll = document.querySelector('.ca-ho-scroll');

// Función para deseleccionar todos los botones
function deseleccionarBotones() {
    // Remueve la clase 'btn-selected' de cada botón en la lista 'botones'
    botones.forEach(boton => boton.classList.remove('btn-selected'));
}

// Manejador de clic para el botón de Horario
btnHorario.addEventListener('click', () => {
    // Mostrar tabla de horario y ocultar tabla de calificación
    tablaHorario.style.display = 'table';
    tablaCalificacion.style.display = 'none';

    // Desplazarse 320px hacia abajo
    ch_scroll.scrollTo({ top: ch_scroll.scrollTop + 330, behavior: 'smooth' });
});

// Manejador de clic para el botón de Calificaciones
btnCalificacion.addEventListener('click', () => {
    // Mostrar tabla de calificación y ocultar tabla de horario
    tablaCalificacion.style.display = 'table';
    tablaHorario.style.display = 'none';

    // Volver al inicio (posición original)
    ch_scroll.scrollTo({ top: 0, behavior: 'smooth' });
});
