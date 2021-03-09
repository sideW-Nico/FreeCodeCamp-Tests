from io import UnsupportedOperation

from typing_extensions import TypeAlias


def arithmetic_arranger(problems, showResult = False):
    
    stringValues1 = str()
    stringValues2 = str()
    stringDashes = str()
    results = str()
        
        
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        splitProblem = problem.split()
        
        firstValue = splitProblem[0]
        secondValue = splitProblem[2]
        operator = splitProblem[1]
        
        lengthV1 = len(firstValue)
        lengthV2 = len(secondValue)
        
        maxLength = max(lengthV1, lengthV2) + 2
        spacing = " " * 4
        
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        if firstValue.isdigit() == False or secondValue.isdigit() == False:
            return "Error: Numbers must only contain digits."
        if lengthV1 > 4 or lengthV2 > 4:
            return "Error: Numbers cannot be more than four digits."
        
        stringValues1 += (" " * (maxLength - lengthV1)) + firstValue + spacing
        stringValues2 += operator + (" " * ((maxLength-1)- lengthV2)) + secondValue + spacing 
        stringDashes += "-" * maxLength + spacing
        
        if showResult:
            arithmeticOperation = None
            
            if operator == "+":
                arithmeticOperation = str(int(firstValue) + int(secondValue))
            else:
                arithmeticOperation = str(int(firstValue) - int(secondValue))
                
            results += " " * (maxLength - len(arithmeticOperation)) + arithmeticOperation + spacing
            

    arranged_problems = stringValues1.rstrip() + "\n" + stringValues2.rstrip() + "\n" + stringDashes.rstrip()
    
    if showResult: arranged_problems += "\n" + results.rstrip()
        
    return arranged_problems

