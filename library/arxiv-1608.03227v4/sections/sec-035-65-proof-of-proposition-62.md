---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-035-65-proof-of-proposition-62
section_title: "Proof of proposition 6.2"
section_number: 6.5
pages: 35-37
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
ik∗◦p∗
k(F) ⋆ik∗◦p∗
k(G) = ik∗◦p∗
k(F ⋆G),
where F = F1 ⊠F2, G = G1 ⊠G2 ∈MFsc
B2
k(X ◦
2 (Gk), W) × MFsc
B2
n−k(X ◦
2 (Gn−k), W). The LHS of the later
formula is the result of the application of the functor CEn(2)
n
combined with extraction of T (2) invariant part
to the matrix factorization C such that:
(6.20)
C♯= ˜F ⊗[Πk
−−(X), Πk
++(Y1 −Adg12(Y2))] ⊗Kπ∗
12(δkW2)(Πk
−−(g12))⊗
˜G ⊗[Πk
−−(Ad−1
g12(X)), Πk
++(Y2 −Adg23(Y3))] ⊗Kπ◦∗
23 (δkW2)(Πk
−−(g23)).
with ˜F = jk∗
n ◦ρ∗
k(F′) and ˜G = jk∗
n ◦ρ∗
k(G′) in conventions of subsection 6.2: jk∗
n (F′) = p∗
k(F), jk∗
n (G′) = p∗
k(G).
Let us ﬁx coordinates X, g23, g13, Y1, Y2, Y3 on X ◦
3 (Gn). We use the factor [Πk
−−(X), Πk
++(Y1−Adg12(Y2))]
to exclude the variables Πk
−−(X) from the other factors. Since Πk
−−(X) is B2
n-equivariant, the exclusion
process uses only the row transformations of the ﬁrst kind and we do not need to worry about the admissibility
conditions. The elimination process changes the factor in (6.20) in the following manner:
˜F →˜F1 := ˜F|Πk
−−(X)=0,
˜G →˜F1 := ˜F|Πk
−−(Ad−1
g12 (X))=0
[Πk
−−(X), Πk
++(Y1 −Adg12(Y2))] →[Πk
−−(X), R1],
[Πk
−−(Ad−1
g12(X)), Πk
++(Y2 −Adg23(Y3))] →[0, Πk
++(Y2 −Adg23(Y3))],
Kπ◦∗
12 (δkW2)(Πk
−−(g12)) →Kπ∗
12(δkW2)(Πk
−−(g12))|Πk
−−(X)=0,
Kπ◦∗
12 (δkW2)(Πk
−−(g23)) →Kπ◦∗
23 (δkW2)(Πk
−−(g23))|Πk
−−(X)=0
We denote the resulting equivariant matrix factorization as C1. The non-equivariant limit C♯
1 is the product of
the above listed terms. Moreover, since the only term in C♯
1 that depends on Πk
−−(X) is the Koszul matrix
factorization [Πk
−−(X), R1], we conclude that R1 is the derivative of the potential π◦∗
13(W) by variables
Πk
−−(X) which equals Πk
++(Y1 −Adg13(Y3)).
Next let us observe that using the row transformations of the ﬁrst kind we can show that the following
equivalence of the matrix factorization
Kπ◦,∗
12 (δkW2)(Πk
−−(g12)) ⊗Kπ◦∗
23 (δkW2)(Πk
−−(g23))|Πk
−−(X)=0
= Kπ◦∗
13 (δkW2)(Πk
−−(g13)) ⊗K0(Πk
−−(g23))|Πk
−−(X)=0
Finally, we use the Koszul complex K0(Πk
−−(g23))|Πk
−−(X)=0 to exclude the variables Πk
−−(g23) from the
product; for that we use the ﬁrst type row transformations so we do not need to worry about the admissibility.
The ﬁnal result of the sequence of row transformations is the equivariant matrix factorizations C2 such that
its non-equivariant limit C♯
2 is the product the following factors:
˜F2 := ˜F|Πk
−−(X)=0,Πk
−−(g23)=0,
˜G2 := ˜F|Πk
−−(Ad−1
g12 (X))=0,Πk
−−(g23)=0
[Πk
−−(X), Y1 −Adg13(Y3)],
[0, Πk
++(Y2 −Adg23(Y3))],
Kπ◦∗
13 (δkW2)(Πk
−−(g13)) ⊗K0(Πk
−−(g23))|Πk
−−(X)=0.
Since the potential π◦∗
13(δkW2) does not depend on Πk
−−(X) the last product is actually just
Kπ◦∗
13 (δkW2)(Πk
−−(g13)) ⊗K0(Πk
−−(g23)).
35
Let us introduce auxiliary space Zcon(Gn) := gn × Pk × Gn × nn × (nk × nn−k) × nn and Zcon(Pk) :=
pn × Pk × Pk × nn × (nk × nn−k) × nn. The variety Zcon(Gn) is a subspace of X ◦
3 deﬁned by equations
Πk
++(Y2 −Adg23(Y3)) = 0, Πk
−−(g23) = 0, thus we can deﬁne the map π◦
13 : Zcon(Gn) →X ◦
2 (Gn) by the
restriction.
We can contract diﬀerentials in complexes [0, Πk
++(Y2 −Adg23(Y3))], Πk
−−(g23) to obtain homotopy equiv-
alence of matrix factorizations over π◦,∗
13 (C[X ◦
2 (Gn)]):
C2 ∼C3,
where C3 ∈MFsc
B2n(Zcon(Gn), π◦
13(W)). Moreover, since we only used admissible row transformations the
matrix factorization C3 has a structure of quasi-Koszul matrix factorization:
C3 = ( ˜
M ⊗Λ•V, d+ + D + d−, ∂+ ∂−),
where V is space dual to span of equations Πk
−−(X), Πk
−−(g13), d+ is the corresponding Koszul diﬀerential
d+ : ˜
M ⊗Λ•V →˜
M ⊗Λ•−1V, and d−: ˜
M ⊗Λ•V →˜
M ⊗Λ•+1V the completing diﬀerentials and ∂−=
P
i>j ∂−
ij,
∂ij : Λi(n2
n) ⊗˜
M ⊗Λ•V →Λj(n2
n) ⊗˜
M ⊗Λ≥•V,
( ˜
M, D, ∂) ∈ModB3
n
per(Z(Gn)).
The locus inside Zcon(Gn) deﬁned by the equations Πk
−−(X) = 0, Πk
−−(g13) = 0 is isomorphic to Zcon(Pn),
by construction
( ˜
M, D, ∂)|Πk
−−(X)=0,Πk
−−(g13)=0 = p∗
k(π◦∗
12(F) ⊗π◦∗
23(G)),
where pk : Zcon(Pk) →X ◦
3 (Gk) × X ◦
3 (Gn−k) is the natural projection.
Hence we can use uniqueness
lemma 3.6 to imply that we have an isomorphism of B3
n equivariant matrix factorizations
C3 = i∗(p∗
k(π◦∗
12(F) ⊗π◦∗
23(G)),
where i is map Zcon(Pk) →Zcon(Gn).
The Lie algebra n(2) does not act on variables Πk
−−(X) and Πk
−−(g13) hence we have
CEn(2)(C3) = i∗(CEn(2)(p∗
k(π◦∗
12(F) ⊗π◦∗
23(G)))).
Let us denote by Ik the kernel of the projection homomorphism Pk →Bk × Bn−k and let I′
k be its
unipotent part. Hence we have the short exact sequence of Lie algebras:
0 →Lie(I′
k) →nn →nk ⊕nn−k →0
and we can use Hochschild-Serre spectral sequence to compute functor CEn(2)
n :
CEn(2)
k
⊕n(2)
n−k(CELie(I′
k)(C3)) ⇒CEn(2)
n (C1).
Since the Lie algebra n(2) only acts on on the second copy of Pk in the product Zcon(Pn) = pn ×Pk ×Pk ×
nn × (nk × nn−k) × nn and the diﬀerentials in p∗
k(π◦∗
12(F) ⊗π◦∗
23(G)) are also I′
k invariant, the computation of
CELie(I′
k)(p∗
k(π◦∗
12(F) ⊗π◦∗
23(G))) reduces to the computation of
H∗
Lie(Lie(I′
k), C[Zcon(Pk)]) = C[nn × Pk × nn × (nk × nn−k) × nn] ⊗H∗
Lie(Lie(I′
k), C[Pk]).
The last computation is equivalent to the following
36
Proposition 6.3.
CELie(I′
k)(C[Pk]) = C[Gk × Gn−k],
where Gk × Gn−k is the subgroup of Pk deﬁned by the equation Πk
++(g) = 0.
Proof. The group Ik acts on Pk by right multiplication. The Lie algebra Lie(I′
k) is generated by the elements
Eij, i ∈[1, n], j ∈[k + 1, n] and direct computation shows that it is a commutative algebra.
Let us denote by E∨
kl the generators of the algebra C[Pk]: E∨
kl(X) = Xkl. Let us denote by ∂ij the
diﬀerential operator corresponding to the action Eij ∈Lie(I′
k). The action of these generators of Lie(I′
k) is
given by:
∂ij =
X
k+1≤l≤n
E∨
jl
∂
∂E∨
il
.
Let us observe that vector of diﬀerential operators ∂i• is related to the vector of diﬀerential operators
∂
∂E∨
i• , • ∈[k + 1, n] by the matrix M = (E∨
lm)l,m∈[k+1,n] and this matrix is invertible. Thus the condition
∂ij(f) = 0 for all i, j is equivalent to the condition
∂f
∂E∨
ij = 0 for all i, j ∈[k + 1, n].
Since the operator
∂
∂E∨
ij is surjective on C[Pk] the statement of the proposition follows.
✷
The proposition implies that CELie(I′
k)(C[Zcon(Pk)]) = C[Zcon(Gk × Gn)] where Zcon(Gk × Gn) := pn ×
Pk × Gk × Gn−k × nn × (nk × nn−k) × nn. Thus the proposition implies that
CEn(2)(C3) = i′
∗(CEnk⊕nn−k((p′
k)∗(π◦∗
12(F) ⊗π◦∗
23(G)))),
where i′ : Zcon(Gk × Gn−k) →Zcon(Gn) and p′
k : Zcon(Gk × Gn−k) →X ◦
3 (Gk) × X ◦
3 (Gn−k).
Hence after extracting the torus invariant part of the last expression we obtain the formula from the
statement of the proposition:
π◦
13∗(CEn(2)(C3))T (2) = i∗
k ◦p∗
k(F¯⋆G).
