buttons = document.getElementsByClassName("button-game")


function handleGameButton(event, index){
  event.preventDefault()
  index--
  document.getElementsByClassName("button-game").item(index).classList.toggle("button-game-clicked")
}