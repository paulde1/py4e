score = input('Enter Score:')

grade = 'F'
try:
    score = float(score)
    if score >= 0.0 or score <= 1.0 :
        if(score >= 0.9):
         grade = 'A'
        if(score >= 0.8):
         grade = 'B'
        if(score >= 0.7):
         grade = 'C'
        if(score >= 0.6):
         grade = 'D'
except:
    print('invalid input score')
    quit()

print(grade)
  
  