let sendBtn = document.getElementById('send_btn');
sendBtn.onclick = send_order;

let clientSelector = document.getElementById('client_selector');
let productSelector = document.getElementById('product_selector');
let countField = document.getElementById('count_field');

function send_order(el) {
    let clientOption = clientSelector.options[clientSelector.selectedIndex];
    let productOption = productSelector.options[productSelector.selectedIndex];
    let token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    let countText = countField.value;
    let count = +countText;

    if(isNaN(count)){
        alert('Некорректное количество товара')
    }

    let data = {
        'csrfmiddlewaretoken': token,
        'client_id': clientOption.value,
        'product_id': productOption.value,
        'count': count
    };

    $.post('', data, sendResult)
};

function sendResult(data, status) {
    alert(data)
}
