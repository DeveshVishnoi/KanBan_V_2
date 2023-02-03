// var card = document.querySelectorAll('.card');
// var list = document.querySelectorAll('.box')
// console.log(list);
// console.log(card);

// var dragItem = null;

// for(var i of card){
//     i.addEventListener('dragstart', dragStart);
//     i.addEventListener('dragend', dragEnd);
// }

// function dragStart(){
//     dragItem = this;
//     setTimeout(() => this.style.display = "none",0)
// }
// function dragEnd(){
//     setTimeout(() => this.style.display = "block",0);
//     dragItem = null;
// }

// for(var j of list){
//     j.addEventListener("dragover", dragOver);
//     j.addEventListener("dragenter", dragEnter);
//     j.addEventListener("dragleave", dragLeave);
//     j.addEventListener("drop", Drop);
// }
// function Drop(e){
//     e.target.append(dragItem)
// }

// function dragOver(e){
//     e.preventDefault( );
//     this.style.border = "1px dotted cyan";
    
// }
// function dragEnter(e){
//     e.preventDefault()
// }
// function dragLeave(){
//     this.style.border = "1px dotted cyan"
// }