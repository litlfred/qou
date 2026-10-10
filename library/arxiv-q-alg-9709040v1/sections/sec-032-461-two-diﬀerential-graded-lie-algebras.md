---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-032-461-two-diﬀerential-graded-lie-algebras
section_title: "Two diﬀerential graded Lie algebras"
section_number: 4.6.1
pages: 15-16
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
LetX be a smooth manifold. We associate with it two diﬀerential gr aded Lie algebras over R. The ﬁrst
diﬀerential graded Lie algebra Dpoly(X) is a subalgebra of the shifted Hochschild complex of the alg ebraA of
functions on X (see 3.4.2). The space Dn
poly(X), n≥− 1 consists of local Hochschild cochains A⊗(n+1)−→A
given by polydiﬀerential operators. In local coordinates ( xi) any element of Dn
poly can be written as
f0⊗... ⊗fn↦→
∑
(I0,...,I n)
CI0,...,I n (x)·∂I0 (f0)...∂ In (fn)
where the sum is ﬁnite, Ik denote multi-indices, ∂Ik denote corresponding partial derivatives, and fk and
CI0,...,I n are functions in ( xi).
The second diﬀerential graded Lie algebra, Tpoly(X) is the graded Lie algebra of polyvector ﬁelds on X:
T n
poly(X) = Γ( X,∧n+1TX ), n≥− 1
endowed with the standard Schouten-Nijenhuis bracket and w ith the diﬀerential d := 0. We remind here the
formula for this bracket:
for k,l≥ 0 [ ξ0∧... ∧ξk,η 0∧... ∧ηl] =
=
k∑
i=0
l∑
j=0
(−1)i+j+k[ξi,η j]∧ξ0∧...∧ξi−1∧ξi+1∧...∧ξk∧η0∧...∧ηj−1∧ηj+1∧...∧ηl, ξi,η j∈ Γ(X,T X ),
for k≥ 0 [ ξ0∧... ∧ξk,h ] =
=
k∑
i=0
(−1)iξi(h)·
(
ξ0∧... ∧ξi−1∧ξi+1∧... ∧ξk
)
h∈ Γ(X,OX ), ξi∈ Γ(X,T X ) .
In local coordinates ( x1,...,x d), if one replaces ∂/∂x i by odd variables ψi and writes polyvector ﬁelds
as functions in ( x1,...,x d|ψ1,...,ψ d), the bracket is
[γ1,γ 2] = γ1•γ2− (−1)k1k2γ•γ1
where introduce the following notation:
γ1•γ2 :=
d∑
i=1
∂γ1
∂ψi
∂γ2
∂xi, γi∈T ki(Rd) .
15
We have an evident map U (0)
1 :Tpoly(X)−→Dpoly(X):
U (0)
1 : (ξ0∧... ∧ξn)↦→

f0⊗... ⊗fn↦→1
(n + 1)!
∑
σ∈Σ n+1
sgn(σ)
n∏
i=0
ξσ i (fi)

 , for n≥ 0,
h↦→
(
1↦→h
)
, h∈ Γ(X,OX ) .
