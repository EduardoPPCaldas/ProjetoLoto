const buttons = document.getElementsByClassName("button-game")


function handleGameButton(event, index){
  event.preventDefault()
  index--
  document.getElementsByClassName("button-game").item(index).classList.toggle("button-game-clicked")
}

function handleGameSubmitButton(event){
  event.preventDefault()

  let totalOfButtonsPressed = 0
  let numbers = []
  const game = new Set()
  const games = new Set()

  for(let button of buttons){
    if(button.classList.contains("button-game-clicked")){
      totalOfButtonsPressed++
    }
  }

  if(totalOfButtonsPressed > 20){
    alert("Selecione exatamente 20 números para criar os jogos!")
  }
  else if(totalOfButtonsPressed < 20){
    alert("Selecione exatamente 20 números para criar os jogos!")
  }
  else{
    for(let i=0; i<buttons.length; i++){      
      if(document.getElementsByClassName("button-game").item(i).classList.contains("button-game-clicked")){
        numbers.push(i+1)
      }
    }

    while(game.size !== 15){
      game.add(Math.floor(Math.random() * numbers.length))
    }
    games.add(game)
    console.log(games)
  }
}