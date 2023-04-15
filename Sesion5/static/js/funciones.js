function evaluar_edad(edad){
    if (edad > 0 && edad < 18){
        window.alert('Es menor de edad')
    } else if(edad >= 18 && edad < 60){
        window.alert('Es mayor de edad')
    }else if(edad >= 60 && edad <= 110){
        window.alert('Es de la tercera edad')
    } else{
        window.alert('Edad no válida')
    }
}

function factorial(n){
    f = n;
    for(i = 1; i < n; i++){
        console.log(i);
        f = f*i;
    }
    return f;
}

function factorial2(n){
    let f = n;
    let i = 1;
    while(i<n){
        console.log(i);
        f = f*i;
        i++;
    }
    return f;
}