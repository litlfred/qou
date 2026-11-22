---
doc_id: arxiv-hep-th-9408099v1
doc_title: "Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD"
section_id: sec-014-113-general-structure-of-the-curve
section_title: "General structure of the curve"
section_number: 11.3
pages: 43-52
source_pdf: 9408099v1.pdf
source_sha256: b534faddd2e3aa71
toc_source: inferred
doc_brief: "Seiberg–Witten, Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD (1994) — exact metric on the moduli space of quantum vacua and exact stable-state spectrum for SU(2) with…"
---
In trying to generalize (11.7) to Nf > 0, it is useful to ﬁrst extract some properties of
the Nf = 0 curve that we will try to generalize:
(1) The family is of the form y2 = F(x, u, Λ), where F is a polynomial in x, u, and Λ that
is at most cubic in x and u.
(2) The part of F(x, u, Λ) that is cubic in x and u is F0 = x2(x −u).
(3) If one assigns the U(1)R charges 4 to u and x, 2 to Λ, and 6 to y, then the family is
U(1)R invariant; and in particular F has charge 12.
(4) F can be written F = F0 + Λ4F1 where F1 = 1
4x.
For the time being we will simply assume that property (1) remains valid in the
presence of matter hypermultiplets. (This property can be at least partly deduced from
our later consideration of the N = 4 and Nf = 4 theories.)
As for property (2), it is easy to see that it must be valid for Nf ≤3. The cubic part of
F (after absorbing a possible multiplicative constant in y) would in general take the form
(x −e1u)(x −e2u)(x −e3u) for some ei. For large u the branch points are at e1u, e2u, e3u,
and ∞. After dividing x by u, the branch points for u →∞are at the ei and ∞, so they
are distinct if the ei are distinct. Thus, if the ei are distinct, the family of curves has no
singularity for u = ∞. This is actually the correct behavior for the conformally invariant
theories, but for Nf ≤3 it would prevent one from getting for u →∞the logarithm
associated with asymptotic freedom as in (4.3). On the other hand, one does not want all
three ei equal, for then u could be eliminated from the cubic term by changing variables
from x to x′ = x −e1u; it would then again be impossible to get a logarithm. So we
can assume for asymptotically free theories that e1 = e2̸ = e3. By a redeﬁnition of x by
x →ax + bu and a rescaling of y, one can assume that e1 = 0, e3 = 1, and hence that the
cubic part of F is x2(x −u).
As far as the third property is concerned, one expects that U(1)R can be treated as a
symmetry if Λ is assigned the correct charge. 4 and 2 are indeed the correct U(1)R charges
of u and Λ. For u, this is just a statement about the classical theory. To understand the
charge of Λ, one notes that the one loop beta function and U(1)R anomaly are such that
42
a one-instanton amplitude is proportional to Λ4 and violates U(1)R by eight units. The
physical meaning of x and y is somewhat mysterious, so we will have to accept their U(1)R
charges of 4 and 6 as an empirical fact.
It is now easy to interpret property (4). Given the anomalous U(1)R conservation
and the fact that F is polynomial, it is clear that in the weak coupling limit of the theory,
obtained by taking Λ →0, F reduces to the cubic term F0. Moreover, since it is only
instantons that violate the U(1)R charge if we do not assign a U(1)R charge to Λ, and a one-
instanton amplitude has the quantum numbers of Λ4, the expansion of F in powers of Λ4
can be interpreted as an expansion in the instanton number. The fact that F = F0 +Λ4F1
means that for Nf = 0, F has only the classical contribution F0 and the one instanton
contribution Λ4F1.
12. The curve for Nf = 1
12.1. Massless Nf = 1
Our next goal is to adapt the principles just described to determine the families of
curves that control the low energy behavior of the N = 2 theories with matter. In doing
so, we let ΛNf be the renormalization scale parameter of the theory with Nf ﬂavors. We
consider ﬁrst the case of Nf = 1 with zero bare mass.
For Nf = 1, the one-instanton amplitude is proportional to Λ13, and an amplitude
with r instantons is proportional to Λ13r. However, for Nf > 0 and one or more massless
hypermultiplets, the equation deﬁning the curve can only receive contributions from terms
with an even number of instantons. This is because an amplitude with an odd number
of instantons violates the internal “parity” symmetry of equation (3.2), while the curve is
invariant under this symmetry. For Nf = 1, given that Λ1 has U(1)R charge 2 and F has
charge 12, the only possible term in F that depends on Λ1 is a two-instanton term, which
must be a constant times Λ16. Therefore, the curve of the massless Nf = 1 theory must
be
y2 = x2(x −u) + tΛ1
6.
(12.1)
43
The constant t can be absorbed in a redeﬁnition of Λ1
eΛ1
6 = tΛ1
6.
(12.2)
Below we will determine t for a particular deﬁnition of Λ1.
Let us now see that this curve has the right properties.
First of all, we have the
expected Z3 symmetry of the u plane, as (12.1) is invariant under multiplying x and u by
a cube root of unity, with y invariant. (From the formulas below for a and aD, it will be
clear that a and aD transform correctly under the symmetry.) To ﬁnd the singularities,
we compute the discriminant of the polynomial on the right hand side of (12.1), with the
result
∆= eΛ6
1(4u3 −27eΛ6
1).
(12.3)
Consequently, on the ﬁnite u plane there are three singular points at u = e
2πin
3 3eΛ2
1/4
1
3 ,
(n = 1, 2, 3), permuted by the Z3 symmetry, and with monodromy conjugate to T. To
ﬁnd the behavior for large u, we note that for large u the branch points are approximately
at x = u, ∞, and ±eΛ13/√u. Upon absorbing a factor of u in x and a factor of u
3
2 in y,
we get a stable situation with branch points at 1, ∞and ±eΛ13/u3/2. The discriminant is
hence of order u−3 for u →∞, so the monodromy is conjugate to PT −3 (the factor of P
arises from the factor of u
3
2 in y).
12.2. Massive Nf = 1
Now we consider the Nf = 1 theory with a non-zero bare mass m for the hypermul-
tiplet. m-dependent terms must vanish for Λ1 →0, since classically the mass m of the
hypermultiplet does not aﬀect the low energy couplings of the vector multiplet. m is odd
under the internal “parity,” so with m̸ = 0, one can have contributions of odd instanton
number to the equation deﬁning the curve; they simply have to be odd in m. Since m has
U(1)R charge 2, the most general possibility is
y2 = x2(x −u) + tΛ1
6 + mΛ1
3(ax + bu) + cm3Λ1
3
(12.4)
with constants a, b, and c that must be determined.
44
To do so we note that when m is large the quark can be integrated out. The low
energy theory is the pure gauge N = 2 theory; its scale Λ0 is determined by the one loop
beta function to be
Λ4
0 = mΛ3
1.
(12.5)
Λ0 for the pure gauge theory was deﬁned such that the singularities are at u = ±Λ2
0.
Then we can use equation (12.5) as a deﬁnition of Λ1. Other deﬁnitions corresponding to
diﬀerent subtraction schemes diﬀer by a multiplicative constant in (12.5).
An obvious constraint on (12.4) is that in the limit of large m we recover the curve
of the Nf = 0 theory.
More precisely, we should consider the scaling limit m →∞,
Λ1 →0 with Λ4
0 = mΛ3
1 held ﬁxed. Comparison of (12.4) and (11.7) shows that a = 1
4 and
b = c = 0. Therefore, the curve is
y2 = x2(x −u) + 1
4mΛ1
3x + tΛ1
6.
(12.6)
By computing the discriminant, one can verify that in the double scaling limit, one of the
singularities moves to inﬁnity; in fact the singularity in question is at
u ≈−m2
64t,
x ≈−8tΛ13
m
.
(12.7)
(It is not necessary here to actually consider the discriminant of the cubic polynomial on the
right of (12.6); the term cubic in x is unimportant near the singularity, which is controlled
by the discriminant and zeroes of the quadratic polynomial −ux2 + 1
4mΛ13x + tΛ16.)
The constant t cannot be determined by the singularities and monodromies of the
curve, since they are invariant under scaling of m or Λ1. To ﬁx t, we note that for large
m, there should be a singularity at u ≈m2 where one of the elementary quarks becomes
massless. Comparing to (12.7), we see that t = −1/64, so the curve is
y2 = x2(x −u) + 1
4mΛ1
3x −1
64Λ1
6.
(12.8)
Of course, we see here the merits of the change of normalization that led us from
(11.1) to (11.7). If one wishes to study the Nf = 0 theory as a low energy limit of a
massive theory with Nf > 0, which has ﬁelds of one-half the W boson charge, it will
45
appear naturally in the form of (11.7). Similarly (as we will see later), renormalization
group ﬂow from the mass-deformed N = 4 theory, which does not have isodoublets, will
lead naturally to (11.1).
Note that given the Nf = 1 curve, the Nf = 0 curve can be immediately determined,
but not the other way around. Of course, that is a manifestation of the usual irreversibility
of the renormalization group.
13. The curve for Nf = 2
13.1. Massless Nf = 2
First we consider the Nf = 2 theory without masses. The instanton amplitude is now
Λ22, and the internal parity implies that without bare masses, only amplitudes with an
even number of instantons contribute. Given that Λ2 has U(1)R charge 2 and the equation
for the curve has charge 12, the curve can receive contributions only from instanton number
2 and is of the form
y2 = x2(x −u) + axΛ2
4 + buΛ2
4.
(13.1)
It remains to determine a and b.
Let us denote the polynomial on the right hand side of (13.1) as F. The discriminant
of F (with respect to x) is a polynomial in u that is quartic (or lower order, for some
special values of a and b). Generically, this polynomial has four simple zeroes, so that the
family of curves (13.1) has four singularities in the u plane, with monodromies conjugate
to T. We want to ﬁnd the values of a and b for which there are instead two singularities
with monodromies conjugate to T 2. This can be done by studying the discriminant or
more directly as follows.
As we have noted before, near a point u = u0 at which F has a double root at x = x0,
F looks like F = const · ((x −x0)2 −(u −u0)n), for some n; the monodromy is then
conjugate to T n. The condition that n > 1 is that
F = ∂F
∂x = ∂F
∂u = 0
(13.2)
46
at x = x0, u = u0. (This is equivalent to saying that the two dimensional variety deﬁned by
the equation y2 = F(x, u) in three variables x, u, and y has a singularity at x = x0, u = u0,
y = 0.) One immediately sees that, with F as above, the equations (13.2) require a = −b.
As in our discussion of Nf = 1, these considerations cannot determine the normalization
of Λ2 and we conclude that the family of curves is
y2 = (x2 −eΛ2
4)(x −u)
(13.3)
for some eΛ2. Below we will express it in terms of a convenient deﬁnition of Λ2. This,
indeed, is a family that we have seen before – it is essentially our old friend (11.1) of
the Nf = 0 theory in the “old” normalization. Note in particular that the expected Z2
symmetry of the u plane has appeared.
13.2. Massive Nf = 2
Now we allow arbitrary bare masses m1, m2 for the quarks. The masses transform
like (3, 1) ⊕(1, 3) of the global SO(4) ∼= SU(2) × SU(2). The polynomial deﬁning the
curve must be SO(4) invariant. Also, terms that are odd (or even) under the internal
parity which changes the sign of one of the m’s must come from an odd (or even) number
of instantons. The most general possible structure of the curve is then
y2 = (x2 −tΛ2
4)(x −u) + m1m2Λ2
2(ax + bu) + c(m1
2 + m2
2)Λ2
4
(13.4)
with constants a, b, and c that must be determined. We deﬁne Λ2 such that when m2
is large, the scale of the low energy Nf = 1 theory is Λ3
1 = m2Λ2
2. Then, we should also
determine the constant t relating Λ2 to eΛ2.
We proceed as in our discussion of the massive Nf = 1 theory. The scaling limit
m2 →∞, Λ2 →0 with Λ3
1 = m2Λ2
2 held ﬁxed determines a = 1
4, b = 0 and c = −1/64.
The curve is then
y2 = (x2 −tΛ2
4)(x −u) + 1
4m1m2Λ2
2x −1
64(m1
2 + m2
2)Λ2
4.
(13.5)
As for Nf = 1, the constant t is determined by imposing that when any mass, say m1, is
large there is a singularity at u = m2
1. Substituting m2 = 0 and u = m2
1 in the discriminant
47
of (13.5), the leading term at large m1 is 4m18Λ24(t−1/64); hence t = 1/64 and the curve
is
y2 = (x2 −1
64Λ2
4)(x −u) + 1
4m1m2Λ2
2x −1
64(m1
2 + m2
2)Λ2
4.
(13.6)
As a check, we can compute the discriminant for m1 = m2 = m and ﬁnd
∆= Λ24
16 (u + mΛ2 + 1
8Λ2
2)(u −mΛ2 + 1
8Λ2
2)(u −m2 −1
8Λ2
2)2.
(13.7)
This shows that when the two quarks are degenerate there is a singularity at u = m2+Λ2
2/8
with two massless particles (double zero of the discriminant) which for large m can be
identiﬁed with that of the massless quarks. The reason for the two-fold degeneracy there is
that the massless particles at the singularity are in a doublet of the global SU(2) symmetry
of the massive theory. The other two singularities - which coincide for m = 0 - come from
simple zeroes of the discriminant corresponding to vacua with one massless multiplet each.
14. The curve for Nf = 3
14.1. Massless Nf = 3
Now we will determine the curve for the Nf = 3 theory with zero bare masses. We do
this using the expected singularity structure: there should be a singularity in the u plane
with monodromy conjugate to T 4 and one with monodromy conjugate to T.
Since the Nf = 3 theory has no symmetry in the u plane, we may as well add a
constant to u and assume that the singularity with monodromy T 4 is at u = 0. The curve
is then given by y2 = F(x, u), where F is cubic in x and u, and at u = 0, F(x, 0) = 0 has
a double root; by adding a constant to x, we may as well assume that the double root is
at x = 0. In fact, F must have the form
F = aΛ3
2x2 + bu2x + cux2 + x3.
(14.1)
This polynomial has two roots within O(u2) of the origin, so the discriminant is propor-
tional to u4 for small u and the monodromy around u = 0 is conjugate to T 4. The structure
in (14.1) was determined as follows. Terms un with n ≤3 or xum with m < 2 would cause
48
the zero of the discriminant at u = 0 to be of order lower than 4, so those terms have been
suppressed. The coeﬃcient of x3 was set to one to agree with the classical limit.
To determine the parameters, we require that b̸ = 0, since otherwise the curve is
singular for all u, not the situation we want. We also ask that (14.1) has the right classical
limit; this is equivalent to saying that the cubic part of F, which is x3 + cux2 + bu2x, is
equal to (x −e1u)2(x −e2u) with e1̸ = e2. Since b̸ = 0, the only way to achieve this is to
have x2 + cux + bu2 be a perfect square, say (x + αu)2. After rescaling x and y so that
α = 1, and renaming x + u as x, we ﬁnally determine our curve:
y2 = x2(x −u) + tΛ3
2(x −u)2.
(14.2)
t is a constant which can be absorbed in a redeﬁnition of Λ3.
Notice that for Nf = 3, a one-instanton amplitude is proportional to Λ3, so the
term in (14.2) proportional to Λ32 can be interpreted as a two-instanton eﬀect. Thus,
the contributions from an odd number of instantons vanish, as expected from the internal
“parity.”
The other singularity of this family, with monodromy conjugate to T, is at u =
−tΛ32/4.
This singularity is presumably associated with vanishing mass of a state of
(nm, ne) = (2, 1).
14.2. Massive Nf = 3
We now determine the curve for the massive Nf = 3 theory. We repeat the steps we
used for Nf = 1, 2. The masses m1, m2, m3 are in the 15 of the global SO(6) symmetry.
The equation for the curve must be compatible with SO(6) invariance and the anomalous
U(1)R, and must reduce to the previous result when the masses vanish. Also, it should be
invariant under the parity transformation which changes the sign of one of the masses and
the sign of the instanton factor Λ3. And it should ﬂow to the massive Nf = 2 curve in the
scaling limit of m3 →∞with Λ2
2 = m3Λ3 ﬁxed. The most general polynomial equation
49
with these properties is
y2 =x2(x −u) + tΛ3
2(x −u)2 −1
64(m1
2 + m2
2 + m3
2)Λ3
2(x −u)
+ 1
4m1m2m3Λ3x −1
64(m1
2m2
2 + m2
2m3
2 + m1
2m3
2)Λ3
2
+ a(m1
2 + m2
2 + m3
2)Λ3
4 + bm1m2m3Λ3
3.
(14.3)
Here we encounter a new element that did not arise for Nf = 1, 2. The two constants a
and b are not determined by the previous considerations nor are they a choice of scale (like
t). To determine them we examine the small m theory.
For m1 = m2 = m3 = 0 there are two singularities. One of them is at u = 0 with four
massless particles and the other at u = −tΛ32/4 where there is a single massless particle.
Correspondingly, the discriminant of the massless curve has a single zero at u = −tΛ32/4
and a fourth order zero at u = 0. When some of the masses are turned on the zero of the
discriminant at u = −tΛ32/4 moves and the multiple zero at u = 0 splits. We will now
examine this splitting and determine the constants a and b. It is enough to consider the
case with m1 = m2 = m3 = m. From our analysis of the monopole structure, we know
that the zero at u = 0 should split to a single zero and a triple zero. The discriminant is
of course holomorphic in all variables, and since the single and triple zero near u = 0 are
unique, their positions also vary holomorphically. (By contrast, if a fourth order zero splits
to two double zeroes, the formula for the locations of the two double roots can contain a
square root branch cut.) Therefore, for small m the discriminant of the curve with three
equal masses should have a zero at u ∼m. Expanding the discriminant of (14.3) in m
with u = λm we ﬁnd that actually
∆= −4m2t2Λ3
8 
3Λ3
2at + m(tΛb + 18λa) + O(m2)

.
(14.4)
To get a zero of ∆for m →0 with λ of order 1, the coeﬃcient of m2 has to vanish. Since
t̸ = 0, this forces a = 0. Then, vanishing of the O(m3) term forces b = 0.
To determine t we impose that for large m there is a singularity at u = m2. The
leading contribution to the discriminant at large m with u = m2 is
1
16m10Λ32(1 +64t) and
therefore t = −1/64.
50
We conclude that the curve is
y2 =x2(x −u) −1
64Λ3
2(x −u)2 −1
64(m1
2 + m2
2 + m3
2)Λ3
2(x −u)
+ 1
4m1m2m3Λ3x −1
64(m1
2m2
2 + m2
2m3
2 + m1
2m3
2)Λ3
2.
(14.5)
As a test we evaluate the discriminant for three equal masses m and ﬁnd that it has a
triple zero at u = m2+mΛ3/8. The three particles at the singularity are in the fundamental
representation of the global SU(3) symmetry. As m varies from zero to inﬁnity they move
from the origin where they are magnetic monopoles to inﬁnity where they are interpreted
as the elementary quarks.
