//console.log('debug: marketing.js loaded 1.0.2');

/**
 * Post url hash changes.
 */
function hashChangeHandler() {
    var hash = window.location.hash;
    var href = window.location.href;
    var message = {
        'from': 'child',
        'hash': hash,
        'href': href
    };
    //console.log('debug: 1. Iframe Window: hashChange message=', message);
    window.postMessage(message, "*");
}
window.addEventListener('hashchange', hashChangeHandler, false);

/**
 * Listen for parent posting messages.
 * 
 * @param {*} event 
 */
function receiveMessage(event) {
    var message = event.data;
    if (message && message.hasOwnProperty('from') && message.from === 'parent') {
        //console.log("debug: Child: reiceved message message=", message);
    }
}
window.addEventListener("message", receiveMessage, false);

/**
 * Workaround for ios ExtJS app in iframe.
 */
window.onload = function() {
    /**
     * This allows the ExtJS full apps to work in the iframe. 
     * @param {*} e 
     */
    function process_touchstart(e) {
        //console.log("debug: touchstart", e);
    }
    window.document.body.addEventListener('touchstart', process_touchstart, false);
}