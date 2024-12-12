from math import sqrt;

absoluteValue = lambda num: abs(num);
roundedNumber = lambda num, roundedTo=0: round(num, roundedTo);
def squareRoot(num, default=False):
   if not default:
      return sqrt(round(abs(num)));
   else:
      return sqrt(num);

'''
======= EXTRA THAT IS NOT A PART OF THE HOMEWORK!!! =====
'''
DictionaryOfFunctions = dict(absoluteValue= absoluteValue, roundedNumber=roundedNumber, squareRoot=squareRoot); #All available functions. Add any new math functions here as key - value pair.

def Calculator(num:float, desiredOperations:list, DictionaryOfFunctions:dict=DictionaryOfFunctions):
   calculatedResults = [dict(x = DictionaryOfFunctions.get(x)(num)) for x in desiredOperations];

   return dict(num=num, DictionaryOfFunctions=DictionaryOfFunctions, desiredOperations=desiredOperations, calculatedResults=calculatedResults);

def PlayAgain(Calculator=Calculator, DictionaryOfFunctions=DictionaryOfFunctions):
   decimal = input("Enter Another Number... ");
   operationsEntered = [];

   try:
      if not isinstance(float(decimal), float): raise ValueError();
      decimal = float(decimal);
      roundedTo = None;
      done = "n";

      while (done == "n"):
         NewOperation = input("Enter an operation.");
                     
         if DictionaryOfFunctions.get(NewOperation): operationsEntered = [*operationsEntered, NewOperation];
         else: raise Exception();
                        
         done = input("Are you done (y/n)?")

      return Calculator(decimal, operationsEntered)
   except ValueError:
      print(ValueError);
      return f"Sorry, but your number must be a number!!!";
   except Exception:
      return f"Sorry... but the operation you entered, {NewOperation} must be within {DictionaryOfFunctions.keys()}...."
   

