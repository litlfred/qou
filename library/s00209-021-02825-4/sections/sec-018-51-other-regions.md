---
doc_id: s00209-021-02825-4
doc_title: "A representation theoretic explanation of the Borcea–Brändén characterization"
section_id: sec-018-51-other-regions
section_title: "Other regions"
section_number: 5.1
pages: 17-19
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
toc_source: outline
doc_brief: "A representation theoretic explanation of the Borcea–Brändén characterization — In 2009, Borcea and Brändén characterized all linear operators on multivariate polynomials which preserve the property"
---
We now generalize the above theorem to other regions via SL2(C) action and topological con-
siderations. Theorem 5.7 can then be considered our most general form of Grace’s theorem.
First though, we deﬁne two new notions in order to simplify the rest of this section.
Deﬁnition 5.2 Fix m ∈N0 and any sets S1, S2 ⊆(CP1)m. We call (S1, S2) a Grace pair if:
for all λ ∈Nm
0 and p, q ∈V (λ) such that p is S1-stable and q is S2-stable, we have that
Dλ(p ⊗q)̸ = 0. That is, if Grace’s theorem holds for S1 and S2.
Deﬁnition 5.3 We say that a Grace pair is disjoint if it is of the form (C1 × · · · × Cm, B1 ×
· · · × Bm) and Ck and Bk are disjoint for all k ∈[m].
This yields the following restatement of the above theorem.
Corollary 5.4 For any m ∈N0, ((H+ ∪R+)m, (H−∪R−)m) is a Grace pair.
1376
J. Leake
The sets considered above intersect at 2 points (0 and ∞), and this ends up being crucial
to the proof. So, in order to extend to the full generality of Grace’s theorem, we will need
to ﬁnd such points even when the stability sets of two polynomials p and q do not a priori
intersect at all. To this end, we give the following lemmas.
Lemma 5.5 Fix λ ∈Nm
0 and any closed circular regions C1, . . . , Cm ⊂CP1. Let p ∈V (λ)
be (C1 ×· · · ×Cm)-stable. There exist open circular regions U1, . . . , Um such that Ck ⊂Uk
for all k ∈[m] and p is (U1 × · · · × Um)-stable.
Proof Follows from compactness of CP1 and closedness of C1 × . . . × Cm and of the zero
set of p.
⊓⊔
For the next lemma, note that the boundary of any circular region C is topologically
equivalent to the unit circle in C (i.e., the boundary of the unit disc). With this, we call a
portion of the boundary of C open if it is open when considered as a subset of the unit circle.
Further recall the characterization of projectively convex regions given by Proposition 4.5.
Lemma 5.6 Fix n ∈N0 and any projectively convex C ≡C◦∪γ ⊂CP1, where C◦is
an open circular region and γ is a connected portion of its boundary. Let p ∈V (n) be
C-stable. There is an open connected subset 
 of the boundary of C◦such that γ ⊆
 and
p is (C◦∪
)-stable.
Proof Let ∂C◦denote the boundary of (the closure of) C◦, and let S ⊆CP1 be the intersection
of ∂C◦and the zero set of p. Since the zero set of p is closed, we have that S is closed in
∂C◦. And further, γ ∩S = ∅by assumption. Deﬁning 
 to be the connected component of
∂C◦\S containing γ then gives the result.
⊓⊔
Using these lemmas and the SL2(C)-invariance of the apolarity form, we obtain the
following generalization of Grace’s theorem. Here, (ii) and (iii) give the multivariate Grace’s
theorem proven in [2].
Theorem 5.7 For m ∈N0 and C1, . . . , Cm, B1, . . . , Bm ⊆CP1, we have that (C1 × · · · ×
Cm, B1 × · · · × Bm) is a Grace pair for the following regions.
(i) For all k ∈[m], Ck and Bk are projectively convex, Ck ∪Bk = CP1, and Ck ∩Bk is
exactly two points.
(ii) For all k ∈[m], Ck is a closed circular region, Bk is an open circular region, and
Ck ∪Bk = CP1.
(iii) For all k ∈[m], Ck is an open circular region, Bk is a closed circular region, and
Ck ∪Bk = CP1.
(iv) For m = 1, C1 and B1 are projectively convex and C1 ∪B1 = CP1.
Proof (i). By Proposition 4.5, every projectively convex region in CP1 is the union of an
open circular region and a portion of its boundary. Since Ck ∪Bk = CP1 and Ck ∩Bk is
exactly two points, we then must have that Ck = φk · (H+ ∪R+) and Bk = φk · (H−∪R−)
for some φk ∈SL2(C). Since Dλ is (SL2(C))m-invariant, the result follows from Theorem
5.1.
(ii). Fix p, q ∈V (λ). If p is (C1 ×· · ·×Cm)-stable and q is (B1 ×· · ·× Bm)-stable, then
Lemma 5.5 implies p is (U1 × · · · × Um)-stable for some open circular regions U1, . . . , Um
such that Ck ⊂Uk for all k ∈[m]. Since Ck ∪Bk = CP1, we then have that Uk ∩Bk is open
and nonempty. Since Uk and Bk are circular regions, their intersection in fact contains an open
A representation theoretic explanation...
1377
annulus or open strip in C. Therefore we may slightly shrink Uk and Bk to get closed circular
regions U ′
k and B′
k such that U ′
k ∪B′
k = CP1 and U ′
k ∩B′
k = ∂U ′
k = ∂B′
k, where ∂B′
k denotes
the boundary of B′
k. We can then further remove portions of the respective boundaries of U ′
k
and B′
k to get projectively convex regions U ′′
k and B′′
k such that U ′′
k ∪B′′
k = CP1 and U ′
k ∩B′
k
is exactly two points. Since U ′′
k ⊂Uk and B′′
k ⊂Bk, we have that p is (U ′′
1 ×· · ·×U ′′
m)-stable
and q is (B′′
1 × · · · × B′′
m)-stable. Therefore (i) implies Dλ(p ⊗q)̸ = 0, and this implies (ii).
(iii). Same argument as (ii).
(iv). Let p, q ∈V (n) be such that p is C1-stable and q is B1-stable. Deﬁning B′
1 :=
CP1\C1 ⊆B1, we further have that q is B′
1-stable. So WLOG we may assume that B1 = B′
1.
Note that this implies ∂C◦
1 = ∂B◦
1; that is, the boundaries coincide. If C1 is a circular region
then so is B1, and therefore Dn(p ⊗q)̸ = 0 by (ii) or (iii). This implies (iv) in this case.
Otherwise by Proposition 4.5, we have that C1 = C◦
1 ∪γ1 where C◦
1 is an open circular
regionand∅̸ = γ1 ⊆∂C◦
1.Analogouslywehave B1 = B◦
1∪ψ1 with∅̸ = ψ1 ⊆∂B◦
1 = ∂C◦
1.
Lemma 5.6 then implies there exist 
1 and 
1, which are open portions of the boundary of
C◦
1, such that γ1 ⊆
1, ψ1 ⊆
1, p is (C◦
1 ∪
1)-stable, and q is (B◦
1 ∪
1)-stable. Since

1 ∪
1 = ∂C◦
1, we then further can ﬁnd closed subsets 
′
1 ⊂
1 and 
′
1 ⊂
1 such that

′
1 ∪
′
1 = ∂C◦
1 and 
′ ∩
′ is exactly two points. Therefore Dn(p ⊗q)̸ = 0 by (i), and this
implies (iv).
⊓⊔
Notice that (ii) and (iii) in this result do not allow for mixed open and closed stability
regions. That is, all of the Ck must be open and all of the Bk closed, or vice versa. We show
that this particular point cannot be ignored, using the following example.
Example 5.8 Let λ = (1, 1, 1), denote E := CP1\D, and consider the polynomial p :=
x1x2x3 −y1y2y3 = Hmgλ(x1x2x3 −1). First, it is easy to see that Dλ(p ⊗p) = 0. Also, p
is D3-stable and E3-stable, but it is not D
3-stable nor E3-stable (zero at (xk, yk) = (1, 1) for
k ∈[3]). That is, the fact that Dλ(p ⊗p) = 0 does not contradict (ii) or (iii) of the previous
theorem.
On the other hand, p is both (D × D × D)-stable and (E × E × E)-stable. This shows
that (D × D × D, E × E × E) is not a Grace pair. That is, mixed open and closed stability
regions cannot be included in (ii) and (iii) of the previous theorem.
As for whether or not the two-point intersection condition can be removed from (i) seems
to be a more subtle point. It would be quite nice if this condition could be removed, but it is
unclear whether or not it is possible.
