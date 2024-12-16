#!/usr/bin/node

// Importing the 'request' module for making HTTP requests
const request = require('request');

// Importing 'util' module for utility functions
const util = require('util');

// Getting the film ID from the command line arguments
const filmId = process.argv[2];

// Constructing the URL for the Star Wars API request based on the film ID
const URL = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

// Promisifying the 'request' function using 'util.promisify' for async/await support
const prequest = util.promisify(request);

// Defining an asynchronous IIFE (Immediately Invoked Function Expression)
(async () => {
  try {
    // Fetching the film data from the API and extracting the response body
    const film = (await prequest(URL, { json: true })).body;

    // Looping through each character URL in the film data
    for (const url of film.characters) {
      // Fetching each character's data from their URL and extracting the response body
      const character = (await prequest(url, { json: true })).body;
      // Printing the name of the character
      console.log(character.name);
    }
  } catch (error) {
    // Handling and printing any errors that occur during the API requests
    console.log(error);
  }
})();