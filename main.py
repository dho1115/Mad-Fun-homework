if __name__ == "__main__":
    from functions import absoluteValue, roundedNumber, squareRoot, Calculator, PlayAgain

    DecimalInput = input("Enter a decimal number.");
    try:
        floatNumber = float(DecimalInput);
        isDecimal = isinstance(floatNumber, float);
        print(dict(absoluteValue=absoluteValue(floatNumber), roundedNumber=roundedNumber(floatNumber), squareRoot=squareRoot(floatNumber)));
        '''
        BONUS!!! CALCULATOR FEATURE.
        '''
        tryCalculator = input("Do you want to try the calculator? ");
        if tryCalculator.lower() == 'y': print(PlayAgain());
        else: print("="*7 + "thank you for playing!!!".title() + "="*7);
    
    except ValueError:
        print(ValueError);
        print(f"Sorry... but {DecimalInput} is not a decimal.")
        