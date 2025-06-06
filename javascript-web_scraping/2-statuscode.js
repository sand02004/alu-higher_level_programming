#!/usr/bin/node

const request = require('request');

// Get the URL from the command-line argument
const url = process.argv[2];

// Make the GET request
request(url, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
