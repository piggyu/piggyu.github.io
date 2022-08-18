//create flashcards objects which contain questions and answers
const myFlashcards1 = {
  question: 'What is the color of sky?',
  answer: 'blue',
  pic:document.getElementById("pic1")
};
const myFlashcards2 = {
  question: 'how many hours are there in one day?',
  answer: '24',
  pic:document.getElementById("pic2")
};
const myFlashcards3 = {
  question: 'Who should you call when there is an emergency?',
  answer: '911',
  pic:document.getElementById("pic3")
};

//put the flashcards objects to myFlashcards array
let myFlashcards=[myFlashcards1,myFlashcards2,myFlashcards3];
let questionmart=document.getElementById("questionmart");
let answermart=document.getElementById("answermart");

//add a listener that shows the answer with one click
let myFlashcardsindex=0;
let i=myFlashcardsindex;
function showanswer(){
  document.getElementById('questionmart').onclick=function(){
    answermart.innerHTML=myFlashcards[i].answer;
  }
}

//set the initial image invisible
myFlashcards[0].pic.style.display="none";
myFlashcards[1].pic.style.display="none";
myFlashcards[2].pic.style.display="none";

//add a listener that shows the message and image when hovering over the question
function showmsg(){
  questionmart.onmouseover=function(){
  console.log("click on the question first");
  myFlashcards[i].pic.style.display="inline";
  }
}

//define the functions for the previous and next button to display one question at a time
function next(){
  myFlashcards[i].pic.style.display="none";
  if(i>myFlashcards.length-2)
  {i=0;}
  else
  {i=i+1;}
  questionmart.innerHTML=myFlashcards[i].question;
  answermart.innerHTML='';
}
function previous(){
  myFlashcards[i].pic.style.display="none";
  if (i>0){
    i=i-1;
  }
  else if(i===0){
    i=myFlashcards.length-1;
  }
  questionmart.innerHTML=myFlashcards[i].question;
  answermart.innerHTML='';
}
