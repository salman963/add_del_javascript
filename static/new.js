window.onload=initAll;

var idBtn;

function initAll(){
        
        idBtn=document.getElementById('AddBook');
        idBtn.onclick=operation;
    
}
function operation(){
    
    var name=document.getElementById('name').value;
    var pages=document.getElementById('pages').value;
    var prize=document.getElementById('prize').value;
    var url='/BookAdd?name='+name+'&pages='+pages+'&prize='+prize;
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        alert(req.responseText);
     
    }
  };
  req.open("GET", url, true);
  req.send();
}