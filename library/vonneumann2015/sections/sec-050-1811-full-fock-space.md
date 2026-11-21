---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-050-1811-full-fock-space
section_title: "Full Fock space"
section_number: 18.1.1
pages: 120-121
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
Full Fock space
Deﬁnition 18.1.2. If H is a real or complex Hilbert space the full Fock space
T (H) is the Hilbert space direct sum ⊕∞
n=0 ⊗n H. By deﬁnition ⊗0H is one
dimensional, spanned by the "vacuum" vector Ω.
Even when H is real one complexiﬁes T (H) so that it is a complex Hilbert
space.
For each n and f ∈H the operator ℓ(f) : ⊗nH →⊗n+1H given by
ℓ(f)(ξ1 ⊗ξ2 · · · ξn) = f ⊗ξ1 ⊗ξ2 ⊗· · · ⊗ξn
is clearly bounded by ||f|| so extends to an operator we will call ℓ(f) on all
of full Fock space.
Exercise 18.1.3. (i) Show that
ℓ(f)∗(ξ1 ⊗ξ2 ⊗· · · ⊗ξn) = ⟨ξ1, f⟩ξ2 ⊗ξ3 · · · ξn,
ℓ(f)∗(ξ) = ⟨ξ, f⟩Ωfor ξ ∈⊗1H,
and ℓ(f)∗Ω= 0.
(ii) Show that
ℓ(f)∗ℓ(g) = ⟨g, f⟩
Proposition 18.1.4. The action of the ℓ(f) and ℓ(f)∗on full Fock space is
irreducible.
Proof. It suﬃces to show that any non-zero vector in T (H) is cyclic. The
vacuum vector Ωis obviously cyclic. Note that the linear span of the images
of the ℓ(f)ℓ(f)∗is the orthogonal complement Ω⊥. The projection onto Ω⊥
is thus in {ℓ(f), ℓ(f)∗}′′. If ξ is any vector we are thus done if ⟨ξ, Ω⟩̸ = 0.
Otherwise ⟨ξ, f1 ⊗f2 · · · fn⟩must be non-zero for some fi ∈H. But then
⟨ℓ(f1)ℓ(f2) · · · ℓ(fn)Ω, ξ⟩̸ = 0 and the vector (ℓ(f1)ℓ(f2) · · · ℓ(fn))∗ξ, which
can be reached from ξ, projects non-trivially onto the vacuum and is thus
cyclic.
One may also consider the right creation operators r(ξ) deﬁned by
r(f)(ξ1 ⊗ξ2 · · · ξn) = ξ1 ⊗ξ2 ⊗· · · ⊗ξn ⊗f.
They satisy the same relations as the ℓ(f) and almost commute with them.
To be precise
120
18.1.5.
ℓ(f)r(g) = r(g)ℓ(f)
and
ℓ(f)r(g)∗−r(g)∗ℓ(f) = −⟨f, g⟩pΩ
where pΩis projection onto the one dimensional subspace spanned by the
vacuum.
The r(f)’s and r(f)∗’s act just as irreducibly as the ℓ’s.
