---
doc_id: arxiv-2010.12819v2
doc_title: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case"
section_id: sec-047-g1-algebraic-description-of-the-ordinary-xxz-cas
section_title: "G.1 Algebraic description of the ordinary XXZ case"
section_number: null
pages: 55-56
source_pdf: 2010.12819v2.pdf
source_sha256: ddc0493d60d48e77
toc_source: outline
doc_brief: "The action of the Virasoro algebra in quantum spin chains. I. The non-rational case — We investigate the action of discretized Virasoro generators, built out of generators of the lattice"
---
To ﬁnd the algebra relevant to the new Hamiltonian densities fj we compare to the R-matrix deﬁned in [59] 19
as R(u) = 1 +f(u)Q +g(u)E, where
f(u) = sinγ− sinu
2 sin(γ−u)− 1
2, (208a)
g(u) = sinγ + sinu
2 sin(γ−u)− 1
2 (208b)
19Section 4.2. O(2) spin model. Note that the sign convention for the oﬀ-diagonal elements in E and Q is here the opposite to
that of [59], to be consistent with the rest of this paper.
55
contain the dependence on u,γ and the operators Qj =···⊗ 1⊗Q⊗ 1⊗··· and Ej =···⊗ 1⊗E⊗ 1⊗··· ,
with
Q =


0 0 0 0
0 1 1 0
0 1 1 0
0 0 0 0

 , (209a)
E =


0 0 0 0
0 1 −1 0
0 −1 1 0
0 0 0 0

 , (209b)
both separately fulﬁl the Temperley-Lieb relations for m = 2 corresponding to q = 1. Together with relations
between operators Qj and Ek they generate an algebra VN that is further discussed in [59].
As before the Hamiltonian is found from the derivative of the transfer matrix, and we obtain from the above
R-matrix the desired Hamiltonian density
hXXZ
j =−γ
π (f′(0)Q +g′(0)E)
=−γ
π
1
2 sinγ
[( q + q−1
2 − 1
)
Q +
( q + q−1
2 + 1
)
E
]
=− γ
π sinγ


0 0 0 0
0 q+q−1
2 −1 0
0 −1 q+q−1
2 0
0 0 0 0

. (210)
Twisted boundary conditions correspond to modifying the oﬀ-diagonal elements in Q and E as in (22) and
(205).
Small-size computations (N = 4, 6) indicate that the state space of the XXZ Hamiltonian at Sz = 0,φ = 0
decomposes into a direct sum of at least two submodules under the action of the algebra VN. We shall further
see in Table 12 that at all sizes, the matrix elements ⟨a−11|LXXZ
−1 |1⟩ and⟨1|LXXZ
1 |a−11⟩ are both zero, in
accordance with what would be expected from a unitary theory. Thus the structure of the scaling limit Virasoro
modules seems to be found to at least some degree at the level of the lattice for the case of c = 1 too, and not
only for c = 1− 6
x(x+1).
