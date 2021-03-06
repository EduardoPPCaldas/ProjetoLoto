const buttons = document.getElementsByClassName("button-game")
const resultsDiv = document.getElementsByClassName("game-results-div")
let numberOfClicks = 0

function clicks(click){
  document.getElementById("clicks").innerHTML = `Números selecionados: ${click}/20`
}
clicks(numberOfClicks)


function handleGameButton(event, index){
  event.preventDefault()
  index--
  if(buttons.item(index).classList.contains("button-game-clicked")){
    buttons.item(index).classList.remove("button-game-clicked")
    numberOfClicks--
    clicks(numberOfClicks)
  }
  else{
    buttons.item(index).classList.add("button-game-clicked")
    numberOfClicks++
    clicks(numberOfClicks)
  }
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

    const resultTitle = document.getElementsByClassName("results-title").item(0)
    resultTitle.classList.remove("invisible")
    resultTitle.classList.add("visible")

    for(let i=0; i<resultsDiv.length; i++){
      resultsDiv.item(i).classList.remove("invisible")
      resultsDiv.item(i).classList.add("visible")
    }
    let gamesInArray = []
    let gameArray = []
    games.forEach((value)=>{ 
      value.forEach((number)=>{
        gameArray.push(number)
      })
      gameArray = gameArray.sort(function(a, b){
        return a - b
      })
      gamesInArray.push(gameArray)
      gameArray=[]
    })
    
    let divLines = -1
    for(let i=0; i<12; i++){
      for(let j=0; j<15; j++){
        if(j%5===0){
          divLines++
          let divNumbers = document.createElement("div")
          divNumbers.classList.add("game-lines")
          resultsDiv.item(i).appendChild(divNumbers)
        }

        let p = document.createElement("p")
        p.classList.add("game-results-numbers")
        p.textContent = gamesInArray[i][j] >= 10 ? `${gamesInArray[i][j]}` : `0${gamesInArray[i][j]}`
        document.getElementsByClassName("game-lines").item(divLines).appendChild(p)
      }
    }
    document.getElementById("create-game-results-button").disabled = true
  }
}

function handleRestartButton(event){
  event.preventDefault()

  document.location.reload(true);
}

function createSuggestions(){
  const suggestions = new Set()
  let suggestionsSorted = []

  while(suggestions.size !== 10){
    suggestions.add(Math.floor(Math.random() * 25) + 1)
  }

  suggestions.forEach(
    (value)=>{
      suggestionsSorted.push(value)
    }
  )

  suggestionsSorted.sort((a , b) => {
    return a - b
  })

  let counter = -1

  for(let i=0; i<10 ; i++){
    if(i%5===0){
      counter++
      let div = document.createElement("div")
      div.classList.add("suggestion-lines")
      document.getElementById("suggestions-body").appendChild(div)
    }
    let p = document.createElement("p")
    p.textContent = suggestionsSorted[i] >= 10 ? `${suggestionsSorted[i]}` : `0${suggestionsSorted[i]}`
    p.classList.add("game-results-numbers")
    p.classList.add("game-suggestions-numbers")
    document.getElementsByClassName("suggestion-lines").item(counter).appendChild(p)
  }
}
createSuggestions()