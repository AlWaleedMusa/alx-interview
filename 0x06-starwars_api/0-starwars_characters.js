#!/usr/bin/node

const request = require('request');

if (process.argv.length > 2) {
  request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`, (error, _, body) => {
    if (error) {
      console.log(error);
    }
    const characters = JSON.parse(body).characters;
    const Name = characters.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseError, __, charactersReqBody) => {
          if (promiseError) {
            reject(promiseError);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(Name)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.log(err));
  });
}
