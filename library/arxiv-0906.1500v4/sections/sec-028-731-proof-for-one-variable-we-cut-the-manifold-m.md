---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-028-731-proof-for-one-variable-we-cut-the-manifold-m
section_title: "Proof for one variable. We cut the manifold M along S = Sϕ and obtain the"
section_number: 7.3.1
pages: 21-22
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — W e study a computational method of the hyperbolic Reidemeister torsion (also called in the"
---
following splitting: M = N ∪ (S × I), where I = [0 , 1] is the closed unit interval. The
boundaries of N and S × I are equal and consist in the disjoint union of two copies of
S denoted S− = S × {0} and S+ = S × {1}. We apply the Multiplicativity Lemma
to the Mayer–Vietoris sequence associated to this splitting to comp ute the Reidemeister
torsion of M . Our assumptions on ρ : π1(M ) → SL2(C) and ϕ : π1(M ) → Zn say that
every restrictions of ρ to π1(Sℓ) are non–abelian, so we have:
Lemma 13. The twisted homology groups of N and S × I are given by:
H∗(S × I; sl2(C(t))ρ) = C(t) ⊗C H∗(S × I; sl2(C)ρ) ≃ C(t) ⊗ H∗(S; sl2(C)ρ),
H∗(N ; sl2(C(t))ρ) = C(t) ⊗C H∗(N ; sl2(C)ρ).
Moreover, H0(S × I; sl2(C(t))ρ) = H2(S × I; sl2(C(t))ρ) = 0 .
Proof of Lemma 13. One has M = N ∪(S×I), where N is a three–dimensional connected
manifold whose boundary consists in S− ∪ S+. One can observe that the actions of the
restrictions ϕ|π1(N ) and ϕ|π1(Sℓ) of the representation ϕ are trivial. So the ﬁrst two
equalities of the lemma hold.
As ρ|π1(Sℓ) is non–abelian, then H0(Sℓ × I; sl2(C(t))ρ) = 0. In the case of a closed
surface, last equality H2(Sℓ × I; sl2(C(t))ρ) = 0 follows from Poincar´ e duality. For
(compact) surface with boundary, last equality H2(Sℓ × I; sl2(C(t))ρ) = 0 follows from
the fact that Sℓ × I has the same homotopy type as a one–dimensional complex. So that
H0(S × I; sl2(C(t))ρ) = H2(S × I; sl2(C(t))ρ) = 0. □
As H∗(M ; sl2(C(t))ρ) = 0, see Proposition 1, the Mayer–Vietoris sequence with coef-
ﬁcients in sl2(C(t)), denoted V, reduces to a single isomorphism:
(30)
V : H1(S−; sl2(C(t))ρ) ⊕ H1(S+; sl2(C(t))ρ)
≃
− →H1(N ; sl2(C(t))ρ) ⊕ H1(S × I; sl2(C(t))ρ)
where H1(S±; sl2(C(t))ρ) ≃ H1(S; sl2(C(t))ρ) ≃ H1(S × I; sl2(C(t))ρ). The isomorphism
in sequence (30) is represented by the following matrix:
(
i−
∗ −i+
∗
−1 t1
)
,
here i± : S± → N is the inclusion and 1 is the identity matrix. The Multiplicativ-
ity Lemma for Reidemeister torsion gives us the identity below, becau se the common
boundary of N and S × I is the disjoint union of two copies of S:
±∆ ρ
M (t) · Tor(S, c∗
S, h∗
S)2 · Tor(V, {h∗
S, h∗
N }, ∅) = Tor(N, c∗
N , h∗
N ) · Tor(S × I, c∗
S, h∗
S).
Thus, since the torsions of S and S × I are the same,
±∆ ρ
M (t) = Tor(V, {h∗
S, h∗
N }, ∅)−1 Tor(N, c∗
N , h∗
N )
Tor(S, c∗
S, h∗
S) = det
(
i−
∗ −i+
∗
−1 t1
) Tor(N, c∗
N , h∗
N )
Tor(S, c∗
S, h∗
S) .
21
The fraction of torsions Tor( N, c∗
N , h∗
N )/Tor(S, c∗
S, h∗
S) is independent of t (because as
we have already observed in the proof of Lemma 13, the actions of t he restrictions ϕ|π1(N )
and ϕ|π1(S) are trivial). This proves that, up to sign,
±∆ ρ
M (t) = det( ti−
∗ − i+
∗ ) Tor(N, c∗
N , h∗
N )
Tor(S, c∗
S, h∗
S)
is a polynomial in t. The one variable case in Theorem 12 is proved.
Remark 15. A result similar to Lemma 13 can be found in [KL99, Proposition 3.6].
