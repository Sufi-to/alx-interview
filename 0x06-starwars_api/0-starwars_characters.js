#!/usr/bin/node
// Script for getting data from the star wars api

const request = require('request');
const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (!err && res.statusCode === 200) {
        resolve(JSON.parse(body).characters);
      } else {
        reject(err);
      }
    });
  });
}
function charPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (!err && res.statusCode === 200) {
        resolve(JSON.parse(body).name);
      } else {
        reject(err);
      }
    });
  });
}

async function printChar (url) {
  try {
    const data = await requestPromise(url);
    for (let i = 0; i < data.length; i++) {
      try {
        const act = await charPromise(data[i]);
        console.log(act);
      } catch (err) {
        console.log('something went wrong when getting character name');
      }
    }
  } catch (err) {
    console.log('Array of movie characers not returned');
  }
}

printChar(filmUrl);
