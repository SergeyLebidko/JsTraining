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

        statDiv = document.getElementById('stat_div');
        if (statDiv == null) {
            manageDiv = document.getElementById('manage_div');
            statDiv = document.createElement('div');
            statDiv.id = 'stat_div';
            statDiv.className = 'basic_block';
            statDiv.innerHTML = statTableGenerator(stat);
            manageDiv.after(statDiv)
        } else {
            statDiv.innerHTML = statTableGenerator(stat);
        }
    }

    function statTableGenerator(statObj) {
        data = statObj.stat;
        description = statObj.description;

        let tableArr = ['<table>'];

        tableArr.push('<tr>');
        for(let key in data){
            tableArr.push('<th>' + description[key] + '</th>')
        }
        tableArr.push('</tr>');

        tableArr.push('<tr>');
        for(let key in data){
            tableArr.push('<td style="text-align: center">' + data[key] + '</td>')
        }
        tableArr.push('</tr>');

        tableArr.push('</table>');
        return tableArr.join('');
    }
}
