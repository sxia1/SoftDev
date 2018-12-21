//Indigo Ink
//Cathy Cai, Sophia Xia
//SoftDev1 pd6
//K30 -- Sequential Progression III: Season of the Witch
//2018-12-21

var list = document.getElementById("thelist");

//upon button push, add an element to the list
var b = document.getElementById("b");
b.addEventListener('click', function(){
    var list_length = list.length;
    console.log(list_length);
    var node = document.createElement("li");
    var textnode = document.createTextNode("item WORD");
    node.appendChild(textnode);
    list.appendChild(node);
});

//when the mouse goes over an item in the list
//change the heading at the top to contain the text of the item
//when the mouse is no longer over an item in the list
//change the heading back to "Hello World!"
//when an item on the list is clicked, remove it from the DOM
/*
  array[0].addEventListener('mouseover', function(){h.innerHTML = array[0].innerHTML;});
  array[1].addEventListener('mouseover', function(){h.innerHTML = array[1].innerHTML;});
  array[2].addEventListener('mouseover', function(){h.innerHTML = array[2].innerHTML;});
  array[3].addEventListener('mouseover', function(){h.innerHTML = array[3].innerHTML;});
  ...
*/
var header = document.getElementById("h");
var array = document.getElementsByTagName("li");
for(var i = 0; i < array.length; i ++){
    var node = array[i];
    node.addEventListener('mouseover', function(){
	h.innerHTML = node.innerHTML;
    });
    node.addEventListener('mouseout', function(){
	h.innerHTML = "Hello World!";
    });
    node.addEventListener('click', function(){
	node.remove();
    });
}

//fibb function
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

//when the second button is pressed, 
//add a new item to your list, showing the next Fibonacci number
var fibblist = document.getElementById("fiblist");
var fb = document.getElementById("fb");
fb.addEventListener('click', function(){
    var list_length = fibblist.length;
    console.log(list_length);
    var node = document.createElement("li");
    var textnode = document.createTextNode(fibb(list_length).toString());
    node.appendChild(textnode);
    fibblist.appendChild(node);
});
