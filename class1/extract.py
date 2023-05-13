text = "X-DSPAM-Confidence:    0.8475"
startpoint = text.find(":")
chosentext = text[startpoint + 1: len(text)].strip()
answerasfloat = float(chosentext)
print(answerasfloat)
