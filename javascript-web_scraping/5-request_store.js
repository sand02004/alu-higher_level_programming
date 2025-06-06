#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

if (!url || !filepath) {
  console.log('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Request error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch URL. Status code: ${response.statusCode}`);
    return;
  }

  fs.writeFile(filepath, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing file:', err);
      return;
    }
    // File saved successfully, no output needed per instructions
  });
});
