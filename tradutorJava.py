import pytesseract as ocr
ocr.pytesseract.tesseract_cmd = r"C:\Users\userName\AppData\Local\Tesseract-OCR\tesseract.exe"
from PIL import Image

isAttribute = 1
isMethod = 2

def lineSpliter(text): #Split the text into phrases
    phrases = text.splitlines()
    
    for space in phrases: #if there is any empty space inside the list, it is removed
        if len(space) <= 2:
            phrases.remove(space)
    return phrases


def phraseClassifier(phrase): #Classifies in attribute and method
    if phrase[0] == '-':
        return isAttribute

    if phrase[0] =='+':
        return isMethod


def variableWriter(variable): #"translates" variable name 
    variableDiv = variable.rsplit(":") #split the variable phrase into what comes before and after ":"
    newVariable = variableDiv[1] +" " +variableDiv[0] #invert position
    return newVariable


def attributeWriter(attributes): #write every attribute
    for attribute in attributes:
        print('private' + variableWriter(attribute)+";\n") #Write as private and add ";"


def methodsWriter(methodsConjunction):  #Write every attribute
    methods = []
    parameters= ''
    
    for method in methodsConjunction: #take methods one by one
         
        methodName = method.rpartition("(")[0] #get string before "("
        
    
        methodReturn = method.rpartition(")")[2].rpartition(":")[2] #get string inside parentheses
        parametersList = method.rpartition("(")[2].rpartition(")")[0].rsplit(",") #get what is inside parentheses and then separate parameters
        for space in parametersList: #if there is any empty space inside the list, it is removed
            if len(space) <= 2:
                parametersList.remove(space)
    
        if parametersList: #if there is a parameter
            parameters=''
            if  len(parametersList) == 1: #if only a parameter
                parameters = variableWriter(parametersList[0])
            else:
                for parameter in parametersList:
                    parameters = variableWriter(parameter)+ ","+parameters
                
                if parameters[len(parameters)-1] ==',': #if the last character is ','
                    parameters=parameters[:-1]

        methodCode = "public" +methodName + "(" + parameters + "){\n\n}\n" #concatenate method String
        print(methodCode)
    


def imageReader(): #translate image into a phrase    
    return (ocr.image_to_string(Image.open(r'image.png'), lang='por'))


if __name__ == '__main__':
    codeLines = lineSpliter (imageReader())

    attributesList = []
    methodsList = []


    for line in codeLines:  
        
        lineClassification =phraseClassifier(line)
        if lineClassification == isAttribute:
            line = line.replace("-","")
            attributesList.append( line)
            

        if lineClassification == isMethod:
            line = line.replace("+","")
            methodsList.append( line)
            
     
    attributeWriter(attributesList)
    methodsWriter(methodsList)
    