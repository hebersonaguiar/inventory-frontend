const axios = require("axios");
const express = require('express');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static("public"));

app.listen(port, () => {
    console.log(`Starting server at: ${port}`);
});

// Define a route handler for HTTP GET requests
app.get("/getHosts", function (req, res) {

  const url = 'http://inventory:5000/hosts';

  // Make a request
  axios.get(url)
    .then(response => {
      // send the collected data back to the client-side DataTable
      res.json({
        "data": response.data
      })
    })
    .catch(function (error) {
       // handle error
       console.log(error);
       res.json({"error": error});
    })
});

app.get("/getHostsUsername?", function (req, res) {

  // const id = req.params.id;
  console.log("In API, value is: "+req.params);

  const url = 'http://inventory:5000/hosts/'+id.str;

  // Make a request
  axios.get(url)
    .then(response => {
      // send the collected data back to the client-side DataTable
      res.json({
        "data": response.data
      })
    })
    .catch(function (error) {
       // handle error
       console.log(error);
       res.json({"error": error});
    })
});