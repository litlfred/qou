---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-020-35-grading-and-deformations
section_title: "Grading and deformations"
section_number: 3.5
pages: 26-26
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
category Aq over K[[q]], with µd
Aq = µd
A + O(q), i.e.
µd
Aq = µd
A + qµd
Aq,1 + q2µd
Aq,2 + · · ·
(3.9)
with each µd
Aq,j comprising K-linear maps
homA(Xd1, Xd) ⊗· · · ⊗homA(X1, X2) →homA(X1, Xd)[2 −d]
for any (X1, . . . , Xd) ∈(Ob A)d. The operations µd
Aq should be q-adically convergent (for us they
will always vanish for q ≫0). In applications, such deformations of Fukaya categories will arise
from (partial) compactiﬁcations of symplectic manifolds M ⊂¯
M, obtained by adding in a divi-
sor ∆= ¯
M\M disjoint from the Lagrangian submanifolds under consideration. The operation
µd
F( ¯
M),j will count pseudoholomorphic d-gons with multiplicity j over ∆, so setting q = 0 corre-
sponds to working in the open part M = ¯
M\∆. Assuming that one can achieve transversality
within the class of almost complex structures which make ∆⊂¯
M a pseudoholomorphic subman-
ifold, positivity of intersections ensures that the µd
Aq are compatible with the ﬁltration on Floer
cochain complexes in ¯
M by powers of q. Under suitable monotonicity hypotheses on ¯
M, one can
further set q = 1 since all series converge.
The formal parameter q of a deformation arising from a partial compactiﬁcation of an open
symplectic manifold with c1 = 0 typically has non-zero degree.
Lemma 3.15. If the ﬁrst Chern class c1( ¯
M) = r[∆], with r ∈Q, then deg(q) = 2r.
This is a consequence of the index theorem for the Cauchy-Riemann equations with totally
real boundary conditions, see [92, Section 11]. It is most familiar in the case when c1( ¯
M) = 0,
and the deformed category is Z-graded, or when ∆⊂
¯
M is an anticanonical divisor and the
deformation parameter has degree 2 (for instance, deforming the cohomology of the zero-section
T n ⊂(C∗)n from an exterior algebra to the Cliﬀord algebra on compactifying to CPn, with ∆
the toric anticanonical divisor).
Suppose then c1( ¯
M) is eﬀective, that c1(M) = 0, and ﬁx a holomorphic volume form η ∈
H0(K ¯
M) with poles of order r along the divisor ∆⊂¯
M. We denote by ιη the absolute indices
for generators of Floer complexes between graded Lagrangian submanifolds (which are assumed
to lie within the open part M).
If L′ is obtained as a Hamiltonian perturbation of L for a
Hamiltonian function whose restriction to L is Morse, the index iη of a point of L ∩L′ is equal to
the Morse index of the corresponding critical point. Suppose now one has a holomorphic polygon
u : D →¯
M with Lagrangian boundary conditions in M. In this setting,
vdim(u) = iη(x0) −
k
X
j=1
iη(xk) + k −2 + 2r∆· im(u)
(3.10)
for a holomorphic (k + 1)-gon with one outgoing boundary puncture x0 (the sign of the last term
corresponds to the fact that η has poles on ∆= r · PD[c1( ¯
M)], and the virtual dimension is
increased by adding positive Chern number components).
