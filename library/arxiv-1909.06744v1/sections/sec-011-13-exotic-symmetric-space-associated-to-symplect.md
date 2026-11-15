---
doc_id: arxiv-1909.06744v1
doc_title: "Springer correspondence for symmetric spaces"
section_id: sec-011-13-exotic-symmetric-space-associated-to-symplect
section_title: "§13. Exotic symmetric space associated to symplectic groups"
section_number: null
pages: 14-16
source_pdf: 1909.06744v1.pdf
source_sha256: 82e3980da78c07da
toc_source: inferred
doc_brief: "Springer correspondence for symmetric spaces — This is a survey on the Springer correspondence for symmetric spaces."
---
We now consider the case of exotic symmetric space associated to symplectic
groups. So assume that H = SpN and X = Gιθ
uni × V . The fact that the set of
H-orbits in X is parametrized by Pn,2 was ﬁrst proved by Kato [K1]. The following
is a reformulation of Kato’s result due to [AH].
Let Mn be the maximal isotropic subspace in V , stable by BH. There exists a
θ-stable Levi subgroup L ⊂G such that Lθ ≃GL(Mn). Then we have embeddings
(13.1)
Lιθ
uni × Mn ⊂Gιθ
uni × V ⊂Guni × V.
Note that the left hand side and the right hand side of (13.1) are enhanced varieties
discussed in Section 7; GL(Mn) acts on Lιθ
uni × Mn diagonally, and their orbits are
15
parametrized by Pn by Lemma 7.1. In turn, G acts on Guni × V diagonally, and
their orbits are parametrized by P2n by Lemma 7.1. We have
Lemma 13.1 ([K1], [AH]). Let λ ∈Pn,2, and λ ∪λ ∈P2n,2. Let OL
λ be the
GL(Mn)-orbit corresponding to λ, and Oλ∪λ the G-orbit corresponding to λ ∪λ.
Then Oλ is the unique H-orbit in X such that
OL
λ ⊂Oλ ⊂Oλ∪λ.
The analogue of Lemma 7.2 and Remark 7.3 also hold for Gιθ
uni × V .
Proposition 13.2. Let Oλ be an H-orbit in Gιθ
uni × V corresponding to λ ∈Pn,2.
(i) For z = (x, v) ∈Gιθ
uni × V , ZH(z) is connected.
(ii) Oλ = `
µ≤λ Oµ, namely the closure relations are described by the dominance
order on Pn,2.
In this case, the map π : f
X →X in Section 11 is given as follows;
f
X = {(x, v, gBH) ∈Gιθ
uni × V × BH | g−1xg ∈Bιθ, g−1v ∈Mn},
X =
[
g∈H
g(Uιθ × V ) = Gιθ
uni × V,
and π : (x, v, gBH) 7→(x, v).
Let Wn be the Weyl group of H = SpN, namely the Weyl group of type Cn. It
is known that W ∧
n ≃Pn,2, we denote by eVλ irreducible representation of Wn cor-
responding to λ ∈Pn,2. (Note the diﬀerence from Vλ, which was deﬁned in (8.3).)
The following theorem was ﬁrst proved by Kato [K1] by applying the Ginzburg the-
ory of Hecke algebras, and then reproved by [SS, I] in the framework of Lusztig’s
theory of the generalized Springer correspondence.
Theorem 13.3. π∗¯Ql[dim X ] is a semisimple perverse sheaf on X , equipped with
Wn-action, and is decomposed as
π∗¯Ql[dim X ] ≃
M
λ∈Pn,2
eVλ ⊗IC(Oλ, ¯Ql)[dim Oλ].
The geometric realization of double Kostka polynomials in terms of Gιθ
uni × V
was conjectured in [AH], and was proved by [K3], [SS, II], independently. In [SS,II],
it is proved by making use of the discussion on character sheaves due to Lusztig
[L4].
Theorem 13.4. For λ ∈Pn,2, put Aλ = IC(Oλ, ¯Ql). Then we have
(i) H iAλ = 0 unless i ≡0 (mod 4).
(ii) For z ∈Oµ ⊂Oλ,
(13.2)
eKλ,µ(t) = ta(λ) X
i≥0
(dim H 4i
z Aλ)t2i.
16
Compare the formula (13.2) with the formula (9.4) in the enhanced case. The
correspondence H 4i ↔t2i in (13.2) is more natural than the correspondence H 2i ↔
t2i in (9.4). Note that the modulo 4 vanishing of the cohomology of Aλ was ﬁrst
noticed by Grojnowski [Gr].
For z = (x, v) ∈Gιθ
uni × V , consider the Springer ﬁbre
π−1(z) ≃BH
z = {gBH ∈BH | g−1xg ∈Bιθ, g−1v ∈Mn}.
Then Hi(BH
z , ¯Ql) has a structure of Wn-module, which is an analogue of the Springer
representations. By using the Springer representation of Wn, we obtain an expression
of double Kostka polynomials, which is an analogue of Corollary 6.2.
Corollary 13.5. Assume that z ∈Oµ. Then Hi(BH
z , ¯Ql) = 0 unless i ≡0 (mod 4),
and we have
eKλ,µ(t) = ta(λ) X
i≥0
⟨H4i(BH
z , ¯Ql), eVλ⟩Wn t2i.
