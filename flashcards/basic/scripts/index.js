//create flashcards objects which contain questions and answers
const myFlashcards1 = {
  question: 'What is the color of sky?',
  answer: 'blue'
};
const myFlashcards2 = {
  question: 'how many hours are there in one day?',
  answer: '24'
};
const myFlashcards3 = {
  question: 'Who should you call when there is an emergency?',
  answer: '911'
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

//define the functions for the previous and next button to display one question at a time, and when it comes to the last one, clicking 'next' shows the first question
function next(){
  if(i>myFlashcards.length-2)
  {i=0;}
  else
  {i=i+1;}
  questionmart.innerHTML=myFlashcards[i].question;
  answermart.innerHTML='';
}
function previous(){
  if (i>0){
    i=i-1;
  }
  else if(i===0){
    i=myFlashcards.length-1;
  }
  questionmart.innerHTML=myFlashcards[i].question;
  answermart.innerHTML='';
}


