$(document).ready(function() {

    const hostToEdit = localStorage.getItem('hosttoedit');
    // console.log("Edit page: " + hostToEdit);

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
    const elEnvironment = document.getElementById('in-environnment');
    // const elDatacenter = document.getElementById('in-datacenter');
    // const elNacionalcjf = document.getElementById('in-nacional-cjf');
    // const elGoal = document.getElementById('in-goal');

    const url = 'http://10.0.0.171:5000/hosts/'+hostToEdit;

    fetch(url)
    .then((response) => {
    return response.json();
    })
    .then((data) => {
    let hosts = data;

    hosts.map(function(host) {
        elHostname.setAttribute('value', `${host.hostname}`);
        elUrl.setAttribute('value', `${host.url}`);
        elCluster.setAttribute('value', `${host.cluster}`);
        elPublicacao.setAttribute('value', `${host.publication}`);
        elMiddleware.setAttribute('value', `${host.midleware}`);
        elFramework.setAttribute('value', `${host.framework}`);
        elLinguagem.setAttribute('value', `${host.app_language}`);
        elPrioridade.setAttribute('value', `${host.priority}`);
        elRisco.setAttribute('value', `${host.risk}`);
        elSigla.setAttribute('value', `${host.acronym}`);
        elRepositorio.setAttribute('value', `${host.repository}`);
        elEnvironment.setAttribute('value', `${host.environnment}`);
        // elDatacenter.setAttribute('selected', `${host.datacenter}`);
        // elNacionalcjf.setAttribute('selected', `${host.national_cjf}`);
        // elGoal.setAttribute('data-content', `${host.goal}`);
        document.getElementById("in-goal").innerHTML = `${host.goal}`;
        document.getElementById("in-"+`${host.national_cjf}`).selected = 'selected';
        document.getElementById("in-"+`${host.datacenter}`).selected = 'selected';
    });
    })
    .catch(function(error) {
    console.log(error);
    });
});


// $(document).ready(function() {
//     document.getElementById("submitFormUpdate").addEventListener("click", myFunction);  
//       function myFunction() {  
//         window.location.href="/servers.html";  
//       }
// });

