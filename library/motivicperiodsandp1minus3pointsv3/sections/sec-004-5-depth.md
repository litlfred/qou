---
doc_id: motivicperiodsandp1minus3pointsv3
doc_title: "Motivic periods and P^1 minus 3 points"
section_id: sec-004-5-depth
section_title: "Depth"
section_number: 5
pages: 18-19
source_pdf: MotivicPeriodsandP1minus3pointsv3.pdf
source_sha256: 7870572b8cc316d0
toc_source: inferred
doc_brief: "Motivic periods and P^1 minus 3 points — This is a review of the theory of the motivic fundamental group of the projective line minus three points, and its relation to multiple zeta values."
---
Thus an Euler sum of weight N and depth r can be expressed as a polynomial in
the above elements, of total weight N and total depth ≤r.
5. Depth
The results of the previous section for N = 2, 3, 4, 6, 8 crucially use the fact that
the depth ﬁltration is dual to the lower central series of the corresponding motivic
Galois group. A fundamental diﬀerence with the case N = 1 is that this fact is
false for P1\{0, 1, ∞}, due to a defect closely related to modular forms.
Recall that 0Π1 is a group for the Ihara action ◦.
Let Lie(0Π1) denote its
Lie algebra. Its bracket is denoted by { , }. Denote the images of the canonical
generators §3.1 by σ2n+1 ∈Lie(0Π1)(Q), for n ≥1. They are elements of the free
graded Lie algebra on two generators x0, x1, and we have, for example
σ3 = [x0, [x0, x1]] + [x1, [x1, x0]]
The higher σ2n+1 are of the form σ2n+1 = ad(x0)2n(x1) plus terms of degree ≥2
in x1, but are not known explicitly except for small n. By theorem 1.2, the σ2n+1
freely generate a graded Lie subalgebra of Lie(0Π1)(Q) which we denote by g. The
depth ﬁltration D on g is the decreasing ﬁltration given by the degree in the letter
x1. In 1993, Ihara and Takao observed that
{σ3, σ9} −3{σ5, σ7} = 691
144 e∆
(5.1)
where e∆is an element with integer coeﬃcients of depth ≥4 (degree ≥4 in x1),
and the coeﬃcient 691 on the right-hand side is the numerator of the Bernoulli
number B12. The element e∆is sparse:8 indeed, computations in the early days
gave the impression that the right-hand side is zero, although we now know that
the σ2n+1 generate a free Lie algebra.
Relations such as (5.1) show that the structure of g is related to arithmetic,
but more importantly show that the associated depth-graded Lie algebra grD g is
not free, since the left-hand side of (5.1) vanishes in gr2
D g. The depth ﬁltration
on g corresponds, dually, to the depth ﬁltration on motivic multiple zeta values,
and (5.1) implies that motivic multiple zeta values of depth ≤2 are insuﬃcient
to span the space of all (real geometric) motivic periods of MT (Z) in weight 12
8‘most’ of its coeﬃcients are zero, see [7], §8 for a closed formula for this element.
Motivic periods and P1\{0, 1, ∞}
19
(one needs to include elements of depth ≥4 such as ζm(2, 2, 2, 3, 3) in a basis). By
counting dimensions, this can be interpreted as a relation, viz:
28 ζm(3, 9) + 150 ζm(5, 7) + 168 ζm(7, 5) = 5197
691 ζm(12) .
(5.2)
The corresponding relation for multiple zeta values was found in [17] and gener-
alised to an inﬁnite family corresponding to cuspidal cohomology classes of SL2(Z).
In particular, the family of motivic multiple zeta values
ζm(2n1 + 1, . . . , 2nr + 1)ζm(2k)
cannot be a basis for H, although it has the right dimensions in each weight
(1.6). The Hoﬀman basis (1.7) gets around such pathologies, since, for example,
its elements in weight 12 have depths between four and six.
In 1997, Broadhurst and Kreimer made exhaustive numerical computations
on the depth ﬁltration of multiple zeta values, which led them to the following
conjecture, translated into the language of motivic multiple zeta values.
Conjecture 5.1. (Motivic version of the Broadhurst-Kreimer conjecture) Let D
denote the increasing ﬁltration on H induced by the depth. Then
X
N,d≥0
dimQ (grD
d HN) sdtN =
1 + E(t)s
1 −O(t)s + S(t)s2 −S(t)s4 ,
(5.3)
where E(t) =
t2
1−t2 , O(t) =
t3
1−t2 , and S(t) =
t12
(1−t4)(1−t6).
Note that equation (5.3) specializes to (1.6) on setting s equal to 1. The series
E(t) and O(t) are the generating series for the dimensions of the spaces of even and
odd single motivic zeta values. The interpretation of S(t) as the generating series
for cusp forms for SL2(Z) suggests a deeper connection with modular forms which
is well understood in depth two. By work of Zagier, and Goncharov, formula (5.3)
has been conﬁrmed in depths 2 and 3 (i.e., modulo s4).
An interpretation for conjecture (5.3) in terms of the structure of grDg, as well
as a complete conjectural description of generators and relations of grDg in terms
of modular forms for SL2(Z) was given in [7]. A deeper geometric understanding
of this conjecture would seem to require a framework which places multiple zeta
values and modular forms on an equal footing, which is the topic of §6.
