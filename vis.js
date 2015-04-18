
//Callback functions
    var error = function (err, response, body) {
        console.log('ERROR [%s]', err);
    };
    var success = function (data) {
        console.log('Data [%s]', data);
    };

    var Twitter = require('twitter-js-client').Twitter;

    //Get this data from your twitter apps dashboard
    var config = {
        "consumerKey": "GdUgSU9KafMv4rDw4jTPK2Zcw",
        "consumerSecret": "lYY7ERRc8GlCBmvraSfuih2GJ15dNQB43UrXazYF3bg4QTMTdi",
        "accessToken": "2244644996-yesu4bH05QsU7l6KxH9xsy9zcQfc7R7Ieosp6zF",
        "accessTokenSecret": "xKUkGUUKMzK4e9I5GTzGiUuEXaFkEve2G7ITZNYIStkr8"
        // "callBackUrl": "https://nodejs.org/"
    }

    var twitter = new Twitter(config);

    //Example calls

var users = ["jordan", "sravanti", "jesslyn", "alice", "jenny"];

  // create sample dataset
  // for loop 
  var sample_data = [
    {"name": "jordan", "size": 10, "image": "jenny.jpg"},
    {"name": "sravanti", "size": 40, "image": "sra.jpg"},
    {"name": "jesslyn", "size": 30, "image": "jenny.jpg"},
    {"name": "alice", "size": 26, "image": "sra.jpg"},
    {"name": "jenny", "size": 12, "image": "jenny.jpg"}
  ]

  // create list of node positions
  var positions = [
    {"name": "jordan", "x": 5, "y": 15},
    {"name": "sravanti", "x": 10, "y": 15},
    {"name": "jesslyn", "x": 15, "y": 15},
    {"name": "alice", "x": 20, "y": 15},
    {"name": "jenny", "x": 25, "y": 15}
  ]

  var colors = ["#528b8b",
                "#388e8e",
                "#8fd8d8",
                "#70dbdb",
                "#000"]

  console.log(colors);

  // create list of node connections
  var connections = [
    {"source": "jordan", "target": "sravanti"},
    {"source": "sravanti", "target": "jesslyn"},
    {"source": "jesslyn", "target": "alice"},
    {"source": "alice", "target": "jenny"}
  ]
  // var newColor = d3plus.color.random();
  // console.log("new color " + newColor)

  // instantiate d3plus
  var visualization = d3plus.viz()
    .container("#viz")  // container DIV to hold the visualization
    .type("network")    // visualization type
    .data(sample_data)  // sample dataset to attach to nodes
    .icon({
      "style": "default",
      "value": "image"
    })
    .nodes(positions)   // x and y position of nodes
    .edges(connections) // list of node connections
    .edges({
      "color": "#000"
    })
    .size("size")       // key to size the nodes
    .id("name")         // key for which our data is unique on
    .color({
      "scale": "category20b"
    })
    .draw()             // finally, draw the visualization!

