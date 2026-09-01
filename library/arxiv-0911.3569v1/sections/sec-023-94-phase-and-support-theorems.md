---
doc_id: arxiv-0911.3569v1
doc_title: "MULTIVARIATE STABLE POLYNOMIALS: THEORY AND APPLICATIONS"
section_id: sec-023-94-phase-and-support-theorems
section_title: "Phase and support theorems."
section_number: 9.4
pages: 29-29
source_pdf: 0911.3569v1.pdf
source_sha256: 4e7c15c9724fb453
---
every monomial xα occurring in f has total degree of the same parity: all are even,
or all are odd.
Theorem 9.8 (Theorem 6.2 of [10]) . Let f ∈ C[x] be Hurwitz stable and with
deﬁnite parity. Then there is a phase 0≤θ <2π such that e−iθf(x) has only real
nonnegative coeﬃcients.
The support of f = ∑
αc(α)xα is supp(f) = {α ∈ Nm : c(α) ⁄= 0}. Let
δi denote the unit vector with a one in the i-th coordinate, and for α∈ Zn let
|α| =∑m
i=1|α(i)|. A jump system is a subset J⊆ Zm satisfying the following two-
step axiom :
(J) If α,β ∈ J and i∈ [m] and ϵ∈{− 1, +1} are such that α′ = α +ϵδi satisﬁes
|α′−β|<|α−β|, then either α′∈ J or there exists j∈ [m] and ε∈{− 1, +1} such
that α′′ =α′ +εδj∈ J and|α′′−β|<|α′−β|.
Jump systems generalize some more familiar combinatorial objects. A jump
system contained in{0, 1}m is a delta-matroid. A delta-matroid J for which|α| is
constant for all α∈ J is the set of bases of a matroid. For bases of matroids, the
two-step axiom (J) reduces to the basis exchange axiom familiar from linear algebra:
if A,B ∈ J and a∈A rB, then there exists b∈B rA such that (A r{a})∪{b}
is in J.
Theorem 9.9 (Theorem 3.2 of [8]). If f∈ S[x] is stable then the support supp(f)
is a jump system.
Recall from Section 7 that for multiaﬃne polynomials with nonnegative coeﬃ-
cients, real stability implies the Rayleigh property. A set system J is convex when
A,B∈ J and A⊆B imply that C∈ J for all A⊆C⊆B.
Theorem 9.10 (Section 4 of [15]). Letf =∑
S⊆[m]c(S)xS be multiaﬃne with real
nonnegative coeﬃcients, and assume that f is Rayleigh.
(a) The support supp(f) is a convex delta-matroid.
(b) The coeﬃcients are log-submodular: for all A,B⊆ [m],
c(A∩B)c(A∪B)≤c(A)c(B).
