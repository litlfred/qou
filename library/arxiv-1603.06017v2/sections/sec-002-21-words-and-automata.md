---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-002-21-words-and-automata
section_title: "Words and Automata"
section_number: 2.1
pages: 3-4
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
A word (ai)i∈I for a ﬁnite, inﬁnite, or a possibly empty subset I of natural numbers N, is a sequence of symbols ai over a ﬁnite
set called an alphabet. The set I usually equals N or Nl = {k ∈N : k < l} for some l. The set of ﬁnite and inﬁnite words over
the alphabet Σ are denoted by Σ∗and Σω, respectively. The empty word is denoted by ϵ. For the ﬁnite word w = a0a1 ···al−1,
the length |w|, is deﬁned and equals l. We let Σl denote the set of all words over Σ of length l. A subword (sometimes called
“factor” in the literature) is a ﬁnite and contiguous subsequence of a word. The subword of w starting at position i of length
k ≥0 is denoted by w[i..i +k −1] = ai ···ai+k−1. Many interesting properties of words can be expressed in terms of their
subwords. For example, the property of having two equal and adjacent subwords, referred to as a square, is discussed in
numerous papers in the area of combinatorics on words. The product of two words x and y, denoted by xy, is the result of
concatenating x by y.
There are cases where our words are deﬁned over alphabets consisting of tuples of symbols, so let us ﬁx our notation
regarding these words. For a word w over an alphabet Σ1 ×Σ2 ...×Σn, we let the projection map πj (w) for 1 ≤j ≤n denote
the word over Σj , obtained from w by looking at the j’th coordinates, i.e., words πj (w) are uniquely deﬁned by
w =
|w|−1
Y
i=0
¡
π1(w)[i],π2(w)[i],...,πn(w)[i]
¢
.
For example, for w = (0,1)(1,1)(0,0) over {0,1}×{0,1} we have π1(w) = 010 and π2(w) = 110.
The reader is probably familiar with the notions of deterministic and nondeterministic ﬁnite state automata. In Walnut,
an automaton M with n inputs (input tapes), is an (n +4)-tuple
¡
Q,q0,F,δ,Σ1,Σ2,...,Σn
¢
, where Q is the (ﬁnite) set of states,
q0 ∈Q is the initial state, F ⊆Q is the set of ﬁnal states, δ : Q ×Σ1 ×Σ2 ×···×Σn →Q is the transition function, and Σi is the
alphabet of the i’th input (tape). The automaton’s alphabet is deﬁned to be the cross product Σ1 ×Σ2 ×···×Σn, and the
notions of accepting a word w or a language over this alphabet is deﬁned as usual. A nondeterministic automaton is deﬁned
similarly, except that the transition function is deﬁned by δ : Q ×Σ1×Σ2×···×Σn →2Q. In Walnut and throughout this article,
the Σi are ﬁnite subsets of integers Z.
Two automata are equal (isomorphic) if their underlying graphs are isomorphic. Two automata are equivalent if they
accept the same language. There exists a determinization algorithm that converts a nondeterministic automaton to an
equivalent deterministic automaton. There exists a minimization algorithm that converts an automaton to an equivalent
automaton with the least number of states (which is unique up to isomorphism). It is known that extending the automata
model by allowing multiple initial states (similar to how there can be multiple ﬁnal states) does not add to the model’s
expressiveness.
Next we extend the notion of accepting languages to relations, since the latter is more natural in Walnut:
Deﬁnition 1 (relations computed by automata). The relation R ⊂Σ∗
1 ×Σ∗
2 ×...×Σ∗
n computed/accepted by M is deﬁned by
R =
©¡
π1(w),π2(w),...,πn(w)
¢
: M accepts w
ª
.
Since for every word w, the words πi(w) are all of the same length, the relation R accepted by an automaton is consisted of
tuples of the words of the same length, i.e., we have
R ⊆
[
l≥0
¡
Σl
1 ×Σl
2 ×···×Σl
n
¢
⊂Σ∗
1 ×Σ∗
2 ×...×Σ∗
n.
For example, the language accepted by the following automaton is L = (0,0)∗(1,1)(0,0)(0,1), whereas the relation accepted
is R =
©
(w1,w2) : w1 ∈0∗100,w2 ∈0∗101, and |w1| = |w2|
ª
:
3
Figure 2.1: Automaton accepting tuples of same length representations of 4 and 5 in binary
In other words, the automaton accepts tuples t = (w1,w2) ∈{0,1}∗×{0,1}∗where w1 and w2 are representations of the
the same length, in the most-signiﬁcant-digit-ﬁrst binary system, of natural numbers 4 and 5 respectively. On the other
hand, referring to the words w in ({0,1}×{0,1})∗that are accepted by this automaton is not very descriptive. That is why, in
this article, we prefer the relation (tuple) terminology over the language (word) terminology.
In almost all depictions of the underlying graphs of automata, such as the one in Figure 2.1, when a transition is not
speciﬁed, it is assumed to be a transition to a dead state. In Walnut we do not store transitions to the dead state. Adding the
dead state and all implicit transitions to it, is called totalizing an automaton.
An automaton with output is a tuple
¡
Q,q0,O,δ,Σ,Σ1,Σ2,...,Σn
¢
where Q,q0,δ,Σj are as before, the set Σ is the output
alphabet, and, instead of a set of ﬁnal states, we have a map O : Q →Σ. The symbol O(q) is called the output of the state q.
An automaton with output can be thought of as an automaton that reads a word over Σ1 ×Σ2 ···×Σn and outputs whatever is
the last state’s output. In Walnut, the output alphabet Σ is a ﬁnite subset of integers. We can think of ordinary automata as a
special case of automata with output by letting the set of ﬁnal states to be F = {q : O(q)̸ = 0}. This is indeed how ordinary
automata are stored in Walnut.
