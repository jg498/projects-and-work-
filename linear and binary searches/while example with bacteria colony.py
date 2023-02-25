time = 0 
population= 1000 
growth_rate = 0.21 
while population < 2000:
    population = (population + growth_rate * population) 
    print (population)
    time =  (time + 1) 
print ("It took %d minutes for the bacteria to double." %time)
print ( "The final population was %6.2f bacteria." % population)

