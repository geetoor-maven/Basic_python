# Di sini kita akan belajar tentang list argument

# metode tanpa atribut
def Buat_html(tag, text):
    buathtml = f"<{tag}>{text}</{tag}>"
    return buathtml

# metode dengan atribut
def Buat_Atribut(tag,text, **atribut):
    html = f"<{tag}"

    for key,value in atribut.items():
        html = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    return html

print()
# Output
html = Buat_html("HTML","This html")
print(html,"\n")

html = Buat_html("Title","Japanese hub")
print(html,"\n")

html = Buat_html("Body","This Body")
print(html,"\n")

print("--Metode dengan atribut--\n")

html = Buat_Atribut("a1","Header", style="Underline")
print(html,"\n")

html = Buat_Atribut("p","Belajar python sangat asyik",color="#ffff",textstyle="bold")
print(html,"\n")