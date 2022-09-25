"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes>0:
        list = []
        count = 0
        i = 2
        x = 2 
        while len(list)!=number_of_primes:
            while x>0:
                y = i%x
                if y==0:
                    count +=1
                x -= 1
            if count<3:
                list.append(i)
            count=0
            i+=1
            x = i
        # for value in list:
        #     print(f'{value}')
        return list
