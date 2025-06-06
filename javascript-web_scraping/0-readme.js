#!/usr/bin/node

const fs = require('fs'); // Import the file system module

const filePath = process.argv[2]; // Get file path from command-line arguments

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err); // Print the error object if reading fails
  } else {
    console.log(data); // Print file content
  }
});
