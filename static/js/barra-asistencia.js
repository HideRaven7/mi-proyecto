document.addEventListener('DOMContentLoaded', function() {
    const barraCircular = document.querySelector('.barra-circular');
    const progresoCircular = barraCircular.querySelector('.progreso-circular');
    const porcentajeSpan = barraCircular.querySelector('.porcentaje');
    const porcentaje = parseFloat(porcentajeSpan.textContent.replace('%', ''));

    const radius = progresoCircular.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;

    progresoCircular.style.strokeDasharray = `${circumference} ${circumference}`;
    progresoCircular.style.strokeDashoffset = circumference;

    const offset = circumference - (porcentaje / 100) * circumference;
    progresoCircular.style.strokeDashoffset = offset;
});