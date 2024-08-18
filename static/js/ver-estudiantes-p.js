document.querySelectorAll('.ver-estudiante-p').forEach((element, index) => {
    element.addEventListener('click', () => {
      document.querySelectorAll('.modal-p-estudiantes')[index].style.display = 'block';
    });
  });