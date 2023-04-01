var x = prompt("Donne un premier num ");
var y = prompt("Donne un deuxièmen num ")

var result = Number(y) - Number(x);

if (result > 10){
    console.log("The result is greater than 10");
} else if (result > 0){
    console.log("but not bigger than 10");
} else if(result ==0){
    console.log("égale à 0");
} else{
    console.log("c'est négatif poto");
}