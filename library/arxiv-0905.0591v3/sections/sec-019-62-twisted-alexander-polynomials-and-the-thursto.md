---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-019-62-twisted-alexander-polynomials-and-the-thursto
section_title: "Twisted Alexander polynomials and the Thurston norm"
section_number: 6.2
pages: 21-23
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
of Alexander that given a knot K ⊂S3 the following inequality holds:
2genus(K) ≥ deg(∆ K ).
This result was ﬁrst generalized to general 3–manifolds by M cMullen [McM02] and then to
twisted Alexander polynomials in [FK06]. The following the orem is [FK06, Theorem 1.1].
The proof builds partly on ideas of Turaev’s in [Tu02b].
Theorem 6.6. Let N be a 3–manifold whose boundary is empty or consists of tori. L et
φ ∈ H 1(N ; Z) be non–trivial and let γ : π1(N ) → GL(k,R ) be a representation such that
22 STEF AN FRIEDL AND STEF ANO VIDUSSI
∆ γ⊗φ
N ⁄= 0. Then
||φ||T ≥ 1
k deg(τ (N,γ ⊗φ)).
Equivalently,
||φ||T ≥ 1
k
(
deg(∆ γ⊗φ
N ) − deg(∆ γ⊗φ
N,0 ) − deg(∆ γ⊗φ
N,2 )
)
.
Remark. In [FK06] it was furthermore shown using ‘KnotTwister’ (cf. [Fr09]) that
twisted Alexander polynomials detect the genus of all knots with up to twelve cross-
ings.
(1) It seems reasonable to conjecture that given an irreduci ble 3–manifold N twisted
Alexander polynomials detect the Thurston norm for any φ ∈H 1(N ; Z). A positive
answer would have interesting consequences for 4–manifold topology as pointed out
in [FV09].
(2) If ∆ γ⊗φ
N = 0, then we deﬁne the torsion twisted Alexander polynomial ˜∆ γ⊗φ
N to be
the order of the R[t±1]–module
TorR[t±1](H1(N ;R[t±1]k)) =
= {v ∈H1(N ;R[t±1]k) |λv = 0 for some λ ∈R[t±1] \ {0} }.
It is then shown in [FK06, Section 4] that the ˜∆ γ⊗φ
N also gives rise to give lower
bounds on the Thurston norm. We point out that by [Hi02, Theor em 3.12 (3)]
and [Tu01, Lemma 4.9] the torsion twisted Alexander polynom ial can be computed
directly from a presentation of H1(N ;R[t±1]k).
Note that Theorem 6.6 gives lower bounds on the Thurston norm for a given φ ∈
H 1(N ; Z). In order to give bounds for the whole Thurston norm ball at o nce, we will
introduce twisted Alexander norms, generalizing McMullen ’s Alexander norm [McM02] and
Turaev’s torsion norm [Tu02a]. In the following let N be a 3–manifold with empty or
toroidal boundary such that b1(N ) > 1. Let ψ : π1(N ) → F := H1(N ; Z)/torsion be the
canonical projection map. Let γ : π1(N ) → GL(k,R ) be a representation. If ∆ γ⊗ψ
N = 0
then we set ||φ||γ
A = 0 for all φ ∈H 1(N ; R). Otherwise we write ∆ γ⊗ψ
N =∑ aifi for ai ∈R
and fi ∈F . Given φ ∈H 1(N ; R) we then deﬁne
||φ||γ
A := max{φ(fi −fj) | (fi,fj) such that aiaj ⁄= 0}.
Note that this norm is independent of the choice of represent ative of ∆ γ⊗ψ
N . Clearly this
deﬁnes a seminorm on H 1(N ; R) which we call the twisted Alexander norm of (N,γ ). Note
that if γ :π1(N ) → GL(1, Z) is the trivial representation, then we just obtain McMulle n’s
Alexander norm.
The following is proved in [FK08a, Theorem 3.1], but we also r efer to the work of Mc-
Mullen [McM02], Turaev [Tu02a], [Tu02b, Section 6], Harvey [Ha05] and Vidussi [Vi99,
Vi03]. The main idea of the proof is to combine Theorem 6.6 wit h Corollary 3.5.
Theorem 6.7. LetN be a 3–manifold with empty or toroidal boundary such that b1(N )>
1. Let ψ : π1(N ) → F := H1(N ; Z)/torsion be the canonical projection map and let
A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS 23
γ : π1(N ) → GL(k,R ) be a representation with R a Noetherian UFD. Then for any φ ∈
H 1(N ; R) we have
||φ||T ≥ 1
k ||φ||γ
A
and equality holds for any φ in a ﬁbered cone of the Thurston norm ball.
We refer to [McM02] and [FK08a] for some calculations, and we refer to [Du01] for more
information on the relationship between the Alexander norm and the Thurston norm.
