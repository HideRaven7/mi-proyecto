document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById("agregarProfesorModal");
    const btn = document.getElementById("agg-profesor-btn");
    const span = document.getElementsByClassName("close")[0];
    const searchBtn = document.getElementById("searchBtn");
    const profesorList = document.getElementById("profesorList");
    const assignmentForm = document.getElementById("assignmentForm");
    const selectedProfesorIdInput = document.getElementById("selectedProfesorId");
    const searchInput = document.getElementById("searchInput");
  
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
  
    // Buscar profesores
    searchBtn.addEventListener('click', () => {
        const searchOption = document.querySelector('input[name="searchOption"]:checked').value;
        const query = searchInput.value;

        fetch(`/admin/buscar-profesores?searchOption=${searchOption}&query=${query}`)
            .then(response => response.json())
            .then(data => {
                profesorList.innerHTML = '';
                data.forEach(profesor => {
                    const profesorDiv = document.createElement('div');
                    profesorDiv.className = 'profesor-item';
                    profesorDiv.innerHTML = `
                        <p>${profesor.nombre} ${profesor.apellido}</p>
                        <button onclick="mostrarFormularioAsignacion(${profesor.id_profesor})">Asignar</button>
                    `;
                    profesorList.appendChild(profesorDiv);
                });
            });
    });

    // Mostrar el formulario de asignación
    window.mostrarFormularioAsignacion = (id) => {
        assignmentForm.style.display = 'block';
        selectedProfesorIdInput.value = id; 
        console.log("ID Profesor asignado:", id); // Verificar el ID
    };
});
