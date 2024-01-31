const axios = require("axios");
const express = require('express');

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static("public"));
app.use(express.urlencoded({extended: false}));

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

  const hostname = req.body.hostname;
  console.log("Update Hostname"+hostname)
  // const url = req.body.url;
  // const environnment = req.body.environnment;
  // const cluster = req.body.cluster;
  // const publicacao = req.body.publicacao;
  // const middleware = req.body.middleware;
  // const framework = req.body.framework;
  // const linguagem = req.body.linguagem;
  // const prioridade = req.body.prioridade;
  // const risco = req.body.risco;
  // const sigla = req.body.sigla;
  // const datacenter = req.body.datacenter;
  // const repositorio = req.body.repositorio;
  // const objetivo = req.body.objetivo;
  // const nacionalcjf = req.body.nacionalcjf;
  
  // const url = 'http://10.0.0.171:5000/hosts/'+hostname;
  const url = 'http://10.0.0.171:5000/hosts/vm-one';

  // Make a request
  axios.put(url, {
    url: req.body.url,
    environnment: req.body.environnment,
    cluster: req.body.cluster,
    publicacao: req.body.publicacao,
    middleware: req.body.middleware,
    framework: req.body.framework,
    linguagem: req.body.linguagem,
    prioridade: req.body.prioridade,
    risco: req.body.risco,
    sigla: req.body.sigla,
    datacenter: req.body.datacenter,
    repositorio: req.body.repositorio,
    objetivo: req.body.objetivo,
    nacionalcjf: req.body.nacionalcjf,
  })
    .then(response => {
      // send the collected data back to the client-side DataTable
      // res.json({
      //   "data": response.data
      // })
      res.redirect('/servers.html');
    })
    .catch(function (error) {
       // handle error
       console.log(error);
       res.json({"error": error});
    })
});