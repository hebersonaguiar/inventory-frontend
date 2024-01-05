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

app.get("/getHostsUsername/:id", function (req, res) {

  const idd = req.params.id;
  const url = 'http://inventory:5000/hosts/'+idd;

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

app.get("/updateinfo", function (req, res) {

  const hostname = req.params.hostname;
  console.log("Update Hostname"+hostname)
  // const formurl = req.params.url;
  // const environnment = req.params.environnment;
  // const cluster = req.params.cluster;
  // const publicacao = req.params.publicacao;
  // const middleware = req.params.middleware;
  // const framework = req.params.framework;
  // const linguagem = req.params.linguagem;
  // const prioridade = req.params.prioridade;
  // const risco = req.params.risco;
  // const sigla = req.params.sigla;
  // const datacenter = req.params.datacenter;
  // const repositorio = req.params.repositorio;
  // const objetivo = req.params.objetivo;
  // const nacionalcjf = req.params.nacionalcjf;
  
  const url = 'http://inventory:5000/hosts/'+hostname;

  // Make a request
  axios.put(url, {
    formurl: req.params.url,
    environnment: req.params.environnment,
    cluster: req.params.cluster,
    publicacao: req.params.publicacao,
    middleware: req.params.middleware,
    framework: req.params.framework,
    linguagem: req.params.linguagem,
    prioridade: req.params.prioridade,
    risco: req.params.risco,
    sigla: req.params.sigla,
    datacenter: req.params.datacenter,
    repositorio: req.params.repositorio,
    objetivo: req.params.objetivo,
    nacionalcjf: req.params.nacionalcjf,
  })
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