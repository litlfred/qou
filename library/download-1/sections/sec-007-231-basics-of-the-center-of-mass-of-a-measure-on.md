---
doc_id: download-1
doc_title: "Central and L p -concentration of 1-Lipschitz maps into R -trees"
section_id: sec-007-231-basics-of-the-center-of-mass-of-a-measure-on
section_title: "Basics of the center of mass of a measure on a CAT(0)-space."
section_number: 2.3.1
pages: 7-9
source_pdf: Download (1).pdf
source_sha256: bbb001c909958e8a
toc_source: inferred
doc_brief: "Central and L p -concentration of 1-Lipschitz maps into R -trees — In this paper, we study the Le´vy-Milman concentration phenomenon of 1-Lipschitz maps from mm-spaces to R-trees."
---
Basics of the center of mass of a measure on a CAT(0)-space.
In this subsection, we review Sturm’s works about measures on a CAT(0)-
space. We refer to [8] and [15] for details. A geodesic metric space X is called a
CAT(0)-space if we have
dXðx; ð1=2ÞÞ2  1
2 dXðx; yÞ2 þ 1
2 dXðx; zÞ2  1
4 dXðy; zÞ2
for any x; y; z 2 X and any minimizing geodesic  : ½0; 1 ! X from y to z. For
example, Hadamard manifolds, Hilbert spaces, and R-trees are all CAT(0)-
spaces.
Let ðX; dXÞ be a metric space. We denote by BðXÞ the set of all ﬁnite Borel
measures  on X with separable supports. We indicate by B1ðXÞ the set of all
Borel measures  2 BðXÞ such that
R
X dXðx; yÞdðyÞ < þ1 for some (hence all)
x 2 X. We also indicate by P1ðXÞ the set of all probability measures in B1ðXÞ.
For any  2 B1ðXÞ and z 2 X, we consider the function hz; : X ! R deﬁned by
hz;ðxÞ :¼
Z
X
fdXðx; yÞ2  dXðz; yÞ2gdðyÞ:
Note that
Z
X
j dXðx; yÞ2  dXðz; yÞ2jdðyÞ  dXðx; zÞ
Z
X
fdXðx; yÞ þ dXðz; yÞgdðyÞ < þ1:
A point z0 2 X is called the center of mass of the measure  2 B1ðXÞ if for any
z 2 X, z0 is a unique minimizing point of the function hz;. We denote the point z0
by cðÞ. A metric space X is said to be centric if every  2 B1ðXÞ has the center of
mass.
PROPOSITION 2.10 (cf. [15, Proposition 4.3]).
Any complete CAT(0)-space
Central and Lp-concentration of 1-Lipschitz maps into R-trees
489
is centric.
A simple variational argument yields the following lemma.
LEMMA 2.11 (cf. [15, Proposition 5.4]).
Let H be a Hilbert space. Then for
each  2 B1ðHÞ with m ¼ ðXÞ, we have
cðÞ ¼ 1
m
Z
H
ydðyÞ:
Let ðT; dTÞ be an R-tree and  2 B1ðTÞ. For z 2 T and T 0 2 C 0
TðzÞ, we put
cz;T 0ðÞ :¼
Z
T 0 dTðz; wÞdðwÞ 
Z
TnT 0 dTðz; wÞdðwÞ:
Let us consider a (possibly inﬁnite) simplicial tree Ts. Here, the length of each
edge of Ts is not necessarily equal to 1. We assume that every vertex of Ts is an
isolated point in the vertex set of Ts.
PROPOSITION 2.12 (cf. [15, Proposition 5.9]).
Let  2 B1ðTsÞ and z 2 Ts.
Then, z ¼ cðÞ if and only if cz;T 0ðÞ  0 for any T 0 2 C 0
TsðzÞ.
PROPOSITION 2.13 (cf.
[15,
Proposition
6.1]).
Let
X
be
a
complete
CAT(0)-space and  2 B1ðXÞ. Assume that the support of  is contained in a
closed convex subset K of X. Then, we have cðÞ 2 K.
Let X be a metric space. For ;  2 P1ðXÞ, we deﬁne the L1-Wasserstein
distance dW
1 ð; Þ between  and  as the inﬁmum of
R
XX dXðx; yÞdðx; yÞ, where
 2 P1ðX  XÞ runs over all couplings of  and , that is, measures  with the
property that ðA  XÞ ¼ ðAÞ and ðX  AÞ ¼ ðAÞ for any Borel subset A  X.
LEMMA 2.14 (cf. [18, Theorem 7.12]).
A sequence fng1
n¼1  P1ðXÞ con-
verges to  2 P1ðXÞ with respect to the distance function dW
1
if and only if the
sequence fng1
n¼1 converges weakly to the measure  and
lim
n!1
Z
X
dXðx; yÞdnðyÞ ¼
Z
X
dXðx; yÞdðyÞ
for some (and then any) x 2 X.
THEOREM 2.15 (cf. [15, Theorem 6.3]).
Let X be a CAT(0)-space. Given
490
K. FUNANO
;  2 P1ðXÞ, we have dXðcðÞ; cðÞÞ  dW
1 ð; Þ.
