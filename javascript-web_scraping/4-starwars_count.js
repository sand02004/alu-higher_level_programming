#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
if (!apiUrl) {
  console.log('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.log('Failed to fetch data');
    return;
  }

  try {
    const data = JSON.parse(body);
    const films = data.results;

    const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

    const count = films.reduce((acc, film) => {
      return film.characters.includes(wedgeUrl) ? acc + 1 : acc;
    }, 0);

    console.log(count);

  } catch (e) {
    console.error('Error parsing JSON:', e.message);
  }
});
