function SendAjaxData(data, note_id) {
	console.log(data)
    console.log(note_id)

	 if (window.XMLHttpRequest) {
        var xhttp=new XMLHttpRequest();
        } else {  // code for IE6, IE5
        var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
              var data = JSON.parse(this.responseText);
              console.log(data);

        }
        };
        var url = "{% url 'note:starUnstar' %}";
        xhttp.open("GET", url+"?data="+data, true);
        xhttp.send();
}