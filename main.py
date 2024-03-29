# Caleb Stanton and Matt Rieckenberg
# Political Compass for 2021 version 1.0


import string
import tkinter as tk
from tkinter import PhotoImage, NW
from tkinter import ttk, RAISED, filedialog
import random
from pylab import *

# Constants
N = -1
P = +1


userName = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

x = datetime.datetime.now()
currentDate = x.strftime("%A") + ", " + x.strftime("%B") + " " + x.strftime("%d") + ", " + x.strftime("%Y")


## (Question: self, number, text, axis, polarity, answer) stores questions as strings,
##  along with all their relevant attributes. These include a unique serial number for indexing purposes,
##  the political axis which the question investigates, their idealogical lean, and a dynamic record of the responses given by the user.

class Question:
    def __init__(self, number, text, axis, polarity, answer):
        self.text = text
        self.number = number
        self.axis = axis
        self.polarity = polarity
        self.answer = answer

    def getNumber(self):
        return self.number

    def getText(self):
        return self.text

    def getAxis(self):
        return self.axis

    def getPolarity(self):
        return self.polarity

    # scoring methods

    def setAnswer(self, a):
        self.answer = a
        # print("Answer set to " + a)

    def getAnswer(self):
        return self.answer


## Below is a compendium of every question to be used on the test,
## Organized into four sections, each pertaining to a specific axis of the political spectrum.
## Questions will be presented to the user in the following numerically ordered sequence

# State Axis Questions --- Positive leans authoritarian, negative leans libertarian

Q1 = Question(1, "Citizens of a nation should hold the right to bear arms", "state", N, "-")

Q2 = Question(2, "Recreational drugs and alcohol should be decriminalized", "state", N, "-")

Q3 = Question(3,
              "My government should restrict immigration or miscegenation" + '\n' + "to preserve the cultural character of my nation",
              "state", P, "-")

Q4 = Question(4, "Mask mandates and lockdowns are needed to prevent the spread of disease", "state", P, "-")

Q5 = Question(5, "To become a truly free country, police departments need to be reformed or demilitarized", "state", N,
              "-")

Q6 = Question(6, "Those who wish to travel should carry a vaccine passport", "state", P, "-")

Q7 = Question(7, "Meat and dairy products need to be limited to combat the climate emergency", "state", P, "-")

Q8 = Question(8, "Sometimes violence is unavoidable in advancing the interests of my political cause", "state", P, "-")

Q9 = Question(9, "I believe in freedom of speech even for those who’s views I despise most", "state", N, "-")

Q10 = Question(10,
               "The primary aim of the justice system is protection" + '\n' + "of the innocent, not rehabilitation of the guilty",
               "state", P, "-")

Q11 = Question(11, "Government has no business in the bedrooms of the nation", "state", N, "-")

Q12 = Question(12, "Religious practices should be taught in school and enforced by the state", "state", P, "-")

Q13 = Question(13, "Every company should be required to have at least one woman on its board", "state", P, "-")

Q14 = Question(14, "Sexwork should be bought and sold as a commodity", "state", N, "-")

Q15 = Question(15, "Security from criminals and terrorists is more precious than personal privacy", "state", P, "-")

Q16 = Question(16, "A baker has no obligation to make a cake for a gay wedding", "state", N, "-")

# Economic Axis Questions --- positive leans towards capitalism, negative leans towards socialism

Q17 = Question(17, "Nuclear power is a safe, viable source of energy", "econ", P, "-")

Q18 = Question(18, "Increasing regulations on fossil fuels will have ambiguous benefits and cripple the economy",
               "econ", P, "-")

Q19 = Question(19, "The industrial revolution and it’s consequences have been a disaster for the human race", "econ", N,
               "-")

Q20 = Question(20, "Single payer healthcare is preferable to a privatized system", "econ", N, "-")

Q21 = Question(21, "Free trade and globalization have been our greatest allies in alleviating poverty", "econ", P, "-")

Q22 = Question(22, "A state-planned economy cannot scale to the efficiency or complexity of the free market", "econ", P,
               "-")

Q23 = Question(23, "Deficit spending is necessary to rebuild our public infrastructure", "econ", N, "-")

Q24 = Question(24, "Water should be a public resource that anyone can access freely", "econ", N, "-")

Q25 = Question(25, "Education would be much more effective if school choice was left to the parents", "econ", P, "-")

Q26 = Question(26, "We lose more in taxes than government could ever give back", "econ", P, "-")

Q27 = Question(27, "Industry should be democratically owned and controlled by labour unions", "econ", N, "-")

Q28 = Question(28, "Raising the minimum wage will not help the working class", "econ", P, "-")

Q29 = Question(29, "Helping the unemployed is of greater urgency than slowing down inflation", "econ", N, "-")

Q30 = Question(30, "Precious metals and cryptocurrencies are more trustworthy than federal banking systems", "econ", P,
               "-")

Q31 = Question(31, "I support regulations enforcing net neutrality", "econ", N, "-")

Q32 = Question(32,
               "The military, courts and police could be replaced with voluntary legal agreements and private protection agencies",
               "econ", P, "-")

Q33 = Question(33, "It’s a tragedy that art and culture are commodified and cheapened by the capitalist system", "econ",
               N, "-")

Q34 = Question(34, "Affordable housing programs to little except destroy property values", "econ", P, "-")

Q35 = Question(35, "A federal jobs initiative is an excellent remedy to economic downturns", "econ", N, "-")

Q36 = Question(36, "Economic growth without equality is an injustice", "econ", N, "-")

# Foreign Policy Axis --- Positive means isolationist, negative means internationalist

Q37 = Question(37, "My country should spread its values around the world, even if it requires military forces",
               "foreign", N, "-")

Q38 = Question(38, "NATO membership is beneficial to my country", "foreign", N, "-")

Q39 = Question(39, "Russian aggression is one of the most serious geopolitical threats today", "foreign", N, "-")

Q40 = Question(40, "It is not our responsibility to take in refugees and asylum seekers", "foreign", P, "-")

Q41 = Question(41,
               "My country should seek to solve its own internal problems before worrying about the rest of the world",
               "foreign", P, "-")

Q42 = Question(42, "It is beneficial to trade with our geopolitical adversaries", "foreign", N, "-")

Q43 = Question(43, "War is ultimately harmful to my country and it should be only used as a defensive measure",
               "foreign", P, "-")

Q44 = Question(44, "The war in Afghanistan is pointless and should be ended soon", "foreign", P, "-")

Q45 = Question(45, "The Iraq War was a mistake", "foreign", P, "-")

Q46 = Question(46, "NATO’s campaigns in Serbia and Libya benefitted the world by removing dictators", "foreign", N, "-")

Q47 = Question(47, "Supranational organizations like the European Union are beneficial", "foreign", N, "-")

Q48 = Question(48, "My country has an important obligation to support the State of Israel", "foreign", N, "-")

Q49 = Question(49,
               "If we withdraw our military presence from the middle east, our peacekeeping efforts will have been for nothing",
               "foreign", N, "-")

Q50 = Question(50, "The rising technological and economic power of the Chinese government is alarming", "foreign", N,
               "-")

Q51 = Question(51, "We should recognize Taiwan as a country, even if it damages our relationship with China", "foreign",
               N, "-")

# Cultural Axis --- Positive means tradition, negative means progress

Q52 = Question(52, "Society was greater in the past", "culture", P, "-")

Q53 = Question(53, "The quality of music has declined over the last hundred years", "culture", P, "-")

Q54 = Question(54, "Surrealist and postmodern works are just as valuable as paintings of people and landscapes",
               "culture", N, "-")

Q55 = Question(55, "Immigration is a net positive to my country", "culture", N, "-")

Q56 = Question(56, "There are foreign and subversive elements in positions of power that seek to sabotage our culture",
               "culture", P, "-")

Q57 = Question(57, "Multiculturalism is something to be proud of", "culture", N, "-")

Q58 = Question(58, "Religion is primitive, it's time to move on", "culture", N, "-")

Q59 = Question(59, "I do not enjoy popular culture", "culture", P, "-")

Q60 = Question(60, "Transgender women are women", "culture", N, "-")

Q61 = Question(61, "Having casual sex doesn't make you a bad person", "culture", N, "-")

Q62 = Question(62, "Drugs and material pleasures weaken one's character, true freedom comes from discipline", "culture",
               P, "-")


class Score:
    Name = ""
    StateScore = 0
    EconScore = 0
    ForeignScore = 0
    CulturalScore = 0
    GoBack = False


# Question Lists
stateAxis = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16]
econAxis = [Q17, Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30, Q31, Q32, Q33, Q34, Q35, Q36]
foreignAxis = [Q37, Q38, Q39, Q40, Q41, Q42, Q43, Q44, Q45, Q46, Q47, Q48, Q49]
cultureAxis = [Q50, Q51, Q52, Q53, Q54, Q55, Q56, Q57, Q58, Q59, Q60, Q61, Q62]

MegaList = stateAxis + econAxis + foreignAxis + cultureAxis


## First window to display
## Greets users and asks their name. Displays logo and current time.
## Initiates the test.

class OpeningWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Political Compass Test 2021')
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        self.configure(bg="#004b8d")

        # labels
        self.welcomeLabel1 = tk.Label(self, text="Welcome to the" + '\n' + "Political Compass Test for 2021",
                                      font=("Georgia", 40, 'bold'), background="#f2552c", foreground="#FAE5D3",
                                      height=2,
                                      width=40, justify='left').place(relx=.35, rely=0.2, anchor="center")
        self.welcomeLabel2 = ttk.Label(self, background="#004b8d", foreground="#F9E79F", font=("Georgia", 15, 'bold'),
                                       text='This test is a new and improved version of the' + '\n' + 'popular political compass test' + '\n' + 'which has become the subject of a lot of memes').place(
            relx=.20, rely=0.5, anchor="center")

        # Image
        self.my_canvas = tk.Canvas(self, width=225, height=225, bg="#004b8d", highlightthickness=0, relief='ridge')
        self.my_canvas.place(relx=0.015, rely=0.6)
        self.img = PhotoImage(file=r"Images/PoliticalCompass.png")

        self.my_image = self.my_canvas.create_image(0, 0, anchor=NW, image=self.img)

        # Name textbox
        self.nameLabel = tk.Label(self, text="Please enter your name here: ", bg="#004b8d", fg="#F9E79F",
                                  font=("Georgia", 15, 'bold')).place(relx=.45, rely=0.4)
        self.nameEntryBox = tk.Entry(self, justify='left', font=("Georgia", 15, 'bold'), width=20, bg='#AED6F1',
                                     fg='#212F3D')
        self.nameEntryBox.place(relx=.80, rely=0.42, anchor="center")

        # Button
        self.button = tk.Button(self, text='Start test ➡', font=("Georgia", 30, 'bold'), height=2, width=20,
                                relief=RAISED, bg="#2ECC71", fg="#4A235A")
        self.button['command'] = self.button_clicked
        self.button.place(relx=.75, rely=.7, anchor="center")

        # Date Label
        self.DateLabel = ttk.Label(self, text=currentDate, background="#004b8d", foreground="#F9E79F",
                                   font=("Georgia", 15, 'bold')).place(relx=.1, rely=.96, anchor="center")

        # Quit the program
        self.quitButton = tk.Button(self, text='Quit ✖', font=("Georgia", 20, 'bold'), height=2, width=20, bg="#E74C3C",
                                    fg="#F9E79F")
        self.quitButton['command'] = self.quitProgram
        self.quitButton.place(relx=.82, rely=.9, anchor="center")

    def button_clicked(self):
        Score.Name = self.nameEntryBox.get()
        print("User's name is " + Score.Name + " and is identified by the username " + userName)
        print(userName + " is starting the quiz")
        print(Score.Name)
        self.destroy()

    def quitProgram(self):
        print("Quitting program now")
        sys.exit()


class SecondLastWindow(tk.Tk, Question, Score):
    def __init__(self):
        super().__init__()
        self.configure(bg="#F39C12")
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        self.title("The quiz is now complete!")

        def FinishQuiz():
            self.destroy()

        self.FinishQuizButton = tk.Button(self, text="Finish Quiz", command=FinishQuiz, font=("Georgia", 30, 'bold'),
                                          height=2,
                                          width=20, bg="#8E44AD", fg="#ECF0F1").place(relx=0.5, rely=0.5,
                                                                                      anchor='center')

    ## (sumScore self question) Computes summation of the users score after they've submitted all the questions.
    ## applies different scoring algorithms depending one what axis the questions fall on.
    ## Does not cut off scores which land outside the range of the compass.
    ## sumScore: question -> Int

    def sumScore(self, question):
        print(question.getNumber())
        if question.getAxis() == "state":
            if question.getPolarity() == N:
                if question.getAnswer() == "A":
                    Score.StateScore += -2
                elif question.getAnswer() == "B":
                    Score.StateScore += -1
                elif question.getAnswer() == "C":
                    Score.StateScore += 2
                elif question.getAnswer() == "D":
                    Score.StateScore += 3
                else:
                    pass
            if question.getPolarity() == P:
                if question.getAnswer() == "A":
                    Score.StateScore += 3
                elif question.getAnswer() == "B":
                    Score.StateScore += 2
                elif question.getAnswer() == "C":
                    Score.StateScore += -1
                elif question.getAnswer() == "D":
                    Score.StateScore += -2
                else:
                    pass
        elif question.getAxis() == "econ":
            if question.getNumber() == 27:
                if question.getAnswer() == "A":
                    Score.EconScore += -7
                elif question.getAnswer() == "B":
                    Score.EconScore += -4
                elif question.getAnswer() == "C":
                    Score.EconScore += 1
                elif question.getAnswer() == "D":
                    Score.EconScore += 2
                else:
                    pass
            elif question.getNumber() == 32:
                if question.getAnswer() == "A":
                    Score.EconScore += 7
                elif question.getAnswer() == "B":
                    Score.EconScore += 4
                elif question.getAnswer() == "C":
                    Score.EconScore += -1
                elif question.getAnswer() == "D":
                    Score.EconScore += -2
                else:
                    pass
            elif question.getPolarity() == N:
                if question.getAnswer() == "A":
                    Score.EconScore += -2
                elif question.getAnswer() == "B":
                    Score.EconScore += -1
                elif question.getAnswer() == "C":
                    Score.EconScore += 1
                elif question.getAnswer() == "D":
                    Score.EconScore += 2
                else:
                    pass
            elif question.getPolarity() == P:
                if question.getAnswer() == "A":
                    Score.EconScore += 2
                elif question.getAnswer() == "B":
                    Score.EconScore += 1
                elif question.getAnswer() == "C":
                    Score.EconScore += -1
                elif question.getAnswer() == "D":
                    Score.EconScore += -2
                else:
                    pass
        elif question.getAxis() == "foreign":
            if question.getPolarity() == N:
                if question.getAnswer() == "A":
                    Score.ForeignScore += -2
                elif question.getAnswer() == "B":
                    Score.ForeignScore += -1
                elif question.getAnswer() == "C":
                    Score.ForeignScore += 1
                elif question.getAnswer() == "D":
                    Score.ForeignScore += 2
                else:
                    pass
            if question.getPolarity() == P:
                if question.getAnswer() == "A":
                    Score.StateScore += 2
                elif question.getAnswer() == "B":
                    Score.StateScore += 1
                elif question.getAnswer() == "C":
                    Score.StateScore += -1
                elif question.getAnswer() == "D":
                    Score.StateScore += -2
                else:
                    pass
        elif question.getAxis() == "culture":
            if question.getPolarity() == N:
                if question.getAnswer() == "A":
                    Score.CulturalScore += -2
                elif question.getAnswer() == "B":
                    Score.CulturalScore += -1
                elif question.getAnswer() == "C":
                    Score.CulturalScore += 1
                elif question.getAnswer() == "D":
                    Score.CulturalScore += 2
                else:
                    pass
            if question.getPolarity() == P:
                if question.getAnswer() == "A":
                    Score.CulturalScore += 2
                elif question.getAnswer() == "B":
                    Score.CulturalScore += 1
                elif question.getAnswer() == "C":
                    Score.CulturalScore += -1
                elif question.getAnswer() == "D":
                    Score.CulturalScore += -2
                else:
                    pass
        else:
            pass


## displays final results of the quiz
## gives users the option to export their scores to a text file with their name the date they completed the test
## opens up a folder browsing window to select locations for the results to be saved

class ResultsWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg="#48C9B0")
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))
        self.title("Here are your results!")

        self.StateAxisLabel = tk.Label(self, text="My final State Axis Score is " + str(Score.StateScore)).pack()
        self.EconomicAxisLabel = tk.Label(self, text="My final Economic Axis Score is " + str(Score.EconScore)).pack()
        self.ForeignAxisLabel = tk.Label(self, text="My final Foreign Policy Axis Score is " + str(
            Score.ForeignScore)).pack()
        self.CulturalAxisLabel = tk.Label(self,
                                          text="My final Cultural Axis Score is " + str(Score.CulturalScore)).pack()

        def select_output_file():
            output_file_path = tk.filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"), ("Any file", "*")))
            print(output_file_path)
            f = open(output_file_path + ".txt", 'w')
            f.write("Results for " + Score.Name + " on " + currentDate + '\n')
            f.write("My final State Axis Score is " + str(Score.StateScore) + '\n')
            f.write("My final Economic Axis Score is " + str(Score.EconScore) + '\n')
            f.write("My final Foreign Policy Axis Score is " + str(Score.ForeignScore) + '\n')
            f.write("My final Cultural Axis Score is " + str(Score.CulturalScore) + '\n')

        def exitProgram():
            sys.exit()

        def graph():
            compass = Compass()
            compass.result(Score.EconScore,Score.StateScore)


        self.ExitButton = tk.Button(self, text="Exit", font=("Georgia", 20, 'bold'), command=exitProgram, width=10,
                                    height=2, bg='orange', fg='black').pack()
        self.ChooseFolder = tk.Button(self, text="Export", command=select_output_file).pack()
        self.SeeGraph = tk.Button(self,text="See graph",command=graph)
        self.SeeGraph.pack()





    def dataToTextFile(self):
        f = open("UserData.txt", "a")
        f.write("Results for " + userName + " on " + currentDate + '\n')
        for x in stateAxis:
            f.write(str(x.getNumber()) + ": " + str(x.getText()) + ": " + x.getAnswer() + '\n')
        for y in econAxis:
            f.write(str(y.getNumber()) + ": " + str(y.getText()) + ": " + y.getAnswer() + '\n')
        for z in foreignAxis:
            f.write(str(z.getNumber()) + ": " + str(z.getText()) + ": " + z.getAnswer() + '\n')
        for w in cultureAxis:
            f.write(str(w.getNumber()) + ": " + str(w.getText()) + ": " + w.getAnswer() + '\n')
        f.write('\n')
        f.write("Your final State Axis Score is " + str(Score.StateScore) + '\n')
        f.write("Your final Economic Axis Score is " + str(Score.EconScore) + '\n')
        f.write("Your final Foreign Policy Axis Score is " + str(Score.ForeignScore) + '\n')
        f.write("Your final Cultural Axis Score is " + str(Score.CulturalScore) + '\n')
        f.write(
            "------------------------------------------------------------------------------------------------------------------------------------" + '\n')
        f.close()



## Main question window operates inside a while loop to display questions to the user as a GUI.
## Presents users with five options to respond to the statement being made.
## Mutates questions answer attribute to match the respondants selection
## There are also previous and quit buttons below the test.

class QuestionWindow(tk.Tk, Question):
    def __init__(self, question):
        super().__init__()
        self.question = question

        # configure the question window
        self.title(question.getAxis() + ' Axis Questions')
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda event: self.attributes("-fullscreen", False))

        # Labels
        self.questionLabel = tk.Label(self, text=question.getText(), font=("Georgia", 17, 'bold'), background="#2ECC71",
                                      foreground="white", width=100, height=2)
        self.questionLabel.place(relx=0.5, rely=0.1, anchor='center')
        self.progressLabel = tk.Label(self, text=str(question.getNumber()) + "/" + str(len(MegaList)),
                                      font=("Georgia", 20, 'bold'))
        self.progressLabel.place(relx=0.9, rely=0.9)

        def stronglyAgree_onClick():
            # print("Strongly Agree clicked")
            question.setAnswer("A")
            self.destroy()

        def moderatelyAgree_onClick():
            # print("Moderately Agree clicked")
            question.setAnswer("B")
            self.destroy()

        def neutral_onClick():
            # print("Neutral Clicked")
            question.setAnswer("E")
            self.destroy()

        def moderatelyDisagree_onClick():
            # print("Moderately Disagree clicked")
            question.setAnswer("C")
            self.destroy()

        def stronglyDisagree_onClick():
            # print("Strongly Disagree clicked")
            question.setAnswer("D")
            self.destroy()

        def quitProgram():
            sys.exit()

        def goBack_onClick():
            # print("Back button pressed")
            self.destroy()
            Score.GoBack = True

        # Option buttons
        self.stronglyAgree = tk.Button(self, text="Strongly Agree", command=stronglyAgree_onClick,
                                       font=("Georgia", 20, 'bold'), height=1, width=20, bg="#008000",
                                       fg="black").place(relx=.5, rely=.25, anchor='center')
        self.moderatelyAgree = tk.Button(self, text="Moderately Agree", command=moderatelyAgree_onClick,
                                         font=("Georgia", 20, 'bold'), height=1, width=20, bg="#12E414",
                                         fg="black").place(relx=.5, rely=.35, anchor='center')

        self.neutral = tk.Button(self, text="Neutral/Unsure", command=neutral_onClick,
                                 font=("Georgia", 20, 'bold'), height=1, width=20, bg="#99A3A4",
                                 fg="black").place(relx=.5, rely=.45, anchor='center')

        self.moderatelyDisagree = tk.Button(self, text="Moderately Disagree",
                                            command=moderatelyDisagree_onClick, font=("Georgia", 20, 'bold'), height=1,
                                            width=20, bg="#FF0000", fg="black").place(relx=.5, rely=.55,
                                                                                      anchor='center')

        self.stronglyDisagree = tk.Button(self, text="Strongly Disagree", command=stronglyDisagree_onClick,
                                          font=("Georgia", 20, 'bold'), height=1, width=20, bg="#7F0000",
                                          fg="black").place(relx=.5, rely=.65, anchor='center')

        self.backButton = tk.Button(self, text="◀Previous Question", font=("Georgia", 20, 'bold'), height=1, width=20,
                                    bg="#F1C40F", fg="black", command=goBack_onClick).place(relx=.2, rely=.85,
                                                                                            anchor='center')

        self.quitButton = tk.Button(self, text="Quit❌", command=quitProgram, font=("Georgia", 20, 'bold'), height=1,
                                    width=10, bg="#E74C3C", fg="black").place(relx=.2, rely=.95, anchor='center')


## (RunQuestion WindowClass list) uses a while loop to traverse a list of questions and calls the question window to display them.
## RuneQuestion: listof questions -> null
def RunQuestion(WindowClass, list):
    counter = 0
    while (counter < len(list)):
        question = list[counter]
        app = WindowClass(question)
        print(question.getNumber())

        if (question.getAxis() == 'state'):  # configures colour of questions
            app.config(bg="#16A085")
            app.questionLabel.config(bg='#F1C40F', fg='#1C2833')
            app.progressLabel.config(bg="#16A085", fg="white")
            app.mainloop()

            if (Score.GoBack):  # adds previous button functionality
                if (counter == 0):
                    Score.GoBack = False
                    continue
                else:
                    counter += -1
                    Score.GoBack = False
                    continue
            else:
                counter += 1
                continue

        elif (question.getAxis() == 'econ'):
            app.config(bg="#EC7063")
            app.questionLabel.config(bg='#BA4A00', fg='white')
            app.progressLabel.config(bg="#EC7063", fg="white")
            app.mainloop()

            if (Score.GoBack):
                if (counter == 0):
                    Score.GoBack = False
                    continue
                else:
                    counter += -1
                    Score.GoBack = False
                    continue
            else:
                counter += 1
                continue




        elif (question.getAxis() == 'culture'):
            app.config(bg='#2E86C1')
            app.questionLabel.config(bg='purple', fg='white')
            app.progressLabel.config(bg="#2E86C1", fg="white")
            app.mainloop()

            if (Score.GoBack):
                if (counter == 0):
                    Score.GoBack = False
                    continue
                else:
                    counter += -1
                    Score.GoBack = False
                    continue
            else:
                counter += 1
                continue




        elif (question.getAxis() == 'foreign'):
            app.config(bg='#D35400')
            app.questionLabel.config(bg='red', fg='black')
            app.progressLabel.config(bg="#D35400", fg="white")
            app.mainloop()

            if (Score.GoBack):
                if (counter == 0):
                    # print("Counter = 0")
                    Score.GoBack = False
                    continue
                else:
                    counter += -1
                    Score.GoBack = False
                    continue
            else:
                counter += 1
                continue

        else:
            pass


class Compass:
    def __init__(self):

        # graph scale
        xmin = -10
        xmax = 10
        ymin = -10
        ymax = 10
        #ticks_frequency = 1

        figure, axes = plt.subplots(figsize=(10, 10))
        figure.patch.set_facecolor("white")

        axes.set(xlim=(xmin, xmax), ylim=(ymin, ymax), aspect="equal")

        arr = np.array([[1, 1], [1, 1]])

        # grid lines
        axes.spines['bottom'].set_position('zero')
        axes.spines['left'].set_position('zero')
        axes.grid(which="both", color="black", linewidth=1, linestyle='-', alpha=0.6)

        axes.autoscale(False)
        axes.imshow(arr, cmap=plt.cm.Reds_r, extent=[-10, 0, 0, 10], interpolation='none', alpha=0.7)
        axes.imshow(arr, cmap=plt.cm.Blues_r, extent=[0, 10, 0, 10], interpolation='none', alpha=0.7)
        axes.imshow(arr, cmap=plt.cm.BuGn_r, extent=[-10, 0, 0, -10], interpolation='none', alpha=0.7)
        axes.imshow(arr, cmap=plt.cm.Purples_r, extent=[0, 10, 0, -10], interpolation='none', alpha=0.7)

        axes.axhline(0, color='grey')
        axes.grid(True)



    def result(self, x, y):

        state = y / 3
        state = round(state * 2) / 2

        econ = x / 4
        econ = round(econ * 2) / 2

        if econ > 10:
            econ = 10

        if state > 10:
            state = 10

        plt.scatter(econ, state)
        show()







## Assembles the different windows of the program in sequence
## Inserts questions library into the GUI and scoring classes
## Program begins and ends with this function

if __name__ == "__main__":


    app = OpeningWindow()
    app.mainloop()

    RunQuestion(QuestionWindow, MegaList)

    app = SecondLastWindow()
    app.mainloop()

    print("Calculating scores")
    for i in range(len(MegaList)):
        app.sumScore(MegaList[i])
    print("Calculations complete")

    app = ResultsWindow()
    app.dataToTextFile()
    app.mainloop()
