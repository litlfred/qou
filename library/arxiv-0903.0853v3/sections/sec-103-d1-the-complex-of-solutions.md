---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-103-d1-the-complex-of-solutions
section_title: "The complex of solutions"
section_number: D.1
pages: 155-155
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
A.4.1. The complex of solutions. — The following is sometimes consid-
ered as a diﬀerence analog of the de Rham complex in one variable, see for
instance [2, 54].
Deﬁnition A.4.2. — We call complex of solutions of M in N the following
complex of C-modules:
tΦ,Ψ : LK(E, F) →Lσ(E, F),
f 7→Ψ ◦f −f ◦Φ.
concentrated in degrees 0 and 1.
It is indeed clear that the source and target are C-modules, that the map
tΦ,Ψ does send the source to the target and that it is C-linear.
Corollary A.4.3. — The homology of the complex of solutions is H0 =
Hom(M, N) and H1 = Ext(M, N), and these equalities are functorial.
Proof. — The statement about H1 is the theorem. As regards H0, the kernel
of tΦ,Ψ is the C-module {f ∈LK(E, F) | Ψ ◦f = f ◦Φ}, that is, Hom(M, N);
and functoriality is obvious in that case.
Corollary A.4.4. — From the exact sequence 0 →N ′ →N →N ′′ →0, one
deduces the “cohomology long exact sequence”:
0 →Hom(M, N ′) →Hom(M, N) →Hom(M, N ′′)
→Ext(M, N ′) →Ext(M, N) →Ext(M, N ′′) →0.
Proof. — We keep the previous notations (and moreover adapt them to
N ′, N ′′). The exact sequence of projective K-modules 0 →F ′ →F →F ′′ →0
being split, both lines of the commutative diagram:
0 −−−−→LK(E, F ′) −−−−→LK(E, F) −−−−→LK(E, F ′′) −−−−→0
ytΦ,Ψ′
ytΦ,Ψ
ytΦ,Ψ′′
0 −−−−→Lσ(E, F ′) −−−−→Lσ(E, F) −−−−→Lσ(E, F ′′) −−−−→0
are exact, and it is enough to call to the snake lemma.
