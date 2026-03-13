import random
import time

print('===Math Tutor===')
num_questions = int(input("How many random practice questions would you like? "))
x = int(input('How low would you like the number be? '))
y = int(input('How high would you like the number be? '))

correct = 0
start_time = time.time()
num_a = []
num_b = []
response = []
for i in range(num_questions):
    a = random.randint(x,y)
    b = random.randint(x,y)
    answer = int(input(f'{a} X {b} = '))
    num_a.append(a)
    num_b.append(b)
    response.append(answer)

    if answer == a * b:
        print("Correct!")
        correct += 1
    else:
        print(f"Incorrect, it's {a*b}")

end_time = time.time()

total_time = round(end_time - start_time,2)
avg_time = total_time/num_questions



print("Thanks for playing!")
print(f'Your score (correct/num of questions): {correct}/{num_questions}')
percentage_score = round(100*(correct/num_questions),2)
print(f'{percentage_score}% correct')
print(f'It took you {total_time} seconds to finish this, and an average time of {avg_time} per question!')
print(f'Saved questions and response:')
for i in range(num_questions):
    print(f'{num_a[i]} X {num_b[i]} = {response[i]}')

