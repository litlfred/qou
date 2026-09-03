---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-004-23-automatic-words
section_title: "Automatic Words"
section_number: 2.3
pages: 6-7
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
An automatic word W = (ai)i≥0 is a word in Σω for which there exists a number system S and an automaton with output
M
¡
Q,q0,O,δ,Σ,S
¢
for which reading x ∈RS outputs W [[x]S] = a[x]S. In other words, for an automatic word, the symbol at
position i for all i can be effectively computed by running an automaton with output on any single representation of i in a
number system. As usual we assume Σ is a ﬁnite subset of Z.
The word T for which the symbol at position i, is the number of 1s in any binary representation of i, modulo 2, is called
the Thue-Morse word. The Thue-Morse word is well-deﬁned since all the inﬁnitely many different binary representations
of an integer have the same number of 1’s. It is instantly clear that T is an automatic word over msd_2 if one notes the
automaton with output in Figure 2.7.
In the introduction, we mentioned that Walnut decides some properties of automatic words. Recall from Section 2.1 that
squares are non-empty words of the form xx. It is easy to see that T has square subwords. The following predicate captures
this property:
∃i∃n∀j, j < n =⇒T [i + j] = T [i +n + j].
Walnut provides a decision procedure that takes predicates like this and decides whether they are true or false. Walnut
does so, by constructing automata for every subpredicate in the predicate above; see Section 2.4 for more details. It starts
by constructing from the automaton in Figure 2.7 an automaton M1
¡
Q,q0,F,δ,msd_2,msd_2,msd_2
¢
for subpredicate
3The automaton accepting +msd_ﬁb has 16 states, which is too big to be represented here.
6
Figure 2.7: The Thue-Morse word
P1 := T [i + j] = T [i + j +n]. This means (see Section 2.4) that M1 is constructed so that it accepts tuples t = (w1,w2,w3)
if and only if |w1| = |w2| = |w3| and substitutions i = [w1]msd_2, j = [w2]msd_2, and n = [w3]msd_2 are satisfying P1. Walnut
then using M1 constructs an automaton M2 for P2 := ∀j, j < n =⇒T [i + j] = T [i + n + j]. The automaton M2 takes
two inputs representing the two free variables i and n in P2. Walnut continues by constructing the automaton M3 for
P3 := ∃n∀j, j < n =⇒T [i + j] = T [i +n + j]. In the end, Walnut returns true if M3 accepts anything. The fact that M1,M2,
and M3 exist is explained in Section 2.4. The details of how Walnut constructs these automata are explained in Section 4.
The details of what comprises a valid predicate is explained in Section 3. To see more examples of the properties of the
Thue-Morse word and their proofs see Section 7.1.
We can extend the deﬁnition of automatic words to higher dimensions. The (n-dimensional) automatic word
W =
¡
ai1,i2,...,in
¢
i1≥0,i2≥0,...,in≥0
is an inﬁnite word over Σ for which there exist number systems Sj and an automaton with output
M
¡
Q,q0,O,δ,Σ,S1,S2,...,Sn
¢
for which reading x, such that πj (x) ∈RSj for all j, outputs
W
£
[π1[x]]S1
¤£
[π2[x]]S2
¤
···
£
[πn[x]]Sn
¤
= a[π1[x]]S1,[π2[x]]S2,...,[πn[x]]Sn .
2.4
