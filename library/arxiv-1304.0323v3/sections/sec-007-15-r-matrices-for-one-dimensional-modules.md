---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS"
section_id: sec-007-15-r-matrices-for-one-dimensional-modules
section_title: "R-matrices for one-dimensional modules"
section_number: 1.5
pages: 19-21
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
of elements in I. Let L(µ) be a free k-module ku(µ) with the generator u(µ) of degree
0. The following lemma can be easily veriﬁed.
Lemma 1.5.1. By deﬁning
xku(µ) = 0, τ ku(µ) = 0, e (ν)u(µ) = δν,µu(µ),
L(µ) becomes an R(αµ1 +··· +αµn) -module if and only if
(a) (αµk,αµk+1)< 0 for 1≤k <n,
(b) if µk =µk+2 (1≤k≤n− 2), then⟨hµk,αµk+1⟩⁄=−1.(1.5.1)
Now we assume (
1.3.5); i.e., R is a symmetric Khovanov-Lauda-Rouquier algebra.
The following lemma immediately follows from the deﬁnition.
Lemma 1.5.2. Let µ = ( µ1,...,µ m) and ν = ( ν1,...,ν n) be a pair of sequences
satisfying (
1.5.1). If µi⁄=νj for any 1≤i≤m and 1≤j≤n, then
RL(µ)z,L(ν)z′
(
u(µ)z⊗u(ν)z′
)
=τn,m
(
u(ν)z′⊗u(µ)z
)
.
We shall use the following lemma later in the type A case.
20 S.-J. KANG, M. KASHIW ARA, M. KIM
Lemma 1.5.3. Leti∈I and let µ = (µ1,...,µ n) be a sequence satisfying (
1.5.1). Set
β = ∑ n
k=1αµk and p = (β,αi)n. Then we have
RL(µ)z,L(i)z′ (u(µ)z⊗u(i)z′)
=
(
(z′−z)pτn··· τ1 +δµn,i(z′−z)p−1τn−1··· τ1
)(
u(i)z′⊗u(µ)z
)
,
RL(i)z,L(µ)z′ (u(i)z⊗u(µ)z′)
=
(
(z′−z)pτ1··· τn +δµ1,i(z′−z)p−1τ2··· τn
)(
u(µ)z′⊗u(i)z
)
.
Proof. We shall prove only the second formula. We prove it by induction on n. Since
n = 1 case is obvious, assume that n> 1. Set µ′ = (µ2,...,µ n) and j =µ1.
First assume that i⁄=j. Then we have
RL(i)z,L(j)z′◦L(µ′)z′ (u(i)z⊗u(j)z′⊗u(µ′)z′)
=
(
L(j)z′◦RL(i)z,L(µ′)z′
)
·
((
RL(i)z,L(j)z′ (u(i)z⊗u(j)z′)
)
⊗u(µ′)z′
)
=
(
L(j)z′◦RL(i)z,L(µ′)z′
) (
τ1(u(j)z′⊗u(i)z)⊗u(µ′)z′
)
=τ1
(
L(j)z′◦RL(i)z,L(µ′)z′
) (
u(j)z′⊗u(i)z⊗u(µ′)z′
)
=τ1
(
u(j)z′⊗RL(i)z,L(µ′)z′ (u(i)z⊗u(µ′)z′)
)
=τ1
(
u(j)z′⊗
((
(z′−z)pτ1··· τn−1 +δi,µ2(z′−z)p−1τ2··· τn−1
)
(u(µ′)z′⊗u(i)z)
) )
.
Hence we obtain
RL(i)z,L(µ)z′ (u(i)z⊗u(µ)z′)
=
(
(z′−z)pτ1(τ2··· τn) +δi,µ2(z′−z)p−1τ1(τ3··· τn)
)
(u(µ)z′⊗u(i)z).
Then the last term vanishes since τ1u(µ)z′ = 0.
Now assume that i =µ1. Then µ2⁄=i. Since we have
RL(i)z,L(i)z′ (u(i)z⊗u(i)z′) = ( τ1(x1−x2) + 1)(u(i)z′⊗u(i)z)
= (( z′−z)τ1 + 1)(u(i)z⊗u(i)z′),
which gives
RL(i)z,L(j)z′◦L(µ′)z′ (u(i)z⊗u(j)z′⊗u(µ′)z′)
=
(
L(j)z′◦RL(i)z,◦L(µ′)z′
) ((
(z′−z)τ1 + 1
)
u(i)z′⊗u(i)z⊗u(µ′)z′
)
= ((z′−z)τ1 + 1)(z′−z)p−1τ2··· τn(u(i)z′⊗u(µ′)z′⊗u(i)z).
Hence we obtain the desired result. □
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 21
