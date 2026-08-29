---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-032-8-working-with-inputoutput
section_title: "Working with Input/Output"
section_number: 8
pages: 32-34
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
Throughout this section it is assumed that all ﬁles have UTF-8 encoding. This is the default encoding for most text editors.
8.1
Deﬁning Automata in Text Files
In this section we learn how to manually deﬁne all automata types in text ﬁles. Recall that an ordinary automaton can
be thought of as an automaton with output, in which states with non-zero outputs are treated as ﬁnal states; see Section
2.1. Therefore suppose M
¡
Q,q0,O,δ,Σ,S1,S2,...,Sn
¢
is an automaton with output with m states and n inputs over number
systems Si. Furthermore suppose that the states are labeled 0 to m −1, i.e., Q =
©
0,1,...,m −1
ª
, and that q0 = 014. To deﬁne
M in a text ﬁle, ﬁrst create a text ﬁle M.txt15. The ﬁrst line must be
S1 S2 ··· Sn
which declares inputs’ number systems. The second line is declaring state 0 as follows:
0 α
where α = O(0). Next lines are declarations of transitions of state 0 which can come in any order. For every α1 ∈ΣS1,α2 ∈
ΣS2,...,αn ∈ΣSn transitions are of the following form
α1 α2 ··· αn -> q
whenever δ
¡
0,α1,α2,...,αn
¢
= q. There is no need to declare transitions to a dead state. For any pair (α1,α2,...,αn) that no
declaration of the form above is mentioned, it is assumed that δ(0,α1,α2,...,αn) is a dead state. We can use ∗, the wildcard
matching symbol, in place of any symbol αi. If there is a transition of the form
α1 α2 ... αi−1 ∗αi+1 ... αn -> q
it is understood that δ
¡
0,(α1,α2,...,αi−1,β,αi+1,...,αn)
¢
= q for every β ∈ΣSi. After transitions of the state 0 are declared,
we declare state 1 followed by its transitions. We continue like this until all states and their transitions are declared. Note that
nowhere in M.txt we are deﬁning the output alphabet Σ. The output alphabet is inferred indirectly by looking at the state
declarations. To see examples refer to Files 2–4.
A non-arithmetic automaton is deﬁned in the same way, except that in the ﬁrst line, for inputs that do not have number
systems associated with them, we write down the alphabet between curly brackets. Alphabets can be any subset of integers.
As an example see File 4.
Deﬁning true or false automata in text ﬁles is easy. They have only one line and it is either true or false.
As one last example, the paperfolding words are given by the following automaton; see Section 5.2 and article [10] for
more details:
Figure 8.1: Automata for paperfolding words
This automaton is deﬁned in the ﬁle PF.txt in directory “/Walnut/Word Automata Library/”:
14If an automaton does not follow these criteria we can always come up with an isomorphic one that does.
15File names in Walnut start with letters and can contain alphanumerics and underscore.
32
1
{ −1 ,1} lsd_2
2
3
0 0
4
* 0 −> 0
5
1 1 −> 1
6
−1 1 −> 2
7
8
1 1
9
* 1 −> 4
10
* 0 −> 3
11
12
2 −1
13
* 0 −> 4
14
* 1 −> 3
15
16
3 1
17
* * −> 3
18
19
4 −1
20
* * −> 4
File 5: PF.txt
8.2
Deﬁning New Automatic Words
The eval and def commands always produce automata accepting a predicate, therefore the result is never an automaton
with output. So to deﬁne an automatic word W , we need to manually deﬁne its corresponding automaton with output in
the directory “/Walnut/Word Automata Library/”. For example, the Thue-Morse word is deﬁned in the ﬁle “/Walnut/Word
Automata Library/T.txt” as follows:
1
msd_2
2
0 0
3
0 −> 0
4
1 −> 1
5
1 1
6
0 −> 1
7
1 −> 0
File 6: T.txt
8.3
Deﬁning New Number Systems
Based on Deﬁnition 3, to deﬁne a new number system S, we need to deﬁne automata for RS, +S, and <S. We do not need
to deﬁne an automaton for =S, because it can be generated easily, since we assumed that w1 =S w2 if and only if w1 = w2
for any two words w1 and w2 of the same length. The automata for number systems must be deﬁned in the directory
“/Walnut/Custom Bases/”. For example, for the number system S, assuming it is msd, one needs to create msd_S.txt,
msd_S_addition.txt, and msd_S_less_than.txt for RS, +S, and <S respectively. If S is lsd, ﬁle names must be lsd_S.txt,
lsd_S_addition.txt, and lsd_S_less_than.txt respectively. The number system S deﬁned in this way can be used in predicates
by typing ?msd_S or ?lsd_S depending on whether S is msd or lsd. If the automaton for <S is not deﬁned by the user, Walnut
assumes that <S is the lexicographic ordering, i.e., if w1 and w2 are of the same length, then w1 <S w2 if and only if w1 comes
before w2 in lexicographic order16. If the automata for RS is not given, then RS is assumed to be Σ∗
S. The alphabet ΣS is
inferred from the automaton for +S which is always given.
16Lexicographic ordering on symbols is assumed to be ··· < −2 < −1 < 0 < 1 < 2 < ···.
33
Note that reversing all automata for msd_n we get the corresponding automata for lsd_n. The same goes with msd_ﬁb
and lsd_ﬁb. Thus for a number system msd_S if we only deﬁne ﬁles for msd_S, but then typing ?lsd_S in a predicate, Walnut
automatically creates automata for lsd_S by reversing those of msd_S and vice versa. However the user should be cautious
since there could very well be number systems for which the difference between msd and lsd is more than the direction of
the arrows in their corresponding automata.
8.4
Converting .gv ﬁles to .jpeg
The drawings of automata in Walnut are stored in .gv ﬁles. Not only can the software Graphviz open the ﬁles with this
extension, but it can also convert them to many different ﬁle formats. For example, suppose you have a ﬁle named
automaton.gv. To convert it to automaton.jpeg type the following in the terminal:
$dot −Tjpg automaton . gv −o automaton . jpeg
See Graphviz to learn how to convert .gv ﬁles to other ﬁle types.
