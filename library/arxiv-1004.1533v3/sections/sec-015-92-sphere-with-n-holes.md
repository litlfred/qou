---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT"
section_id: sec-015-92-sphere-with-n-holes
section_title: "Sphere with n holes"
section_number: 9.2
pages: 36-38
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
doc_brief: "TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invarian ts, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
by objects Y1,...,Y n ∈ ObjZ(C) (see Example 7.2). Choose the cell decomposition
of N as in Example 7.2; then
H(N,Y 1,...,Y n)
=
⨁
X1,...,X n,U 1,...,U n∈Irr(C)
⟨X1,U 1,X ∗
1,...,X n,U n,X ∗
n⟩ ⊗ ⟨U ∗
1,Y 1⟩ ⊗ · · · ⊗ ⟨U ∗
n,Y n⟩
≃
⨁
X1,...,X n∈Irr(C)
⟨X1,Y 1,X ∗
1,...,X n,Y n,X ∗
n⟩.
Consider now the cylinder N ×I with the cell decomposition shown in Figure 27.
l
j1
jn
i1 in
k1
kn
Y1 Yn
Figure 27. Cylinder over sphere with n embedded disks
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 37
This cell decomposition contains ( n + 1) 3-cells: n open tubes and one large
3-cell. Thus, the invariant Z(N × I) is given by
(Z(N × I),ϕ ⊗ϕ ′) =
∑
l,k 1,...,k n∈Irr(C)
D ·Z0 · · · · ·Zn
where
ϕ =ϕ 0 ⊗ϕ 1 ⊗ · · · ⊗ϕ n ∈H(N,i 1,...,i n)
= ⟨Xi1,U 1,X ∗
i1,...,X in,U n,X ∗
in ⟩ ⊗ ⟨U ∗
1,Y 1⟩ ⊗ · · · ⊗ ⟨U ∗
n,Y n⟩
ϕ ′ =ϕ ′
0 ⊗ϕ ′
1 ⊗ · · · ⊗ϕ ′
n ∈H(N,j 1,...,j n)∗
= ⟨Xjn,V ∗
n,X ∗
jn,...,X j1,V ∗
1,X ∗
j1 ⟩ ⊗ ⟨V1,Y ∗
1 ⟩ ⊗ · · · ⊗ ⟨Vn,Y ∗
n ⟩
D is the normalization factor:
D = 1
D2(n+1)dl
n∏
a=1
dka
√
dia
√
dja
√
dUa
√
dVa
andZ0,...,Z n are the factors corresponding to the ( n + 1) 3-cells of the decompo-
sition:
Z0 =
ϕ 0
ϕ ′
0
α 1 β1 α ∗
1
α n βn α ∗
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
l ll
Zi =
ϕ i
β ∗
i
ϕ ′
i
Ui
Vi
Yi
ki
38 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
Using Lemma 1.3, we see that it can be rewritten as follows:
(Z(N × I),ϕ ⊗ϕ ′) =
∑
l,k 1,...,k n∈Irr(C)
D
ϕ 0
ϕ ′
0
α 1
ϕ 1
ϕ ′
1
α ∗
1
α n
ϕ n
ϕ ′
n
α ∗
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
k1 l l knl
Thus, identifyingH(N,i 1,...,i n) ≃ ⟨Xi1,Y 1,X ∗
i1,... ) as in Example 7.2 and using
Lemma 1.1, we see that
(Z(N × I),ϕ ⊗ϕ ′) =
∑
l∈Irr(C)
1
D2(n+1)dl
n∏
a=1
√
dia
√
dja
ϕ
ϕ ′
Y1 Yni1
j1
in
jn
ll
...
...
