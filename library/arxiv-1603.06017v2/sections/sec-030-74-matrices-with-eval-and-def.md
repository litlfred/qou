---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-030-74-matrices-with-eval-and-def
section_title: "Matrices with eval and def"
section_number: 7.4
pages: 29-29
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
We postponed discussing the exact syntax of the eval and def commands until this section. These two commands can take an
optional argument:
• eval <name> <space separated list of free variables>? <predicate>
• def <name> <space separated list of free variables>? <predicate>
The question marks are representing the fact that the corresponding arguments are optional. When a list of free variables
is preset, in addition to the ordinary computation, Walnut will calculate the incidence matrices of the underlying graph of
the computed automaton, corresponding to the transitions labeled by the listed free variables. It stores the matrices in the
Maple syntax in a .mpl ﬁle in “/Walnut/Result/” directory.
Suppose M
¡
Q,q0,F,δ,S1,...,Sm
¢
is the automaton calculated for the predicate (x1,...,xn) : P′. For a free variable xi and a
value v ∈ΣSi, we let M_xi_v denote the |Q|×|Q| matrix where the entry M_xi_v[p][q]12, for every pair of states p and q, is
the number of tuples transitioning from p to q with v in the i’th coordinate, or more formally
M_xi_v[p][q] =
¯¯¯
n
(α1,...,αi,...,αm) : δ
¡
(α1,...,αi,...,αm),p
¢
= q such that αi = v and αj ∈ΣSj for j̸ = i
o¯¯¯.
We already saw in Figure 7.4 an automaton accepting b = a +1. Now writing
eval example a "b=a+1" ;
causes Walnut to calculate the matrices M_a_0 and M_a_1:
M_a_0 =
·1
1
0
0
¸
M_a_1 =
·1
0
0
1
¸
In the same command, we could ask Walnut to calculate the incidence matrices for b as well as a by writing:
eval example a "b=a+1" ;
M_b_0 =
·1
0
0
1
¸
M_b_1 =
·1
1
0
0
¸
.
There are a lot of interesting things one can do using incidence matrices. For example for Fibonacci word, and Sturmian
words in general, the number of distinct subwords of length n, i.e., subword complexity, is n +1. Now can one verify this
using Walnut? The answer is yes. Please refer to [14] for this and a lot of other interesting applications.
7.5
