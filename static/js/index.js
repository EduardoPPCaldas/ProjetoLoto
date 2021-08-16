const buttons = document.getElementsByClassName("button-game")
const resultsDiv = document.getElementsByClassName("game-results-div")

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

    while(games.size !== 12){

      while(game.size !== 15){
        game.add(numbers[Math.floor(Math.random() * numbers.length)])
      }
      const auxSet = new Set(game) 
      games.add(auxSet)
      game.clear()
    }

    for(let i=0; i<resultsDiv.length; i++){
      resultsDiv.item(i).classList.remove("invisible")
      resultsDiv.item(i).classList.add("visible")
    }
    let counter = 0    
    games.forEach((value)=>{ 
      value.forEach((number)=>{
        let p = document.createElement("p")
        p.classList.add("game-results-numbers")
        p.textContent = `${number}`
        resultsDiv.item(counter).appendChild(p)
      })
      counter++
    })
  }
}