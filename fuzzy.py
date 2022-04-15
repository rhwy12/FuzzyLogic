from simpful import *

# A simple fuzzy inference system for the tipping problem
# Create a fuzzy system object
FS = FuzzySystem()

# Define fuzzy sets and linguistic variables
S_1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=25, d=37.5), term="dry")
S_2 = FuzzySet(function=Triangular_MF(a=25, b=50, c=75), term="average")
S_3 = FuzzySet(function=Trapezoidal_MF(a=62.5, b=75, c=100, d=100), term="wet")
FS.add_linguistic_variable("G", LinguisticVariable([S_1, S_2, S_3], concept="moisture of the ground", universe_of_discourse=[0, 100]))

F_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=50), term="cold")
F_2 = FuzzySet(function=Triangular_MF(a=0, b=55, c=65), term="cool")
F_3 = FuzzySet(function=Triangular_MF(a=60, b=65, c=70), term="average")
F_4 = FuzzySet(function=Triangular_MF(a=65, b=75, c=85), term="warm")
F_5 = FuzzySet(function=Triangular_MF(a=80, b=90, c=90), term="hot")
FS.add_linguistic_variable("T", LinguisticVariable([F_1, F_2, F_3, F_4, F_5], concept="temperature", universe_of_discourse=[0, 90]))

# Define output fuzzy sets and linguistic variable
T_1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=100), term="little")
T_2 = FuzzySet(function=Triangular_MF(a=50, b=125, c=200), term="a little")
T_3 = FuzzySet(function=Triangular_MF(a=150, b=225, c=300), term="average")
T_4 = FuzzySet(function=Triangular_MF(a=250, b=325, c=400), term="much")
T_5 = FuzzySet(function=Triangular_MF(a=350, b=425, c=425), term="very much")
FS.add_linguistic_variable("w", LinguisticVariable([T_1, T_2, T_3, T_4, T_5], universe_of_discourse=[0, 425]))

# Define fuzzy rules
R1 = "IF (G IS dry) OR (T IS hot) THEN (w IS very much)"
R2 = "IF (G IS dry) AND (T IS warm) THEN (w IS much)"
R3 = "IF (G IS dry) AND (T IS average) THEN (w IS much)"
R4 = "IF (G IS dry) AND (T IS cool) THEN (w IS a little)"
R5 = "IF (G IS dry) AND (T IS cold) THEN (w IS little)"
R6 = "IF (G IS average) AND (T IS hot) THEN (w IS much)"
R7 = "IF (G IS average) AND (T IS warm) THEN (w IS average)"
R8 = "IF (G IS average) AND (T IS average) THEN (w IS average)"
R9 = "IF (G IS average) AND (T IS cool) THEN (w IS a little)"
R10 = "IF (G IS average) AND (T IS cold) THEN (w IS little)"
R11 = "IF (G IS wet) AND (T IS hot) THEN (w IS average)"
R12 = "IF (G IS wet) AND (T IS warm) THEN (w IS a little)"
R13 = "IF (G IS wet) AND (T IS average) THEN (w IS a little)"
R14 = "IF (G IS wet) AND (T IS cool) THEN (w IS little)"
FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14])

# Set antecedents values
FS.set_variable("G", 40)
FS.set_variable("T", 30)

# Perform Mamdani inference and print output
print(FS.Mamdani_inference(["w"]))
