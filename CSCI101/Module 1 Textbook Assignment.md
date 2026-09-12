# Module 1 - Textbook Assignment


### On a normal day, most people perform several algorithms without even noticing. Describe 2 algorithms you perform on your typical day.  Think about the details of the steps involved and write out the steps in any convenient notation.


*Prepare Breakfast*
- Open freezer
- Pull out individually wrapped breakfast sandwich
- Close freezer
- Remove sandwich from plastic
- Wrap sandwich in paper towel
- Place sandwich in microwave
- Press 'Defrost'
- Set weight to 0.6
- Press 'Start' (will cook for 1 min 48 sec)
- Remove sandwich from microwave
- Unwrap sandwich from paper towel
- Place sandwich on plate
- Wait until sandwich not lava (cool enough to handle safely)
- Eat sandwich

*Start Work Day*
- Open laptop
- Type password
- Open Outlook
- Check emails
- Any emails that need responses?
    - If so, respond
- Any emails that need action?
    - If so, flag for later
- Open Teams
- Any messages that need responses?
    - If so, respond
- Open Slack
- Any messages that need responses?
    - If so, respond
        

### How do the 2 processes you described meet the criteria for algorithms presented in Chapter 1 of the book?

Though both algorithms above are given in a precise order, clearly have a stopping point, and produce a result, the steps of the Prepare Breakfast algorithm are closer to true primitives - each step could be done by anyone who can reach the freezer and microwave, and do not require further knowledge or explanation. My second example for starting my work day would require prior knowledge of the password, how to operate the laptop, what criteria emails or messages need to meet that would warrant a response or a flag, and knowledge of how to handle responding or flagging.

---

### A heuristic is a concept related to an algorithm in computer science. It generally describes a technique that finds an approximate solution to a problem in order to speed up finding an answer. How could you turn the addition algorithm from figure 1.2 into a heuristic that finds an approximate answer faster?  How does your process differ from the algorithm?

A good way to turn the addition algorithm into a heuristic is to lessen the number of digits in the given numbers 'a' and 'b' that are precisely added and carried to the next iteration. Keep only the first two or three digits and change the remaining digits to 0. 
For example: 75683 + 45224 becomes 75000 + 45000 (rounding could be used for a slight bit more accuracy)
This differs from the algorithm by only caring about the first few digits that contribute *most* to the final sum - which is what we do in our heads a lot for approximating numbers when we don't need a precise answer. The value of 'm' could be 2 or 200, and the time to add 'a' and 'b' would be the same

---

### Below is an algorithm for refilling paper in a printer. For each step in the algorithm state whether the instruction is ambiguous and why or why not

- Pull the paper tray completely out of the machine. 
    - *Ambiguous - Does specify whether the tray should remain attached to the machine*
- Press and slide the paper guides to fit the paper. 
    - *Ambiguous - Does not specify how to adjust the paper guides or what 'fit the paper' means in terms of alignment or spacing.*
- Fan the stack of paper well. 
    - *Ambiguous - I am not even sure exactly what is meant by 'fan' here or what qualifies as 'well'*
- Load the paper in the paper tray with the printing surface face down. 
    - *Ambiguous - Does not specify which side of the paper is the printing surface, which could lead to incorrect loading.*
- Make sure the paper is below the maximum paper mark (v v v). 
    - *Good - Shows what the 'maximum paper mark' looks like to avoid confusion*
- Slowly push the paper tray completely into the machine. 
    - *Ambiguous - 'Slowly' is subjective, and no information is given as to what will signify that they tray is 'completely' pushed into the machine*
- Lift the support flap to prevent the paper from sliding off the output tray. 
    - *Ambiguous - Does not specify how high to lift the support flap or how to ensure that the paper does not slide off the output tray.*

---

### There are three basic types of algorithmic operations (sequential, iterative, and conditional).  For each of the algorithm steps below identify what type of operation it is.

Get the 6 lotto number picks from the user. *sequential* *COULD be iterative if you are asking 6 individual times*
Test the 6 numbers to see if they match the winning numbers for the week. *iterative & conditional*
Award the prize to the winner. *sequential*
Repeat for each of the lotto number picks. *iterative*

---

### The algorithm for converting from decimal to hexadecimal is as follows
1. Get the decimal number
2. Set i = 0
3. repeat steps 4 - 7 until the number is equal to 0
4. Take the modulus (find the remainder) of the number and 16 and store the answer in ai 
5. If ai >= 10, change ai to the appropriate hex digit (10 = A, 11 = B, 12 = C, 13 = D, 14 = E, 15 = F)
6. Divide the number by 16 
7. Increment i by 1
Print ai-1, ai-2, . . . a1, a0

#### Trace through the algorithm for the number 432.  Show what steps are executed and in what order.  Show what the value of each known "a" value is at each step.

                                  i = 0          i = 1              i = 2            i = 3
```
input num                   //num = 432     
i = 0                       //i = 0       
a = []                      //a = []       
while num != 0:             //true          //true            //true            //false - exit loop
    ai = num % 16           //ai = 0        //ai = 11         //ai = 1
    if ai >= 10:            //false         //true            //false
        ai = tohex(ai)                      //ai = B        
    num = num/16            //num = 27      //num = 1         //num = 0
    i++                     //i = 1         //i = 2           //i = 3
    a.append(ai)            //a = [0]       //a = [0,B]       //a = [0,B,1]

print (reverse(a))                                                              //print 1 B 0
```
