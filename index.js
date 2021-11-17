let cookies = document.cookie;
cookies = cookies.split(";");
cookies = cookies.map(cookie => cookie.replace(" ", ""));
let text = "{";
for (i=0;i<cookies.length;i++) {x=cookies[i].split("="); text+="\""+x[0]+"\""+": "+x[1]+",\n";}
text += "}"
