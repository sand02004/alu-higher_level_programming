#!/usr/bin/node

const fs = require('fs');

// Get the file path and the string to write from command-line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file using UTF-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.log(err); // Print error object if writing fails
  }
});
