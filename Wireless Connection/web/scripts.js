let keyWpress = 0, keyApress = 0, keySpress = 0, keyDpress = 0;

// 监听键盘按下事件
document.addEventListener('keydown', function(event) {
    switch (event.key) {
        case 'w':
        case 'W':
            keyWpress = 1;
            break;
        case 'a':
        case 'A':
            keyApress = 1;
            break;
        case 's':
        case 'S':
            keySpress = 1;
            break;
        case 'd':
        case 'D':
            keyDpress = 1;
            break;
    }
});

// 监听键盘松开事件
document.addEventListener('keyup', function(event) {
    switch (event.key) {
        case 'w':
        case 'W':
            keyWpress = 0;
            break;
        case 'a':
        case 'A':
            keyApress = 0;
            break;
        case 's':
        case 'S':
            keySpress = 0;
            break;
        case 'd':
        case 'D':
            keyDpress = 0;
            break;
    }
});
