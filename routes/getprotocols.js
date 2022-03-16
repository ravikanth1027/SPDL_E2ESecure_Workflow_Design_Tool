var express = require('express');
var Principal = require('../classes/Principal');
var PObject = require('../classes/PObject');
var router = express.Router();
var glob = require("glob")
const fs = require('fs')
const lineReader = require('line-reader');

router.get('/', function(req, res, next) {
 	filename = req.query.proto
 	var data = []

	lineReader.eachLine('savedprotocols/'+ filename, function(line){
	    /*if(line == )*/
	    console.log(line)
	    data.push(line);
		}, function (err){
  			if (err) throw err;
 				res.json({"filecontent" : data})
		});
});
module.exports = router;



