#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (error) throw error;
  const movieActors = JSON.parse(body).characters;
  exactOrder(movieActors, 0);
});

const exactOrder = (movieActors, x) => {
  if (x === movieActors.length) return;
  request(movieActors[x], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    exactOrder(movieActors, x + 1);
  });
};
