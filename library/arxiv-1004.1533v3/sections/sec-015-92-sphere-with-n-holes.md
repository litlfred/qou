---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-015-92-sphere-with-n-holes
section_title: "Sphere with n holes"
section_number: 9.2
pages: 36-38
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
toc_source: outline
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invariants, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
by objects Y1, . . . , Yn ∈Obj Z(C) (see Example 7.2). Choose the cell decomposition
of N as in Example 7.2; then
H(N, Y1, . . . , Yn)
=
M
X1,...,Xn,U1,...,Un∈Irr(C)
⟨X1, U1, X∗
1, . . . , Xn, Un, X∗
n⟩⊗⟨U ∗
1 , Y1⟩⊗· · · ⊗⟨U ∗
n, Yn⟩
≃
M
X1,...,Xn∈Irr(C)
⟨X1, Y1, X∗
1, . . . , Xn, Yn, X∗
n⟩.
Consider now the cylinder N ×I with the cell decomposition shown in Figure 27.
l
j1
jn
i1
in
k1
kn
Y1
Yn
Figure 27. Cylinder over sphere with n embedded disks
TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT
37
This cell decomposition contains (n + 1) 3-cells: n open tubes and one large
3-cell. Thus, the invariant Z(N × I) is given by
(Z(N × I), ϕ ⊗ϕ′) =
X
l,k1,...,kn∈Irr(C)
D · Z0 · · · · · Zn
where
ϕ = ϕ0 ⊗ϕ1 ⊗· · · ⊗ϕn ∈H(N, i1, . . . , in)
= ⟨Xi1, U1, X∗
i1, . . . , Xin, Un, X∗
in⟩⊗⟨U ∗
1 , Y1⟩⊗· · · ⊗⟨U ∗
n, Yn⟩
ϕ′ = ϕ′
0 ⊗ϕ′
1 ⊗· · · ⊗ϕ′
n ∈H(N, j1, . . . , jn)∗
= ⟨Xjn, V ∗
n , X∗
jn, . . . , Xj1, V ∗
1 , X∗
j1⟩⊗⟨V1, Y ∗
1 ⟩⊗· · · ⊗⟨Vn, Y ∗
n ⟩
D is the normalization factor:
D =
1
D2(n+1) dl
n
Y
a=1
dka
p
dia
p
dja
p
dUa
p
dVa
and Z0, . . . , Zn are the factors corresponding to the (n + 1) 3-cells of the decompo-
sition:
Z0 =
ϕ0
ϕ′
0
α1
β1
α∗
1
αn
βn
α∗
n
i1
j1
U1
V1
i1
j1
in
jn
Un
Vn
in
jn
l
l
l
Zi =
ϕi
β∗
i
ϕ′
i
Ui
Vi
Yi
ki
38
BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
Using Lemma 1.3, we see that it can be rewritten as follows:
(Z(N × I), ϕ ⊗ϕ′) =
X
l,k1,...,kn∈Irr(C)
D
ϕ0
ϕ′
0
α1
ϕ1
ϕ′
1
α∗
1
αn
ϕn
ϕ′
n
α∗
n
i1
j1
U1
Y1
V1
i1
j1
in
jn
Un
Vn
Y1
in
jn
k1
l
l
kn
l
Thus, identifying H(N, i1, . . . , in) ≃⟨Xi1, Y1, X∗
i1, . . . ) as in Example 7.2 and using
Lemma 1.1, we see that
(Z(N × I), ϕ ⊗ϕ′) =
X
l∈Irr(C)
1
D2(n+1) dl
n
Y
a=1
p
dia
p
dja
ϕ
ϕ′
Y1
Yn
i1
j1
in
jn
l
l
. . .
. . .
