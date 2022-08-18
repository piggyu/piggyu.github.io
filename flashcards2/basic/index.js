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
let myFlashcards=[myFlashcards1,myFlashcards2,myFlashcards3];

let myFlashcardsindex=0;
let i=myFlashcardsindex;
document.getElementById("a1").style.display="none";
document.getElementById("q2").style.display="none";
document.getElementById("a2").style.display="none";
document.getElementById("q3").style.display="none";
document.getElementById("a3").style.display="none";

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



