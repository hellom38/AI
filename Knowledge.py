import random
""" SYSTEM:

P Q R
∧ ¬ ∨ ⊨ ⊢ → ↔

P = say hi
Q = running
R = raining
1. I say hi to Jon only if he is not running , ¬Q → P
2. If it is raining Jon will not run R → not Q
3. It is raining R


Formula: ""
"""

rotating_variables = ["P", "Q", "R"]

class Variable:
    def __init__(self,name,assigned_value = None):
        if not assigned_value:
            self.assigned_value = random.choice(rotating_variables)
            rotating_variables.remove(self.assigned_value)
        else:
            self.assigned_value = assigned_value
        self.name = name
    
class Premise:
    def __init__(self,premise=""):
        self.premise = premise


class Symbol:
    def __init__(self,firstval,secondval):
        self.firstval = firstval
        self.secondval = secondval

class Not:
    def __init__(self, val):
        self.val = val
    
    def __str__(self):
        return f'¬{self.val}'
        
class Conjunction(Symbol):
    def __str__(self):
        return f'{self.firstval} ∧ {self.secondval}'

class Disjunction(Symbol):
    def __str__(self):
        return f'{self.firstval} ∨ {self.secondval}'

class Conditional(Symbol):
    def __str__(self):
        return f'{self.firstval} → {self.secondval}'

class Biconditional(Symbol):
    def __str__(self):
        return f'{self.firstval} ↔ {self.secondval}'


raining = Variable("Raining","P")
jon_running = Variable("Jon is running","Q")
say_hi = Variable("Say hi to Jon","R")

first = Premise(raining)
second = Premise(Conditional(raining,Not(jon_running)))
third = Premise(Biconditional(Not(jon_running),say_hi))

    