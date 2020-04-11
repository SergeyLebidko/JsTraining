var txt = 'Глобальная переменная';

document.write('<br>' + txt + '<br>');
show();
document.write(txt + '<br>');

function show() {
    txt = 'Локальная переменная';
    document.write(txt + '<br>');
}