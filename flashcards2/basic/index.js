let myFlashcards1={
  question:document.getElementById("q1"),
  answer:document.getElementById("a1")
};
let myFlashcards2={
  question:document.getElementById("q2"),
  answer:document.getElementById("a2")
};
let myFlashcards3={
  question:document.getElementById("q3"),
  answer:document.getElementById("a3")
};

//put the flashcards objects to myFlashcards array
let myFlashcards=[myFlashcards1,myFlashcards2,myFlashcards3];

//set the initial display of all the q&a invisible
let myFlashcardsindex=0;
let i=myFlashcardsindex;
document.getElementById("a1").style.display="none";
document.getElementById("q2").style.display="none";
document.getElementById("a2").style.display="none";
document.getElementById("q3").style.display="none";
document.getElementById("a3").style.display="none";

//define the functions for the previous and next button to display one question at a time
function next(){
  myFlashcards[i].question.style.display="none";
  myFlashcards[i].answer.style.display="none";
  if(i>myFlashcards.length-2)
  {i=0;}
  else
  {i=i+1;}
  myFlashcards[i].question.style.display="inline";
}
function previous(){
  myFlashcards[i].question.style.display="none";
  myFlashcards[i].answer.style.display="none";
  if (i>0){
    i=i-1;
  }
  else if(i===0){
    i=myFlashcards.length-1;
  }
  myFlashcards[i].question.style.display="inline";
}


function showanswer(){
  myFlashcards[i].question.onclick=function(){
  myFlashcards[i].answer.style.display="inline";
  }
}



