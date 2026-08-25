---
doc_id: bn
doc_title: "Braid groups and Hodge theory"
section_id: sec-042-12-the-hyperelliptic-case
section_title: "The hyperelliptic case"
section_number: 12
pages: 52-55
source_pdf: bn.pdf
source_sha256: 95ed0908ceb54a1c
doc_brief: "Braid groups and Hodge theory — This paper gives an account of the unitary representations of the braid group that arise via the Hodge theory of cyclic branched cove r- ings of P1, highlighting their"
---
In this section we discuss the hyperelliptic case, where X takes the form
y2 = (x −b1) · · ·(x −bn) (12.1)
andω =dx/y. A special feature of this case is that the symmetry T ∗ω = −ω
is preserved by the Teichm¨ uller geodesic ﬂow. Consequently, the period map
fq : T ∗
0,n → H g,g
is compatible with a natural action of SL 2(R). We will use this compatibility
to analyzefq and its image, and (in the next section) to describe fq explicitly
for the Teichm¨ uller curves coming from regular polygons [V 1].
The period domain. In the hyperelliptic case we have d = 2, q = −1,
and H 1(X)q =H 1(X). Thus the period domain
Hg,g ⊂ PH 1(X) ∼
= PCg,g
coincides with the space of all positive lines in the cohomol ogy of X (§6).
The real points
Rg ∼
= RP2g−1
of its ambient projective space PH 1(X) correspond to lines of the form [ Cv],
v ∈H 1(X, R). Since ⟨v,v ⟩ = 0 for v ∈H 1(X, R), we have Rg ⊂∂Hg,g . By
restricting our attention to automorphisms that preserve t his real structure,
we may regard the period domain as the homogeneous space
Hg,g = Sp 2g(R)/(SO(2, R) × Sp2g−2(R)). (12.2)
51
Secant lines. We say a line L ⊂ PH 1(X) is a secant if it joins a pair
of real points p,q ∈ Rg. Every secant has the form L = PV , where V ⊂
H 1(X) is invariant under complex-conjugation and has signature (1, 1). The
intersectionsS =L ∩ Hg,g form the leaves of the secant foliation S of Hg,g .
Each leaf is a totally geodesic copy of CH1 (up to the sign of its metric).
The secant foliation can also be deﬁned by observing that SL 2(R) acts
C ∼
= R2, and hence on H 1(X) = Hom( π1(X), C); the orbits of this action
project to the leaves of S.
W eierstrass forms. Now assume n = 2g + 1 is odd. Let Hg denote the
moduli space of hyperelliptic Riemann surfaces of genus g. Using (12.1),
each point conﬁguration [B] = [ {b1,...,b n}] in M∗
0,n determines an X ∈ H g
and a line Cω ⊂ Ω(X), where ω = dx/y. We refer to ω as a Weierstrass
form, since its divisor ( ω) = (2g − 2)~∞ is supported on a single Weierstrass
point of X. The map [ B] ↦→[(X,ω )] gives a bijection
M∗
0, 2g+1 ∼
= PΩ Hg(2g − 2) ∼
= ~Hg, (12.3)
where ~Hg is the degree (2g+2) covering space of Hg parameterizing Riemann
surfaces with a chosen Weierstrass point.
Each Weierstrass form determines a quadratic diﬀerential ω2 on C −B
hence a complex Teichm¨ uller geodesic W ∼
= H through ([ C,B ]). These
geodesics form the leaves of the Weierstrass foliation W of T ∗
0, 2g+1. Under
the isomorphism (12.3), the leaves of W correspond to the orbits of SL 2(R)
on Ω Hg(2g − 2) (see e.g. [KZ]). Since the actions of SL 2(R) on Ω Hg and
H 1(X) are compatible, we ﬁnd:
Theorem 12.1 The period map fq : T ∗
0, 2g+1 → H g,g sends the Weierstrass
foliation W to the secant foliation S. Its restriction to each leaf is an isom-
etry.
Ergodicity . For g = 1, fq simply gives the standard homeomorphism
between T ∗
0, 3 and H1, 1 ∼
= H.
Forg > 1 and n = 2g + 1, the period map is still an equivariant local
homeomorphism ( §6). But the braid group now acts very diﬀerently on
its domain and its range: while the orbits of Bn in Teichm¨ uller space are
discrete, a typical orbit in the period domain is dense. In fact:
Proposition 12.2 The action of ρq(Bn) on Hg,g is ergodic for g >1.
Proof. Equation (12.2) gives Hg,g =G/F , where F is a closed subgroup of
G = Sp 2g(R); and Γ = ρq(Bn) is a lattice in G by Theorem 11.2. But for
52
g >1, F is noncompact, so Γ acts ergodically on G/F by the Howe–Moore
theorem [HM].
Thus the image of fq is an open set of full measure, and fq is not a
covering map to its image (else ρq(Bn) would have discrete orbits).
Proposition 12.3 The group Kerρq has inﬁnite orbits on T ∗
0, 2g+1, and
hence the period map fq is inﬁnite-to-one for g >1.
Proof. The square of a Dehn twist about a loop enclosing an odd number of
points ofB lifts to a Dehn twist in Mod(X) which acts trivially on homology.
For more on ‘isoperiodic forms’, see [Mc6, §9].
The image of the period map. Although the period map has a compli-
cated structure, its image is reasonably tame. Indeed, the r esults of [Kap]
easily imply:
Theorem 12.4 Forg >1, the complement of the image of the period map
fq : T ∗
0, 2g+1 → H g,g
is a nonempty, countable union of secant lines.
Proof. Let G = Sp 2g(R), H = Sp 2(R) × Sp2g−2(R), Γ = ρq(B2g+1). By
Theorem 11.2, Γ is a lattice in G. The image of the period map, modulo
the secant foliation, is a nonempty, open, Γ-invariant subs etU ⊂ H g,g/S ∼
=
G/H. By Ratner’s theorem, for any x ∈ G there is a connected Lie group
J with H ⊂J such that
ΓxH = ΓxJ and Γ ∩Jx is a lattice in Jx =xJx −1
[Rat].
We will show G/H −U is countable. Suppose [ xH] ⁄∈U . Then Γ xH
is not dense in G, and hence J ⁄= G. As shown in [Kap, §3], this implies
J =H. Thus Γ x = Γ ∩Hx is a lattice Hx. There are only countably many
possibilities for Γ x, since it is a ﬁnitely-generated subgroup of Γ; and Hx is
the Zariski closure of Γ x, so there are only countably many possibilities for
Hx. But NG(H)/H is ﬁnite (in fact trivial for g > 2), so Hx determines
[xH] up to ﬁnitely many choices.
Thus the complement of the image of fq is a countable union of leaves of
the secant foliation. The complement is nonempty by [Kap, §1]: a cohomol-
ogy class p∗ :π1(X) → Z[i] determined by a degree one map p :X → C/Z[i]
can never be realized by a holomorphic 1-form.
53
The case n = 2 g + 2: relative periods and quadratic diﬀerentials.
Similar results hold for the period map fq : T ∗
0, 2g+2 → H g,g . In this case
ω = dx/y has a pair of distinct zeros at the points {P,Q } lying over ∞
in X, and fq is a submersion with 1-dimensional ﬁbers. The ﬁbers form
the leaves of the absolute period foliation A of T ∗
0, 2g+2. Along any ﬁber A,
one can normalize ω so its absolute periods are constant; then the (locally
well-deﬁned) relative period function
z =
∫ Q
P
ω
determines a (globally well-deﬁned) holomorphic quadrati c diﬀerential q =
dz2 onA. The natural foliation of T ∗
0, 2g+2 by complex Teichm¨ uller geodesics
(analogous to W) is transverse to A, so it gives rise to a homeomorphism
map φ :A →A′ whenever fq(A) and fq(A′) are joined by a secant; and in
fact φ is a Teichm¨ uller mapping, with dilatation proportional to q/|q|. See
[Mc6, §8] for a more detailed discussion, in the case of genus two.
