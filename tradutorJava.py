import pytesseract as ocr
ocr.pytesseract.tesseract_cmd = r"C:\Users\user\AppData\Local\Tesseract-OCR\tesseract.exe"
from PIL import Image

normal = 0
isAttribute= isGet = 1
isMethod= isSet = 2

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

def methodClassifier(method): #classifies methods in get e set 
    if (method[:3]=='get'):
        return isGet
    if (method[:3]=='set'):
        return isSet
    else:
        return normal

def getAndSetWriter(methodName,methodType):
    parameter = methodName[3].lower() + methodName[4:]
    #print(parameter)
    if methodType == isGet:
        return ('  return this.'+ parameter +";")
    if methodType == isSet:
        return ('  this.'+ parameter +" = "+ parameter +";")

def variableWriter(variable): #"translates" variable name 
    variableDiv = variable.rsplit(":") #split the variable phrase into what comes before and after ":"
    newVariable = variableDiv[1] +" " +variableDiv[0] #invert position
    return newVariable


def attributeWriter(attributes): #write every attribute
    for attribute in attributes:
        print('private' + variableWriter(attribute)+";\n") #Write as private and add ";"


def methodsWriter(methodsConjunction):  #Write every attribute
   
    for method in methodsConjunction: #take methods one by one
        function ='' 
        parameters='' 
        methodName = method.rpartition("(")[0].replace(" ","") #get string before "("
        methodClassification = methodClassifier(methodName)
            
    
        methodReturn = method.rpartition(")")[2].rpartition(":")[2] #get string inside parentheses
        parametersList = method.rpartition("(")[2].rpartition(")")[0].rsplit(",") #get what is inside parentheses and then separate parameters

        if(methodClassification != normal):
                   
           function = getAndSetWriter(methodName,methodClassification)          

        if len(parametersList[0])>= 2: #if there is a parameter       
            
                
            for parameter in parametersList:
                parameters = variableWriter(parameter)+ ","+parameters
            if parameters[len(parameters)-1] ==',': #if the last character is ','
                parameters=parameters[:-1]

        methodCode = "public "+methodReturn+" " +methodName + "(" + parameters + "){\n"+function+"\n}\n" #concatenate method String
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
    