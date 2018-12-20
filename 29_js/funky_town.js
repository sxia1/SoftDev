//PoppySeeds
//Damian Wasilewicz, Sophia Xia
//SoftDev1 pd6
//K29 -- Sequential Progression II: Electric Boogaloo
//2018-12-19

var fibb = function(n){
    if(n == 0){
	return 0;
    }
    else if (n == 1){
	return 1;
    }
    else{
	return fibb(n -1) + fibb(n -2);
    }
};

var gcd = function (a,b) {
    // this means the previous modulo was 0, so a divided into b
    if (b == 0) {
	return a;
    }
    // finds the smallest interval between the two numbers,
    // if that interval fully divides into b, that is the gcd
    else {
	return gcd(b, a % b);
    }
};

var stulist = ["james", "tyler", "lauren", "becky", "oliver", "frank"];

var randstu = function(){
    var num = Math.floor(Math.random() * stulist.length);
    return stulist[num];
};

var a_tag = document.getElementById("resa");
var b_tag = document.getElementById("resb");
var c_tag = document.getElementById("resc");

var a = document.getElementById("buta");
a.addEventListener('click', function() {
    console.log(fibb(10));
    a_tag.innerHTML = fibb(10);
});

var b = document.getElementById("butb");
b.addEventListener("click", function() {
    console.log(gcd(10, 5));
    b_tag.innerHTML = gcd(10, 5);
});

var c = document.getElementById("butc");
c.addEventListener("click", function(){
    var name = randstu();
    console.log(name);
    c_tag.innerHTML = name;
});
