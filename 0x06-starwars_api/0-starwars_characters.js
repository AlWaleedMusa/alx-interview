#!/usr/bin/node

const https = require('https');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

function httpsGet(url) {
    return new Promise((resolve, reject) => {
        https.get(url, (res) => {
            let data = '';
            
            res.on('data', chunk => {
                data += chunk;
            });

            res.on('end', () => {
                resolve(JSON.parse(data));
            });
        }).on('error', (err) => {
            reject(err);
        });
    });
}

async function getCharacters(movieId) {
    try {
        const film = await httpsGet(apiUrl);

        for (const characterUrl of film.characters) {
            const character = await httpsGet(characterUrl);
            
            console.log(character.name);
        }
    } catch (error) {
        console.error(`Error fetching data: ${error}`);
    }
}

getCharacters(movieId);
