Objeto = {

    __init__: function (id, modelo, ventana_id) {
        Objeto.id = id;
        Objeto.modelo = modelo;
        Objeto.ventana_id = ventana_id;
        Objeto.url_base = "/" + modelo + "/" + id;
        return this
    },

    eliminar: function () {
        $("#" + Objeto.ventana_id).find("a").attr('href', Objeto.url_base + "/eliminar");
    },

}

$(document).on('ready', function() {


});