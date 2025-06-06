#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
if (!apiUrl) {
  console.log('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request('https://swapi-api.alx-tools.com/api/people/18/', (error, response, body) => {
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
    console.log(data.films.length);
  } catch (e) {
    console.error('Error parsing JSON:', e.message);
  }
});
