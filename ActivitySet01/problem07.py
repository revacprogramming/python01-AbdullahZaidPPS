# Strings

#text = "X-DSPAM-Confidence:    0.8475"
text = "X-DSPAM-Confidence:    0.8475"
index = text.find(':')
string = text[index+5:29]
stri1 = float(string)
print(stri1)