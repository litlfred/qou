---
doc_id: motivicperiodsandp1minus3pointsv3
doc_title: "Motivic periods and P^1 minus 3 points"
section_id: sec-008-131-motivic-mzvs-let-t-mt-z-the-betti-and-de-rha
section_title: "Motivic MZV’s. Let T = MT (Z). The Betti and de Rham realisations"
section_number: 1.3.1
pages: 4-5
source_pdf: MotivicPeriodsandP1minus3pointsv3.pdf
source_sha256: 7870572b8cc316d0
doc_brief: "Motivic periods and P^1 minus 3 points — This is a review of the theory of the motivic fundamental grou p of the projective line minus three points, and its relation to mult iple zeta values."
---
provide functors ωB, ωdR, and integration deﬁnes a canonical element comp B,dR ∈
IsomT (ωdR, ωB)(C). Since the de Rham functor ωdR is graded by the weight, the
ring of motivic periods P m
MT (Z) is also graded. 1 It contains graded subrings
P m, +
MT (Z), R ⊂ P m, +
MT (Z) ⊂ P m
MT (Z)
of geometric periods (periods of motives whose weights are ≥ 0), denoted by a
superscript +, and those which are also invariant under comp lex conjugation (de-
noted by a subscript R, since their periods lie in R as opposed to C).
Next, one has to show that the integral (1 .2) deﬁnes a period of an object M
in MT (Z) (this can be done in several ways: [19], [36], [14])). This d eﬁnes a
matrix coeﬃcient [ M, w, σ]m, where w encodes the integrand, and σ the domain of
integration, which we call a motivic multiple zeta value ( §2.2)
ζm(n1, . . . , nr) ∈ P m
MT (Z) .
Its weight is n1 + . . . + nr and its period is (1 .2). Most (but not all) of the known
algebraic relations between multiple zeta values are also k nown to hold for their
motivic versions. Motivic multiple zeta values generate a g raded subalgebra
H ⊂ P m, +
MT (Z), R . (1.5)
The description §1.1, (1) of U dR enables one to compute the dimensions of the
motivic periods of MT (Z) in each degree by a simple counting argument:
if dN := dim Q
(
P m, +
MT (Z), R
)
N then
∑
N ≥0
dN tN = 1
1 − t2 − t3 . (1.6)
This implies a theorem proved independently by Goncharov an d Terasoma [14],[36].
1In the ﬁeld of multiple zeta values, the ‘weight’ refers to on e half of the Hodge-theoretic
weight, so that Lm has degree 1 instead of 2. I shall adopt this terminology from here on.
Motivic periods and P1\{ 0, 1, ∞} 5
Theorem 1.4. The Q-vector space spanned by multiple zeta values of weight N
has dimension at most dN , where the integers dN are deﬁned in (1.6).
So far, this does not use the action of the motivic Galois grou p, only a bound
on the size of the motivic periods of MT (Z). The role of P1\{0, 1, ∞} is that the
automorphism group of its fundamental groupoid yields a for mula for the coaction
(1.4) on the motivic multiple zeta values ( §2.5). The main theorem uses this
coaction in an essential way, and is inspired by a conjecture of M. Hoﬀman [25].
Theorem 1.5. The following set of motivic MZV’s are linearly independent :
{ζm(n1, . . . , nr) for ni = {2, 3}} . (1.7)
From the enumeration (1 .6) of the dimensions, we deduce that H = P m, +
MT (Z), R,
and that (1 .7) is a basis for H. From this, one immediately sees that U dR acts
faithfully on H, and theorem 1 .2 follows easily. As a bonus we obtain that U dR
has canonical generators σ2n+1 (deﬁned in §3.1), and, furthermore, by applying
the period map we obtain the
Corollary 1.6. Every multiple zeta value of weight N is a Q-linear combination
of ζ(n1, . . . , nr), where ni ∈ {2, 3} and n1 + . . . + nr = N .
The point of motivic periods is that they give a mechanism for obtaining infor-
mation on the action of GdR, via the period map, from arithmetic relations between
real numbers. For theorem 1 .5, the required arithmetic information comes from a
formula for ζ(2, . . . ,2, 3, 2, . . . ,2) proved by Zagier [38] using analytic techniques.
