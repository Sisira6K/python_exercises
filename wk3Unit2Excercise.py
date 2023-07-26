"""One of the nice features of Python is that it supports Unicode. Therefore it is possible to use emojis 
just like other characters in strings. In this exercise you will use this feature to build an emoji translator.
Below is a dictionary that maps English terms to Emojis (broken into multiple lines for better readability)."""
emojis= {
"happy": "😃",
"heart": "😍",
"rotfl": "🤣",
"smile": "😊",
"crying": "😭",
"kiss": "😘",
"clap": "👏",
"grin": "😁",
"fire": "🔥",
"broken": "💔",
"think": "🤔",
"excited": "🤩",
"boring": "🙄",
"winking": "😉",
"ok": "👌",
"hug": "🤗",
"cool": "😎",
"angry": "😠",
"python": "🐍"
}
newsentence =""
sentence=input("Please enter a sentence: ")
words = sentence.split()
print(words)
for i in words :
    if i in emojis:
        newsentence= newsentence +" "+emojis[i]       
    else :       
        newsentence=newsentence+" "+i
print(newsentence)
    