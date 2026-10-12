from database import questions_collection

questions = [

{
"question":"What is 2 + 2?",
"options":["2","3","4","5"],
"correct_answer":"4",
"difficulty":0.1,
"topic":"Arithmetic"
},

{
"question":"What is 5 × 6?",
"options":["30","35","25","20"],
"correct_answer":"30",
"difficulty":0.2,
"topic":"Arithmetic"
},

{
"question":"What is 9 + 8?",
"options":["16","17","18","15"],
"correct_answer":"17",
"difficulty":0.2,
"topic":"Arithmetic"
},

{
"question":"What is 15 - 7?",
"options":["6","7","8","9"],
"correct_answer":"8",
"difficulty":0.2,
"topic":"Arithmetic"
},

{
"question":"Solve: 2x + 4 = 10",
"options":["2","3","4","5"],
"correct_answer":"3",
"difficulty":0.3,
"topic":"Algebra"
},

{
"question":"Solve: x + 7 = 12",
"options":["4","5","6","7"],
"correct_answer":"5",
"difficulty":0.3,
"topic":"Algebra"
},

{
"question":"Solve: 3x = 15",
"options":["3","4","5","6"],
"correct_answer":"5",
"difficulty":0.3,
"topic":"Algebra"
},

{
"question":"What is 12 × 4?",
"options":["36","48","42","40"],
"correct_answer":"48",
"difficulty":0.3,
"topic":"Arithmetic"
},

{
"question":"Solve: x² = 16",
"options":["2","3","4","5"],
"correct_answer":"4",
"difficulty":0.4,
"topic":"Algebra"
},

{
"question":"What is 25 ÷ 5?",
"options":["4","5","6","7"],
"correct_answer":"5",
"difficulty":0.4,
"topic":"Arithmetic"
},

{
"question":"Derivative of x²?",
"options":["x","2x","x²","1"],
"correct_answer":"2x",
"difficulty":0.5,
"topic":"Calculus"
},

{
"question":"Derivative of 5x?",
"options":["5","x","1","0"],
"correct_answer":"5",
"difficulty":0.5,
"topic":"Calculus"
},

{
"question":"Integral of 1/x?",
"options":["ln(x)","x","x²","1/x"],
"correct_answer":"ln(x)",
"difficulty":0.6,
"topic":"Calculus"
},

{
"question":"What is 7²?",
"options":["49","42","36","56"],
"correct_answer":"49",
"difficulty":0.5,
"topic":"Algebra"
},

{
"question":"Solve: 4x + 8 = 24",
"options":["2","3","4","5"],
"correct_answer":"4",
"difficulty":0.6,
"topic":"Algebra"
},

{
"question":"What is the square root of 81?",
"options":["7","8","9","10"],
"correct_answer":"9",
"difficulty":0.6,
"topic":"Algebra"
},

{
"question":"What is 13 × 7?",
"options":["81","91","101","87"],
"correct_answer":"91",
"difficulty":0.7,
"topic":"Arithmetic"
},

{
"question":"Derivative of x³?",
"options":["3x²","x²","2x","x³"],
"correct_answer":"3x²",
"difficulty":0.7,
"topic":"Calculus"
},

{
"question":"Integral of x?",
"options":["x²/2","x²","2x","ln(x)"],
"correct_answer":"x²/2",
"difficulty":0.8,
"topic":"Calculus"
},

{
"question":"Solve: x² + 4 = 20",
"options":["2","3","4","5"],
"correct_answer":"4",
"difficulty":0.9,
"topic":"Algebra"
}

]

questions_collection.insert_many(questions)

print("20 Questions inserted successfully!")