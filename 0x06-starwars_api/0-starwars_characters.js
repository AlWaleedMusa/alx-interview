#!/usr/bin/node

const request = require('request');

const makeRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) return reject(err);
      resolve(JSON.parse(body));
    });
  });
};

const printActorsInOrder = async (actors, index = 0) => {
  if (index >= actors.length) return;

  try {
    const actor = await makeRequest(actors[index]);
    console.log(actor.name);
    await printActorsInOrder(actors, index + 1);
  } catch (err) {
    console.error('Error fetching actor:', err);
  }
};

const fetchMovieCharacters = async () => {
  const movieId = process.argv[2];
  if (!movieId) {
    console.error('Please provide a movie ID as the first argument.');
    return;
  }

  try {
    const film = await makeRequest('https://swapi-api.hbtn.io/api/films/' + movieId);
    const actors = film.characters;
    await printActorsInOrder(actors);
  } catch (err) {
    console.error('Error fetching movie data:', err);
  }
};

fetchMovieCharacters();
