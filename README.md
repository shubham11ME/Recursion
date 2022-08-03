# Recursion
Find the solution of problem related to Recursion.

In this repo I'' share the problem and solution related to Recursion.

--> What is Recursion?
-- A way of solving a problem by having a function calling itself.
-- or a method of solving a problem where solution depends on the solution to the similar instances of same problem.
-- such problem can be solve by attration as well.
-- Real life example - Russian Nesting Doll

--> Property of Recursion?
--1. Performing the same operation multiple time with different input.
--2. In every step we try smaller input to make the problem smaller.
--3. Base condition is needed to stop the recursion, otherwise infinite loop will occur.

--> Why Recursion?
--1. Recursive thinking is very important in programming and it helps you breaks down the big problem into smaller ones and easier to use.
 - It's simpler to Iterative(like loops) way of programming.
-- If recursion is easy to use then we can use recursion over the iterative one.
Ans. No, because there are situation where iteration performs faster than recursion, so it's depends on situation.

--> When to choose Recursion?
Ans. if you can divide the problem into similar sub problems, then you can use recursion.
-- ** problem must be similar, otherwise recursion can't be useful.
	> if you can divide the problem into similar sub problems
	> Design an algorithm to compute nth...
	> write code ot list the n...
	> Implement a method to compute all.
	> Practice
--2. the prominent usage of recursion in data strctures like trees and graphs.
--3. Interviews
--4. It is used in many algorithms (divide and conquer, greedy and dynamic programming)

--> When to use/avoid Recursion?
1.	When to use it :-
•	When a problem can easily breakdown into similar sub problems.
•	When we are fine with extra overhead (both time and space) that comes with it.
Example: if we are developing a mobile application that will run on low and high memory device as well, so in this case recursion is not advisable. But if you are developing algorithm for critical system, which must be so fast, like airbag system in the car, only a fraction of second matter, you must avoid using recursion.
•	When we need a quick working solution instead of efficient one.
•	When traverse a tree
•	When we use memorization in recursion.
2.	When to avoid it: -
•	All the opposite case of upper cases.
•	If time and space complexity matter for us.
•	Recursion uses more memory. If we use embedded memory. For example, an application that takes more memory in the phone is not efficient.
•	If not implemented correctly, then Recursion can be slow.

--> How to write Recursion in 3 steps:
Step 1: Recursive case – the flow
Step 2: Base case – stopping criterion
Step : Unintentional case – the constraint


