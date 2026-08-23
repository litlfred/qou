---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-010-31-torsions-from-lifts-of-the-holonomy-represent
section_title: "Torsions from lifts of the holonomy representation"
section_number: 3.1
pages: 16-18
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
Let M 3 be a closed, orientable hyperbolic 3-manifold. Its holonomy represe n-
tations is unique up to conjugation:
hol∶ π1M 3 → Isom+(H3) ≅PSL2(C).
To get a natural representation in a linear group one can lift the holo nomy to
SL2(C). Such a lift always exists [15] and it depends naturally on a choice of a
spin structure, because the group of isometries is naturally identiﬁ ed with the
frame bundle of H3 and SL 2(C) with the spin bundle, cf. [63].
3.1.1 Lifts of the holonomy
There is natural action of H 1(M 3; Z/slash.l⟩ft2Z) on the set of lifts ̺ to SL (2, C) of the
holonomy representation: viewing H 1(M 3; Z/slash.l⟩ft2Z) as morphisms from π1M 3 to
Z/slash.l⟩ft2Z, a morphism ǫ∶ π1M 3 → Z/slash.l⟩ft2Z maps a representation ̺ to (−1)ǫ̺.
Proposition 3.1. (a) There is a natural bijection between the set of lifts of th e
holonomy representation and the set of spin structures.
This is an isomorphism of aﬃne spaces on the vector space H 1(M 3; Z/slash.l⟩ft2Z).
(b) If M 3 and
M
3
are the same manifold with opposite orientations, then ther e
is a natural bijection between spin structures on M 3 and on M
3
so that lifts
of the holonomy correspond to complex conjugates.
Item (a) can be found essentially in [15], see also [63].
A quick way of proving Item (b) is using the bijection of Item (a), kno wing
that complex conjugation in PSL 2(C) is the result of composing with an isom-
etry that changes the orientation of H3. On the other hand, this bijection can
be constructed explicitly from frame bundles and spin, but details ar e not given
here.
For a spin structure σ, the corresponding lift of the holonomy, according to
Proposition 3.1(a), will be denoted by
̺σ∶ π1M 3 → SL2(C).
The behavior of torsion by mutation is also interesting. Mutation is th e
operation that consists in cutting along a genus two surface, apply ing the hy-
perelliptic involution and gluing again. Notice that one does do not requ ire the
surface to be essential, thus the genus two surface can be replac ed by a (prop-
erly embedded) torus with one or two punctures or a sphere with th ree or four
punctures (in particular a Conway sphere for a knot exterior). Se e [27].
Let (M 3)µ denote the result of mutation, by [87] (M 3)µ is hyperbolic with
the same volume as M 3.
Remark 3.2. There is a natural correspondence between the spin structures
on M 3 and the spin structures on (M 3)µ.
Here is an explanation of the remark, using the natural bijection be tween
lifts of the holonomy and spin structures in Proposition 3.1. Assume t hat Σ
separates M 3 in two components M1 and M2. Then
π1M 3 ≅π1M1 ∗π1Σ π1M2.
16
If ̺σ∶ π1(M 3) → SL2(C) is a lift of the holonomy, then ̺σ(µ)∶ π1(M 3)µ → SL2(C)
is deﬁned so that ̺σ(µ)/divid⟩s.alt0π1M1 = ̺σ/divid⟩s.alt0π1M1 and ̺σ(µ)/divid⟩s.alt0π1M2 is conjugate to ̺σ/divid⟩s.alt0π1M2
by a matrix in PSL 2(C) that realizes the involution µ on Σ. When Σ does
not separate, then the construction is similar from the presentat ion of π1M 3 as
HNN-extension.
3.1.2 T orsions for closed 3-manifolds
The following theorem is a particular case of Raghunathan’s. With oth er co-
homology results, it is discussed in Appendix B. In particular the follow ing
theorem is stated in Corollary B.2.
Theorem 3.3. Let M 3 be a closed, orientable, hyperbolic 3-manifold. Then
any lift of its holonomy representation is acyclic.
With Mostow rigidity, this yields immediately a topological invariant of th e
spin manifold.
Deﬁnition 3.4. Let M 3 be a compact, oriented, hyperbolic 3-manifold with
spin structure σ. The torsion of (M 3, σ) is deﬁned as
τ (M 3, σ) ∶= tor(M 3, ̺σ) ∈C∗ (13)
where ̺σ = /tild⟩comb.alt1hol is the lift of the holonomy hol corresponding to the spin structu re
σ.
Remark 3.5. There is no sign indeterminacy, i.e. it is a well deﬁned complex
number, because ̺σ is a representation in C2, which is even dimensional, and
χ(M 3) = 0, see Remark 2.7.
Here are some of its properties.
Proposition 3.6. The torsion τ (M 3, σ) in Deﬁnition 3.4 has the following
properties:
(a) It is a topological invariant of the spin manifold (M 3, σ).
(b) There are examples of manifolds M 3 with two spin structures σ and σ′ such
that τ (M 3, σ) ≠τ (M 3, σ′).
(c) Let
M
3
denote the manifold M 3 with opposite orientation. If one changes
the orientation and the spin structure accordingly as in Pro position 3.1, then
the torsion is the complex conjugate
τ (M
3
, σ) = τ (M 3, σ).
(d) Let (M 3)µ denote the result of mutation. If σµ denotes the corresponding
spin structure as in Remark 3.2, then
τ ((M 3)µ, σµ) = τ (M 3, σ).
(e) Let M 3 be an oriented hyperbolic manifold with one cusp and with spi n
structure σ. The set of modules of the torsions obtained by Dehn ﬁlling on
M 3, /divid⟩s.alt0τ (M 3
p/sl⊗sh.leftq, σ)/divid⟩s.alt0 so that σ extends to M 3
p/sl⊗sh.leftq, is dense in the interval
/brack⟩tl⟩ft.alt31
4 /divid⟩s.alt1τ (M 3, σ)/divid⟩s.alt1, +∞/par⟩nright.alt3 .
17
Item (a) follows from uniqueness of the hyperbolic structure, by M ostow
rigidity. To prove (b) it suﬃces to compute an example, this is done in C orol-
lary 3.27. Item (c) is straightforward from Proposition 3.1. Item (d ) is proved
in [61]. Finally, (e) is proved later when discussing cusped manifolds, as this
will follow immediately from a surgery formula.
Item (e) shows that this torsion is not obviously related to the hype rbolic
volume. The following theorem, a particular case of [6, Thm. 4.5], ﬁnds a
relation (we use the convention of torsion opposite to [6]):
Theorem 3.7 (Bergeron and Venkatesh, [6]) . Let M 3 be a compact oriented
hyperbolic 3-manifold. Assume that M 3
n → M 3 is a sequence of coverings such
that the injectivity radius of M 3
n converges to inﬁnity. Then
lim
n→∞
log /divid⟩s.alt0τ (M 3
n, σ)/divid⟩s.alt0
vol(M 3n) = 11
12π .
Equivalently;
lim
n→∞
log /divid⟩s.alt0τ (M 3
n, σ)/divid⟩s.alt0
deg(M 3n → M 3) = 11
12π vol(M 3).
This theorem relies on analytic torsion and on L2-torsion, as −11
12π is the L2-
torsion of H3. The proof uses the L2-Laplacian of hyperbolic space, and it
is based on approximations of averages of the trace of the diﬀeren ce of heat
kernels, see Equation (12). They require the notion of strong acy clicity (the
property in Theorem B.1) to avoid eigenvalues of the Laplacian appro aching to
zero. This has been generalized in [1], in particular without requiring th at the
M 3
n are coverings. See also [73].
