---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS"
section_id: sec-008-16-uniqueness-of-r-matrices
section_title: "Uniqueness of R-matrices"
section_number: 1.6
pages: 21-22
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS R-MATRICES OF QUANTUM AFFINE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
two simple modules (after adding spectral parameters) remains sim ple.
Lemma 1.6.1. Assume that k is a ﬁeld. Let z, z′ be algebraically independent inde-
terminates and set K = k(z,z′). Let M and N be a simple R(β)-module and a simple
R(γ)-module, respectively. Then K⊗k[z,z ′](Mz◦Nz′) is a simple K⊗R(β +γ)-module.
Proof. In this proof, we write Mz for the K⊗R(β)-module K⊗k[z]Mz for the sake of
simplicity. Recall that Sm,n :={w∈ Sm+n|w(k)<w (k + 1) for any k⁄=m}. Then
we can easily see that
Mz◦Nz′ = ⨁
w∈Sm,n
ϕw·Mz⊗Nz′.
Indeed, it follows from ( 1.4.6) and the fact that xi−xj : Mz⊗Nz′ → Mz⊗Nz′ is
bijective for 1 ≤i≤m<j ≤m +n.
Let L be a non-zero K⊗R(β +γ)-submodule of Mz◦Nz′. For u∈ Mz◦Nz′, we
write
u =
∑
w∈Sm,n
ϕwuw with uw∈Mz⊗Nz′,
and set S(u) ={w∈ Sm,n|uw⁄= 0}.
Let us take a non-zero u∈ L such that the cardinality of S(u) is minimal and let
w∈S(u). Assume that there exists w′⁄=w in S(u). Since we have
{
1≤k≤m +n|w−1(k)≤m
}
⁄⊂
{
1≤k≤m +n|w′−1(k)≤m
}
,
there exists a such that 1 ≤w−1(a)≤m and m<w ′−1(a).
Take a monic polynomial f (x) such that f (xk)|N = 0 for 1 ≤k≤n. Then f (xk−z′)
acts by zero on Mz⊗Nz′ for k > m, and the action of f (xk−z′) is invertible on
Mz⊗Nz′ for k≤m. Hence f (xw′−1(a)−z′)uw′ = 0. Since
f (xa−z′)u =
∑
y∈S(u)\{w′}
ϕyf (xy−1(a)−z′)uy,
the minimality of S(u) implies that f (xa−z′)u = 0. In particular, we have f (xw−1(a)−
z′)uw = 0, which implies that uw = 0. It is a contradiction and we conclude that
S(u) ={w} and u =ϕwuw.
Since ϕw−1ϕw : Mz⊗Nz′ → Mz⊗Nz′ is a K[x1,...,x m+n]-linear isomorphism, we
haveuw∈L. Since Mz⊗Nz′ is a simpleK⊗R(β)⊗R(γ)-module, we haveMz⊗Nz′⊂
L, and we conclude that L =Mz◦Nz′. □
This lemma immediately implies the following proposition which says that an R-
matrix for simple modules is unique up to constant multiple.
22 S.-J. KANG, M. KASHIW ARA, M. KIM
Proposition 1.6.2. Assume that k is a ﬁeld and let z, z′ be independent indetermi-
nates. Let M and N be a simple R(β)-module and R(γ)-module, respectively. Then
we have
HomR(β+γ)
(
Mz◦Nz′,Mz◦Nz′
)
≃ k[z,z′],
HomR(β+γ)
(
Mz◦Nz′,Nz′◦Mz
)
≃ k[z,z′](z−z′)−sRMz,Nz′.
Heres is the order of zeroes of RMz,Nz′ (see (
1.4.8)).
Proof. The ﬁrst assertion immediately follows from the preceding lemma. The second
follows from the ﬁrst since RMz,Nz′ gives an isomorphism from K⊗k[z,z ′](Mz◦Nz′) to
K⊗k[z,z ′](Nz′◦Mz), where K = k[z,z′, (z−z′)−1]. □
