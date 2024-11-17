#!/usr/bin/node
/*
 * The “0. Star Wars Characters” project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming,
 * API interaction, and asynchronous programming in JavaScript.
 * 
 */


const request = require('request');

const body = request("https://swapi-api.alx-tools.com/api/films/3", { json: true}, (error, response, body) => {
	for (const character of body.characters){
		name = request(character, {json : true}, (error, response, body) =>
			{
				console.log(body.name);
			}
		);
	}
}
);


