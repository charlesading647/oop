# I am creating the class called Learners
class Learners:
    def __init__(self, name, age, goal):
        self.name = name
        self.age = age
        self.goal = goal

    def introduce(self):
        return f"Habari jina langu ni {self.name} nina miaka {self.age} na ndoto yangu ni kuwa {self.goal}."

charles = Learners ("Charles", 19, "Ethical hacker")
safari = Learners ("safari", 22, "Goalkeeper")

print(charles.introduce())
print(safari.introduce())