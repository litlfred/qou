---
doc_id: arxiv-math-0405249v5
doc_title: "Twisted homology of quantum SL(2)"
section_id: sec-004-hochschild-homology-of-hopf-algebras
section_title: "hochschild homology of hopf algebras"
section_number: null
pages: 6-7
source_pdf: 0405249v5.pdf
source_sha256: bc699482e5cd7679
doc_brief: "Twisted homology of quantum SL(2) — We calculate the twisted Hochschild and cyclic homology (in the sense of Kustermans, Murphy and Tuset) of the coordinate algebra o f the quan- tum SL(2) group"
---
For arbitrary algebras, the Hochschild homologies are deri ved functors in
the category of A⊗A op-modules, and working with explicit resolutions
usually involves lengthy calculations. But if A is a Hopf algebra then
we can describe H∗(A,M) for an arbitrary A-bimoduleM as a derived
functor in the category of A-modules. Deﬁne a right A-moduleM′ which
isM as a vector space with right action given by
m ◭a :=
∑
S(a(2))⊲m⊳a (1), a ∈A,m∈M. (15)
Consider k as the trivial A-moduleA/kerε. Feng and Tsygan proved:
proposition 2.3 [5] There is an isomorphism of vector spaces
Hn(A,M)≃ TorA
n (M′,k ).
Proof. The Tor A
n (M′,k ) are computed from the complex ( C∗,d ) (with
zeroth tensor component now being M′) with boundary map d given by
d = ˜d0 +
n−1∑
i=1
(−1)idi + (−1)n ˜dn, (16)
6
where the di are as above and
˜d0(a0,a 1,...,a n) := (a0 ◭a1,a 2,...,a n),
˜dn(a0,a 1,...,a n) := (ε(an)a0,a 1,...,a n−1). (17)
We deﬁne two linear maps ξ,ξ ′ :Cn→Cn by
ξ(a0,a 1,...,a n) := (S((a1...a n)(2))⊲a 0, (a1)(1),..., (an)(1))
ξ′(a0,...,a n) := ((a1...a n)(2))⊲a 0, (a1)(1),..., (an)(1)). (18)
Then ξ◦ξ′ =ξ′◦ξ = idCn . It is easily checked that ξ commutes with di
for 1≤i≤n− 1 and that ξ◦ ˜di =di◦ξ,i = 0,n . Hence ξ◦d =b◦ξ and
ξ is an isomorphism of complexes of k-vector spaces. ✷
Let π :M′→ H0(A,M) be the canonical projection. Then we have
π(m ◭ a) = ε(a)π(m), and if we consider H0(A,M) as trivial right A-
module, then π⊗ idA⊗n induces a morphism
Hn(A,M)→H0(A,M)⊗k TorA
n (k,k ).
IfA is commutative and M =A with the standard bimodule structure,
then H0(A,M) =A, π is the identity, and the above map is the isomor-
phism of the Hochschild-Kostant-Rosenberg theorem. For M = σA the
map deﬁnes a “classical shadow” of twisted Hochschild homol ogy.
