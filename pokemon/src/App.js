import React, { useEffect, useState } from 'react';

function App() {
  const [ pokeJSON, updatePokeJSON ] = useState({})
  useEffect(() => {
    fetch('https://pokeapi.co/api/v2/pokemon/ditto')
      .then(response => response.json())
      .then(json => updatePokeJSON(json))
  }, [])

  return (
    <div className="App">
      <ul>
      {console.log(pokeJSON)}
      {pokeJSON.game_indices ? pokeJSON.game_indices.map((gameIndex, i) => 
          (<li otherthing="hi" key={i}><a href="{gameIndex.version.url}">{gameIndex.version.name}</a></li>)) : ''}
      </ul>
    </div>
  );
}

export default App;
