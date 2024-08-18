document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.descripcion-m-c-editar').addEventListener('click', function() {
        const editableElement = document.querySelector('.editable');

        if (editableElement.tagName.toLowerCase() === 'p') {
            // Convertir <p> a <textarea>
            const pElement = editableElement;
            const pContent = pElement.textContent;
            const textarea = document.createElement('textarea');
            textarea.style.resize = 'none'
            // textarea.style.minWidth = '930px'
            textarea.id = 'texto-material-curso';
            textarea.value = pContent;
            textarea.className = 'editable'; // Para mantener la clase y el estilo del CSS

            pElement.replaceWith(textarea);
        } else if (editableElement.tagName.toLowerCase() === 'textarea') {
            // Convertir <textarea> a <p>
            const textarea = editableElement;
            const textareaContent = textarea.value;
            const pElement = document.createElement('p');

            pElement.id = 'texto-material-curso';
            pElement.textContent = textareaContent;
            pElement.className = 'editable'; // Para mantener la clase y el estilo del CSS

            textarea.replaceWith(pElement);
        }
    });
});
