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
                  '<a class="btn btn-primary buttonModal" id="'+ data +'" href="#" role="button" data-bs-toggle="modal" data-bs-target="#moreInfoModal" onclick="parseHostname()"><input type="text" style="display:none" id="hostName" placeholder="'+ data +'" value="'+ data +'"/>Mais</a>' :
                  data;
            }},
            {data: "hostname" , render : function ( data, type, row, meta ) {
                  return type === 'display'  ?
                    '<a class="btn btn-primary" id="#" href="/server-edit.html" role="button" onclick="getValueHost()"><input type="text" style="display:none" id="edithostName" placeholder="'+ data +'"  value="'+ data +'"/>Edit</a>' :
                    data;
              }},
          ]
        })
});

function getValueHost(){
  var host = document.getElementById("hostName").placeholder;
  // console.log("Host to edit: " + host);
  localStorage.setItem('hosttoedit', host);
}


function parseHostname() {
  // Create a new DataTable object
  var host = document.getElementById("hostName").placeholder;
  // var teste = document.querySelector("#hostName").value;
  // localStorage.setItem('greeting', host);
  // localStorage.setItem('hostnamevalue', host);
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