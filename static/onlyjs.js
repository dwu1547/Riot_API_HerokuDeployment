
//test
document.getElementById("temp_region").innerHTML ="This will be the summoner stats page"; //document.getElementById("region").innerHTML

//transfer ranks to card (Solo/Duo)
var ranksolo = document.getElementById("solorank").textContent;
if(String(ranksolo).includes("Unranked") == false) {
var getsolo = ranksolo.split("_");
document.getElementById("cardsolotier").innerHTML = getsolo[0];
document.getElementById("cardsolorank").innerHTML = getsolo[1];
document.getElementById("soloimg").src = "static/badges/" + ranksolo + ".png";
//"static/badges/" + String(getsolo[0]) + "_" + String(getsolo[1]) +"_badge.png";k
}else{
document.getElementById("cardsolotier").innerHTML = "Unranked";
document.getElementById("cardsolorank").innerHTML = "NaN";
document.getElementById("soloimg").src = "static/badges/unranked_badge.png";
}

//transfer ranks to card (Flex)
var rankflex = document.getElementById("flexrank").textContent;
if(String(rankflex).includes("Unranked") == false) {
var getflex = rankflex.split("_");
document.getElementById("cardflextier").innerHTML = getflex[0];
document.getElementById("cardflexrank").innerHTML = getflex[1];
document.getElementById("fleximg").src = "static/badges/" + rankflex + ".png";

}else{
document.getElementById("cardflextier").innerHTML = "Unranked";
document.getElementById("cardflexrank").innerHTML = "NaN";
document.getElementById("fleximg").src = "static/badges/" + "unranked_badge.png";
}

//transfer ranks to card (TT)
var ranktt = document.getElementById("ttrank").textContent;
if(String(ranktt).includes("Unranked") == false) {
var gettt = ranktt.split("_");
document.getElementById("cardtttier").innerHTML = gettt[0];
document.getElementById("cardttrank").innerHTML = gettt[1];
document.getElementById("ttimg").src = "static/badges/" + ranktt +".png";

}else{
document.getElementById("cardtttier").innerHTML = "Unranked";
document.getElementById("cardtttier").innerHTML = "Unranked";
document.getElementById("cardttrank").innerHTML = "NaN";
document.getElementById("ttimg").src = "static/badges/unranked_badge.png";
}