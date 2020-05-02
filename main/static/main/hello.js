function start() {
    let clientBtn = document.getElementById('client_btn');
    let productBtn = document.getElementById('product_btn');
    let orderBtn = document.getElementById('order_btn');
    let statBtn = document.getElementById('stat_btn');

    let clientDiv = document.getElementById('client_div');
    let productDiv = document.getElementById('product_div');
    let orderDiv = document.getElementById('order_div');

    clientBtn.onclick = function (el) {
        clientDiv.style.display = 'block';
        productDiv.style.display = 'none';
        orderDiv.style.display = 'none';
    };

    productBtn.onclick = function (el) {
        clientDiv.style.display = 'none';
        productDiv.style.display = 'block';
        orderDiv.style.display = 'none';
    };

    orderBtn.onclick = function (el) {
        clientDiv.style.display = 'none';
        productDiv.style.display = 'none';
        orderDiv.style.display = 'block';
    };

    statBtn.onclick = function (el) {
        $.get('/main/stat/', {}, refresh_stat)
    };

    function refresh_stat(data, status) {
        let stat = eval(data);
        manageDiv = document.getElementById('manage_div');

        statDiv = document.createElement('div');
        statDiv.className = 'basic_block';
        statDiv.innerHTML = '<h1>Получилось!</h1>';

        manageDiv.after(document.createElement('br'), statDiv)
    }
}
