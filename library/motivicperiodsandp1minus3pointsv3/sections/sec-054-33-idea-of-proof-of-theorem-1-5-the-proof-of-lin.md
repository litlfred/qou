---
doc_id: motivicperiodsandp1minus3pointsv3
doc_title: "Motivic periods and P1\{ 0, 1, ∞} Francis Brown∗"
section_id: sec-054-33-idea-of-proof-of-theorem-1-5-the-proof-of-lin
section_title: "Idea of proof of theorem 1 .5. The proof of linear independence is"
section_number: 3.3
pages: 16-16
source_pdf: MotivicPeriodsandP1minus3pointsv3.pdf
source_sha256: 7870572b8cc316d0
doc_brief: "Motivic periods and P1\{ 0, 1, ∞} Francis Brown∗ — This is a review of the theory of the motivic fundamental grou p of the projective line minus three points, and its relation to mult iple zeta"
---
by induction on the number of 3’s. In the case where there are n o 3’s, one can
easily show by adapting an argument due to Euler that
ζ(2, . . . ,2/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
n
) = π2n
(2n + 1)! .
The next interesting case is where there is one 3.
Theorem 3.5. (Zagier [38]). Let a, b ≥ 0. Then
ζ(2, . . .2/bracehtipupleft
/bracehtipdownright/bracehtipdownleft/bracehtipupright
a
, 3, 2, . . . ,2/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
b
) = 2
a+b+1∑
r=1
(−1)r(Ar
a,b − Br
a,b ) ζ(2r + 1) ζ( 2, . . . ,2/bracehtipupleft
/bracehtipdownright/bracehtipdownleft/bracehtipupright
a+b+1−r
)
where, for any a, b, r ∈ N, Ar
a,b =
( 2r
2a+2
)
, and Br
a,b =
(
1 − 2−2r)( 2r
2b+1
)
.
Zagier’s proof of this theorem involves an ingenious mixtur e of analytic tech-
niques. The next step in the proof of theorem 1 .5 is to lift Zagier’s theorem to
the level of motivic multiple zeta values by checking its com patibility with the
coaction (2 .18) and using theorem 2.7. Since then, the proof of theorem 3. 5 was
simpliﬁed by Li [31], and Terasoma [37] has veriﬁed that it ca n be deduced from
associator equations. Since the associator equations are k nown to hold between
motivic multiple zeta values, it follows that, in principle , this part of the proof can
now be deduced directly by elementary methods (i.e., withou t using theorem 2.7).
From the motivic version of theorem 3.5, one can compute the a ction of the
abelianization of U dR on the vector space built out of the elements ζm(n1, . . . , nr),
with ni = 2 , 3, graded by the number of 3’s. This action can be expressed by
certain matrices constructed out of the combinatorial form ula (2.18), whose entries
are linear combinations of the coeﬃcients Ar
a,b and Br
a,b of theorem 3.5. The key
point is that these matrices have non-zero determinant 2-ad ically, and are hence
invertible. At its heart, this uses the fact that the Br
a,b terms in theorem 3.5
dominate with respect to the 2-adic norm due to the factor 2 −2r.
