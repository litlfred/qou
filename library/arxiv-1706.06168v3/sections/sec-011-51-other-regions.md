---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-011-51-other-regions
section_title: "Other Regions"
section_number: 5.1
pages: 15-16
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
---
We now generalize the above theorem to other regions via SL 2(C) action and topological considerations.
Theorem 5.7 can then be considered our most general form of Grace’s theorem . First though, we deﬁne two
new notions in order to simplify the rest of this section.
Deﬁnition 5.2. Fixm ∈ N0 and any sets S1,S 2 ⊆ (CP1)m. We call ( S1,S 2) a Grace pair if: for all λ ∈ Nm
0
and p,q ∈V (λ) such that p is S1-stable and q is S2-stable, we have that Dλ(p ⊗q) ⁄= 0. That is, if Grace’s
theorem holds for S1 and S2.
Deﬁnition 5.3. We say that a Grace pair is disjoint if it is of the form ( C1 × · · · ×Cm,B 1 × · · · ×Bm) and
Ck and Bk are disjoint for all k ∈ [m].
This yields the following restatement of the above theorem.
Corollary 5.4. For any m ∈ N0, ((H+ ∪ R+)m, (H− ∪ R−)m) is a Grace pair.
The sets considered above intersect at 2 points (0 and ∞), and this ends up being crucial to the proof.
So, in order to extend to the full generality of Grace’s theorem, we will need to ﬁnd such points even when
the stability sets of two polynomials p andq do not a priori intersect at all. To this end, we give the following
lemmas.
Lemma 5.5. Fixλ ∈ Nm
0 and any closed circular regionsC1,...,C m ⊂ CP1. Let p ∈V (λ) be (C1×· · ·×Cm)-
stable. There exist open circular regions U1,...,U m such that Ck ⊂Uk for all k ∈ [m] andp is (U1×· · ·×Um)-
stable.
Proof. Follows from compactness of CP1 and closedness of C1 ×... ×Cm and of the zero set of p.
For the next lemma, note that the boundary of any circular region C is topologically equivalent to the
unit circle in C (i.e., the boundary of the unit disc). With this, we call a portion of the boundary of C open
if it is open when considered as a subset of the unit circle. Further re call the characterization of projectively
convex regions given by Proposition 4.5.
Lemma 5.6. Fix n ∈ N0 and any projectively convex C ≡ C◦ ∪γ ⊂ CP1, where C◦ is an open circular
region and γ is a connected portion of its boundary. Let p ∈V (n) beC-stable. There is an open connected
subset Γ of the boundary of C◦ such that γ ⊆ Γ and p is (C◦ ∪ Γ) -stable.
Proof. Let∂C ◦ denote the boundary of (the closure of) C◦, and let S ⊆ CP1 be the intersection of ∂C ◦ and
the zero set of p. Since the zero set of p is closed, we have that S is closed in ∂C ◦. And further, γ ∩S = ∅
by assumption. Deﬁning Γ to be the connected component of ∂C ◦ \S containingγ then gives the result.
Using these lemmas and the SL 2(C)-invariance of the apolarity form, we obtain the following generaliza -
tion of Grace’s theorem. Here, ( ii) and (iii) give the multivariate Grace’s theorem proven in [ BB09b].
Theorem 5.7. Form ∈ N0 andC1,...,C m,B 1,...,B m ⊆ CP1, we have that (C1 × · · · ×Cm,B 1 × · · · ×Bm)
is a Grace pair for the following regions.
15
(i) For all k ∈ [m], Ck and Bk are projectively convex, Ck ∪Bk = CP1, and Ck ∩Bk is exactly two points.
(ii) For all k ∈ [m], Ck is a closed circular region, Bk is an open circular region, and Ck ∪Bk = CP1.
(iii) For all k ∈ [m], Ck is an open circular region, Bk is a closed circular region, and Ck ∪Bk = CP1.
(iv) For m = 1, C1 and B1 are projectively convex and C1 ∪B1 = CP1.
Proof. (i). By Proposition 4.5, every projectively convex region in CP1 is the union of an open circular region
and a portion of its boundary. Since Ck ∪Bk = CP1 and Ck ∩Bk is exactly two points, we then must have
thatCk =φk · (H+ ∪ R+) and Bk =φk · (H− ∪ R−) for some φk ∈ SL2(C). Since Dλ is (SL 2(C))m-invariant,
the result follows from Theorem 5.1.
(ii). Fix p,q ∈V (λ). If p is (C1 ×· · ·×Cm)-stable and q is (B1 ×· · ·×Bm)-stable, then Lemma 5.5 implies
p is (U1 × · · · ×Um)-stable for some open circular regions U1,...,U m such that Ck ⊂Uk for all k ∈ [m]. Since
Ck ∪Bk = CP1, we then have that Uk ∩Bk is open and nonempty. Since Uk and Bk are circular regions,
their intersection in fact contains an open annulus or open strip in C. Therefore we may slightly shrink Uk
andBk to get closed circular regions U ′
k andB′
k such that U ′
k ∪B′
k = CP1 andU ′
k ∩B′
k =∂U ′
k =∂B ′
k, where
∂B ′
k denotes the boundary of B′
k. We can then further remove portions of the respective boundar ies of U ′
k
and B′
k to get projectively convex regions U ′′
k and B′′
k such that U ′′
k ∪B′′
k = CP1 andU ′
k ∩B′
k is exactly two
points. Since U ′′
k ⊂Uk andB′′
k ⊂Bk, we have that p is (U ′′
1 ×· · ·×U ′′
m)-stable and q is (B′′
1 ×· · ·×B′′
m)-stable.
Therefore (i) implies Dλ(p ⊗q) ⁄= 0, and this implies ( ii).
(iii). Same argument as ( ii).
(iv). Let p,q ∈V (n) be such that p is C1-stable and q is B1-stable. Deﬁning B′
1 := CP1 \C1 ⊆B1, we
further have thatq isB′
1-stable. So WLOG we may assume that B1 =B′
1. Note that this implies ∂C ◦
1 =∂B ◦
1 ;
that is, the boundaries coincide. If C1 is a circular region then so is B1, and therefore Dn(p ⊗q) ⁄= 0 by (ii)
or (iii). This implies ( iv) in this case.
Otherwise by Proposition 4.5, we have that C1 = C◦
1 ∪γ1 where C◦
1 is an open circular region and
∅ ⁄= γ1 ⊆ ∂C ◦
1 . Analogously we have B1 = B◦
1 ∪ψ1 with ∅ ⁄= ψ1 ⊆ ∂B ◦
1 = ∂C ◦
1 . Lemma 5.6 then implies
there exist Γ 1 and Ψ 1, which are open portions of the boundary of C◦
1 , such that γ1 ⊆ Γ 1, ψ1 ⊆ Ψ 1, p is
(C◦
1 ∪ Γ 1)-stable, and q is (B◦
1 ∪ Ψ 1)-stable. Since Γ 1 ∪ Ψ 1 = ∂C ◦
1 , we then further can ﬁnd closed subsets
Γ ′
1 ⊂ Γ 1 and Ψ ′
1 ⊂ Ψ 1 such that Γ ′
1 ∪ Ψ ′
1 =∂C ◦
1 and Γ ′ ∩ Ψ ′ is exactly two points. Therefore Dn(p ⊗q) ⁄= 0
by (i), and this implies ( iv).
Notice that (ii) and (iii) in this result do not allow for mixed open and closed stability regions. T hat is,
all of the Ck must be open and all of the Bk closed, or vice versa. We show that this particular point cannot
be ignored, using the following example.
Example 5.8. Let λ = (1, 1, 1), denote E := CP1 \ D, and consider the polynomial p :=x1x2x3 −y1y2y3 =
Hmgλ(x1x2x3 − 1). First, it is easy to see that Dλ(p ⊗p) = 0. Also, p is D3-stable and E3-stable, but it is
not D
3
-stable nor E
3
-stable (zero at ( xk,y k) = (1, 1) for k ∈ [3]). That is, the fact that Dλ(p ⊗p) = 0 does
not contradict (ii) or (iii) of the previous theorem.
On the other hand, p is both ( D × D × D)-stable and ( E ×E ×E)-stable. This shows that ( D × D ×
D,E ×E ×E) is not a Grace pair. That is, mixed open and closed stability regions ca nnot be included in
(ii) and (iii) of the previous theorem.
As for whether or not the two-point intersection condition can be r emoved from (i) seems to be a more
subtle point. It would be quite nice if this condition could be removed, b ut it is unclear whether or not it is
possible.
