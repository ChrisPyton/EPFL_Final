
var temperature = prompt("Quel température fait-il ?");
var météo = prompt("Quel météo ?");

if (temperature == "cold" && météo == "raining"){
    console.log("take an umbrella and a warm jacket.");
}else if (temperature == "warm" && météo == "raining"){
    console.log("take an umbrella and a t-shirt.");
}else if (temperature == "cold" && météo == "sunny"){
    console.log("take sunglasses and a warm jacket.");
}else if (temperature == "warm" && météo == "sunny"){
    console.log("take sunglasses and a t-shirt.");
 }else{
    "stay home!";
 }

