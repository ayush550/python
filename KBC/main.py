#list of questions along with their 4 options and final correct answer
questions = [
  ["You should save your computers from: ", "Viruses", "Time-bomb", "worms", "All of the above", "4"], 

  ["World wide web is being standard by: ", "Worldwide corporation", "W3C", "World Wide Consortium", "World Wide Web Standard", "2"], 

  ["Microsoft windows is an: ", "Operating system", "Graphic Processor", "Word Program", "Database Program", "1"], 

  ["Who took Ashoka's pillar inscription of Topra and Meerut to Delhi?: ", "Alauddin Khilji", "Firoz Shah Tughlaq", "Muhammad Ghori", "Sikandar Lodi", "2"], 

  ["Kushinara(Kushinagar) was the capital of?: ", "Bhagos", "Lichhans", "Mallas", "Sakas", "3"], 

  ["U.P. covers how much area of the total geographical area of India? : ", "13.50%", "9.40%", "8.40%", "7.33%", "4"],

  ["How many states share their boundary with U.P?: ", "6", "7", "8", "9", "3"],

  ["Electric bulb filament is made of?: ", "Copper", "Aluminum", "Lead", "Tungsten", "4"],

  ["Which of the following non-metal remains liquid at room temperature?: ", "Phosphorous", "Bromine", "Chlorine", "Helium", "2"],

  ["Washing soda is the common name for: ", "Sodium carbonate", "Calcium Bicarbonate", "Sodium Bicarbonate", "Calcium Carbonate", "1"],

  ["______ was the first Chief Election Commissioner of India ?: ", "Sukumar Sen", "T N Seshan", "Sunil Arora", "M S Gill", "1"],

  ["Name the first female amputee to climb Mount Everest ?: ", "Arunima Sinha", "Poorna Malavath", "Anshu Jamsenpa", "Premlata Agarwal", "1"],

  ["Which of the following is the largest delta in the world ?: ", "Ganges-Brahmaputra Delta", "Amazon Delta", "Indus River Delta", "Danube Delta", "1"],

  ["Who was the first woman Chief Minister of an Indian state ?: ", "Indira Gandhi", "Sucheta Kriplani", "Sarojini Naidu", "Mamta Banerjee", "2"],

  ["The First Health Minister of Independent India was ?: ", "Maulana Abdul Kalam Azad", "Sardar Vallabhbhai Patel", "Vijayalakshmi Pandit", "Rajkumari Amrit Kaur", "4"],

  ["Who among the following was appointed as India’s first Lokpal ?: ", "Justice A K Sikri", "Justice N V Ramana", "Justice Pinaki Chandra Ghose", "Justice S A Bobde", "3"],
]

# print(len(questions))

#list of rewords for each and every question
reward = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]

# print(len(reward))

earnedReward = 0

print('Welcome to KBC\n')

for i in range(0, len(questions)+1):
  question = questions[i]
  print("\n"+question[0]+"\n")
  print("1:   " + question[1], "    2:   " + question[2])
  print("3:   " + question[3], "    4:   " + question[4])
  print("\nEnter your option (1-4) or else enter 0 to quit ")
  ans = int(input())

  # print(question)
  # print(question[-1]
  
  if ans == 0:
    if i == 0:
      earnedReward = 0
    else:
      earnedReward = reward[i-1]
    break
  elif i == 4:
    earnedReward = 10000
  elif i == 9:
    earnedReward = 320000
  elif i == 15:
    earnedReward = 70000000

  if ans == int(question[-1]):
    print(f"\nCorrect Answer, you've Won Rs.{reward[i]}\n")
  elif (ans > 4):
    print("Sorry! Wrong Input")
    break
  else:
    print("Sorry! wrong Answer")
    break

print("\n\nThanks for Playing")
print(f"\nYou have won Rs.{earnedReward}")    
