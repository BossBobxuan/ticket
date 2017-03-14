function xmlreq(){
	var xmlhttp;
	xmlhttp=new XMLHttpRequest();
	xmlhttp.open("GET","/piaoapp/getnumber/",true);
	xmlhttp.send();
	xmlhttp.onreadystatechange=function()
  	{
  	if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    	document.getElementById("title").innerHTML=xmlhttp.responseText;
    }
  	}
}


function settime(){
	window.setInterval(xmlreq,3000);
}
window.onload=function(){
	xmlreq();
	settime();
	
};