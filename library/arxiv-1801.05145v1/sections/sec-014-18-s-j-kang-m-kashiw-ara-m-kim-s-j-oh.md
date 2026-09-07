---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-014-18-s-j-kang-m-kashiw-ara-m-kim-s-j-oh
section_title: "S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH"
section_number: 18
pages: 18-20
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
be the associated quantum group and the KLR algebras, respec tively. Then there exists
a Z[q±1]-algebra isomorphism
U −
q (g)∨
Z[q±1] ≃K(R-gmod).(2.2)
KLR algebras also categorify the upper global bases.
Deﬁnition 2.1.3. We say that a KLR algebra R is symmetric if Qi,j(u,v ) is a poly-
nomial in u −v for all i,j ∈I.
In particular, the corresponding generalized Cartan matrix A is symmetric. In sym-
metric case, we assume ( αi,αi) = 2 for i ∈I.
Theorem 2.1.4 ([
40, 39]). Assume that the KLR algebra R is symmetric and the base
ﬁeld k is of characteristic 0. Then under the isomorphism (2.2) in Theorem 2.1.2, the
upper global basis corresponds to the set of the isomorphism classes of self-dual simple
R-modules.
2.2. R-matrices for KLR algebras.
For |β| =n and 1 ≤a<n , we deﬁne ϕa ∈R(β) by
ϕae(ν) =



(
τaxa −xaτa
)
e(ν) if νa =νa+1,
τae(ν) otherwise.
They are called the intertwiners. Since {ϕa}1≤a<n satisﬁes the braid relation, ϕw :=
ϕi1 · · ·ϕiℓ does not depend on the choice of reduced expression w =si1 · · ·siℓ.
Form,n ∈ Z≥0, let us denote by w[m,n ] the element of Sm+n deﬁned by
w[m,n ](k) =
{
k +n if 1 ≤k ≤m,
k −m if m<k ≤m +n.
Let β,γ ∈ Q+ with |β| = m, |γ| = n, and let M be an R(β)-module and N an
R(γ)-module. Then the map M ⊗N → N ◦M given by u ⊗v ↦− →ϕw[n,m](v ⊗u) is
R(β) ⊗R(γ)-linear, and hence it extends to an R(β +γ)-module homomorphism
RM,N : M ◦N − − →N ◦M.
Assume that the KLR algebra R(β) is symmetric. Let z be an indeterminate which
is homogeneous of degree 2, and let ψz be the graded algebra homomorphism
ψz : R(β) → k[z] ⊗R(β)
given by
ψz(xk) = xk +z, ψ z(τk) = τk, ψ z(e(ν)) = e(ν).
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 19
For an R(β)-module M, we denote by Mz the
(
k[z] ⊗R(β)
)
-module k[z] ⊗M with
the action of R(β) twisted by ψz. Namely,
e(ν)(a ⊗u) = a ⊗e(ν)u,
xk(a ⊗u) = (za) ⊗u +a ⊗(xku),
τk(a ⊗u) = a ⊗(τku)
for ν ∈ Iβ, a ∈ k[z] and u ∈ M. Note that the multiplication by z on k[z] induces
an R(β)-module endomorphism on Mz. For u ∈ M, we sometimes denote by uz the
corresponding element 1 ⊗u of the R(β)-module Mz.
For a non-zero M ∈R(β)-mod and a non-zero N ∈R(γ)-mod,
let s be the order of zero of RMz,N : Mz ◦N − − →N ◦Mz; i.e., the
largest non-negative integer such that the image of RMz,N is contained
in zs(N ◦Mz).
(2.3)
Note that such an s exists because RMz,N does not vanish ([
14, Proposition 1.4.4 (iii)]).
We denote by Rren
Mz,N the morphism z−sRMz,N .
Deﬁnition 2.2.1. Assume that R(β) is symmetric. For a non-zero M ∈ R(β)-mod
and a non-zero N ∈R(γ)-mod, let s be an integer as in (2.3). We deﬁne
rM,N : M ◦N →N ◦M
by
rM,N =Rren
Mz,N |z=0,
and call it the renormalized R-matrix .
By the deﬁnition, the renormalized R-matrix rM,N never vanishes.
We deﬁne also
rN,M : N ◦M →M ◦N
by
rN,M =
(
(−z)−tRN,Mz
)
|z=0,
where t is the order of zero of RN,Mz .
If R(β) and R(γ) are symmetric, then s coincides with the order of zero of RM,Nz,
and
(
z−sRMz,N
)
|z=0 =
(
(−z)−sRM,Nz
)
|z=0 (see, [ 15, (1.11)]).
By the construction, if the composition ( N1 ◦ rM,N2
) ◦ (rM,N1
◦N2) for M,N 1,N 2 ∈
R-mod doesn’t vanish, then it is equal to rM,N1◦N2
.
Deﬁnition 2.2.2. A simple R(β)-moduleM is called real if M ◦M is simple.
The following lemma was used signiﬁcantly in [ 15].
