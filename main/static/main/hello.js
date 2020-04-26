function start() {
    let clientBtn = document.getElementById('client_btn');
    let productBtn = document.getElementById('product_btn');
    let orderBtn = document.getElementById('order_btn');

    clientBtn.onclick = function (el) {
        change_display('client_div')
    };

    productBtn.onclick = function (el) {
        change_display('product_div')
    };

    orderBtn.onclick = function (el) {
        change_display('order_div')
    };

    function change_display(id) {
        let display = document.getElementById(id).style.display;
        if (display == 'none') {
             document.getElementById(id).style.display = 'block';
        } else {
            document.getElementById(id).style.display = 'none';
        }
    }
}
