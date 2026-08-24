---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-011-23-fibred-3-manifolds
section_title: "Fibred 3-manifolds"
section_number: 2.3
pages: 12-13
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
determined up to isomorphism by its second Stiefel-Whitney class w2(E) ∈ H 2(Y ; Z2). Let
f : Y → S1 be a 3-manifold which ﬁbres smoothly over the circle. The ﬁbre f −1(pt) is nec-
essarily homologically essential and primitive, and we ﬁx an SO(3)-bundle E overY for which
⟨w2(E), [f −1(pt)]⟩⁄= 0. Indeed, we take E to be the mapping torus of a lift of the monodromy
ofY to the unique non-trivial SO(3)-bundle over a preferred ﬁbre f −1(pt), with w2(E) Poincar´ e
dual to a section of f . The Chern-Simons functional
a↦→
∫
Y
a∧da +a∧a∧a
on the aﬃne space Ω 1(Y ) of connexions A =A0 +a onE has critical points the ﬂat connexions,
which give rise to irreducible representations of π1(Y ) into SO(3) whose restriction to the ﬁbre
Σ = f −1(pt) deﬁnes a ﬂat connexion in the original bundle E|Σ . In other words, the relevant
representations of π1(Y ) are exactly those arising from ﬁxed-points of the natural action of the
monodromyφ off (lifted to E) on M(Σ). All of these representations are non-abelian, since they
restrict to non-abelian representations of π1(Σ). By counting solutions to the anti-self-dual Yang-
Mills equations on Y× R, one can deﬁne a Morse-Floer theory for the Chern-Simons funct ional
and hence an instanton Floer homology groupHF inst(Y ;E). The classical theorem of Dostoglou
and Salamon [25] asserts
HF inst(Y ;E) ∼= HF (ˆρ(φ)). (2.6)
Since the ﬁxed points of mapping classes on M(Σ) deﬁne representations of π1(Y ), the latter
can be studied via symplectic Floer homology; this will be the approach taken in the proof of
Corollary 1.7 later.
Remark 2.7. IfYh→S1 has monodromy h withim(1−h∗) = H1(Σ; Z) for the induced action on
H1(Σ; Z), the mapping torus is a homology S1×S2, and there is a unique SO(3)-bundle over Yh.
In particular, the left hand side of Equation (2.6) is independent of t he lift of h to the principal
bundle E→ Σ. It follows that the Floer homologies on the representation variet y of all lifts of
h to ˆΓ(Σ) are actually isomorphic, which doesn’t seem obvious directly.
Finally, one can consider the set of non-abelian SO(3)-representations of π1(Y ) and its be-
haviour under coverings, analogously to recent interest in the gro wth of Betti numbers or Hee-
gaard genus of covers. Long and Reid [62] proved that any hyper bolic 3-manifold has ﬁnite
covers with arbitrarily many representations into the dihedral gro up A5 and hence non-abelian
SO(3)-representations. However, these covers are not cyclic. Ia n Agol pointed out to the author
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 13
that if a 3-manifold Y has a non-trivial JSJ-decomposition – for instance, the mapping to rus of
a reducible surface diﬀeomorphism – some ﬁnite cover has fundamen tal group mapping onto a
rank 2 free group, hence there are covers with inﬁnitely many non- abelianSO(3)-representations.
However, ifY is actually hyperbolic, properties of SO(3)-representations under cyclic covers seem
mysterious, and the second statement in Corollary 1.7 seems to be n ew.
2.4. F aithfulness. For a symplectic manifoldX consider the conjugation-invariant Floer-theoretic
entropy of a mapping class φ∈ Symp(X)/ Ham(X)
hF loer(φ) = lim sup 1
n log rkKHF (φn).
As mentioned in the Introduction, for area-preserving diﬀeomorp hisms of a surface Σ the Floer-
theoretic entropy (of the action on Σ itself) co-incides with the top ological entropy which in
turn co-incides with the periodic entropy, or rather their minimal va lues on the isotopy class
[21, 31, 33]. Thus
hF loer(φ)> 0⇔ φ has a pseudo-Anosov component. (2.7)
This follows from the classical fact that pseudo-Anosov maps have exponentially growing numbers
of periodic points realising exponentially many diﬀerent Nielsen classes ; Floer-theoretically one
can actually make much more precise statements [21]. Recall also the re is a natural representation
ˆρ : ˆΓ(Σ) −→π0 Symp(M(Σ))
where Γ(Σ) → Γ g is a Z2g
2 -extension of the mapping class group π0 Diﬀ +(Σ g). Mildly abusing
notation, we will say ˆφ∈ ˆΓ(Σ) has a pseudo-Anosov component if that is true of its image φ∈ Γ g.
