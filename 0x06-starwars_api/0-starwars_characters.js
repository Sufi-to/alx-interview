#!/usr/bin/node
const axios = require('axios');
const argv = process.argv;
const movieId = argv[2];
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${movieId}/`;

axios.get(urlMovie)
  .then(response => {
    const characters = response.data.characters;
    if (characters && characters.length > 0) {
      fetchCharacters(characters);
    }
  })
  .catch(error => {
    console.error('Error fetching movie:', error.message);
  });

async function fetchCharacters(characters) {
  for (const characterUrl of characters) {
    try {
      const response = await axios.get(characterUrl);
      console.log(response.data.name);
    } catch (error) {
      console.error('Error fetching character:', error.message);
    }
  }
}