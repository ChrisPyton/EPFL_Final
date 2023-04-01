var language_1 = prompt("language 1 ?");
var language_2 = prompt("language 2 ?");
var number = prompt("number ?");
var color = prompt("color ?");

if (language_1 =="Python" && language_2 =="Python" || language_1 == "Javascript" && language_2=="Python"){
    console.log("it's a good course");
}else if(language_1 == "Python" && language_2 == "Javascript" || language_1 =="Javascript" && language_2 =="Python"){
    console.log("this is Thinking and Creating with Code course");
}else if (number > 10 || color =="blue"){
    console.log("the test is true");
}else if(number < 10 || color != "blue"){
    console.log("it's true");
}
