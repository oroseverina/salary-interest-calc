#Severina Oro

output_file = open("output.txt","w")

def main():
    file_not_open = "T"
    file_name = input ("Please enter name of file: ")
    while file_not_open == "T":
        try: #try block for opening a file that might be invalid 
            variable_file = open (file_name, "r")
            file_not_open = "F"
        except FileNotFoundError:
            print("Invalid file name was entered.")
            file_name=input ("Please enter a different file name: ")
    line = variable_file.readline()

    while line !="":
        principle,rate,compound,years= line.split(",")
        try: #try block for converting string to number
            principle= float(principle)
            rate = float(rate)/100
            compound= float (compound)
            years= float(years)
            Newr=rate
    #if statements allow for the different incentives from the bank to be added to the final amount
            if principle>= 5000 and principle<= 10000:
                Newr = Newr + 0.005                  
            elif principle>= 10001 and principle<= 50000:
                Newr= Newr + 0.0075                                                            
            elif principle>= 50000:
                Newr = Newr + 0.01
            Amount = calc_amount (principle, Newr, compound, years)
            if years>= 10 and rate>= 0.05:
                Amount = Amount + (principle*0.01*years)
            if rate > 0.10:
                Amount = Amount + 50.00
            output_file.write("After "+str(years) + " years, the amount is $"+str(format (Amount,',.2f'))+"\n")

        except ValueError:
            print("Invalid Data was read from the input file.")
            
        line= variable_file.readline()   


    variable_file.close()
    output_file.close()
        
def calc_amount(p,r,n,t): #this function calculates the amount of money in the bank account after a specific amount of time
    Newr=r
    A = p*(1+(Newr/n))**(n*t)    
    return A

main()

        
        
    
    

    
            
    
    
