 document.getElementById('imagen-materia').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
    const imgElement = document.createElement('img');
    imgElement.src = e.target.result;

    const imageContainer = document.getElementById('imagen-materia-js');
    imageContainer.innerHTML = ''; // Limpiar el contenedor antes de agregar la nueva imagen
    imageContainer.appendChild(imgElement);
};

    if (file) {
        reader.readAsDataURL(file);
 }
});