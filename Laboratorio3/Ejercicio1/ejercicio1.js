let fechaActual= new Date();
let day=fechaActual.getDay();
console.log(fechaActual);
console.log(day);
console.log(fecha(day));
function fecha(day){
    switch(day){
        case 0:
            return "domingo";
        case 1:
            return "lunes";
        case 2:
            return "martes";
        case 3:
            return "miercoles";
        case 4:
            return "jueves";
        case 5:
            return "viernes";
        case 6:
            return "sabado";
        default:
            return "no valido";                           
    }
}