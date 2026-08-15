---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-176-622-a-sequence-of-central-extensions-for-simplic
section_title: "A sequence of central extensions. — For simplicity, we write G"
section_number: 6.2.2
pages: 111-112
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
for GA0. The Lie algebra g of G consists in all nilpotent matrices of the form:







0r1 ... ... ... ...
... ... ... F i,j ...
0 ... ... ... ...
... 0 ... ... ...
0 ... 0 ... 0rk







,
where 0r is the square null matrix of size r and where each Fi,j is in Mat ri,rj
for 1≤i<j ≤k. For each integerδ, write g≥δ the sub-Lie algebra of matrices
whose only non null blocks Fi,j have level µj−µi≥δ; it is actually an ideal
of g and G≥δ := In + g≥δ is a normal subgroup of G. Moreover, one has an
exact sequence:
0→ G≥δ/G≥δ+1→ G/G≥δ+1→ G/G≥δ→ 1,
actually, a central extension. The map g↦→In +g induces an isomorphism
from the vector space g≥δ/g≥δ+1 to the kernel G≥δ/G≥δ+1 of this exact
sequence. We write g(δ) this group: it consists of matrices in g whose only
non null blocks Fi,j have level µj−µi =δ. (This is the reason why we wrote
a 0 instead of a 1 at the left of the exact sequence !)
106 CHAPTER 6. GEOMETRY OF THE SPACE OF CLASSES
Restricting the above consideration to Λ := Λ I(M0) considered as a sheaf
of subgroups of G (with coeﬃcients in function ﬁelds), we get a similar central
extension:
0→λ(δ)→ Λ/Λ≥δ+1→ Λ/Λ≥δ→ 1.
Now, a fundamental theorem in the non-abelian cohomology of sheaves says
that we have an exact sequence of cohomology sets:
Theorem 6.2.1. — One has an exact sequence of pointed sets:
0→H 1(Eq,λ (δ))→H 1(Eq, Λ/Λ≥δ+1)→H 1(Eq, Λ/Λ≥δ)→ 1.
Proof. — The exactness should be here understood in a rather strong sense.
The sheaf λ(δ) is here a pure isoclinic holomorphic vector bundle of degree −δ
and rank ∑
µj −µi=δ
rirj. Its ﬁrst cohomology group V (δ) is therefore a vector
space of dimension δ ∑
µj −µi=δ
rirj. The theorem says that V (δ) operates on the
pointed set H 1(Eq, Λ/Λ≥δ+1) with quotient the pointed set H 1(Eq, Λ/Λ≥δ).
For a proof, see [ 23, th. 1.4 and prop. 8.1].
Corollary 6.2.2 . — There is a natural bijection of H 1(Eq, ΛI(M0)) with⨁
δ≥1
H 1(Eq,λ (δ)).
Proof. — Indeed, the cohomology sets being pointed, the theorem yi elds a
bijection of each H 1(Eq, Λ/Λ≥δ+1) with H 1(Eq, Λ/Λ≥δ)×H 1(Eq,λ (δ)).
We shall write F≤δ(M0) := H 1(Eq, Λ/Λ≥δ+1). This space is the solution
to the following classiﬁcation problem: two matrices with d iagonal part A0
are declared equivalent if their truncatures correspondin g to the levels ≤ δ
are analytically equivalent (through a gauge transform in G); and there is no
condition on the components with levels >δ . This is exactly the equivalence
under C((z))q;s for δ < s≤ δ + 1. The corresponding Birkhoﬀ-Guenther
normal forms have been described in section 3.4. The extreme cases are δ >
µk−µ1, where F≤δ(M0) is the whole space F(M0); and δ < 1, where it is
trivial.
