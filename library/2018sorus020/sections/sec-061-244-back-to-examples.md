---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-061-244-back-to-examples
section_title: "Back to Examples"
section_number: 2.4.4
pages: 82-85
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
1. The trefoil knot.
The incompressible surface Σ is an annulus, henceρΣ : Z→ SL2(k(t)) is
abelian, and the theorem cannot apply. Nevertheless the torsion has a pole of
order one at ideal points corresponding toΣ, hence the equality of theorem
remains true.
2. The ﬁgure-eight knot.
There are two incompressible surfaces Σ1 and Σ2 that are two-holed tori,
and the torsion vanishes at order1 at each ideal point. Again the equality
1 =−χ(Σi)− 1 holds form =n = 1
3. The knot 5.2.
There are two incompressible surfacesΣ1 and Σ2 (see Figure 1 in the intro-
duction), and we haveχ(Σ1) = −4,χ (Σ2) = −2. At the ideal points, the
torsion vanishes at order1 (corresponds to Σ1) and 3 (corresponds to Σ2),
thus the equality of Theorem 2.0.2 holds.
4. The knot 6.1.
Again, there are two incompressible surface, the ﬁrst of Euler characteristic
−2(atwo-holedtorus),andthesecondofEulercharacteristic −6(atwo-holed
genus 3 surface). At the corresponding ideal points, the vanishing order of
tor(M, Ad◦ρ) is 1, respectively 5, that corresponds again with the equality
case of the theorem.
81
82
Chapitre 3
The standard torsion
Here M is a compact connected orientable 3-manifold, whose boundary is a torus.
In this chapter we pickX a one-dimensional component of irreducible type of the
character varietyX(M), and denote byk(X) its function ﬁeld. Here we consider the
action of the fundamental groupπ1(M) on the 2-dimensional vector spacek(X)2
through the tautological representationρ :π1(M)→ SL2(k(X)), and the correspon-
ding cohomological complexC∗(M,ρ ). When this complex is acyclic (for instance
whenX is a component of the character variety of a hyperbolic manifold that carries
the holonomy character, say ageometric component), the Reidemeister torsion of
this complex deﬁnes a rational function on the complex curveX. We prove that
this function’s zeros are precisely charactersχ¯ρ∈X where the residual cohomology
group H1(M, ¯ρ) are not trivial, and that this function is regular (it has no poles on
X). Moreover, we consider ¯X a smooth projective model, and show that an ideal
point of ¯X is a pole of the torsion function if it detects an incompressible surface
that splitsM into two handlebodies and which satisﬁes the following condition : the
boundary slopeγ is known (see [CCG+94]) to be mapped by the limit representa-
tion on a matrix with eigenvalue a root of unity. Moreover the order of this root
of unity divides the minimal number of boundary components of any component of
the incompressible surface Σ associated to this ideal point by the construction of
Section 1.3. We assume that the root of unity is 1, and we will say that the boun-
dary curve hastrivial eigenvalues. Such an assumption is motivated by numerical
computations, and by the fact that it occurs in many known examples. In fact it has
been a diﬃcult task to ﬁnd roots of unity diﬀerent of±1 with this construction, see
[Dun99] for the ﬁrst known example. The results of this chapter will be the core of
the upcoming paper [Ben17], we summarize them in the following theorems :
83
Theorem 3.0.1. Let X be a one dimensional component of the character variety
X(M) and ρ :π1(M)→ SL2(k(X)) the tautological representation. Assume that the
complex C∗(M,ρ ) is acyclic. Then tor(M,ρ ) is a regular function onX. Moreover
its order at a pointχ∈ X is given by the length of the torsion moduleH2(M,ρ )v,
wherev is the valuation associated toχ on the function ﬁeldk(X). In particular it
vanishes if and only ifH1(M, ¯ρ) is non trivial, where¯ρ is the residual representation
¯ρ :π1(M)
ρ
− →SL2(Ov)
modt
−−−→SL2(k) whose character isχ.
Theorem 3.0.2. Let x∈ ˆX be an ideal point in the smooth projective model of
X, and assume that an associated incompressible surfaceΣ is a union of parallel
homeomorphic copies Σi such that M\Si is a (union of) handlebodie(s). If the
