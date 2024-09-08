#!/usr/bin/node
// Script for getting data from the star wars api

const request = require('request');
const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

function getFilm (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (err, res, body) {
      if (!err && res.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(err);
      }
    });
  });
}

async function getActors (filmUrl) {
  try {
    const filmData = await getFilm(filmUrl);
    for (const charUrl of filmData.characters) {
      try {
        const charData = await getFilm(charUrl);
        console.log(charData.name);
      } catch (error) {
        console.error(`Error fetching character data: ${error}`);
      }
    }
  } catch (err) {
    console.error(`Error fetching movie data: ${err}`);
  }
}

getActors(filmUrl);
