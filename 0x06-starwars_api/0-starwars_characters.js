#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(filmUrl, (err, res, body) => {
  if (err) {
    console.error('Error fetching movie:', err);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  printCharactersInOrder(characters, 0);
});

function printCharactersInOrder (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (err, res, body) => {
    if (err) {
      console.error('Error fetching character:', err);
      return;
    }

    const characterData = JSON.parse(body);
    console.log(characterData.name);

    printCharactersInOrder(characters, index + 1);
  });
}
