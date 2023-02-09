#!/usr/bin/node
const request = require('request');
request.get('https://swapi-api.alx-tools.com/api/films/:id' + process.argv[2] + '/', (err, response, body) => {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
