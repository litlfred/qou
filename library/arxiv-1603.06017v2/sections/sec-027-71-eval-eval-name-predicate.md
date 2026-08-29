---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-027-71-eval-eval-name-predicate
section_title: "eval: eval <name> <predicate>"
section_number: 7.1
pages: 22-26
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
This is the most important command in Walnut and it stands for “evaluate.” This command takes two arguments. The
ﬁrst argument is a name for the evaluation. Name of the evaluation starts with a letter and could contain alphanumerics
and underscore. The ﬁles generated as the result of the eval command, all share the name given in the ﬁrst argument. The
second argument is a predicate that we want to evaluate. Predicates are always placed between quotation marks. To see the
deﬁnition for predicates see Section 3.9. In this article we typeset predicates in math mode in LATEX. However, the reader
should note that this typesetting is different from the one they see in the terminal. Let us see an example:
eval four "a = 4" :
a = 4 : 4 states −3ms
total computation time : 3ms
This evaluates to an automaton with one binary input labeled a. This is the automaton (a) : a = 4. To learn about the notation
(a) : a = 4 see Section 2.4. The automaton accepts only if a is the most-signiﬁcant-digit-ﬁrst binary representation of 4, i.e., if
it belongs to 0∗100. This automaton is drawn and saved in the directory “/Walnut/Result/” in a ﬁle named four.gv as shown
in Figure 7.1. The graph drawing software Graphviz is required to open this ﬁle; see Section 6.
Figure 7.1: Content of the ﬁle four.gv
How does Walnut know to use the most-signiﬁcant-digit-ﬁrst binary system? Walnut defaults to msd_2 which is how we
show the most-signiﬁcant-digit-ﬁrst binary system in Walnut; see Section 2.2 to learn about this notation and to learn about
number systems in general. To explicitly mention msd_2 type:
eval four "?msd_2 a = 4" ;
Similarly, for the least-signiﬁcant-digit-ﬁrst binary type:
eval lsd_four "?lsd_2 a = 4" ;
22
Figure 7.2: lsd_four.gv
Here is another example, this time in lsd_3:
eval ternary_example "?lsd_3 a < 5" ;
Figure 7.3: ternary_example.gv
This automaton accepts exactly those words representing the numbers 0,1,2,3,and 4 in the least-signiﬁcant-digit ternary
base, i.e., 0∗,10∗,20∗,010∗,110∗respectively. Note the trailing zeros in the representations as opposed to the leading zeros in
a most-signiﬁcant-digit-ﬁrst (msd) number system. Also note that this automaton accepts the empty word. This is because
in the deﬁnition of number systems we agreed that the empty word represents 0.
Let us see an example of an automaton with 2 inputs:
eval two_inputs "b = a +1" ;
This constructs the automaton (a,b) : b = a+1 in which the ﬁrst input corresponds to a, and the second input corresponds to
b. Recall from Section 2.4 that Walnut uses lexicographic ordering on the name of variables when constructing automata. So,
for example, even though the ﬁrst variable that appears in b = a +1 is b, it corresponds to the second input in the automaton.
Figure 7.4: two_inputs.gv
Walnut generates two other ﬁles as the outcomes of the eval command which can also be found in the directory
“/Walnut/Result/”. For the evaluation two_inputs, these two ﬁles are named two_inputs_log.txt and two_inputs.txt and they
are both text ﬁles.
The ﬁle two_inputs_log.txt contains the details of the evaluation including the intermediate steps and the time each of
those steps took to complete. In our example, there are not many intermediate steps involved:
b = 2 : 3 states −0ms
total computation time : 0ms
File 1: two_inputs_log.txt
23
In addition to two_inputs_log.txt , another ﬁle with the name two_inputs_detailed_log.txt will be created if the command
ends in two colons instead of a colon or a semicolon.
The ﬁle two_inputs.txt contains the deﬁnition of the automaton in Figure 7.4:
1
msd_2 msd_2
2
0 0
3
0 0 −> 0
4
0 1 −> 1
5
1 1 −> 0
6
1 1
7
1 0 −> 1
File 2: two_inputs.txt
Line 1 indicates that the ﬁrst and the second inputs of the automaton are both in msd_2. The two states 0 and 1 in Figure
7.4 are declared in Lines 2 and 6. The ﬁrst zero in Line 2 refers to the state 0 and the second zero refers to its output. Likewise,
the ﬁrst one in Line 6 refers to the state 1 and the second one refers to its output. Note that the automaton for evaluation
two_inputs is not an automaton with output, however all automata are stored as automata with outputs in Walnut; see
Section 2.1. For an ordinary automaton, states with non-zero outputs are interpreted as ﬁnal states, and states with zero
outputs are interpreted as non-ﬁnal states. So here state 0 is non-ﬁnal, whereas state 1 is ﬁnal. Transitions for states 0 and 1
are declared in Lines 3-5 and 7 respectively. For example, state 0 on (0,0) transitions to itself, and on (0,1) transitions to state
1. Transitions not depicted are transitions to the dead state. For example, state 1 transitions to the dead state on every tuple
except (1,0). To learn more about deﬁnition of an automaton in text ﬁles and how to manually deﬁne automata in text ﬁles
see Section 8.1.
In Section 2.3, we talked about the Thue-Morse word. The Thue-Morse word’s corresponding automaton with output,
depicted in Figure 2.7, is deﬁned in directory “/Walnut/Word Automata Library/” in a ﬁle named T.txt. We can refer to the
Thue-Morse word in predicates by typing T . See Section 8.2 on how to deﬁne new automatic words in Walnut.
We talked about square subwords in the Thue-Morse word.
The following predicate is satisﬁed by (i,n) if
T [i..i +n −1] = T [i +n..i +2n −1], i.e., if there exists a square subword of length 2n starting at position i.
eval squares_in_thue_morse_word "n > 0&(Ak k < n =>T [i +k] = T [i +n +k])" ;
The order of a square is half its length. Now if we want to ﬁnd all natural numbers n for which there exists a square of order n
in the Thue-Morse word, we simply use the existential quantiﬁer E:
eval order_of_squares_in_thue_morse_word "Ei n > 0&(Ak k < n =>T [i +k] = T [i +n +k])" ;
Figure 7.5: order_of_squares_in_thue_morse_word.gv
Based on this automaton, the natural number n with msd_2 representation of the form 0∗(1|11)0∗is an order of a square in
the Thue-Morse word. In other words, the set of orders in the Thue-Morse word is
©
n : there exists k ≥0 such that n = 2k or n = 2k+1 +2kª
Overlaps are the words of the form axaxa where a is a symbol and x is any word, e.g., the word “alfalfa” in English is an
overlap. It is a known that the Thue-Morse word avoids overlaps. How do we make sure, using Walnut, that the Thue-Morse
word does not have any overlaps? The result of the following predicate must be the true automaton; see Section 5.1, if the
Thue-Morse does not have any overlaps:
24
eval thue_morse_does_not_have_overlaps "∼(Ei,n n > 0&(Ak k <=n =>T [i +k] = T [i +n +k]))" :
n > 0 : 2 states −1ms
k <= n : 2 states −1ms
T [(i +k)] = T [((i +n)+k)] : 12 states −6ms
(k <=n =>T [(i +k)] = T [((i +n)+k)]) : 25 states −1ms
(Ak(k <=n =>T [(i +k)] = T [((i +n)+k)])) : 1 states −27ms
(n > 0&(Ak(k <=n =>T [(i +k)] = T [((i +n)+k)]))) : 1 states −0ms
(Ei,n(n > 0&(Ak(k <=n =>T [(i +k)] = T [((i +n)+k)])))) : 1 states −1ms
∼(Ei,n(n > 0&(Ak(k <=n =>T [(i +k)] = T [((i +n)+k)])))) : 1 states −0ms
total computation time : 38ms
Figure 7.6: thue_morse_does_not_have_overlaps.gv
The automaton in Figure 7.6 is the true automaton. For more information see Section 5.1.
Note that if a predicate is not valid Walnut returns an error:
eval invalid "x + y + z" ;
the final
result of the evaluation
is not of type automaton
:
eval invalid "x + y + z" ;
To understand why this is not a valid predicate see Section 3.5. In the following examples note how Walnut points to the
locations of the errors in the predicates. By saying "char at n", Walnut tries to convey that there is something wrong going on
at the vicinity of the n’th character in the predicate.
eval invalid2 "(x + y + z = 0" ;
unbalanced parenthesis
: char at 0
:
eval invalid2 "(x + y + z = 0" ;
eval invalid3 "(∼x) = 0" ;
operator ∼cannot be applied to the operand x of type variable
: char at 1
:
eval invalid3 "(∼x) = 0" ;
eval invalid4 "T [i + j] = i −1" ;
operator = cannot be applied to operands T [(i + j)] and (i −1) of types word and arithmetic
respectively
: char at 6
:
eval invalid4 "T [i + j] = i −1" ;
eval invalid5 "T [2] = 1" ;
operator = cannot be applied to operands T [2] and 1 of types word and number l i t e r a l
respectively
: char at 4
:
eval invalid5 "T [2] = 1" ;
The last example can be ﬁxed as follows:
eval fixed5 "T [2] = @1" ;
To understand why see Section 3.8.
The last thing to note about the eval command is that Walnut overrides the ﬁles generated by an evaluation if the name
of the evaluation is used in a new evaluation.
25
7.2
