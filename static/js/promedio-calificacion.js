function sumarCalificaciones() {
    var fila = this.parentElement.parentElement; // Obtiene la fila actual
    var inputs = fila.getElementsByTagName('input');
    var totalCalificaciones = 0;
    var cantidadCalificaciones = 0;

    for (var j = 0; j < inputs.length - 1; j++) {
        if (inputs[j].value.trim() !== '') { // Verifica si el valor no está vacío
            var calificacion = parseFloat(inputs[j].value);
            if (!isNaN(calificacion) && calificacion >= 0 && calificacion <= 100) { // Validación adicional
                totalCalificaciones += calificacion;
                cantidadCalificaciones++;
            }
        }
    }

    if (cantidadCalificaciones === 4) { // Asegura que haya exactamente cuatro calificaciones válidas
        var promedioCalificaciones = totalCalificaciones / 4; // Calcula el promedio directamente
        var promedioRedondeado = Math.round(promedioCalificaciones);

        fila.lastElementChild.textContent = promedioRedondeado.toFixed(0);
    } else {
        fila.lastElementChild.textContent = ''; // Si no hay exactamente cuatro calificaciones válidas, deja el resultado en blanco
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var filas = document.getElementsByClassName('fila-calificacion');
    for (var i = 0; i < filas.length; i++) {
        var inputs = filas[i].getElementsByTagName('input');
        for (var j = 0; j < inputs.length - 1; j++) {
            inputs[j].addEventListener('input', sumarCalificaciones);
        }
    }
});
