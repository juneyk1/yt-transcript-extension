const btn = document.getElementById("summarize");
btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Summarizing..."; 
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url; // extract url of current tab
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/summary?url=" + url, true); // request GET for summary for the url
        xhr.onload = function() {
            var text = xhr.responseText; // load the summary
            const p = document.getElementById("output");
            p.innerHTML = text; // display summary to extension
            btn.disabled = false;
            btn.innerHTML = "Summarize";
        }
        xhr.send();
    });
});