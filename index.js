// cookie = 貼上
let text = "{";
for (i=0;i<cookie.length;i++) {
    text+="\""+cookie[i].name+"\": \""+cookie[i].value+"\",\n"
}
text += "}"
console.log(text)
