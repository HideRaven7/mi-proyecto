function calcularPorcentaje() {
    var fila = this.parentElement.parentElement;
    var inputs = fila.getElementsByTagName('input');
    var totalAsistencias = 0;
    var cantidadAsistencias = 0;

    for (var j = 0; j < inputs.length - 1; j++) {
        if (inputs[j].value.trim() !== '') {
            var asistencia = parseInt(inputs[j].value);
            if (!isNaN(asistencia)) {
                totalAsistencias += asistencia;
                cantidadAsistencias++;
            }
        }
    }

    if (cantidadAsistencias === 5) {
        var promedioAsistencias = totalAsistencias / 5; 
        var resultado = promedioAsistencias.toFixed(0) + '%'; 
        fila.lastElementChild.textContent = resultado; 
    } else {
        fila.lastElementChild.textContent = '';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var filas = document.getElementsByClassName('fila-asistencia');
    for (var i = 0; i < filas.length; i++) {
        var inputs = filas[i].getElementsByTagName('input');
        inputs[4].addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                calcularPorcentaje.call(this);
            }
        });
    }
});