---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-014-321-the-distinguished-curve-of-characters
section_title: "The distinguished curve of characters"
section_number: 3.2.1
pages: 19-26
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
The variety of SL 2(C)-representations of M 3 is the set
hom(π1M 3, SL2(C)),
which it is an aﬃne algebraic set: if a generating set of π1M 3 has k elements,
then hom (π1M 3, SL2(C)) embeds in SL 2(C)k ⊂C4k, by mapping a representa-
tion to the image of its generators. The algebraic equations are indu ced by the
relations of the group.
19
The group PSL 2(C) acts on hom (π1M 3, SL2(C)) by conjugation, and the
aﬃne algebraic quotient is the variety of characters
X(M 3) ∶= X(M 3, SL2(C)) = hom(π1M 3, SL2(C))/slash.l⟩ft /slash.l⟩ftPSL2(C).
This is deﬁned in terms of the invariant functions: X(M 3, SL2(C)) is the alge-
braic aﬃne set whose function ring C[X(M 3, SL2(C))] is the ring of invariant
functions
C[hom(π1M 3, SL2(C))]PSL2(C).
By [93], see also [7, Appendix B] each component that contains the lift of
the holonomy of M 3 is a curve.
Deﬁnition 3.13. An irreducible component of X(M 3, SL2(C)) that contains
a lift of the holonomy is called a distinguished component and it is denoted by
X0(M 3).
For many manifolds, e.g. for 2-bridge knot exteriors, there is a uniq ue distin-
guished component. A priori there could be more components, but the deﬁnition
makes sense because they would be isomorphic. More precisely, the re are two
characters of the holonomy representation in PSL 2(C) that are complex conju-
gate from each other, that correspond to the diﬀerent orientat ions. When lifting
them to SL 2(C), this gives 2 /divid⟩s.alt0H 1(M 3; Z/slash.l⟩ft2Z)/divid⟩s.alt0 characters, two for each spin struc-
ture. The corresponding components X0(M 3) are isomorphic by means of the
natural action of H 1(M 3; Z/slash.l⟩ft2Z) and complex conjugation.
Recently, Casella, Luo, and Tillmann [11] have shown an example of hy -
perbolic manifold with one cusp M 3 such that the holonomy characters of the
diﬀerent orientations lie in diﬀerent components of X(M 3, PSL2(C)). To my
knowledge, the following question is still open:
Question 3.14. Once M 3 is oriented, are all the lifts of the oriented holonomy
contained in a single irreducible component of X(M 3, SL2(C))?
The distinguished component X(M 3, SL2(C)) is a curve and it was studied
by Thurston in his proof of the hyperbolic Dehn ﬁlling theorem [93]. Mor e
precisely, in a neighborhood of the holonomy of the complete struct ure of M 3,
the representations are holonomies of incomplete structures, an d in some cases
the completion is a Dehn ﬁlling. This is discussed in Paragraph 3.2.3.
3.2.2 T orsion on the distinguished curve of characters
We say that a character χ ∈X(M 3) is trivial if it takes values in {±2}, i.e. it is
a lift or the trivial character in PSL 2(C).
An irreducible character is the character of a unique conjugacy cla ss of repre-
sentations. A reducible character can correspond to more conju gacy classes, but
if the character is non-trivial, then either all representations with this character
are acyclic, either none of them is (Lemma A.3).
Deﬁnition 3.15. Deﬁne the torsion function on X0(M 3) minus the trivial
character:
TM (χρ) = /brac⟩l⟩ft.alt4 tor(M 3, ρ) if ρ is acyclic;
0 if χρ is non-trivial and ρ non-acyclic, (15)
where χρ denotes the character of ρ.
20
Proposition 3.16. For a hyperbolic oriented manifold with one cusp, the tor-
sion deﬁnes a rational function on X0(M 3), TM ∈C(X0(M 3)), which is regular
away from the trivial character.
In particular, if the trivial character is not contained in X0(M 3) (e.g. if
b1(M 3) = 1), then TM ∈C[X0(M 3)], i.e. it is holomorphic (with no poles)
TM ∶ X0(M 3) → C.
Remark 3.17. We prove that the trivial representation cannot be approached
by irreducible ones when b1(M 3) = 1 in Appendix A. This is always the case
when M 3 is a knot exterior.
Proof. The dimension of each cohomology group is upper semi-continuous on
the representation (see [42, Lemma 3.2], this is a particular case of t he semi-
continuity theorem [38, Ch. III, Theorem 12.8]). With Lemma A.3, we c an
conclude that acyclicity holds true in a dense open Zariski domain U ⊂X0(M 3),
after removing the trivial character if required. The fact that th e function TM
is algebraic on this domain is clear, as this is deﬁned from polynomials on t he
entries of ρ. Invariance by conjugation is one of the properties of the torsion .
Thus it remains to deal with the points where it is not acyclic. Recall th at by
Lemma A.3 a representation with nontrivial character is acyclic if and only all
representations with the same character are.
First notice that H 0(M 3; ρ) is trivial when the character χρ is non-trivial,
because this cohomology group is naturally isomorphic to the space o f invariants
Cρ(π1M 3). More precisely, Cρ(π1M 3) is non-trivial only when all elements in
ρ(π1M 3) have 1 as eigenvalue, which means that their trace is 2, i.e. χρ is
trivial. Thus by duality H0(M 3; ρ) = 0 when χρ is non-trivial.
Now ﬁx a representation ρ1 which is not acyclic and non-trivial. Non-
acyclicity implies that H1(M 3; ρ1) ≠0 and H2(M 3; ρ1) ≠0, as H0(M 3; ρ1) = 0,
the homotopical dimension of M 3 is 2, and χ(M 3) = 0. Notice that M 3 has
the simple homotopy type of a 2-complex (see [80, Page 54] for insta nce), that
can be used to compute the torsion. Using the notation of Section 2 .1, ﬁx a
basis {v1, v2} for C2 and lifts of cells ˜ ei
j of a triangulation of M 3. Then deﬁne
a family of basis ci(ρ) by varying the representation in vk ⊗ρ ˜ei
j. Now choose
˜b1(ρ) = c2(ρ) and ˜b0(ρ), a linear combination of c1(ρ) with constant coeﬃcients
(though c1(ρ) changes with ρ), so that ∂(˜b0(ρ1)) = c0(ρ1). The function
ρ ↦ [∂˜b1(ρ) ⊔ ˜b0(ρ), c1(ρ)]/slash.l⟩ft[∂˜b0(ρ), c0(ρ)] (16)
is well deﬁned in the set where its denominator does not vanish. This is a Zariski
open set that contains ρ1. On this set ∂˜b1(ρ) = ∂c2(ρ) has maximal rank iﬀ ρ
is acyclic, thus the function (16) vanishes when ρ is not acyclic, and when ρ is
acyclic (16) is the torsion.
Example 3.18. For the ﬁgure eight knot, in [51] Kitano computes it:
TM (ρ) = 2 − 2 tr(ρ(m)) = 2 − 2χρ(m) ,
where m denotes the meridian of the knot. Notice that here the function on ly
depends on tr (ρ(m)), namely the evaluation of the character at m, and one
does not need to describe the variety of characters. In general, as tr (ρ(m)) is a
non-constant function on the curve X0(M 3), TM (ρ) and χρ(m) = tr(ρ(m)) are
related by a polynomial equation; compare with [23].
21
3.2.3 Dehn ﬁlling space
Again let M 3 be an oriented, ﬁnite volume hyperbolic manifold with one cusp.
Consider the peripheral torus T 2, which is the boundary of a compact core of
M 3. Choose a frame on the peripheral torus T 2, i.e. two simple closed curves
that generate π1T 2, denote this frame by {m, l}. The notation suggests that
the canonical choice for a knot exterior is the pair meridian-longitud e.
A Dehn ﬁlling on M 3 is the result of gluing a solid torus D2 × S1 to a
compact core M 3 along the boundary. Up to homeomorphism, this manifold
depends only on the (unoriented) homology class in T 2 of the meridian, i.e. the
curve ∂D 2 × {∗}. This curve is written as ±(p m + q l), and the Dehn ﬁlling is
denoted by M 3
p/sl⊗sh.leftq.
When /divid⟩s.alt0p/divid⟩s.alt0+ /divid⟩s.alt0q/divid⟩s.alt0 is suﬃciently large, by Thurston’s theorem Mp/sl⊗sh.leftq is hyperbolic.
To prove it, he introduces the Thurston’s parameters of the Dehn ﬁlling space,
by writing, for representations close to the holonomy of the comple te hyperbolic
structure,
ρ(m) = ± /par⟩nl⟩ft.alt4eu/sl⊗sh.left2 1
0 e−u/sl⊗sh.left2/par⟩nright.alt4 ρ(l) = ± /par⟩nl⟩ft.alt4ev/sl⊗sh.left2 f (u)
0 e−v/sl⊗sh.left2/par⟩nright.alt4 (17)
with u, v ∈C in a neighborhood of the origin. For the holonomy of the complete
structure, u = v = 0 and write
cs = cs(l, m) = f (0) ∈C − R.
Deﬁnition 3.19. The parameter u ∈U ⊂C as above is called the Thurston
parameter and cs = cs(l, m) ∈C − R the cusp shape of the complete structure.
The Thurston parameter u is in fact a parameter of a double branched cov-
ering of a neighborhood of the lift of the holonomy ̺, as the local parameter
of X0(M 3) is tr (ρ(m)) = ±2 cosh u
2 . For the complete structure, the periph-
eral group acts as a lattice on a horosphere, that we view as C. Up to aﬃne
equivalence, this lattice is given by m ↦ 1, l ↦ cs.
Lemma 3.20 (Neumann and Zagier [79]) . There exists a (standard) neighbor-
hood of the origin U ⊂C such that:
(a) The map U → X0(M 3) such that u ↦ χρ, where ρ is as in (17) is a double
branched covering of a neighborhood in X0(M 3) of the character of the
holonomy of the complete structure.
(b) v is an analytic odd function on u that satisﬁes
v(u) = cs u + O(u3).
(c) f (u) = sinh(v)/slash.l⟩ft sinh(u).
The generalized Dehn ﬁlling coeﬃcients are the (p, q) ∈R2 ∪ {∞} such that
p u + q v = 2πi (18)
when u ≠0 and ∞ when u = 0.
Theorem 3.21. [93, 79] The generalized Dehn ﬁlling coeﬃcients deﬁne a home -
omorphism between U and a neighborhood of ∞ in S2 = R2 ∪ {∞}. If a pair of
coprime integers (p, q) ∈Z2 lies in the image of this homeomorphism, then M 3
p/sl⊗sh.leftq
is hyperbolic, with holonomy whose restriction to M 3 satisﬁes (18).
22
We are interested in properties of M 3
p/sl⊗sh.leftq.
Theorem 3.22 (Neumann and Zagier [79]) .
vol(M 3
p/sl⊗sh.leftq) = vol(M 3) − π2 Im(cs)
/divid⟩s.alt0p + cs q/divid⟩s.alt02 + O /par⟩nl⟩ft.alt4 1
/divid⟩s.alt0p + cs q/divid⟩s.alt04 /par⟩nright.alt4 .
We are also interested in the complex length of the soul of the solid to rus
added by Dehn ﬁlling, which is a short geodesic. Let r and s be integers satisfy-
ing p s − q r = 1, this complex length is r u + s v. A straightforward computation
yields [82]:
Remark 3.23. The complex length of the core of the solid torus M 3
p/sl⊗sh.leftq is
r u + s v = 2πi r
p + v
p = 2πi s
q + u
q
Given a spin structure σ on M 3, it may extend or not to M 3
p,q. It is easy to
give a characterization using the bijection of Proposition 3.1.
Lemma 3.24. [63] A spin structure σ on M extends to Mp,q iﬀ the correspond-
ing lift of the holonomy ̺σ (for the complete structure on M 3) satisﬁes
tr(̺σ(p m + q l)) = −2.
3.2.4 T orsion for Dehn ﬁllings
Let /divid⟩s.alt0p/divid⟩s.alt0+/divid⟩s.alt0q/divid⟩s.alt0 be suﬃciently large and let σ be a spin structure on M 3 extensible to
M 3
p/sl⊗sh.leftq. Let ρp/sl⊗sh.leftq,σ denote the lift of the holonomy of the restriction to M 3 of the
hyperbolic structure on M 3
p/sl⊗sh.leftq, and χp/sl⊗sh.leftq,σ the corresponding character. Let λp/sl⊗sh.leftq
denote the complex length of the soul of the ﬁlling torus. There is a s urgery
formula:
Proposition 3.25. Let M 3 be as above. For /divid⟩s.alt0p/divid⟩s.alt0+ /divid⟩s.alt0q/divid⟩s.alt0 suﬃciently large:
τ (M 3
p/sl⊗sh.leftq, σ) = TM (χp/sl⊗sh.leftq,σ )
2(1 − cosh(λp/sl⊗sh.leftq/slash.l⟩ft2)) .
This proposition can be proved using Mayer-Vietoris (Proposition 2.1 0) to
the pair (M 3, D2 × S1). The proof can be found for instance in [49] for the
ﬁgure eight knot, and in [94] for twist knots, but it applies to every c usped
manifold, and it is essentially done too in [82, Proposition 4.10]. The only
computation required is the torsion of the solid torus added by Dehn ﬁlling, or
its core geodesic, which is (by Example 2.16):
1
det /par⟩nl⟩ft.alt4/par⟩nl⟩ft.alt41 0
0 1 /par⟩nright.alt4 − /par⟩nl⟩ft.alt4eλp/slash.left q/sl⊗sh.left2 0
0 e−λp/slash.left q/sl⊗sh.left2/par⟩nright.alt4/par⟩nright.alt4
= 1
2(1 − cosh(λp/sl⊗sh.leftq/slash.l⟩ft2)).
Remark 3.26. The complex length λp/sl⊗sh.leftq is deﬁned up to addition of a term
in 2 πiZ. The spin structure (or equivalently a choice of lift of the holonomy)
determines λp/sl⊗sh.leftq up to 4 πiZ, as the holonomy of this curve is conjugate to
/par⟩nl⟩ft.alt4eλp/slash.left q/sl⊗sh.left2 0
0 e−λp/slash.left q/sl⊗sh.left2/par⟩nright.alt4 .
23
Corollary 3.27. There exist closed hyperbolic manifolds N 3 with two spin
structures σ and σ′ so that τ (N 3, σ) ≠τ (N 3, σ′).
Proof. The manifolds are obtained by Dehn ﬁlling on the ﬁgure eight knot.
Consider the sequence pn/slash.l⟩ftqn = 2n so that both spin structures on the ﬁgure
eight knot exterior M 3 extend to M 3
pn/sl⊗sh.leftqn
, i.e. H1(M 3
2n; Z/slash.l⟩ft2Z) ≅Z/slash.l⟩ft2Z. The
corresponding lifts diﬀer on the sign of the trace of the meridian. As the core
of the solid torus is homologous to the meridian, the sign of the trace s of these
cores diﬀer. Hence for one of the lifts the complex length (modulo 4 πiZ) is λ2n,
for the other one it is λ2n + 2πi by Remark 3.26. By Remark 3.23, one may
approximate
λ2n = 2πi
2n + O /par⟩nl⟩ft.alt3 1
n2 /par⟩nright.alt3 . (19)
The goal is to show that the limit
lim
n→+∞
/divid⟩s.alt0τ (M2n, σ)/divid⟩s.alt0
/divid⟩s.alt0τ (M2n, σ′)/divid⟩s.alt0 (20)
is not 1. By Proposition 3.25 it is the product of the limits:
lim
n→∞
1 − cosh(λ2n/slash.l⟩ft2)
1 − cosh((λ2n + 2πi)/slash.l⟩ft2) = lim
n→∞
1 − cos π
2n
1 + cos π
2n
= 0 (21)
(using the approximation (19)) and
lim
n→∞
TM (χ2n,σ)
TM (χ2n,σ′) = τ (M 3, σ)
τ (M 3, σ′) . (22)
As for one of the spin structures the trace of the meridian is 2 and f or the other
−2, by Example 3.18, the limit in (22) is (2 − 2 ⋅ (−2))/slash.l⟩ft(2 − 2 ⋅ 2) = −3. Thus the
limit (20) vanishes, hence it is not 1.
The previous argument applies to any knot exterior, the precise va lue of the
torsion is not needed. Corollary 3.27 holds true also for cusped manif olds, by
applying an analogous formula for partial surgery.
Corollary 3.28. The set of modules of the torsions /divid⟩s.alt2τ (M 3
p/sl⊗sh.leftq, σ)/divid⟩s.alt2 obtained by
Dehn ﬁlling on M 3, so that the spin structure σ on M 3 extends to M 3
p/sl⊗sh.leftq, is
dense in
/brack⟩tl⟩ft.alt31
4 /divid⟩s.alt0τ (M 3, σ)/divid⟩s.alt0, +∞/par⟩nright.alt3 .
Proof. By the surgery formula, Proposition 3.25, it suﬃces to show that
/divid⟩s.alt11 − cosh(λp/sl⊗sh.leftq/slash.l⟩ft2)/divid⟩s.alt1
is dense in the interval [0, 2]. Let r, s ∈Z be such that ps−qr = 1, by Remark 3.23,
λp/sl⊗sh.leftq = 2πi r
p + u
p and u → 0. Then the result follows from the density of cos (π r
p )
in [−1, 1]. Notice that extendibility of σ is just determined by a condition
a p + b q ≡0 mod 2, for a, b ∈Z/slash.l⟩ft2Z depending on σ.
As the surgery formula shows, this density is a consequence of the contribu-
tion of the core geodesics. Notice that in Theorem 3.7 the hypothes is require
the length of geodesics to be bounded below away from zero.
24
3.2.5 Branched coverings on the ﬁgure eight
We next consider another family of examples. We consider it only for t he ﬁgure
eight knot, but it generalizes to other manifolds.
Consider M 3
n the n-th cyclic branched covering of S3, branched along the
ﬁgure eight knot. It is hyperbolic for n ≥4. Its torsion may be computed
by means of the twisted Alexander polynomial, by using the formula ` a la Fox,
Proposition 2.15, due to Turaev [95], see also [25, 83, 89, 85, 109]. M ore precisely,
this polynomial is
pχ(t) = t2 − 2χ(m)t + 1,
by (46), cf. [54]. Notice that its value at 1 agrees with Example 3.18. T he
holonomy of M 3
n extends to a holonomy of the quotient orbifold M 3
n/slash.l⟩ft(Z/slash.l⟩ftnZ)
in PSL 2(C). It induces a representation of the exterior of the not S3 − K that
lifts to SL 2(C), that we denote by ρn. Since a rotation of angle 2 π/slash.l⟩ftn has trace
±2 cos(π/slash.l⟩ftn), we have
χρn (m) = tr(ρn(m)) = ±2 cos(π/slash.l⟩ftn).
Using Proposition 2.15, if Σ n ⊂Mn is the lift of the branching locus, then
tor(M 3
n − Σ n, σ) =
n−1
/product.disp
k=0
pχn (e2πi k
n ) =
n−1
/product.disp
k=0
/par⟩nl⟩ft.alt2e4πi k
n ∓ 4 cos(π/slash.l⟩ftn)e2πi k
n + 1/par⟩nright.alt2 .
By the surgery formula (Proposition 3.25) and knowing that the com plex length
of the core geodesic is ≈
√
3 π
n + O /par⟩nl⟩ft.alt11
n3 /par⟩nright.alt1 (Remark 3.23),
tor(M 3
n, σ) = 1/slash.l⟩ft2
1 − cosh /par⟩nl⟩ft.alt2
√
3 π
n + O /par⟩nl⟩ft.alt11
n3 /par⟩nright.alt1/par⟩nright.alt2
n−1
/product.disp
k=0
/par⟩nl⟩ft.alt2e4πi k
n ∓ 4 cos(π/slash.l⟩ftn)e2πi k
n + 1/par⟩nright.alt2 . (23)
In particular,
lim
n→∞
log /divid⟩s.alt0tor(M 3
n, σ)/divid⟩s.alt0
n = lim
n→∞
1
n
n−1
/summ⊗tion.disp
k=0
log /divid⟩s.alt2e4πi k
n ± 4 cos(π/slash.l⟩ftn)e2πi k
n + 1/divid⟩s.alt2. (24)
Here we used that lim x→0+ x log x = 0 to get rid of the ﬁrst term, outside the
product, in (23). As t2 ∓ 4t + 1 has no roots in the unit circle, the limit (24)
converges to
1
2π /integr⊗l.disp/divides.⊗lt0z/divides.⊗lt0=1
log /divid⟩s.alt0z2 ± 4z + 1/divid⟩s.alt0.
Thus by Jensen’s formula
lim
n→∞
log /divid⟩s.alt0tor(M 3
n, σ)/divid⟩s.alt0
n = log /divid⟩s.alt02 +
√
3/divid⟩s.alt0.
This approach uses the ideas on Mahler measure of [89]. It applies to a
hyperbolic knot provided that the torsion polynomial has no roots in the unit
circle. It is easy to prove that the roots of the polynomial are not r oots of
the unity, but this does not discard roots in the unit circle. For the a djoint
representation, the nonexistence of roots in the unit circle has be en proved by
Kapovich [46].
25
4 Torsions for higher dimensional representa-
tions of hyperbolic three-manifolds
This section is devoted to further Reidemeister torsions naturally a ssociated to
hyperbolic three-manifolds, those obtained by using the (ﬁnite dime nsional and
linear) representations of SL 2(C).
