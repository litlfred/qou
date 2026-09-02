---
doc_id: s00209-021-02825-4
doc_title: "Mathematische Zeitschrift (2022) 300:1359–1400 A representation theoretic explanation of the Borcea–Brändén characterization Jonathan Leake 1 © The Author(s) 2021"
section_id: sec-015-51-other-regions
section_title: "Other regions"
section_number: 5.1
pages: 17-19
source_pdf: s00209-021-02825-4.pdf
source_sha256: 85ca5ec21f42a988
---
We now generalize the above theorem to other regions via SL2(C) action and topological con-
siderations. Theorem 5.7 can then be considered our most general form of Grace’s theorem.
First though, we deﬁne two new notions in order to simplify the rest of this section.
Deﬁnition 5.2 Fix m ∈ N0 and any sets S1, S2 ⊆ (CP1)m . We call (S1, S2) a Grace pair if:
for all λ ∈ Nm
0 and p, q ∈ V(λ) such that p is S1-stable and q is S2-stable, we have that
Dλ(p ⊗ q) ⁄= 0. That is, if Grace’s theorem holds for S1 and S2.
Deﬁnition 5.3 We say that a Grace pair is disjoint if it is of the form (C1 ×···× Cm, B1 ×
···× Bm) and Ck and Bk are disjoint for all k ∈[ m].
This yields the following restatement of the above theorem.
Corollary 5.4 For any m ∈ N0, ((H+ ∪ R+)m,( H− ∪ R−)m) is a Grace pair.
123
1376 J. Leake
The sets considered above intersect at 2 points (0 and ∞), and this ends up being crucial
to the proof. So, in order to extend to the full generality of Grace’s theorem, we will need
to ﬁnd such points even when the stability sets of two polynomials p and q do not a priori
intersect at all. To this end, we give the following lemmas.
Lemma 5.5 Fix λ ∈ Nm
0 and any closed circular regions C1,..., Cm ⊂ CP1.L e tp ∈ V(λ)
be (C1 ×···× Cm)-stable. There exist open circular regions U1,..., Um such that Ck ⊂ Uk
for all k ∈[ m] and p is (U1 ×···× Um)-stable.
Proof Follows from compactness of CP1 and closedness of C1 × ... × Cm and of the zero
set of p. ⊓⊔
For the next lemma, note that the boundary of any circular region C is topologically
equivalent to the unit circle in C (i.e., the boundary of the unit disc). With this, we call a
portion of the boundary of C open if it is open when considered as a subset of the unit circle.
Further recall the characterization of projectively convex regions given by Proposition 4.5.
Lemma 5.6 Fix n ∈ N0 and any projectively convex C ≡ C◦ ∪ γ ⊂ CP1,w h e r eC◦ is
an open circular region and γ is a connected portion of its boundary. Let p ∈ V(n) be
C-stable. There is an open connected subset /Gamma1of the boundary of C◦ such that γ ⊆ /Gamma1and
pi s (C◦ ∪ /Gamma1)-stable.
Proof Let∂C◦ denote the boundary of (the closure of)C◦,a n dl e tS ⊆ CP1 be the intersection
of ∂C◦ and the zero set of p. Since the zero set of p is closed, we have that S is closed in
∂C◦. And further, γ ∩ S = ∅ by assumption. Deﬁning /Gamma1to be the connected component of
∂C◦\S containing γ then gives the result. ⊓⊔
Using these lemmas and the SL 2(C)-invariance of the apolarity form, we obtain the
following generalization of Grace’s theorem. Here, (ii) and (iii) give the multivariate Grace’s
t h e o r e mp r o v e ni n[2].
Theorem 5.7 For m ∈ N0 and C1,..., Cm, B1,..., Bm ⊆ CP1, we have that (C1 ×···×
Cm, B1 ×···× Bm) is a Grace pair for the following regions.
(i) For all k ∈[ m],C k and B k are projectively convex, Ck ∪ Bk = CP1, and C k ∩ Bk is
exactly two points.
(ii) For all k ∈[ m],C k is a closed circular region, B k is an open circular region, and
Ck ∪ Bk = CP1.
(iii) For all k ∈[ m],C k is an open circular region, B k is a closed circular region, and
Ck ∪ Bk = CP1.
(iv) For m = 1,C 1 and B1 are projectively convex and C1 ∪ B1 = CP1.
Proof (i). By Proposition 4.5, every projectively convex region in CP1 is the union of an
open circular region and a portion of its boundary. Since Ck ∪ Bk = CP1 and Ck ∩ Bk is
exactly two points, we then must have that Ck = φk · (H+ ∪ R+) and Bk = φk · (H− ∪ R−)
for some φk ∈ SL2(C).S i n c eDλ is (SL2(C))m -invariant, the result follows from Theorem
5.1.
(ii). Fix p, q ∈ V(λ).I f p is (C1 ×···× Cm)-stable and q is (B1 ×···× Bm)-stable, then
Lemma 5.5 implies p is (U1 ×···× Um)-stable for some open circular regions U1,..., Um
such that Ck ⊂ Uk for all k ∈[ m].S i n c eCk ∪ Bk = CP1, we then have that Uk ∩ Bk is open
and nonempty. SinceUk and Bk are circular regions, their intersection in fact contains an open
123
A representation theoretic explanation... 1377
annulus or open strip in C. Therefore we may slightly shrink Uk and Bk to get closed circular
regions U′
k and B′
k such that U′
k ∪ B′
k = CP1 and U′
k ∩ B′
k = ∂U′
k = ∂ B′
k ,w h e r e∂ B′
k denotes
the boundary of B′
k . We can then further remove portions of the respective boundaries of U′
k
and B′
k to get projectively convex regions U′′
k and B′′
k such that U′′
k ∪ B′′
k = CP1 and U′
k ∩ B′
k
is exactly two points. SinceU′′
k ⊂ Uk and B′′
k ⊂ Bk ,w eh a v et h a tp is (U′′
1 ×···× U′′
m)-stable
and q is (B′′
1 ×···× B′′
m)-stable. Therefore (i) implies Dλ(p ⊗ q) ⁄= 0, and this implies (ii).
(iii). Same argument as (ii).
(iv). Let p, q ∈ V(n) be such that p is C1-stable and q is B1-stable. Deﬁning B′
1 :=
CP1\C1 ⊆ B1,w ef u r t h e rh a v et h a tq is B′
1-stable. So WLOG we may assume that B1 = B′
1.
Note that this implies ∂C◦
1 = ∂ B◦
1 ; that is, the boundaries coincide. If C1 is a circular region
then so is B1, and therefore Dn(p ⊗ q) ⁄= 0 by (ii) or (iii). This implies (iv) in this case.
Otherwise by Proposition 4.5,w eh a v et h a tC1 = C◦
1 ∪ γ1 where C◦
1 is an open circular
region and∅ ⁄= γ1 ⊆ ∂C◦
1 . Analogously we haveB1 = B◦
1 ∪ψ1 with∅ ⁄= ψ1 ⊆ ∂ B◦
1 = ∂C◦
1 .
Lemma 5.6 then implies there exist /Gamma11 and /Psi11, which are open portions of the boundary of
C◦
1 , such that γ1 ⊆ /Gamma11, ψ1 ⊆ /Psi11, p is (C◦
1 ∪ /Gamma11)-stable, and q is (B◦
1 ∪ /Psi11)-stable. Since
/Gamma11 ∪ /Psi11 = ∂C◦
1 , we then further can ﬁnd closed subsets /Gamma1′
1 ⊂ /Gamma11 and /Psi1′
1 ⊂ /Psi11 such that
/Gamma1′
1 ∪ /Psi1′
1 = ∂C◦
1 and /Gamma1′∩ /Psi1′is exactly two points. Therefore Dn(p ⊗ q) ⁄= 0 by (i), and this
implies (iv). ⊓⊔
Notice that (ii) and (iii) in this result do not allow for mixed open and closed stability
regions. That is, all of the Ck must be open and all of the Bk closed, or vice versa. We show
that this particular point cannot be ignored, using the following example.
Example 5.8 Let λ = (1, 1, 1), denote E := CP1\D, and consider the polynomial p :=
x1x2x3 − y1 y2 y3 = Hmgλ(x1x2x3 − 1). First, it is easy to see that Dλ(p ⊗ p) = 0. Also, p
is D3-stable and E3-stable, but it is not D
3
-stable nor E3-stable (zero at (xk, yk) = (1, 1) for
k ∈[ 3]). That is, the fact that Dλ(p ⊗ p) = 0 does not contradict (ii) or (iii) of the previous
theorem.
On the other hand, p is both (D × D × D)-stable and (E × E × E)-stable. This shows
that (D × D × D, E × E × E) is not a Grace pair. That is, mixed open and closed stability
regions cannot be included in (ii) and (iii) of the previous theorem.
As for whether or not the two-point intersection condition can be removed from (i) seems
to be a more subtle point. It would be quite nice if this condition could be removed, but it is
unclear whether or not it is possible.
