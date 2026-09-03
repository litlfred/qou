---
doc_id: arxiv-0709.3157v1
doc_title: "V . Mateu"
section_id: sec-001-qcd-in-the-presence-of-external-sources
section_title: "QCD in the presence of external sources"
section_number: null
pages: 2-3
source_pdf: 0709.3157v1.pdf
source_sha256: 22a0d9a93c9dcb8d
doc_brief: "V . Mateu — The implementation of tensor sources in Chiral Lagrangians allows the computation of Green functions and form factors involving tensor currents , that is, quark bilinears of the form ¯qi"
---
The external ﬁeld method was ﬁrst introduced by Leutwyler [9 ], and makes easier the
computation of QCD Green functions and form factors. It enforces chiral Ward identities
exactly by promoting the global chiral symmetry to a local on e. The basic idea is to
introduce in the QCD action a set of local ﬁelds coupled to the QCD currents :
Z[vμ ,aμ,s, p, ¯t μν] =
∫
D ¯q Dq DGμ exp
[
i
∫
d4x
{
L 0
QCD + Lext(vμ,aμ,s, p, ¯tμν)
}]
,
(1)
where L 0
QCD is the massless QCD Lagrangian and
Lext = ¯q γμ (vμ + γ5 aμ )q − ¯q (s − i γ5 p)q + ¯q σμν ¯t μν q , (2)
where vμ, aμ, s, p and ¯t μν are hermitian matrices in ﬂavor space. The vector and axial-
vector external ﬁelds are chosen to be traceless in ﬂavor space, but the rest of them will
in general have a non-vanishing trace. For making the chiral symmetry transformations
manifest, one uses the left– and right–handed fermion ﬁelds . Then the tensor source is
split as [8]
¯q σμν ¯t μνq = ¯qLσ μνt†
μνqR + ¯qR σ μνt μνqL , (3)
with
t μν = Pμνλ ρ
L ¯t λ ρ, Pμνλ ρ
R = 1
4 (gμλ gνρ −gνλgμρ +i εμνλ ρ) , Pμνλ ρ
L =
(
Pμνλ ρ
R
) †
. (4)
It is not difﬁcult to check that PL R are chiral projectors, and then t μν and t †
μν are the
left– and right–handed projections of the tensor ﬁeld ¯t μν. So the tensor source is its own
chiral partner, as one expects from the fact that γ5 σ μν is not independent from σ μν.
We want Lext to have the same symmetries as L 0
QCD. Moreover we want chiral
symmetry to hold even at a local level, that is, invariance un der the transformation
qL R → gL R(x) qL R, with gL R(x) SU(n f )L R matrices. We cannot impose local invariance
on Lext and L 0
QCD separately : it must be done on Lext + L 0
QCD, being the ℓμ = vμ +aμ
and rμ = vμ − aμ the analogs of gauge ﬁelds. It is customary to group the scala r and
pseudoscalar sources in the combination χ = 2B0 (s +i p), being B0 related to the quark
condensate. Then local chiral invariance dictates the tran sformation properties of the
external sources to be :
rμ → gR rμ g†
R + ig R
∂μ g†
R , ℓ
μ → gL ℓμ g†
L + ig L
∂μ g†
L ,
χ → gR χ g†
L , t
μν → gR t μν g†
L . (5)
