#!/usr/bin/node
const argv = process.argv;
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

const axios = require('axios');


axios.get(urlMovie)
  .then(response => {
    const characters = response.data.characters;

    if (characters && characters.length > 0) {
      const limit = characters.length;
      CharRequest(0, characters, limit);
    }
  })
  .catch(error => {
    console.error('Error fetching movie:', error);
  });

function CharRequest (idx, characters, limit) {
  if (idx === limit) {
    return;
  }

  axios.get(characters[idx])
    .then(response => {
      console.log(response.data.name);
      idx++;
      CharRequest(idx, characters, limit);
    })
    .catch(error => {
      console.error('Error fetching character:', error);
    });
}