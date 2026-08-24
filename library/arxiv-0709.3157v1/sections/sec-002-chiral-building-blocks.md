---
doc_id: arxiv-0709.3157v1
doc_title: "V . Mateu"
section_id: sec-002-chiral-building-blocks
section_title: "Chiral building blocks"
section_number: null
pages: 3-3
source_pdf: 0709.3157v1.pdf
source_sha256: 22a0d9a93c9dcb8d
doc_brief: "V . Mateu — The implementation of tensor sources in Chiral Lagrangians allows the computation of Green functions and form factors involving tensor currents , that is, quark bilinears of the form ¯qi"
---
χPT is based on the spontaneous breakdown of the global G = SU(n f )L ⊗ SU(n f )R
ﬂavour symmetry down to its subgroup SU(n f )V . The dynamical ﬁelds φa = (π,K, η)
are assumed to be the (pseudo–)Goldstone bosons associated to this breakdown. The
general formalism for effective Lagrangians with spontaneously broken symmetries was
worked out by Callan, Coleman, Wess and Zumino [10], and for o ur case groups the
n2
f − 1 ﬁelds in the matrix u transforming under G as
u(φa) = exp
( i
2F0
φa λa
)
, u(φa) → gR u(φa)h† = hu (φa)g†
L . (6)
h is the so called compensating ﬁeld and depends on gL R and u itself. Eq. (6) deﬁnes a
non–linear representation of the chiral group G.
At very low energies,
φa are the only active ﬁelds and thence u is the only building
block of the theory. Then the QCD action in this regime reads
Z[vμ,aμ,s, p, ¯t μν] =
∫
D uDu† exp
[
i
∫
d4x Lχ(u;vμ,aμ,s, p, ¯tμν)
]
, (7)
where Lχ necessarily is invariant under the same set of transformations as Lext + L 0
QCD
is invariant.
The ﬁrst step to ﬁnd the most efﬁcient set of building blocks i s to manipulate ℓμ and
rμ in such a way that the derivative is not explicit :
F μν
L = ∂μ ℓν − ∂νℓμ − i [ℓμ, ℓν] , F μν
R = ∂μrν − ∂νrμ − i [rμ,rν] .
uμ = i
{
u†(∂μ − ir μ)u − u(∂μ − i ℓμ)u†
}
uμ → hu μ h† . (8)
Since it will prove to be very convenient to have a set of opera tors transforming as uμ
under G, we use the set introduced in Refs. [4, 11]
hμν = ∇ μuν + ∇ νuμ , f μν
± = uF μν
L u† ± u† F μν
R u ,
t μν
± = u† t μν u† ± ut μν † u , χ± = u† χ u† ± u χ† u . (9)
As a result, one can deﬁne a unique covariant derivative for them all, e.g.,
∇ ρX = ∂ρX + [Γρ,X ] , Γρ = 1
2
{
u†(∂ρ − ir ρ)u + u(∂ρ − i ℓρ)u†
}
, (10)
