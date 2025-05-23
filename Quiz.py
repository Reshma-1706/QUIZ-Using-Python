Questions=("How many elements in periodic table?",
           "Which animal lays largest eggs?",
           "What is the Most abundant gas in Earth's atmosphere?",
           "How many bones in the human body?",
           "which planet is hottest?")
options=(("A.116","B.117","C.118","D.119"),
         ("A.whale.","B.hen","C.elephant","D.Ostrich"),
         ("A.Nitrogen","B.Oxygen","C.CO2","D.H2O"),
         ("A.206","B.306","C.208","D.207"),
         ("A.Mecury","B.venus","C.Earth","D.mars"))

answers=("C","D","A","A","C")
gusses=[]
score=0
question_num=0
for question in Questions:
    print("---------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess=input("Enter(A,B,C,D): ").upper()
    gusses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num] }is correct answer!")

    question_num+=1

print("-----------------------------------------------------")
print("                       RESULTS                       ")
print("-----------------------------------------------------")
print("answers:", end=" ")
print()
for answer in answers:
    print(answer,end=" ")
print()
for guess in gusses:
    print(guess,end=" ")
print()

score=int(score/len(answers)*100)
print(f"YOUR SCORE IS: {score}%")