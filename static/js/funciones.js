async function entrarMenu() {
    let visualizador = document.getElementById("menu-side-bar");
    visualizador.removeAttribute("class");

}

async function salirMenu() {
    let visualizador = document.getElementById("menu-side-bar");
    visualizador.setAttribute("class","no-mostrar");
}