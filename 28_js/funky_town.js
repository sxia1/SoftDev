//Indigo Ink
//Cathy Cai, Sophia Xia
//SoftDev1 pd6
//K28 -- Sequential Progression
//2018-12-28

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

var stulist = ["james", "tyler", "lauren", "becky", "oliver", "frank"];

var randstu = function(){
    var num = Math.floor(Math.random() * stulist.length);
    return stulist[num];
}
