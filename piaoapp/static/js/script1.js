function xmlreq(){
	var xmlhttp;
  var input=document.getElementById('input');

	xmlhttp=new XMLHttpRequest();
	xmlhttp.open("GET","ok.php?id="+input.innerHTML,true);
	xmlhttp.send();

	xmlhttp.onreadystatechange=function()
  	{
  	   if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
    	   window.location.href="lingpiao.php"
        }
      
  	}

}
function click(){
  var button=document.getElementById('ling');
  button.onclick=xmlreq;
  button.touchend=xmlreq;
}
window.onload=click;