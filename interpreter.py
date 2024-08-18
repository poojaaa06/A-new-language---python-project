

import sys

class FlagLangInterpreter:
    def __init__(self):
        self.variables = {}

    def flagrate(self, value):
        sys.stdout.write(value + '\n')

    def interpret(self, code):
        lines = code.split('\n')
        condition_satisfied = False
        for line in lines:
            line = line.strip()
            if line.startswith("flagrate"):
                value = line.split("(", 1)[1].split(")")[0].strip()
                self.flagrate(value)
            elif line.startswith("alohomora"):
                params = line.split("(", 1)[1].split(")")[0].split(",", 1)
                condition = params[0].strip()
                message = params[1].strip()[1:-1]  # Extract the message
                if condition:
                    # Replace logical operators with their Python equivalents
                    condition = condition.replace("verum", "and").replace("autem", "or")
                    condition_satisfied = eval(condition)
                    if condition_satisfied:  # Only print if condition is met
                        self.flagrate(message)
            elif line.startswith("periculum"):
                if not condition_satisfied:
                    params = line.split("(", 1)[1].split(")")[0].split(",", 1)
                    condition = params[0].strip()
                    message = params[1].strip()[1:-1]  # Extract the message
                    if condition:
                        # Replace logical operators with their Python equivalents
                        condition = condition.replace("verum", "and").replace("autem", "or")
                        condition_satisfied = eval(condition)
                        if condition_satisfied:  # Only print if condition is met
                            self.flagrate(message)

            elif line.startswith("colloportus"):
                if not condition_satisfied:
                    value = line.split("(", 1)[1].split(")")[0].strip()
                    self.flagrate(value)
                # Reset the condition after printing the message in alohomora
                condition_satisfied = False
            elif line.startswith("accio"):
                params = line.split("(", 1)[1].split(")")[0].split(",", 1)
                var_name = params[0].strip()
                value = params[1].strip()
                self.variables[var_name] = value
                # Print the assigned value
                self.flagrate("Value assigned to " + var_name + ": " + value)
            elif line.startswith("alohomora"):
                params = line.split("(", 1)[1].split(")")[0].split(",", 1)
                condition = params[0].strip()
                message = params[1].strip()[1:-1]  # Extract the message
                if condition:
                    # Replace logical operators with their Python equivalents
                    condition = condition.replace("verum", "and").replace("autem", "or")
                    condition_satisfied = eval(condition)
                    if condition_satisfied:  # Only print if condition is met
                        self.flagrate(message)
            elif line.startswith("periculum"):
                if not condition_satisfied:
                    params = line.split("(", 1)[1].split(")")[0].split(",", 1)
                    condition = params[0].strip()
                    message = params[1].strip()[1:-1]  # Extract the message
                    if condition:
                        # Replace logical operators with their Python equivalents
                        condition = condition.replace("verum", "and").replace("autem", "or")
                        condition_satisfied = eval(condition)
                        if condition_satisfied:  # Only print if condition is met
                            self.flagrate(message)
            elif line.startswith("colloportus"):
                if not condition_satisfied:
                    value = line.split("(", 1)[1].split(")")[0].strip()
                    self.flagrate(value)
                # Reset the condition after printing the message in alohomora
                condition_satisfied = False
            elif line.strip().startswith("accio"):
                # Extract the variable name and value inside reparo()
                parts = line.split("(", 1)[1].split(",", 1)
                var_name = parts[0].strip()
                value = parts[1].split(")")[0].strip()
                self.variables[var_name] = value
            elif line.startswith("reducto"):
                params = line.split("(", 1)[1].split(")")[0].split(",", 1)
                var_name = params[0].strip()
                value1, value2 = map(int, params[1].strip().split("et"))
                result = value1 - value2
                self.variables[var_name] = result
                self.flagrate("Result of reducto: " + str(result))
            elif line.startswith("gemino"):
                params = line.split("(", 1)[1].split(")")[0].split(",", 1)
                var_name = params[0].strip()
                value1, value2 = map(int, params[1].strip().split("et"))
                result = value1 * value2
                self.variables[var_name] = result
                self.flagrate("Result of gemino: " + str(result))
            elif line.startswith("diffindo"):
                params = line.split("(", 1)[1].split(")")[0].split(",", 1)
                var_name = params[0].strip()
                value1, value2 = map(int, params[1].strip().split("et"))
                result = value1 / value2
                self.variables[var_name] = result
                self.flagrate("Result of diffindo: " + str(result))
            elif line.strip().startswith("expecto_patronum"):
                # Extract the variable name inside expecto_patronum()
                var_name = line.split("(", 1)[1].split(")")[0].strip()
                num = int(self.variables.get(var_name, 0))  # Get the value of the variable
                for i in range(num):
                    self.flagrate("Expecto Patronum!")
            
            

                

