---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-025-appendix-a-not-approximating-the-trivial-represe
section_title: "Appendix A Not approximating the trivial representation"
section_number: null
pages: 44-45
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
resentation
For a manifold M 3 there are components of X(M 3, PSL2(C)) that consist of
characters of abelian representations. When b1(M 3) = 1 those components are
curves, and their union is denoted by
X ab(M 3, PSL2(C)).
The number of components of X ab(M 3, PSL2(C)) depends on the torsion of
H1(M 3; Z).
Being irreducible is a Zariski open property for a character [16]. On t he other
hand, every reducible character is also the character of an abelian representation.
This yields that X ab(M 3, PSL2(C)) are precisely the components consisting
only of reducible characters.
Lemma A.1. Assume that b1(M 3) = 1. Then the trivial character belongs to
a single irreducible component of X(M 3, PSL2(C)), which is one of the curves
of X ab(M 3, PSL2(C)).
Corollary A.2. If b1(M 3) = 1, then the trivial character does not belong to
X0(M 3, PSL2(C)).
44
Proof of Lemma A.1. The proof uses the projection
π∶ hom(π1M 3, PSL2(C)) → X(M 3, PSL2(C))
ρ ↦ χρ
(55)
and the dimension of its ﬁbre. For the trivial character χ0, a representation
ρ ∈π−1(χ0) is conjugate to
ρ(γ) = ± /par⟩nl⟩ft.alt41 h(γ)
0 1 /par⟩nright.alt4 , ∀γ ∈π1M 3, (56)
where h∶ π1M 3 → C is a group homomorphism. (Not to be confused with the
cusp shape of peripheral representations, as h is deﬁned in the whole group
π1M 3.) Conjugating the representation (56) by a diagonal matrix means re-
placing the morphism h by a multiple. Thus, as b1(M 3) = 1, there are only
two orbits by conjugation in π−1(χ0): the trivial and the non-trivial morphism
h∶ π1M 3 → C. By looking at the dimension of the stabilizers, these orbits have
dimension either 0 (for h trivial) or 2 (for h non-trivial). Hence the dimension
of π−1(χ0) is 2. On the other hand, on components Y of X(M 3, PSL2(C)) that
contain irreducible representations, the generic dimension of π−1 is 3, the di-
mension of PSL 2(C). Since this dimension is upper semi-continuous, the trivial
character cannot belong to an irreducible component of X(M 3, PSL2(C)) that
contains irreducible characters. Hence it must belong to a compone nt whose
characters are all reducible.
Lemma A.3. Let ρ1, ρ2 ∈hom(π1M 3, SL2(C)) have the same character. If
χρ1 = χρ2 is nontrivial, then ρ1 is acyclic if and only if ρ2 is acyclic.
Proof. For every character there is a unique closed orbit by conjugation, so
that every other orbit accumulates to it, see [58]. So we may assume that the
conjugation orbit of ρ2 accumulates to ρ1. By semi-continuity, ρ1 acyclic implies
that so is ρ2. Next assume that ρ1 is not acyclic. Up to conjugacy, there exists
a group homomorphism φ∶ π1M 3 → Z and λ ∈C − {0, ±1} such that
ρ1(γ) = /par⟩nl⟩ft.alt4λφ(γ) 0
0 λ−φ(γ)/par⟩nright.alt4 and ρ2(γ) = /par⟩nl⟩ft.alt4λφ(γ) f (γ)
0 λ−φ(γ)/par⟩nright.alt4
for every γ ∈π1M 3. Here f ∶ π1M 3 → C is a crossed morphism: f (γ1γ2) =
f (γ1) + λ2φ(γ)f (γ2), for all γ1, γ 2 ∈π1M 3. The homology of ρ1 decomposes as a
direct sum of π1M 3-modules: C ⊕ {0} and {0} ⊕ C, and both are nonzero (one
is dual from the other). The ρ2-module does not decompose, but there is an
exact sequence of π1M 3-modules
0 → C ⊕ {0} → C2 → C → 0
where π1M 3 acts on C2 via ρ2, and the action on the other modules is the same
as for ρ1. From the corresponding long exact sequence in homology it follows
easily that ρ2 is not acyclic.
