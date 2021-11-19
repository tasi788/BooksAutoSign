// cookie = 貼上
let cookiejar = {};
for(var c of cookie) {
  cookiejar[c.name] = c.value;
}
console.log(JSON.stringify(cookiejar))
