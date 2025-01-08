// Team JD :: Jayden Zhang, Danny Huang
// SoftDev pd5
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello"; // global variables
var j = 20; 


//assign an anonymous fxn to a var
var f = function(x) 
{
    var j=30; // variable in a variable [local variable]
    return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) { // function in a object, can be called with o.func(x)
              return x+30;
          }
        };

//create a new node in the tree
var addItem = function(text) // adds a bullet point to the list.
{
    var list = document.getElementById("thelist"); // calls the list with the HTML ID
    var newitem = document.createElement("li"); // creates next list item
    newitem.innerHTML = text;
    list.appendChild(newitem); // add it to the list and HTML updates [adds LOCALLY, does not directly change HTML file]
};

//prune a node from the tree
var removeItem = function(n) // removes a list item by the index
{
    var listitems = document.getElementsByTagName('li'); // retrieves a list item.
    listitems[n].remove(); // removes it LOCALLY from the list,
};

//color selected elements red
var red = function() // note: prioritizes blue color for some reason; works if you manually clear all class names.
{
    var items = document.getElementsByTagName("li"); // retrieves list item.
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red'); // adds red to the class of each item in the list to turn them red using css.
    }
};

//color a collection in alternating colors
var stripe = function() // note: prioritizes blue color for some reason; works if you manually clear all class names.
{
    var items = document.getElementsByTagName("li"); // gets all list items on the document.
    for(var i = 0; i < items.length; i++) { // changes them into alternating red and blue locally. 
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue');
	}
    }
};


//insert your implementations here for...
// FIB
let fib = function(n){
    if(n == 0){
        return 0;
    }
    else if (n == 1) {
        return 1;
    }
    else {
        return fib(n-1) + fib(n-2);
    }
}
// FAC
let fact = function(n){
    if (n == 1){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
}
// GCD
let gcd = function(a, b){
    var gcd
    for(i=0; i <= Math.min(a, b); i++){
        if(a%i==0 && b%i==0){
            gcd = i;
        }
    }
    return gcd
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {  // note: => is equailavent to function and is placed after the parameters
    // body
    return retVal;
};