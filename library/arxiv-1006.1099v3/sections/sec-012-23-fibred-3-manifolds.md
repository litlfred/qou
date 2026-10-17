---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-012-23-fibred-3-manifolds
section_title: "Fibred 3-manifolds"
section_number: 2.3
pages: 12-13
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
determined up to isomorphism by its second Stiefel-Whitney class w2(E) ∈H2(Y ; Z2).
Let
f : Y →S1 be a 3-manifold which ﬁbres smoothly over the circle. The ﬁbre f −1(pt) is nec-
essarily homologically essential and primitive, and we ﬁx an SO(3)-bundle E over Y for which
⟨w2(E), [f −1(pt)]⟩̸ = 0. Indeed, we take E to be the mapping torus of a lift of the monodromy
of Y to the unique non-trivial SO(3)-bundle over a preferred ﬁbre f −1(pt), with w2(E) Poincar´e
dual to a section of f. The Chern-Simons functional
a 7→
Z
Y
a ∧da + a ∧a ∧a
on the aﬃne space Ω1(Y ) of connexions A = A0 + a on E has critical points the ﬂat connexions,
which give rise to irreducible representations of π1(Y ) into SO(3) whose restriction to the ﬁbre
Σ = f −1(pt) deﬁnes a ﬂat connexion in the original bundle E|Σ. In other words, the relevant
representations of π1(Y ) are exactly those arising from ﬁxed-points of the natural action of the
monodromy φ of f (lifted to E) on M(Σ). All of these representations are non-abelian, since they
restrict to non-abelian representations of π1(Σ). By counting solutions to the anti-self-dual Yang-
Mills equations on Y × R, one can deﬁne a Morse-Floer theory for the Chern-Simons functional
and hence an instanton Floer homology group HFinst(Y ; E). The classical theorem of Dostoglou
and Salamon [25] asserts
HFinst(Y ; E) ∼= HF(ˆρ(φ)).
(2.6)
Since the ﬁxed points of mapping classes on M(Σ) deﬁne representations of π1(Y ), the latter
can be studied via symplectic Floer homology; this will be the approach taken in the proof of
Corollary 1.7 later.
Remark 2.7. If Yh →S1 has monodromy h with im(1−h∗) = H1(Σ; Z) for the induced action on
H1(Σ; Z), the mapping torus is a homology S1 ×S2, and there is a unique SO(3)-bundle over Yh.
In particular, the left hand side of Equation (2.6) is independent of the lift of h to the principal
bundle E →Σ. It follows that the Floer homologies on the representation variety of all lifts of
h to bΓ(Σ) are actually isomorphic, which doesn’t seem obvious directly.
Finally, one can consider the set of non-abelian SO(3)-representations of π1(Y ) and its be-
haviour under coverings, analogously to recent interest in the growth of Betti numbers or Hee-
gaard genus of covers. Long and Reid [62] proved that any hyperbolic 3-manifold has ﬁnite
covers with arbitrarily many representations into the dihedral group A5 and hence non-abelian
SO(3)-representations. However, these covers are not cyclic. Ian Agol pointed out to the author
FLOER COHOMOLOGY AND PENCILS OF QUADRICS
13
that if a 3-manifold Y has a non-trivial JSJ-decomposition – for instance, the mapping torus of
a reducible surface diﬀeomorphism – some ﬁnite cover has fundamental group mapping onto a
rank 2 free group, hence there are covers with inﬁnitely many non-abelian SO(3)-representations.
However, if Y is actually hyperbolic, properties of SO(3)-representations under cyclic covers seem
mysterious, and the second statement in Corollary 1.7 seems to be new.
