$(document).ready(function() {
    // function editValue() {
    //   var hostEdit = document.getElementById("edithostName").placeholder;
      const hostEdit = localStorage.getItem('hostnamevalue');
    //   var hostEdit = sessionStorage.getItem("hostnamevalue");
      console.log(hostEdit);
    
      const elHostname = document.getElementById('in-hostname');
      const elUrl = document.getElementById('in-url');
      const elCluster = document.getElementById('in-cluster');
      const elPublicacao = document.getElementById('in-publicacao');
      const elMiddleware = document.getElementById('in-middleware');
      const elFramework = document.getElementById('in-framework');
      const elLinguagem = document.getElementById('in-linguagem');
      const elPrioridade = document.getElementById('in-prioridade');
      const elRisco = document.getElementById('in-risco');
      const elSigla = document.getElementById('in-sigla');
      const elRepositorio = document.getElementById('in-repositorio');
    
      const url = 'http://10.0.0.171:5000/hosts';
    
      fetch(url)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        let hosts = data;
    
        hosts.map(function(host) {
          elHostname.setAttribute('placeholder', `${host.hostname}`);
          elUrl.setAttribute('placeholder', `${host.url}`);
          elCluster.setAttribute('placeholder', `${host.cluster}`);
          elPublicacao.setAttribute('placeholder', `${host.publication}`);
          elMiddleware.setAttribute('placeholder', `${host.midleware}`);
          elFramework.setAttribute('placeholder', `${host.framework}`);
          elLinguagem.setAttribute('placeholder', `${host.app_language}`);
          elPrioridade.setAttribute('placeholder', `${host.priority}`);
          elRisco.setAttribute('placeholder', `${host.risk}`);
          elSigla.setAttribute('placeholder', `${host.acronym}`);
          elRepositorio.setAttribute('placeholder', `${host.repository}`);
        });
      })
      .catch(function(error) {
        console.log(error);
      });
    });