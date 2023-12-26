$(document).ready(function() {
  // Create a new DataTable object
  table = $('#servers-list').DataTable({
        "lengthMenu": [ [15, 50, 100, -1], [15, 50, 100, "All"] ],
        "pagingType": "simple",
      //  scrollY: 400,
        scrollCollapse: true,
        order: [[ 0, 'asc' ], [3, 'desc' ]],
        ajax: {
          url: '/getHosts',
        },
        columns: [
            { data: 'id' },
            { data: 'hostname' },
            { data: 'ip' },
            { data: 'architecture' },
            { data: 'plataform' },
            { data: 'processor' },
            { data: 'so' },
            { data: 'distribution' },
            { data: 'mem_total' },
            { data: 'mem_free' },
            { data: 'up_time' },
            { data: 'mac_address' },
            { data: 'created_at' },
            { data: 'updated_at' },
            { data:'environnment' },
            {data: "hostname" , render : function ( data, type, row, meta ) {
                return type === 'display'  ?
                  '<a class="btn btn-primary buttonModal" id="'+ data +'" href="#" role="button" data-bs-toggle="modal" data-bs-target="#moreInfoModal" onclick="parseHostname()"><input type="text" style="display:none" id="hostName" placeholder="'+ data +'"/>Mais</a>' :
                  data;
            }},
            {data: "hostname" , render : function ( data, type, row, meta ) {
                  return type === 'display'  ?
                    '<a class="btn btn-primary" id="#" href="/server-edit.html" role="button"><input type="text" style="display:none" id="edit-hostName" placeholder="'+ data +'"/>'+ data +'</input>Edit</a>' :
                    data;
              }},
          ]
        })
});

// $(document).ready(function() {
function parseHostname() {
  // Create a new DataTable object
  var host = document.getElementById("hostName").placeholder;
  var url = '/getHostsUsername/'+host;
  table = $('#additionalInformation').DataTable({
    //  "lengthMenu": [ [15, 50, 100, -1], [15, 50, 100, "All"] ],
    //  "pagingType": "simple",
    //  scrollY: 400,
      scrollCollapse: false,
      paging: false,
      searching: false,
      destroy: true,
    //  order: [[ 0, 'asc' ], [3, 'desc' ]],
      ajax: {
      type: "GET",
        url: url,
      },
      columns: [
          { data: 'url' },
          { data: 'cluster' },
          { data: 'publication' },
          { data: 'midleware' },
          { data: 'framework' },
          { data: 'app_language' },
          { data: 'priority' },
          { data: 'risk' },
          { data: 'acronym' },
          { data: 'goal' },
          { data: 'datacenter' },
          { data: 'repository' },
          { data: 'national_cjf' }
        ]
      })
}


$(document).ready(function() {
  var hostEdit = document.getElementById("hostName");
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