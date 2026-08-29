---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-011-linear-sigma-model
section_title: "Linear sigma model"
section_number: null
pages: 16-17
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
Spontaneous symmetry breaking occurs if the ground state ha s a lower symmetry than the Hamiltonian.
For example, in the linear sigma model [Schwinger, 1957], [G ell-Mann and L´ evy, 1960], the Lagrangian
is constructed in terms of the O(4) multiplet ( σ,π 1,π 2,π 3),
L = 1
2 (∂µσ∂ µσ +∂µ⃗ π·∂µ⃗ π) − m2
2 (σ2 +⃗ π2) − λ
4 (σ2 +⃗ π2)2, (60)
whereλ> 0. Under parity we assume σ(t,⃗ x) ↦→σ(t, −⃗ x) and πi(t,⃗ x) ↦→ −πi(t, −⃗ x). The Lagrangian is
invariant under the inﬁnitesimal transformations





σ
π1
π2
π3




 ↦→





σ′
π′
1
π′
2
π′
3




 =
(
/BD −i
6∑
a=1
ǫaTa
)





σ
π1
π2
π3




,
where the six 4 × 4 matrices are given by
T1 =





0 0 0 0
0 0 0 0
0 0 0 −i
0 0 i 0




, T 2 =





0 0 0 0
0 0 0 i
0 0 0 0
0 −i 0 0




, T 3 =





0 0 0 0
0 0 −i 0
0 i 0 0
0 0 0 0




,
T4 =





0 −i 0 0
i 0 0 0
0 0 0 0
0 0 0 0




, T 5 =





0 0 −i 0
0 0 0 0
i 0 0 0
0 0 0 0




, T 6 =





0 0 0 −i
0 0 0 0
0 0 0 0
i 0 0 0




.
The linear combinations Ri = (Ti +Ti+3)/2 and Li = (Ti −Ti+3)/2,i = 1, 2, 3, satisfy the commutation
relations corresponding to an SU(2) ×SU(2) Lie group. The multiplet ( σ,π 1,π 2,π 3) transforms according
to the ( 1
2, 1
2 ) representation. By choosing m2 < 0, the symmetry is realized in the Nambu-Goldstone
mode [Nambu, 1960], [Goldstone, 1961]. Let us assume that th e ground state is characterized by the
vacuum expectation values
⟨σ⟩=v ≡ −
√
−m2
λ , ⟨πi⟩= 0. (61)
Introducing σ =v +σ′, the Lagrangian reads
L = 1
2 (∂µσ′∂µσ′ +∂µ⃗ π·∂µ⃗ π)+ 1
2 (−2m2)σ′2+λvσ ′(π2
1 +π2
2 +π2
3 +σ′2)+λ
4 (π2
1 +π2
2 +π2
3 +σ′2)2−λ
4v4. (62)
The ground-state conﬁguration is no longer invariant under the full group O(4). While the generators
T1,T2, and T3 annihilate the ground state of Eq. (61), the generators T4,T5, and T6 do not. The model-
independent feature of the above example is given by the fact that for each of the three generators T4,T5,
and T6 which do not annihilate the ground state one obtains a massless Goldstone boson. This is why
Eq. (62) contains no mass terms for the pions. In fact, the num ber of Goldstone bosons is determined
by the structure of the symmetry groups [Goldstone et al., 19 62]. Let G denote the symmetry group
of the Lagrangian with nG generators and the subgroup H the symmetry group of the ground state
with nH generators. For each generator which does not annihilate th e vacuum one obtains a massless
Goldstone boson, i.e., the total number of Goldstone bosons equals nG −nH.
The Lagrangians used in motivating the phenomenon of a spontaneous symmetry breakdown are
typically constructed in such a fashion that the degeneracy of the ground states is built into the potential
16
at the classical level (the prototype being the “Mexican hat ” potential). As in the above case, it is then
argued that an elementary Hermitian ﬁeld of a multiplet transforming non-trivially u nder the symmetry
groupG acquires a vacuum expectation value signaling a spontaneou s symmetry breakdown. However,
there also exist theories such as QCD where one cannot infer f rom inspection of the Lagrangian whether
the theory exhibits spontaneous symmetry breaking. Rather , the criterion for spontaneous symmetry
breaking is a non-vanishing vacuum expectation value of som e Hermitian operator, not an elementary
ﬁeld, which emerges through the dynamics of the underlying t heory. In particular, we will see that the
quantities developing a vacuum expectation value may also b e local Hermitian operators composed of
more fundamental degrees of freedom of the theory.
While the model of Eq. (60) is constructed to illustrate the c oncept of a spontaneous symmetry
breaking, it is not fully understood theoretically why QCD s hould exhibit this phenomenon. We will ﬁrst
