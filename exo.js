function saysay(name){
console.log("hello "+name);
}

saysay("Rick");

function hola(naam){
var message = "hello " + naam;
return message;
}

var result = hola("Rick");
console.log(result);

function add(nb1,nb2){
var resultat = nb1 + nb2;
return resultat;
}
var result2 = add(3,4);
console.log(result2);

//Temperature converter

function Temperature(Celsius){
var degree = (Celsius * 9/5) + 32;
return degree;
}

var result3 = Temperature(21.5);
console.log(result3);

var Number1 =5;
var string = "3";
var result = Number1 + Number(string); 

// cm in inch

function convert(cm){
var inch = cm / 2.54;
return cm.toString() + " represents " + inch.toString() + " Inches";
}

console.log(convert(10));
