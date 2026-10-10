---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-034-35-knizhnik-zamolodchikov-differential-equations-a
section_title: "Knizhnik-Zamolodchikov differential equations, and the braiding"
section_number: 35
pages: 220-222
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
35. Knizhnik-Zamolodchikov differential equations, and the braiding
The conformal Hamiltonian determines the braiding of Rep(Vgk) explicitly. In the setting
of loop groups, formulae for the braiding may be found in [181] in the type A case and

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 221
see also Chapter 9 Lemma 6.1 in [169]. The fusion tensor product is defined via Connes
fusion, a tensor product operation of bimodules over von Neumann algebras [28]. The
braiding gives rise to certain commutation properties satisfied by four-point functions
of primary fields, called braiding properties in [181], [169] that reflect the action of the
braiding operators in the category of projective finite energy representations with Connes
fusion tensor product. We are interested to unravel the action of the braiding operators
on the corresponding lowest energy subspaces. In this way we shall be able to compare
the braiding of Rep(Vgk
) arising from the setting of loop groups directly with the braiding
that we obtain from our construction in Theorem 2.8 (a) that in turn has been unravelled
in Prop. 33.11.
We consider ϕ4, . . . , ϕ1 charged primary field of type

m4
0i3
m3
i3i2
m2
i2i1
m1
i10

respectively. The four point functions of these fields is defined as the formal Laurent
series F = (Γ, ϕ4(v4, t4). . . ϕ1(v1, t1)Γ), with Γ ∈ H0[0] of norm 1. As for the case of
a single primary field, it follows from the intertwining property that F takes values in
HomG(Vm1 ⊗ Vm2 ⊗ Vm3 ⊗ Vm4, C) = (V
∗
m4 ⊗ V
∗
m3 ⊗ V
∗
m2 ⊗ V
∗
m1
)
G. Moreover F is a formal
solution of a first order partial differential equation, called the Knizhnik-Zamolodchikov
equation,
∂F
∂ti
=
1
k + h
∨
X
j̸=i
Ωi,j
ti − tj
F
with the convention that the denominators are expanded in series in the region |t4| > · · · >
|t1| and
Ωi,j =
X
r
πi(Xr)πj (X
r
),
with Xr ∈ g a basis and Xr a dual basis, πi the action of g on the i-th factor of V
∗
m4 ⊗
V
∗
m3 ⊗ V
∗
m2 ⊗ V
∗
m1
. In particular, Ωi,i acts as the Casimir Ci.
The theory of KZ equations implies, among other things, that products of primary fields
ϕ
m3
m4,j (v3, t)ϕ
m2
j,m1
(v2, s) are single valued weakly holomorphic functions in {(t, s) : t/s /∈
[0, +∞)} on the finite energy vectors.
A braiding is determined by an isomorphism between the subspace of HomG(V2 ⊗
V3, V4) ≃ (V4 ⊗ V
∗
3 ⊗ V
∗
2
)
G of the initial terms of and that of HomG(V3 ⊗ V2, V4) ≃
(V4 ⊗ V
∗
2 ⊗ V
∗
3
)
G. We want to know the action of Ω2,3. It follows from an algebraic
manipulation that relates Ω2,3 to the Casimirs Ωi,i = Ci, as in Subsect. 32.2, i = 0, . . . , 3,
and the fact that π1 + · · · + π3 = 0 that Ω2,3 acts on this space as multiplication by
1
2
(C4 − C2 − C3). It is explained in the proof of Lemma 3.1, Chaper 7, [169], how this
action explicitly determines the braiding previously defined using the conformal hamiltonian L0 in the special case where the decomposition of H1 ⊠ H2 is multiplicity-free. This is
called abelian braiding in [181], [169]. We thus have the following corollary of this lemma
that is implicit in [169].

222 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Corollary 35.1. Let H2 and H3 be finite energy unitary projective representations of
LG such that Connes fusion tensor product is multiplicity-free. Then braiding operator
c(H2, H3) acts between the corresponding lowest energy spaces V2 and V3 respectively as
Σe
iπ
2(k+h∨)
Ω
: V2 ⊗ V3 → V3 ⊗ V2 (35.1)
where Ω acts as multiplication by C2+C3−C4 on a simple module V4 of the tensor product.
Proof. The proof follows from a decomposition of V2 ⊗ V3 into simple representations V4
and the previous discussion. □
Note that formula (35.1) is in [113], without details on the eigenvalues of Ω. On one
hand, regardless the multiplicity-free property, a braiding is completely determined by
the operators c(V, Vλ), with V the generating representation, by Prop. 5.5, provided the
associator is determined.
On the other hand, we note that in Prop. 33.11 we have derived the same formula for
the braiding as (35.1) for the special braidings c(V, Vλ), and we recall that the proof of this
fact relies on the analysis of Lemma 3.6.2 in [185].
