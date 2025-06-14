function solve(val) {
    var v = document.getElementById("result");
    v.value += val;
}
function result() {
    var v = document.getElementById("result");
    try {
        v.value = eval(v.value);
    } catch (e) {
        v.value = "Error";
    }
}
function clearDisplay() {
    var v = document.getElementById("result");
    v.value = "";
}
function backspace() {
    var v = document.getElementById("result");
    v.value = v.value.slice(0, -1);
}
