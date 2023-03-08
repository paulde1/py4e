def scoreKeep():
    score = input('Enter Score:')

    grade = 'Score out of range'
    try:
        score = float(score)
        if score >= 0.0 and score <= 1.0:
            if(score >= 0.9):
                grade = 'A'
            elif(score >= 0.8):
                grade = 'B'
            elif(score >= 0.7):
                grade = 'C'
            elif(score >= 0.6):
                grade = 'D'
            else: grade = 'F'
        print(grade)
        return grade
    except:
        print ("error: invalid score type")
        quit()
    
scoreKeep()


  
  