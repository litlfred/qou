---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-005-15-instanton-floer-homology
section_title: "Instanton Floer homology"
section_number: 1.5
pages: 4-6
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
section, deﬁned by a monodromy map h∈ Γ(Σ g,1) in the mapping class group of a once-marked
surface f −1(pt). Up to isomorphism there is a unique non-trivial SO(3)-bundle E→ f −1(pt),
with⟨w2(E),f −1(pt)⟩⁄= 0; the section of Yh→S1 deﬁnes a distinguished extension of E to an
SO(3) bundle (still denoted) E→Yh. If Yh is a homology S1×S2, this is the unique non-trivial
SO(3)-bundle over Yh up to isomorphism. Any such E admits no reducible ﬂat connexion, hence
is “admissible” in the sense of Donaldson [24], so there is an associated Z4-graded instanton Floer
homology group HF inst(Yh;E) computed from the Chern-Simons functional on connexions in E.
Nowh acts canonically on M(f −1(pt)) via an element ˆh∈ ˆΓ(f −1(pt)), and the famous theorem
of Dostoglou and Salamon [25] gives an isomorphism HF inst(Yh;E)∼=HF (ˆρ(ˆh)). Appealing in
addition to Theorems 1.1 and (the proof of) 1.6 yields:
Corollary 1.8. Fix a 3-manifold Yh → S1 ﬁbred by genus 2 curves, which in addition is a
homologyS1×S2, and let E→Yh be the non-trivial SO(3)-bundle. There is an isomorphism of
Z2-graded C-vector spaces
HF inst(Yh;E) ∼= C⊕HF (h)⊕ C. (1.1)
By work of Cotton-Clay [21] the central summand HF (h) on the right side, which is com-
puted on the curve Σ 2 itself rather than on any associated moduli space, can be algorithm ically
computed from a presentation of h as a word in positive and negative Dehn twists, or from a
suitable traintrack. In general, if we make no assumption on the act ion of h on H1(Σ 2; Z), the
instanton Floer homologies HF inst(Yh;E) of the diﬀerent principal bundles E→ Yh arising as
mapping tori of h are given by Hochschild cohomologies C⊕HH ∗(hξ)⊕ C, with hξ the various
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 5
autoequivalences of F(Σ 2) obtained by combining the action of h and tensoring by some ﬂat
line bundle ξ∈ H 1(Σ 2; Z2). We should emphasise that it seems to be very hard to compute
these instanton Floer homology groups by direct computations on Yh, or even to write down the
underlying chain groups.
1.6. Witten’s conjecture. We include a brief speculative discussion, which should nonetheless
set these topological results in a helpful context. The space M(Σ g) is always a simply-connected
Fano variety, symplectomorphic to the variety of (g−2)-dimensional linear subspaces of Q0∩Q1⊂
P2g+1, hence there is an evaluation from the total space of a projective bundle
Pg−2 ~× M(Σ g)−→Q0∩Q1.
Probably deeper analysis of the birational structure of this map wo uld help relate the Fukaya
category of the intersection of quadrics to that of the moduli spa ce. Explicitly:
Conjecture 1.9. There is a C-linear equivalence of Z2-graded triangulated categories
DπF(Σ g) ≃ DπF(M(Σ g); 4(g− 2)).
We give a slightly more precise statement in Remark 2.19. Conjecture 1.9 should be seen in
light of Witten’s conjecture relating Seiberg-Witten and Donaldson in variants in low-dimensional
topology. The spaces M(Σ g) arise as moduli spaces of instantons on Σ g×S1. The corresponding
moduli spaces of Seiberg-Witten solutions on Σ g×S1 are given by symmetric products of Σ g. A
theorem of Munoz [70] implies the spectrum of quantum multiplication b y the ﬁrst Chern class
on M(Σ g) is given (dropping some factors of i) by
{−4(g− 1),−4(g− 2),..., −4, 0, 4,..., 4(g− 2), 4(g− 1)}.
The Fukaya category F(M(Σ g)) breaks into summands indexed by these values. Moreover, the
summands for±λ should be equivalent. Naively, one would expect the Fukaya categor y summand
F(M(Σ g); 4(g−k−1)) to be built out of the Fukaya category of the symmetric produc t Symk(Σ g),
when|k|<g (this is an intentionally vague statement, not least because we have not speciﬁed a
symplectic form on the symmetric product). In particular, the sum mands corresponding to the
outermost eigenvalues±4(g−1) are expected to be semisimple (equivalent to the Fukaya categor y
of a point). Whilst we do not prove this, Theorem 1.6 provides rather strong evidence. More
precisely, that theorem is proved by showing that the symplectic Flo er cohomology HF (φ) has a
distinguished rank one summand, given by its generalized eigenspace for the eigenvalue 4(g− 1).
This should be compared to similar rank one pieces of monopole or Heeg aard Floer homology
[78, 57], in that context associated to the “top” Spin c-structure. In this vein, Conjecture 1.9
– or Theorem 1.1, when g = 2 – can be viewed as an instance of the general “Seiberg-Witten
= Donaldson” philosophy, for invariants of mapping tori coming from the next highest Spin c-
structure.
Practically, one might hope – by analogy with derived categories of sh eaves, cf. Section 1.7
below – that Fukaya categories behave well under both blowing up an d down, and under passing
to the total space of a projective bundle. Then Thaddeus’ work o n ﬂip diagrams [101], in which
ﬂips along projective bundles over symmetric products explicitly rela te a projective bundle over
M(Σ g) to a projective space, would seem to give a cut-and-paste route to assembling F(M(Σ g))
from the F(Symk(Σ g)). In reality, it seems hard to give a complete argument on these line s using
current technology. The intermediate spaces in Thaddeus’ work h ave less good monotonicity
properties than M(Σ g) itself, whilst there is some delicacy in the choice of symplectic form on
Symk(Σ g). Note that the latter delicacy is absent precisely for the summand s corresponding to
Symk(Σ g) for k = 0, 1, which are those treated in this paper.
6 IV AN SMITH
