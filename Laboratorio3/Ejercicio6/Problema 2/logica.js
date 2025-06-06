function seleccionarInterfaz(tipo){
    let interfaz = document.getElementById("interfaz");
    if (tipo === "aritmetica") {
        operacionesAritmeticas();
        //interfaz.innerHTML = "<p>Interfaz de operaciones aritméticas (próximamente)</p>";
    } else if (tipo === "logica") {
        operacionesLogicas();
        //interfaz.innerHTML = "<p>Interfaz de operaciones lógicas (próximamente)</p>";
    } else if (tipo === "bits") {
        operacionesBits();
        //interfaz.innerHTML = "<p>Interfaz de operaciones de bits (próximamente)</p>";
    }
    
}
function operacionesAritmeticas(){
    let interfaz = document.getElementById("interfaz");
    let html = `
        <h2>Operaciones aritméticas</h2>
        <div class="fila-horizontal">
            <input type="number" id="num1" placeholder="Número 1">
            <select id="operacion">
                <option value="sumar">Sumar</option>
                <option value="restar">Restar</option>
                <option value="multiplicar">Multiplicar</option>
                <option value="dividir">Dividir</option>
            </select>
            <input type="number" id="num2" placeholder="Número 2">
            <button onclick="calcular()">Calcular</button>
        </div>
        <p id="resultado"></p>
    `;

    interfaz.innerHTML = html;

}
function calcular(){
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let operacion = document.getElementById("operacion").value;
    let resultado = document.getElementById("resultado");
    let res;
    if (isNaN(num1) || isNaN(num2)) {
        alert("Por favor ingrese números válidos.");
        return;
    }
    switch (operacion) {
        case "sumar":
            res = num1 + num2;
            break;
        case "restar":
            res = num1 - num2;
            break;
        case "multiplicar":
            res = num1 * num2;
            break;
        case "dividir":
            if (num2 !== 0) {
                res = num1 / num2;
            } else {
                res = "Error: División por cero";
            }
            break;
    }
    resultado.innerText = "Resultado: " + res;
}
function operacionesLogicas(){
    let interfaz = document.getElementById("interfaz");
    let html = `
        <h2>Operaciones lógicas</h2>
        <div class="fila-horizontal">
            <select id="num1">
                <option value="v">Verdadero (v)</option>
                <option value="f">Falso (f)</option>
            </select>
            <select id="num2">
                <option value="v">Verdadero (v)</option>
                <option value="f">Falso (f)</option>
            </select>
            <select id="operacion">
                <option value="and">∧ (AND)</option>
                <option value="or">∨ (OR)</option>
                <option value="not">¬ (NOT - solo num1)</option>
                <option value="equiv">↔ (Si y solo si)</option>
                <option value="implica">→ (Entonces)</option>
            </select>
            <button onclick="calcularLogica()">Calcular</button>
        </div>
        <p id="resultado"></p>
    `;
    interfaz.innerHTML = html;
    document.getElementById("operacion").addEventListener("change", function () {
        const operacion = this.value;
        const num2 = document.getElementById("num2");

        if (operacion === "not") {
            num2.disabled = true;
            num2.value = ""; //limpiar el campo
        } else {
            num2.disabled = false;
        }
    });
}
function calcularLogica(){
    let num1 = document.getElementById("num1").value.toLowerCase();
    let num2 = document.getElementById("num2").value.toLowerCase();
    let operacion = document.getElementById("operacion").value;
    let resultado = document.getElementById("resultado");
    let res;
    if (num1 !== "v" && num1 !== "f") {
        alert("Por favor ingrese valores booleanos válidos (v o f).");
        return;
    }
    if (operacion !== "not" && (num2 !== "v" && num2 !== "f")) {
        alert("Por favor ingrese 'v' o 'f' como valor para el segundo número.");
        return;
    }
    let bool1 = (num1 === "v");
    let bool2 = (num2 === "v");
    switch (operacion) {
        case "and":
            res = bool1 && bool2;
            break;
        case "or":
            res = bool1 || bool2;
            break;
        case "not":
            res = !bool1;
            break;
        case "equiv":
            res = bool1 === bool2;
            break;
        case "implica":
            res = !bool1 || bool2; // A → B = ¬A ∨ B
            break;
        default:
            res = "Operación no válida";
    }

    resultado.innerText = "Resultado: " + (res ? "v" : "f");
}
function operacionesBits(){
    let interfaz = document.getElementById("interfaz");
    let html = `
        <h2>Operaciones de bits</h2>
        <div class="fila-horizontal">
            <input type="number" id="num1" placeholder="Número 1">
            <input type="number" id="num2" placeholder="Número 2">
            <select id="operacion">
                <option value="and">AND</option>
                <option value="or">OR</option>
                <option value="xor">XOR</option>
                <option value="not">NOT (solo num1)</option>
            </select>
            <button onclick="calcularBits()">Calcular</button>
        </div>
        <p id="resultadoBinario"></p>
        <p id="resultadoDecimal"></p>
    `;

    interfaz.innerHTML = html;
    document.getElementById("operacion").addEventListener("change", function () {
        const operacion = this.value;
        const num2 = document.getElementById("num2");
        if (operacion === "not") {
            num2.disabled = true;
            num2.value = "";
        } else {
            num2.disabled = false;
        }
    });

}
function calcularBits() {
    let num1 = document.getElementById("num1").value.trim();
    let num2 = document.getElementById("num2").value.trim();
    let operacion = document.getElementById("operacion").value;
    let resultadoBinario = document.getElementById("resultadoBinario");
    let resultadoDecimal = document.getElementById("resultadoDecimal");

    // Validar entrada binaria
    if (!/^[01]+$/.test(num1) || (operacion !== "not" && !/^[01]+$/.test(num2))) {
        alert("Por favor ingrese solo números binarios (compuestos de 0 y 1).");
        return;
    }
    let n1 = parseInt(num1, 2);
    let n2 = parseInt(num2, 2);
    let res;
    switch (operacion) {
        case "and":
            res = n1 & n2;
            break;
        case "or":
            res = n1 | n2;
            break;
        case "xor":
            res = n1 ^ n2;
            break;
        case "not":
            // Obtener NOT de solo los bits de num1
            let length = num1.length;
            let mask = (1 << length) - 1; // Ej: para 4 bits: 1111
            res = (~n1) & mask;
            break;
        default:
            res = NaN;
    }
    if (!isNaN(res)) {
        resultadoBinario.innerText = "Resultado en binario: " + res.toString(2).padStart(num1.length, '0');
        resultadoDecimal.innerText = "Resultado en decimal: " + res;
    } else {
        resultadoBinario.innerText = "Resultado no válido";
        resultadoDecimal.innerText = "";
    }
}