fetch('https://pokeapi.co/api/v2/pokemon/pikachu')
  .then((response) => response.json())
  .then((responseJson) => {
    console.log(responseJson);
  });
