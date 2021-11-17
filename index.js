// cookie = 貼上
let text = "{";
for (i=0;i<cookie.length;i++) {
    text+="\""+a[i].name+"\": \""+a[i].value+"\",\n"
}
text += "}"
console.log(text)
