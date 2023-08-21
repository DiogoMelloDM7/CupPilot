function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Verifica se o cookie começa com o nome do token CSRF
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function excluirJogador(jogadorId, equipeId) {
    if (confirm("Tem certeza que deseja excluir este jogador?")) {
        const csrftoken = getCookie('csrftoken');
        fetch(`/excluir-jogador/${jogadorId}`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": csrftoken,

            },
        })
        .then((response) => {
            if (response.ok) {
                window.location.href = `/editarequipe/${equipeId}` // Atualiza a página após excluir o item
            } else {
                alert("Ocorreu um erro ao excluir o jogador.");
            }
        })
        .catch((error) => {
            console.error("Erro na solicitação AJAX:", error);
        });
    }
}

function excluirEquipe(pk) {
    if (confirm("Tem certeza que deseja excluir esta equipe?")) {
        const csrftoken = getCookie('csrftoken');
        fetch(`/excluirequipe/${pk}`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": csrftoken,

            },
        })
        .then((response) => {
            if (response.ok) {
                window.location.reload();
            } else {
                alert("Ocorreu um erro ao excluir a equipe.");
            }
        })
        .catch((error) => {
            console.error("Erro na solicitação AJAX:", error);
        });
    }
}

function exibeTrocaDeNome(){
    let div = document.getElementById('trocadenome')
    let div2 = document.getElementById('nomeatual')
    div.style.display = "block";
    div2.style.display = "none";
}

function exibeAdicionarEquipe(){
    let div = document.getElementById("divtime")
    div.style.display = "block"
}

function excluirCampeonato(campeonatoId) {
    if (confirm("Tem certeza que deseja excluir este campeonato?")) {
        const csrftoken = getCookie('csrftoken');
        fetch(`/excluircampeonato/${campeonatoId}`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": csrftoken,

            },
        })
        .then((response) => {
            if (response.ok) {
                window.location.href = `/meuscampeonatos`
            } else {
                alert("Ocorreu um erro ao excluir o campeonato.");
            }
        })
        .catch((error) => {
            console.error("Erro na solicitação AJAX:", error);
        });
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const rodadas = document.querySelectorAll(".rodada-principal");
    let rodadaAtual = 1;

    function mostrarRodada(numeroRodada) {
        rodadas.forEach(function(rodada) {
            rodada.style.display = "none";
        });
        document.getElementById(`rodadaRodada ${numeroRodada}`).style.display = "block";
    }

    mostrarRodada(rodadaAtual);

    document.querySelectorAll(".avancar").forEach(function(botao) {
        botao.addEventListener("click", function() {
            rodadaAtual++;
            if (rodadaAtual > rodadas.length) {
                rodadaAtual = 1;
            }
            mostrarRodada(rodadaAtual);
        });
    });

    document.querySelectorAll(".voltar").forEach(function(botao) {
        botao.addEventListener("click", function() {
            rodadaAtual--;
            if (rodadaAtual < 1) {
                rodadaAtual = rodadas.length;
            }
            mostrarRodada(rodadaAtual);
        });
    });
});

