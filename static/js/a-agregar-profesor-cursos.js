document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById("agregarProfesorModal");
    const btn = document.getElementById("agg-profesor-btn");
    const span = document.getElementsByClassName("close")[0];
    const searchBtn = document.getElementById("searchBtn");
    const profesorList = document.getElementById("profesorList");
  
    // Abrir el modal
    btn.onclick = function() {
      modal.style.display = "block";
    }
  
    // Cerrar el modal
    span.onclick = function() {
      modal.style.display = "none";
    }
  
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }
  
    // Manejar búsqueda de profesores
    searchBtn.onclick = function() {
      // Borrar lista de profesores
      profesorList.innerHTML = "";
  
      // Obtener opción de búsqueda y valor de búsqueda
      const searchOption = document.querySelector('input[name="searchOption"]:checked').value;
      const searchInput = document.getElementById("searchInput").value.toLowerCase();
  
      // Hacer una solicitud a la API o base de datos para obtener los profesores
      fetch(`/buscarProfesores?opcion=${searchOption}&valor=${searchInput}`)
        .then(response => response.json())
        .then(profesores => {
          // Mostrar resultados
          profesores.forEach(profesor => {
            const div = document.createElement("div");
            div.textContent = `${profesor.nombre} - ${profesor.materia} - ${profesor.matricula}`;
            profesorList.appendChild(div);
          });
        })
        .catch(error => {
          console.error('Error al buscar profesores:', error);
        });
    }
  });
  