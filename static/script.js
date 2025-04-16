// Lidar com o envio do formulário
//document.getElementById("review-form").addEventListener("submit", function(event) {
  //event.preventDefault();

  // Obter os valores do formulário
  const name = document.getElementById("nome").value;
  const rating = document.getElementById("nota").value;
  const comment = document.getElementById("comentario").value;

  // Validação da nota
  if (rating < 1 || rating > 5) {
    alert("A nota deve estar entre 1 e 5.");
    return; // Para evitar adicionar avaliações inválidas
  }

  // Criar um novo comentário
  const reviewItem = document.createElement("li");
  reviewItem.innerHTML = `<strong>${name}</strong> (Nota: ${rating})<br>${comment}`;

  // Adicionar o comentário à lista
  document.getElementById("reviews-list").appendChild(reviewItem);

  // Limpar o formulário
  document.getElementById("review-form").reset();
//});
