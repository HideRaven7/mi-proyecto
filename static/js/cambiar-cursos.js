document.getElementById('cursos').addEventListener('change', function () {
    var cursoSelect = this.value
    if(cursoSelect) {
        window.location.href = cursoSelect;
    }
})
