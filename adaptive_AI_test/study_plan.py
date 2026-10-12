def generate_study_plan(ability):
    
    if ability < 0.3:
        return "Focus on basic arithmetic and algebra fundamentals."

    elif ability < 0.6:
        return "Practice medium difficulty algebra and calculus problems."

    else:
        return "Work on advanced GRE-level quantitative reasoning questions."