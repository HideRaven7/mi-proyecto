const inputImagen = document.getElementById('subir-imagen');
const imagenPreview = document.getElementById('preview');

inputImagen.addEventListener('change', function() {
    if (this.files && this.files[0]) {
        const lector = new FileReader();

        lector.onload = function(e) {
            const imagen = document.createElement('img');
            imagen.src = e.target.result;
            imagenPreview.innerHTML = '';
            imagenPreview.appendChild(imagen);
        };

        lector.readAsDataURL(this.files[0]);
    }
});