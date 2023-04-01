var first = prompt("donne un num");
var second = prompt("donne un deuxième");

if ((Number(second) - Number(first))>10){
    console.log("The result is > 10");
}else{ 
    if((Number(second) - Number(first))>0){
        console.log("the result > 0");
    } else{
        console.log("negative number");
    }

}
