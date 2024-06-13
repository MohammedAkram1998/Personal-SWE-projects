
//FORM VALIDATION
function validate() {
	
	// Check that the firstname field is not blank
	if(document.regForm.firstname.value == "") {
		document.getElementById("firstnameMessage").innerHTML = "(First Name Can't Be Blank!!)";
		return false;
	} 
	// Check that the lastname field is not blank
	if(document.regForm.lastname.value == "") {
		document.getElementById("lastnameMessage").innerHTML = "(Last Name Can't Be Blank!!)";
		return false;
	}
	// Check that the Email field is not blank
	if(document.regForm.Email.value == "") {
		document.getElementById("emailMessage").innerHTML = "(Email Can't Be Blank!!)";
		return false;
	}
		return true;		
}


//IMAGE ROTATOR
console.log('Script loaded');

// Create an array to store the images for the rotator
var rotator_images = new Array();
rotator_images[0] = "Assets/Images/Facilities1.jpg";
rotator_images[1] = "Assets/Images/Facilities2.jpg";
rotator_images[2] = "Assets/Images/Facilities3.jpg";
rotator_images[3] = "Assets/Images/Facilities4.jpg";
rotator_images[4] = "Assets/Images/Facilities5.jpg";

// Create a counter variable to remember the current image
var counter = 0;

// Declare the functions for previous
function prev_image() {
	if(counter > 0) {
		counter = counter - 1;
	} else {
		counter = rotator_images.length-1;
	}
	
	document.getElementById("rotator_image").src = rotator_images[counter];
}

// Declare the functions for next
function next_image() {
	if(counter == rotator_images.length-1) {
		counter = 0;
	} else {
		counter = counter + 1;
	}
	
	document.getElementById("rotator_image").src = rotator_images[counter];
}

// Set the click events for the buttons
window.onload = function(){
document.getElementById("prev").onclick = function() { prev_image() };
document.getElementById("next").onclick = function() { next_image() };
}



//CHESS QUIZ
//Create an array to hold the quiz questions 
var questions = [];

//Create an array to hold the quiz answers
var answers = [];

//Set the questions and answers

//First Question
questions[0]  = "What shape does the knight move in?";
answers[0] = "L";

//Second Question
questions[1]  = "What does N stand for in chess?";
answers[1] = "Knight";

//Third Question
questions[2]  = "What colour traditionally goes first?";
answers[2] = "White";

//Fourth Question
questions[3]  = "How does the pawn capture?";
answers[3] = "Diagonally";

//Fifth Question
questions[4]  = "How many points is the king worth";
answers[4] = "0";

//Sixth Question
questions[5]  = "How many points is a rook worth?";
answers[5] = "5";

//Seventh Question
questions[6]  = "Can a king directly put another king in checkmate?";
answers[6] = "No";

//Eighth Question
questions[7]  = "Name the piece that is worth 1 point";
answers[7] = "Pawn";

//Nineth Question
questions[8]  = "How many pointa is the queen worth";
answers[8] = "9";

//Tenth Question
questions[9]  = "How many chess pieces make the first move";
answers[9] = "Barry Allen";

var currentQuestion;

//Value Question
function setQuestion(questionNumber) {
	currentQuestion = questionNumber;
	document.getElementById("question").innerHTML = questions[questionNumber];
	
	
}

//Determine right and wrong
function checkAnswer() {
	var tmpAnswer = document.getElementById("answer").value;
	if(tmpAnswer == answers[currentQuestion]) {
		document.getElementById("correct").innerHTML = 'Correct, you are good!!';
	} else { 
		document.getElementById("correct").innerHTML = 'Wrong!!!!!!!';
    }
}




