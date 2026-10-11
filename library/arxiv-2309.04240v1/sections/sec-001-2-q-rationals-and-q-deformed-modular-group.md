---
doc_id: arxiv-2309.04240v1
doc_title: "BURAU REPRESENTATION OF BRAID GROUPS AND q-RATIONALS"
section_id: sec-001-2-q-rationals-and-q-deformed-modular-group
section_title: "q-rationals and q-deformed modular group"
section_number: 2
pages: 3-4
source_pdf: 2309.04240v1.pdf
source_sha256: 792154a0d6a57e34
toc_source: outline
doc_brief: "BURAU REPRESENTATION OF BRAID GROUPS AND q-RATIONALS — We establish a link between the new theory of q-deformed ratio- nal numbers and the classical Burau representation of the braid group B3."
---
In this section we give the precise and adapted for computations deﬁnition of
the q-rationals, and recall their main properties, which are necessary for the proof
of the main result.
Among several equivalent deﬁnitions of q-rationals we will use
the one based on PSL(2, Z)-invariance (or on B3-invariance).
2.1. The main deﬁnition. Consider the set Q ∪{∞} rational numbers, extended
by one additional element ∞which will always be represented by the quotient 1
0.
The group SL(2, Z) of matrices with integer coeﬃcients
M =

r
v
s
u

,
r, v, s, u ∈Z,
ru −vs = 1,
acts on Q ∪{∞} by linear-fractional transformations:
M · x = rx + v
sx + u.
This action is homogeneous and eﬀective for the modular group PSL(2, Z).
Following [24], consider the following matrices of GL(2, Z[q, q−1]):
(2.1)
Rq :=
 
q
1
0
1
!
,
Lq :=
 
1
0
1
q−1
!
.
They generate a subgroup PSL(2, Z)q in the group
PGL(2, Z[q, q−1]) = GL(2, Z[q, q−1])/{±qnId}.
which is isomorphic to PSL(2, Z) and thus can be considered as q-deformed modular
group [24, 18]. Evaluating at q = 1 one recovers R = Rq|q=1 and L = Lq|q=1 the
standard generators of the modular group SL(2, Z). This allows one to consider
q-analogs of matrices Mq for every M ∈SL(2, Z).
4
S. MORIER-GENOUD, V. OVSIENKO, AND A. VESELOV
We have a natural action of PSL(2, Z)q on the space Z(q) of rational functions
in q with integer coeﬃcients, which can be considered as q-deformed version of
the standard linear-fractional action of the modular group.
More precisely, for
every M ∈SL(2, Z), written as a monomial in R and L, let Mq be a matrix in
GL(2, Z[q, q−1]) given by the same monomial in Rq and Lq. If f(q) ∈Z(q), then
the linear-fractional action
(2.2)
f(q) 7→Mq · f(q)
is a well-deﬁned action of PSL(2, Z). In other words, Mq does depend on the choice
of the monomial in R and L presenting M, but the result of (2.2) does not.
Deﬁnition 1. The set of q-rationals is the set of rational functions in the orbit
of
any point from the set {0, 1, ∞} (all of them remain independent of q after
deformation) for the linear-fractional action (2.2).
Example 2. For instance,
Lq·∞= Rq·0 = 1,
RqRq·0 = 1+q,
LqRq·0 =
q
1 + q ,
LqRqRq·0 =
q + q2
1 + q + q2 ,
. . .
are considered as the q-analogs of respectively 1, 2, 1
2, 2
3, . . .
Remark 3. The notion of q-rationals extends that of q-integers:
[n]q
:=
1 + q + q2 + . . . + qn−1
[−n]q
:=
−q−1 −q−2 . . . −q−n,
that goes back to the works of Euler and Gauss. These q-integers and the corre-
sponding q-binomial coeﬃcients are essential in quantum algebra and mathematical
physics. They are also the key ingredients for the theory of q-analogs in combina-
torics. Most classical sequences of integers have interesting q-analogs often arising
as generating functions.
