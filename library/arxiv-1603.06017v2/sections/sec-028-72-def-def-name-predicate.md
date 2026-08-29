---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-028-72-def-def-name-predicate
section_title: "def: def <name> <predicate>"
section_number: 7.2
pages: 26-27
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
The word def stands for deﬁne. The syntax for this command is exactly the same as the syntax for eval command. The only
difference between this command and eval is that the automaton constructed is saved in the directory “/Walnut/Automata
Library/” for later use. Suppose we write the following:
def sum10 "x + y = 10" ;
This creates as usual the ﬁles sum10.gv, sum10.txt, and sum10_log.txt in the directory “/Walnut/Result/”. However, it also
saves a copy of sum10.txt in the directory “/Walnut/Automata Library/”. Any automaton saved in this directory can be called
in other predicates by referring to its name and the special character $. To learn about calling see Sections 3.7 and 4.5.
Let us see examples of predicates calling the automaton sum10:
eval lessThanThree "Ea a >=8&$sum10(b,a)" ;
This predicate is satisﬁed by numbers b for which there exist an a >=8 such that b + a = 8, i.e., 0,1,2:
Figure 7.7: lessThanThree.gv
We can send the same variable to both arguments of sum10:
eval
five "$sum10(a,a)" ;
Figure 7.8: ﬁve.gv
We can send constants to any arguments of sum10:
eval three "$sum10(7,a)" ;
Figure 7.9: three.gv
Indeed, we can send any arithmetic expressions or predicates with one free variable to arguments:
eval three "$sum10(a −2,3∗a)" ;
eval three "Eb $sum10(a,b +3 = 10)" ;
26
The resulting automaton for both of these is depicted in Figure 7.9. We can call sum10 to deﬁne new automata:
def threeSum10 "$sum10(x + y,z)" ;
Now we can write
eval three "Ey,z $threeSum10(x, y,z)& y = 2& z = 5" ;
The result of this evaluation is again depicted in Figure 7.9.
Now look at the following example:
eval nonsense "$sum10(a = b,4)" ;
argument 1 of function sum10 cannot be an automaton with != 1 inputs
: char at 1
:
eval nonsense "$sum10(a = b,4)" ;
This is because the ﬁrst argument is a predicate with two free variables.
We cannot send a variable in lsd_2 to an automaton that accepts only msd_2, and expect getting anything interesting in
return. The following example would run ﬁne, but the result is another nonsense:
eval another_nonsense "?lsd_2 $sum10(x,4)" ;
Figure 7.10: another_nonsense.gv
The number of arguments when calling an automaton should match the number of inputs of that automaton:
eval invalid "$sum10(x, y,z)" ;
function sum10 requires 2 arguments
: char at 1
:
eval invalid "$sum10(x, y,z)" ;
Always remember the roles of the inputs to an automaton created by the def command. For example, look at the following
examples of the def command:
def f1 "y < x" ;
def f2 "x < y" ;
Now the following evaluates to an automaton accepting representations of numbers > 1:
eval greater_than_1 "$f1 (a ,1) " ;
whereas the following evaluates to an automaton accepting representations of numbers < 1:
eval less_than_1 "$f2 (a ,1) " ;
This is because f1 is an automaton for which the ﬁrst argument is greater than the second argument, whereas, f2 is an
automaton for which the ﬁrst argument is less than the second argument. Always remember that Walnut sorts inputs of an
automaton based on their labels’ lexicographic order.
7.3
