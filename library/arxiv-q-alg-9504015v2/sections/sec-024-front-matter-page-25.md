---
doc_id: arxiv-q-alg-9504015v2
doc_title: "Witten's invariants of rational homology spheres at prime values of K and trivial connection contribution"
section_id: sec-024-front-matter-page-25
section_title: "Front matter (page 25)"
section_number: null
pages: 25-25
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
toc_source: inferred
doc_brief: "Witten's invariants of rational homology spheres at prime values of K and trivial connection contribution — We establish a relation between the coeﬃcients of asymptotic expansion of the trivial"
---
we can say that Lp,q is constructed by a chain surgery U(−q,−p) = SU(−p,q) applied to an
empty knot, times a factor
√
K
sin( π
K). Then we can read the result directly from eq. (4.8) by
setting there N = 1, sign (L) = 0, α = 1 and
U(−q,−p) =

−q
s
−p
r


(4.25)
instead of U(p,q):
Z′(Lp,q) =
 |p|
K
!
sign (p) ˇq4∗(p∗(q−r)−Φ(U(−q,−p))) ˇq2∗ˇq2∗p∗−ˇq−2∗p∗
ˇq −1
=
 |p|
K
!
sign (p) ˇq3s∨(q,p) ˇq2∗ˇq2∗p∗−ˇq−2∗p∗
ˇq −1
(4.26)
=
 |p|
K
!
sign (p) ˇq3s∨(q,p) (−1)p∗+1 ˇq
p∗
2 −ˇq−p∗
2
ˇq
1
2 −ˇq−1
2 ,
here s∨(q, p) is the “checked” Dedekind sum, that is, its denominator is inverted modulo K
as in eq. (1.13). We used the relation ˇq2∗= −ˇq
1
2 in order to derive the last expression in this
equation. Although it might look simpler than the previous one, it obscures the fact that
Z′(Lp,q) ∈ZZ[ˇq]. Also note that the expression ˇq
p∗
2 by itself is ambiguous since p∗is deﬁned
only modulo K.
Comparing the second expression in the r.h.s. of eq. (4.26) with the formula for the trivial
connection contribution to Witten’s invariant of the lens space
Z(tr)(Lp,q; k) = Z(S3; k)sign (p)
q
|p|
ˇq3s(p,q) ˇq
p
2 −ˇq−p
2
ˇq
1
2 −ˇq−1
2
(4.27)
derived in [10] we can easily check the relation (1.20).
The formula (4.8) also allows us to check the Proposition 1.1 for Seifert manifolds which
are rational homology spheres.
Consider an (N + 1)-component link L in S3 consisting
of N unknots Lj, 1 ≤j ≤N simply linked to a single unknot L0.
A Seifert manifold
X

p1
q1 , . . . , pn
qn

is constructed by performing (pj, qj) surgeries on the components Lj and a
(0, 1) surgery on L0 (see, e.g. [9]). The Jones polynomial of L is known [1] to be equal to
Jβ,α1,...,αN(L; k) =
1
sin

π
K

QN
j=1 sin

π
Kβαj

sinN−1 
π
Kβ

,
(4.28)
