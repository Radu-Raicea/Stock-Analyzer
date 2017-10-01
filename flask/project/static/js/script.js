
$(document).ready( function () {
    $('#stocks_table').DataTable();
} );

function add_stock() {
    var market = document.getElementById("addStockForm").elements[0].value;
    var ticker = document.getElementById("addStockForm").elements[1].value;
    var form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', '/add/' + market + '/' + ticker);
    form.style.display = 'hidden';
    document.body.appendChild(form)
    form.submit();
}

function remove_stock(market, ticker) {
    var form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute('action', '/remove/' + market + '/' + ticker);
    form.style.display = 'hidden';
    document.body.appendChild(form)
    form.submit();
}
