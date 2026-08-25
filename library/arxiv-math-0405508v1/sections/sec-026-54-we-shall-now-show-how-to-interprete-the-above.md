---
doc_id: arxiv-math-0405508v1
doc_title: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B"
section_id: sec-026-54-we-shall-now-show-how-to-interprete-the-above
section_title: "We shall now show how to interprete the above in terms of knot"
section_number: 5.4
pages: 22-24
source_pdf: 0405508v1.pdf
source_sha256: ef2e41cf67f3a411
doc_brief: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B — 30 sections: Introductory remarks on knots, bra; Geck–Lambropoulou; Geck–Lambropoulou"
---
diagrams, and how to calculate alternatively the above solid torus kn ot invari-
ants using initial conditions and applying skein relations on the mixed link
diagrams.
Let L+, L −, L 0 be oriented mixed link diagrams that are identical, except
in one crossing, where they are as depicted below:
,
L + L _
,
L 0
Let also M+, M −, M 0 be oriented mixed link diagrams that are identical, except
in the regions depicted below:
,
M + M _
,
M 0
Markov traces and knot invariants 23
In [7], (5.2) it is shown that the knot invariant deﬁned there (which is a special
member of the family of invariants deﬁned above), satisﬁes the two recursive
linear formulae.
1
√q
√
λ XL+ − √q
√
λ XL− = (√q − 1√q ) XL0
1√Q XM+ −
√
Q XM− = (
√
Q − 1√Q ) XM0
These are the two skein relations that derive from the deﬁning quad ratic rela-
tions of H, and the ﬁrst one of them is the well-known skein rule used for the
evaluation of the homﬂy-pt polynomial. The same reasoning applies to any
invariant of Deﬁnition 5.3 above.
Take now a braid α in B1,n . Then π(α ) is an A-linear combination of
elements in the basis of Hn. (In terms of diagrams, we have used on Xˆα the
skein relations above.) This fact and Proposition 3.4 imply now that, un der
conjugation and the skein relations, Xˆα can be further written as an A-linear
combination of the values of X on diagrams of the form ˆd∗
1 · · · d∗
n, where d∗
i is
either 1 , s i or t′
i, 0 (with inverses mixed up). If now b is the number of t′
i, 0’s
in d∗
1 · · · d∗
n, then ˆd∗
1 · · · d∗
n is a mixed link on b components, such that each
component links once (in a positive sense) with the special ﬁxed one, but they
are otherwise unlinked with each other. Therefore ˆd∗
1 · · ·d∗
n is isotopic to the
mixed link ˆt′t′
1 · · · t′
b−1, pictured below.
b
Now τ(t′t′
1 · · · t′
k−1) = yk is one of the initial conditions from Theorem 4.3, and
using Deﬁnition 5.3 we can calculate X ˆt′t′
1···t′
k−1
. Hence, we proved that the two
skein rules together with the following (inﬁnitely many) initial condition s
Xˆ1 = 1 (1 ∈ B1, 1), X ˆα k
=
[
− 1 − λq
√
λ(1 − q)
] k−1
yk
(with α k = t′t′
1 · · · t′
k−1 ∈ B1,k for all k ≥ 1) determine uniquely the invari-
ant X.
Remarks 5.5 Let α ∈ B1,n . The above discussion shows geometrically that,
ﬁrstly, τ ◦ π(α ) can be calculated as a linear combination of terms τ(d∗
1 · · · d∗
n)
