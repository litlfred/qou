---
doc_id: arxiv-1904.13129v1
doc_title: "On the regularity of critical points for O’Hara’s knot energies: From smoothness to analyticity"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 3-4
source_pdf: 1904.13129v1.pdf
source_sha256: dfa7fd0ebf1ab8c4
---
3 we decompose the ﬁrst variation of O’Hara’s energies into th e orthogonal projec-
tion of a main part Qα and two remaining parts Rα
1 and Rα
2 of lower order. The
main part Qα and its derivatives are estimated in Section 4. Since the orthogonal
projection of Qα appears in the ﬁrst variation of O’Hara’s energies, we estim ate
the tangential part of Qα using new estimates for a kind of fractional derivative of
a product of two functions that, in Section 5, that behave like a fractional Leibniz
rule. In Section 5 and Section 6 we cut-oﬀ the singularities of the singular integrals
involved and derive uniform estimates. More precisely, in S ection 6 we rewrite the
orthogonal projection of the truncated remaining terms so t hat they may be ex-
pressed by integrals over analytic functions. In Section 7 we realize that estimates
do not depend on the cut-oﬀ parameter and hold for the orthogo nal projections
of Qα, Rα
1 , Rα
2 , and its derivatives. Finally, we will use the estimates to p rove
Theorem 1.2 using Cauchy’s method of majorants.
2. Preliminaries
2.1. F ractional Sobolev spaces. We denote by | · | the Euclidean norm on Cn
for any integer n ≥ 1. In this article we work with closed curves on the periodic
domain R/Z so that a curve f : R → Rn is periodic with unit periodicity.
On the regularity of critical points for O’Hara’s knot energ ies: From smoothness to analyticity. 4
We know that for any f ∈ L2(R/Z, Cn) the Fourier series of f in x ∈ R/Z is
given by ∑
k∈Z
ˆf (k)e2πikx, where the k-th Fourier coeﬃcient of f are given by
ˆf (k) =
∫ 1
0
f (x)e−2πikxdx.
The fractional Sobolev space of order s ≥ 0 (i.e. the Bessel potential space of
order s ≥ 0) is deﬁned as
H s(R/Z, Cn) := {f ∈L2(R/Z, Cn) | ‖f ‖Hs := ‖f ‖Hs(R/Z,Cn) :=
√
(f,f )Hs < ∞},
equipped with the scalar product
(f,g )Hs := (f,g )Hs(R/Z,Cn) :=
∑
k∈Z
(1 +k2)s⟨ˆf (k),ˆg(k)⟩Cn.
Furthermore, we will need the embeddings H s(R/Z, Cn) ⊆ H t(R/Z, Cn) for
any 0 ≤ t < s(cf. [ DNPV12, Prop. 2.1, Corol. 2.3]) as well as H s(R/Z, Cn) ⊆
C(R/Z, Cn) for any s > 1
2 (cf. [ DNPV12, Theor. 8.2]), from which we can deduce
that the Fourier series of any f ∈H s(R/Z, C) withs> 1
2 converges absolutely and
uniformly to f . In fact the space H m, for any integer m ≥ 0, coincides with the
classical Sobolev space and the norms ‖ · ‖ Hm and ‖f ‖W m := (∑ m
ν=0 ‖∂νf ‖2
L2)
1
2
are equivalent (cf. [ Rei09, Lem. 1.2] or [ AF03, 7.62]). Furthermore, let us also
mention the Banach algebra property of H m for any integer m ≥ 1, i.e. there exists
a positive constant Cm such that
‖fg ‖Hm ≤Cm‖f ‖Hm‖g‖Hm (2.1)
for all f,g ∈H m(R/Z, R) (cf. [ AF03, Theor. 4.39]).
