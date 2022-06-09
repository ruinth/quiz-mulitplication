import pyinputplus as pyip
import random, time
questionNum, correctAns, wrongAns = 0,0,0
harders,difficulty,skips =0, 1, 5
skipped, timeouts= 0,0
numH,numI=0,8
print(' This is a math test')
time.sleep(1.5)
print(' the questions will get harder after every 7 answered correctly')
time.sleep(1.5)
print(' enter an answer or enter [s] to skip (you only have 5)')
time.sleep(1.5)
print(' The game will end after 5 wrong answers or when [x] is entered')
time.sleep(1.5)
print(' Good luck!')
time.sleep(2.25)
while wrongAns + timeouts < 5:
    numA, numB = random.randint(numH,numI), random.randint(numH,numI)
    numC = numA * numB
    questionNum +=1
    prompt = f'Question {questionNum}: {numA}*{numB}\n'
    playerAns = pyip.inputNum(prompt,allowRegexes=['x','s'], timeout = 22, limit = 1, default = 'TO')
    if playerAns == 'x':
        questionNum -=1
        break
    if playerAns == 's':
        if skips > 1:
            print(f'skipped - {numC}\n')
            skips-=1
            skipped +=1
            time.sleep(0.75)
        elif skips ==1:
            print(f'final skip used - {numC}\n')
            skips-=1
            skipped +=1
            time.sleep(0.75)
        else:
            wrongAns +=1
            print(f'no skips left - {numC}\n')
            time.sleep(0.75)
    elif playerAns == numC:
        print('correct\n')
        time.sleep(0.75)
        correctAns +=1
        harders+=1
        if harders == 7:
            harders-=7
            numI+=3
            numH+=1
            difficulty+=1
    elif playerAns == 'TO':
        print(f'timeout - {numC}\n')
        time.sleep(0.75)
        timeouts+=1
    elif playerAns != numC:
        print(f'incorrect - {numC}\n')
        time.sleep(0.75)
        wrongAns+=1
questionNum= questionNum - skipped
incorrectNumber = wrongAns + timeouts
print(f' correct answers : {correctAns}\n incorrect answers : {incorrectNumber}\n questions timed out : {timeouts}\n total questions answered : {questionNum}\n difficulty level reached : {difficulty}\n skips used : {skipped}')