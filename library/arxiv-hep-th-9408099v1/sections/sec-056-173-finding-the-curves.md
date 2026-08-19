---
doc_id: arxiv-hep-th-9408099v1
doc_title: "E. Witten Institute for Advanced Study"
section_id: sec-056-173-finding-the-curves
section_title: "Finding the Curves"
section_number: 17.3
pages: 75-80
source_pdf: 9408099v1.pdf
source_sha256: b534faddd2e3aa71
doc_brief: "Seiberg–Witten, Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD (1994) — exact metric on the moduli space of quantum vacua and exact stable-state spectrum for SU(2) with…"
---
Now we would like to ﬁnd a suitable set of curves Ca on whichλ will have poles. In this
section we set v = 1 and work on the uncompactiﬁed manifold X given by y2 =F (x,u ).
To guess what the Ca may be, let us look back to some of the models treated earlier,
for instance the massive Nf = 2 theory. In equation (15.3), we found an explicit formula
for λ in this theory; it had poles at
x = ± 1
8 Λ 2
2
y = ±i
8 Λ 2
2(m1 ±m2).
(17.20)
74
This can be interpreted as follows. The equation y2 = F (x,u ) describes a double
cover of the x −u plane. The equation
x = ±Λ 2
2/8 (17 .21)
describes (for a given choice of the sign) a line in that plane . A generic line L in the x −u
plane would be described by
x =βu +θ, (17.22)
for some β, θ. The double cover y2 =F (x,u ), restricted to the line L, would be given by
an equation
y2 =g(u) (17 .23)
where generically g(u) is not the square of a polynomial. That being so, the double
cover of L is generically an irreducible complex curve, which is obvio usly invariant under
α :y → −y. That is not what we want, because ω is odd underα; we need cycles on X that
are odd. For the special case that the parameters in (17.22) a re as in (17.21), the double
cover (17.23) reduces to y2 = −(m1 ±m2)2Λ 24/64. Here the right hand side is the square
of a polynomial (in fact a constant), and so the double cover c onsists of two branches, with
y = i(m1 ±m2)Λ 22/8 or y = −i(m1 ±m2)Λ 22/8. If we call the two branches D+,± and
D−, ± (the second subscript denotes the sign for x in (17.21), and the ﬁrst is the sign of
y), then the diﬀerences C± =D+,± −D−,± are divisors that are odd under α. The explicit
determination of the residue of λ in section 15 amounted to expressing the cohomology
class [ω] as a linear combination of C+ and C−.
We can imitate this in the case at hand
y2 = (x −e1u)(x −e2u)(x −e3u) +F1(x,u ) (17 .24)
(where F1(x,u ) is of degree ≤ 2 in x and u). We introduce the line L of (17.22), and
consider again the double cover of L deduced from (17.24). This is described by an equation
y2 =g(u) where for generic u,g(u) is cubic. If g is cubic, it cannot be a square, so y2 =g(u)
describes an irreducible cover of L, necessarily invariant under y ↔ −y.
75
Therefore, we must adjust the coeﬃcients in (17.22) to kill t he cubic term in g(u).
This requires that we set β =ei for some i. Then g is quadratic in u and the equation for
the double cover is of the general form
y2 =Au2 +Bu +C. (17.25)
The polynomial on the right hand side of (17.25) is a square wh en and only when the
discriminant vanishes,
0 = ∆ = B2 − 4AC, (17.26)
When ∆ = 0, (17.25) can be written in the form y2 =A(u−t)2 for some t, and its solutions
consist of two branches y = ±
√
A(u −t). If we call these branches D+ and D−, we get a
divisor C =D+ −D− that is odd under α.
Now actually, A is linear in θ, B is quadratic, and C is cubic. So the discriminant is
quartic in θ and has four zeroes θa. For each we get a line La whose double cover has two
componentsD±,a. So we get four odd divisors Ca =D+,a −D−,a. As we discussed in the
last subsection, four is the dimension of the odd part of the c ohomology of X, so there are
as many Ca as we would need for a basis of that odd part. We will see that th ey are a
basis.
But actually, the above construction began by setting β = ei for some ﬁxed i. We
could have carried out the above steps for any i = 1, 2, or 3. So making the dependence on
i explicit, we have divisors D(i)±,a, and α-odd divisors C(i)a. Of course, Spin(8) triality
permutes the (i) superscript.
Intersection Pairings
We would like to prove that the C(i)a of ﬁxed i do furnish a basis of the odd part of
the cohomology. Since there are four of them, it suﬃces to pro ve that they are linearly
independent; for this purpose, it is enough to work on X (where the intersection pairings are
topological invariants) and prove that the matrix of inters ection pairings is non-degenerate.
So we have to calculate C(i)a ∩C(i)b. For a ⁄=b, this vanishes, for the following reason.
The divisors D(i)±,a are given by
x =eiu +θav
y = ±
√
A(u −tav)v.
(17.27)
76
(Since we are working on X, we have restored v. In doing this, we made the equations
homogeneous, remembering that x,u,v,y have degree 1, 1, 1, 2.) Any two of these curves
(for distinct a and b, but regardless of the independent choices of ± signs) meet precisely
at the Z2 orbifold point x −e1u =y =v = 0, so the pairings of these curves with distinct
a and b are
D(i)
±,a ∩D(i)
±,b = 1
2 (17.28)
where the two ± signs are chosen independently. (The 1 /2 comes because an intersection
at the orbifold point is counted with weight 1 /2.) Recalling that C(i)a =D(i)+,a −D(i)−,a
we get C(i)a ∩C(i)b = 0 for a ⁄= b. However, C(i)a ∩C(i)a = −4.16 Putting these results
together,
C(i)
a ∩C(i)
b = −4δab. (17.29)
This matrix is in particular nondegenerate, showing that fo r ﬁxed i, the C(i)a give a basis
of the relevant piece of the cohomology.
Triality
This result may seem esoteric, but by extending it a bit, we wi ll see Spin(8) triality
at work in the classical geometry. To this end, we want to calc ulate the intersections
C(i)a ∩C(j)b for i ⁄=j. We claim that
C(i)
a ∩C(j)
b = ±2, for i ⁄=j. (17.30)
Granted this, let us see how the statement is connected with S pin(8) triality.
Since the C(i)a of ﬁxed i are a basis of the odd part of the cohomology, the C(j)a can
be expanded as linear combinations of the C(i)a. In fact, we will expand everything in
terms of the C(1)a. Comparing (17.30) to (17.29), we see that the expansion coe ﬃcients
are all ±1/2. In the above we adopted no particular convention as to what was D(i)+,a
and what was D(i)−,a, so we have not ﬁxed the signs of the C(i)a. Picking an arbitrary
16 The value is obviously independent of i and a. That it is −4 requires a slightly more detailed
analysis that we omit. The value −4 in fact follows from our determination below that C (i)
a ∩
C (j)
b = ±2 for i ⁄= j.
77
sign for C(2)1, we can ﬁx the signs of all the C(1)a by requiring that the expansion of C(2)1
has all plus signs:
C(2)
1 = 1
2
(
C(1)
1 +C(1)
2 +C(1)
3 +C(1)
4
)
. (17.31)
Now, we consider C(2)a witha> 1. We can carry out a relabeling of the a index, since its
meaning has not been ﬁxed in any special way. The C(2)a, a> 1 are orthogonal to C(2)1,
and have expansion coeﬃcients ±1/2 in terms of the C(1)a. These conditions are enough
to ensure that, up to permutations on the a index and changes in sign of C(2)a,
C(2)
2 = 1
2
(
C(1)
1 +C(1)
2 −C(1)
3 −C(1)
4
)
C(2)
3 = 1
2
(
C(1)
1 −C(1)
2 +C(1)
3 −C(1)
4
)
C(2)
4 = 1
2
(
C(1)
1 −C(1)
2 −C(1)
3 +C(1)
4
)
.
(17.32)
It remains to consider the C(3)a. They must have expansion coeﬃcients of ±1/2 in
terms of either the C(1)a or the C(2)a. This ensures that, up to permutations and sign
changes of the C(3)a, they are given by
C(3)
1 = 1
2
(
C(1)
1 +C(1)
2 +C(1)
3 −C(1)
4
)
C(3)
2 = 1
2
(
C(1)
1 +C(1)
2 −C(1)
3 +C(1)
4
)
C(3)
3 = 1
2
(
C(1)
1 −C(1)
2 +C(1)
3 +C(1)
4
)
C(3)
4 = 1
2
(
−C(1)
1 +C(1)
2 +C(1)
3 +C(1)
4
)
.
(17.33)
Let us compare this to Spin(8) triality. The Nf = 4 theory has four masses
m1,m 2,m 3,m 4 which are the “eigenvalues” of a mass matrix that is in the adj oint repre-
sentation of Spin(8). So they transform under triality like the weights of Spin(8). Under
the exchange of the vector with the positive chirality spino r (leaving the negative chirality
spinor ﬁxed) the masses transform by a formula that was alrea dy presented in (10.4):
m′
1 = 1
2 (m1 +m2 +m3 +m4)
m′
2 = 1
2 (m1 +m2 −m3 −m4)
m′
3 = 1
2 (m1 −m2 +m3 −m4)
m′
4 = 1
2 (m1 −m2 −m3 +m4).
(17.34)
78
Under the exchange of the vector with the other spinor, the ma sses transform to
m′′
1 = 1
