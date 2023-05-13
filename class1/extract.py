text = "X-DSPAM-Confidence:    0.8475"
startpoint = text.find(":")
chosentext = text[startpoint + 2:]
answerasfloat = float(chosentext)
print(answerasfloat)
