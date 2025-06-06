#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
if (!apiUrl) {
  console.log('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
    return;
  }

  try {
    const todos = JSON.parse(body);
    const completedTasksCount = {};

    todos.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId;
        if (!completedTasksCount[userId]) {
          completedTasksCount[userId] = 0;
        }
        completedTasksCount[userId]++;
      }
    });

    console.log(completedTasksCount);
  } catch (e) {
    console.error('Error parsing JSON:', e.message);
  }
});
