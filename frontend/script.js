document.addEventListener("DOMContentLoaded", () => {
    const tabela = document.getElementById("tabela-dados");
    const form = document.getElementById("form-registro");
    const selectAno = form.data_lancamento;
    const buscaInput = document.getElementById("busca-filme");

    for (let ano = 2026; ano >= 1950; ano--) {
        const opt = document.createElement("option");
        opt.value = opt.textContent = ano;
        selectAno.appendChild(opt);
    }

    const carregar = () => {
        const busca = buscaInput.value.trim();
        const url = "http://127.0.0.1:5000/api/registros" + (busca ? `?titulo=${encodeURIComponent(busca)}` : "");

        fetch(url)
            .then(r => r.json())
            .then(dados => {
                tabela.innerHTML = "";
                if (dados.length === 0) {
                    tabela.innerHTML = "<tr><td colspan='5'>Nenhum resultado encontrado.</td></tr>";
                    return;
                }

                dados.forEach(d => {
                    const tr = document.createElement("tr");
                    tr.innerHTML = `
                        <td><input value="${d.nome}" /></td>
                        <td><input value="${d.titulo}" /></td>
                        <td><input value="${d.data_lancamento}" type="number"/></td>
                        <td>
                            <select>
                                <option value="Alugar">Alugar</option>
                                <option value="Reservar">Reservar</option>
                            </select>
                        </td>
                        <td>
                            <div class="grupo-botoes">
                                <button class="editar">
                                    <img src="static/imagens/lapis.png" alt="Editar" width="20" height="20">
                                </button>
                                <button class="excluir">
                                    <img src="static/imagens/excluir.png" alt="Excluir" width="20" height="20">
                                </button>
                            </div>
                        </td>`;

                    const select = tr.querySelector("select");
                    select.value = d.description === "Reservar" ? "Reservar" : "Alugar";

                    tr.querySelector(".editar").onclick = () => {
                        const [nome, titulo, ano] = tr.querySelectorAll("input");
                        const desc = tr.querySelector("select");

                        fetch(`http://127.0.0.1:5000/api/registros/${d.registro_id}`, {
                            method: "PUT",
                            headers: { "Content-Type": "application/json" },
                            body: JSON.stringify({
                                nome: nome.value,
                                titulo: titulo.value,
                                data_lancamento: ano.value,
                                description: desc.value
                            })
                        }).then(res => {
                            if (!res.ok) {
                                return res.json().then(ret => abrirModal(ret.erro || "Erro ao editar."));
                            }
                            carregar();
                        });
                    };

                    tr.querySelector(".excluir").onclick = () => {
                        fetch(`http://127.0.0.1:5000/api/registros/${d.registro_id}`, {
                            method: "DELETE"
                        }).then(res => {
                            if (!res.ok) {
                                return res.json().then(ret => abrirModal(ret.erro || "Erro ao excluir."));
                            }
                            carregar();
                        });
                    };

                    tabela.appendChild(tr);
                });
            });
    };

    form.onsubmit = e => {
        e.preventDefault();
        const dados = Object.fromEntries(new FormData(form).entries());

        fetch("http://127.0.0.1:5000/api/registros", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        }).then(async (res) => {
            const retorno = await res.json();
            if (!res.ok) {
                abrirModal(retorno.erro || "Erro ao cadastrar.");
                return;
            }
            form.reset();
            carregar();
        });
    };

    buscaInput.addEventListener("input", carregar);

    carregar();
});

function abrirModal(mensagem) {
    document.getElementById("mensagem-erro-modal").textContent = mensagem;
    document.getElementById("modal-erro").style.display = "block";
}

function fecharModal() {
    document.getElementById("modal-erro").style.display = "none";
}
