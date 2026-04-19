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
stored_premises = []
stored_variables = []
class Variable:
    def __init__(self,name,assigned_value = None):
        if assigned_value is None:
            self.assigned_value = random.choice(rotating_variables)
            rotating_variables.remove(self.assigned_value)
        else:
            self.assigned_value = assigned_value
        self.name = name
        self.store()
    
    def store(self):
        stored_variables.append(self)
    def __str__(self):
        return self.name
    
class Premise:
    def __init__(self,premise=""):
        self.premise = premise
        self.store()
    
    def store(self):
        stored_premises.append(self)
    
    def __str__(self):
        return self.premise

    


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

class Table_of_truth:

    def __init__(self, table="",variables="",premises=""):
        if table:
            self.truth_table = table

        else:
            self.truth_table = {}
        
        self.generate_table_variables(variables)
        self.generate_table_operators(premises)


    def check_operators(self,premise,truth_table_premises={},truth_table_basepremises={}):
        x_list = {}
        premival = premise.premise
        if isinstance(premival,Symbol):
            #if True:
            if not isinstance(premival.firstval,Symbol) and not isinstance(premival.firstval,Not) and not isinstance(premival.secondval,Symbol) and not isinstance(premival.secondval,Not):
                if premival.__class__ == Conjunction:
                    for i in self.truth_table["Variables"][premival.firstval]:
                        firstval = self.truth_table["Variables"][premival.firstval][i]
                        secondval = self.truth_table["Variables"][premival.secondval][i]
                        if firstval == True and secondval == True:
                            x_list.update({
                                i : True
                            })
                        else:
                            x_list.update({
                                i : False
                            })
                if premival.__class__ == Disjunction:
                    for i in self.truth_table["Variables"][premival.firstval]:
                        firstval = self.truth_table["Variables"][premival.firstval][i]
                        secondval = self.truth_table["Variables"][premival.secondval][i]
                        if firstval == True or secondval == True:
                            x_list.update({
                                i : True
                                })
                        else:
                            x_list.update({
                                i : False
                            })
                if premival.__class__ == Conditional:
                    for i in self.truth_table["Variables"][premival.firstval]:
                        firstval = self.truth_table["Variables"][premival.firstval][i]
                        secondval = self.truth_table["Variables"][premival.secondval][i]
                        if firstval == True and secondval == False:
                            x_list.update({
                                i : False
                            })
                        else:
                            x_list.update({
                                i : True
                            })
                if premival.__class__ == Biconditional:
                    for i in self.truth_table["Variables"][premival.firstval]:
                        firstval = self.truth_table["Variables"][premival.firstval][i]
                        secondval = self.truth_table["Variables"][premival.secondval][i]
                        if (firstval == True and secondval == True) or (firstval == False and secondval == False):
                            x_list.update({
                                i : True
                            })
                        else:
                            x_list.update({
                                i : False
                            })
                return truth_table_premises.update({ premise : x_list})
            else:
                smallest_child = premival
                while isinstance(smallest_child.firstval,Symbol) or isinstance(smallest_child.secondval, Symbol):
                    if isinstance(smallest_child.firstval,Symbol):
                        smallest_child = smallest_child.firstval.child
                    
        else:
            if isinstance(premival,Not):
                    x_list.update({
                        "val" : False
                    })
            else:
                    x_list.update({
                        "val" : True
                    })
            
            return truth_table_basepremises.update({ premise : x_list})
            
                
            


    def generate_table_variables(self,list_variables):
        truth_table_variables = {}
        num = 2**len(list_variables)
        for counter,x in enumerate(list_variables, start=1):  
            num_swaps = int(num/(2**counter))
            print(num_swaps)
            x_list = {}
            var_counter = 0
            print(num)
            while len(x_list) != num:
                for i in range(num_swaps*var_counter, num_swaps*(var_counter+1)):
                    x_list.update({
                        i : False
                    })
                var_counter += 1

                for i in range( num_swaps*var_counter, num_swaps*(var_counter+1)):
                    x_list.update({
                        i : True
                    })
                
                var_counter += 1

            
            truth_table_variables.update({x : x_list})
        self.truth_table.update({"Variables" : truth_table_variables})

    def generate_table_operators(self,list_premises):
        truth_table_premises = {}
        for x in list_premises:
            print("list:",x.premise)
            truth_table_premises = self.check_operators(x)
        self.truth_table.update({"ComplexPremises" : truth_table_premises})
        self.truth_table.update({"BasePremises" : truth_table_premises})



raining = Variable("Raining","P")
jon_running = Variable("Jon is running","Q")
say_hi = Variable("Say hi to Jon","R")

first = Premise(raining)
second = Premise(Conditional(raining,Not(jon_running)))
third = Premise(Biconditional(Not(jon_running),say_hi))
truthtable = Table_of_truth(variables=stored_variables,premises=stored_premises)
