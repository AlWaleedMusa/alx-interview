#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) throw error;
  const movie_actors = JSON.parse(body).characters;
  exactOrder(movie_actors, 0);
});

const exactOrder = (movie_actors, x) => {
  if (x === movie_actors.length) return;
  request(movie_actors[x], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    exactOrder(movie_actors, x + 1);
  });
};
