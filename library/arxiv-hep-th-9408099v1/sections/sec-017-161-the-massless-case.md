---
doc_id: arxiv-hep-th-9408099v1
doc_title: "Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD"
section_id: sec-017-161-the-massless-case
section_title: "The massless case"
section_number: 16.1
pages: 57-70
source_pdf: 9408099v1.pdf
source_sha256: b534faddd2e3aa71
toc_source: inferred
doc_brief: "Seiberg–Witten, Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD (1994) — exact metric on the moduli space of quantum vacua and exact stable-state spectrum for SU(2) with…"
---
The ﬁrst step is to ﬁnd the right family of curves for the conformally invariant case,
that is when the bare masses are zero. In this case, the classical formulas
a =
 1
2
√
2u,
for Nf = 4
√
2u
for N = 4,
aD = τa
(16.2)
are exact. So we wish to ﬁnd a curve y2 = F(x, u, τ) such that the diﬀerential form
ω =
( √
2
8π
dx
y
for Nf = 4
√
2
4π
dx
y
for N = 4,
(16.3)
9 Holomorphy of F is needed in order for the coeﬃcient τ(u, mi, Λ) in front of Wα
2 in the low
energy theory to be holomorphic in the ﬁeld u and the parameters mi and Λ, as follows from [3].
Absence of singularities in F is less obvious.
56
has the periods ( ∂aD
∂u , ∂a
∂u), with (aD, a) given in (16.2).
Now, a genus one curve E and a diﬀerential form with periods a multiple of (τ, 1) can
be found as follows. Let E be the quotient of the complex z plane by the lattice generated
by π and πτ. Let ω0 = dz. Obviously, the periods of ω0 (integrated on contours that run
from 0 to π and from 0 to πτ, respectively) are π and πτ.
To ﬁnd an algebraic description of E (see section I.6 of [26] or section III.3 of [27]),
one introduces the Weierstrass P function, which obeys
P(z) = P(z + 1) = P(z + τ) = P(−z)
(16.4)
and has for its only singularity on E a double pole at the origin. If one sets x0 = P(z),
y0 = P′(z), then one ﬁnds
y0
2 = 4x0
3 −g2(τ)x0 −g3(τ).
(16.5)
Here g2 = 60π−4G4(τ), g3 = 140π−6G6(τ), and G4, G6 are the usual Eisenstein series
G4(τ) =
X
m,n∈Z̸=0
1
(mτ + n)4
G6(τ) =
X
m,n∈Z̸=0
1
(mτ + n)6
(16.6)
which deﬁne modular forms for SL(2, Z) of weight 4 and 6, respectively. Since the deﬁnition
of x0 and y0 was such that y0 = dx0/dz, one also can rewrite ω0 = dz as
ω0 = dx0
y0
.
(16.7)
Now, set x = x0u, y = 1
2y0u3/2, and
ω =



√
2/u
4π ω0 =
√
2
8π
dx
y
for Nf = 4
√
2/u
2π ω0 =
√
2
4π
dx
y
for N = 4.
(16.8)
The equation for the curve becomes
y2 = x3 −1
4g2(τ)xu2 −1
4g3(τ)u3.
(16.9)
57
This change of variables and in particular the normalization of u is motivated by the
following requirement. For weak coupling (τ →i∞) we should recover our curve y2 =
F0(x, u) = x2(x −u). It is easy to check from the asymptotic behavior g2 = 4
3 + O(q),
g3 =
8
27 + O(q) that after replacing x in (16.9) by x −u/3 we ﬁnd F0.
The periods of ω are now
√
2/u
4
(1, τ) for Nf = 4 and
√
2/u
2
(1, τ) for N = 4 and (since
in general the periods of ω are da/du and daD/du), one has
a =
 1
2
√
2u
for Nf = 4
√
2u
for N = 4
aD = τa,
(16.10)
as desired.
Thus, we have determined the appropriate curve for the massless theory. The coeﬃ-
cients are modular forms. This is not really a new test of S-duality; it is equivalent to the
fact that the metric of the classical theory is S-dual, which is one of the traditional pieces
of evidence for S-duality.
Spin Structures
The equation (16.9) for the curve can be factored
y2 = (x −e1(τ)u) (x −e2(τ)u) (x −e3(τ)u) ,
(16.11)
with the ei being the roots of the cubic polynomial 4x3−g2x−g3; they obey e1+e2+e3 = 0.
The classical formulas for the ei ([27], p. 69; note we set ω1 = π) are
e1 −e2 = θ3
4(0, τ)
e3 −e2 = θ1
4(0, τ)
e1 −e3 = θ2
4(0, τ),
(16.12)
where θi are the θ functions
θ1(0, τ) =
X
n∈Z
q
1
2 (n+1/2)2
θ2(0, τ) =
X
n∈Z
(−1)nq
1
2 n2
θ3(0, τ) =
X
n∈Z
q
1
2 n2
(16.13)
58
and hence
e1 = 2
3 + 16q + 16q2 + O(q3)
e2 = −1
3 −8q
1
2 −8q −32q
3
2 −8q2 + O(q
5
2 )
e3 = −1
3 + 8q
1
2 −8q + 32q
3
2 −8q2 + O(q
5
2 )
(16.14)
(note that unlike [27], we use q = e2πiτ). As g2 and g3 are modular forms of weight 4
and 6, the ei are of weight 2 (indeed, the theta functions are of weight 1/2). However,
the ei are not modular forms for SL(2, Z) because there is no modular-invariant way to
select a particular root of the cubic. Rather, the ei are modular forms of three diﬀerent
(conjugate) subgroups of SL(2, Z), each of index three.
Actually, there is a natural one-to-one association of the ei with the even spin struc-
tures on E. This can be seen as follows, beginning with the description of E as the quotient
of the z-plane by a lattice. The even spin structures of E are in natural correspondence
with the non-zero half-lattice points z = 1/2, τ/2, and (τ + 1)/2. Since P(z) = P(−z),
the derivative y = P′(z) vanishes at these points (indeed, up to a lattice translation those
points are invariant under z ↔−z). So the half-lattice points are zeroes of y. Looking at
the equation (16.11), we see therefore that the half-lattice points have x = eiu, for i = 1, 2,
or 3. So the even spin structures (or half-lattice points) correspond to the ei. (And each
ei is a modular form for the subgroup of SL(2, Z) that ﬁxes that spin structure – these
subgroups are conjugate to Γ0(2), the subgroup of SL(2, Z) obtained by requiring that the
upper right entry be even.)
For the N = 4 theory, the relation of the ei to the spin structures will have no
particular importance.
For Nf = 4, it is very important since, as we know already,
SL(2, Z) permutes the three eight-dimensional representations of Spin(8) in the same way
that it acts on the spin structures. So the three ei are permuted under Spin(8) triality.
16.2. The curve for N = 4
We recall that N = 4 supersymmetric Yang-Mills theory can be regarded as N =
2 super Yang-Mills theory with an additional matter ﬁeld that is a hypermultiplet in
the adjoint representation of the gauge group.
One can give a bare mass m to that
59
hypermultiplet, explicitly breaking N = 4 to N = 2. In this subsection we analyze the
resulting theory, for gauge group SU(2).
We ﬁrst consider the theory for weak coupling, that is for |q| ≪1, with m̸ = 0. There
is one singularity at u ≈1
4m2 where a component H of the elementary hypermultiplet is
massless. This gives a monodromy conjugate to T 2.10 In addition, at an energy of order
Λ0 ∼q1/4m, the theory evolves to a strongly coupled pure N = 2 gauge theory. As was
explained in [9], this theory has two singularities, associated with massless monopoles, with
monodromies conjugate to T 2. So altogether, we get three singularities, each conjugate to
T 2.11
Of course, the above analysis was valid for very weak coupling.
Could it be, for
instance, that what we described above as one singularity conjugate to T 2 is really a pair
of singularities conjugate to T, separated by an amount that vanishes for weak coupling?
SL(2, Z) group theory alone would permit this, but it is impossible because each of the
singularities arises when a single hypermultiplet becomes massless.
So we are looking for a family of curves
y2 = F(x, u)
(16.15)
(with cubic F) that – as u varies – has precisely three singularities each conjugate to T 2.
The restriction that this places on F was explained in our discussion of the Nf = 2 theory
in section 13.1. There is a singularity at u0 with monodromy T n for n > 1 (generically n
will be 2) if and only if for some x0,
F = ∂F
∂x = ∂F
∂u = 0
(16.16)
10 The elementary hypermultiplet for N = 4 has twice the electric charge of the hyperdoublets
that we have considered earlier. As a massless hyperdoublet gives monodromy T, and the one-loop
beta function which determines the monodromy is proportional to the square of the charge, the
massless H particle would give monodromy T 4 in the conventions of the Nf = 4 theory. With the
N = 4 conventions, the monodromy is T 2.
11 These three singularities are permuted under monodromies in q and m. This is the reason the
N = 4 conventions in which they are all conjugate to T 2 are preferable to the Nf̸ = 0 conventions
in which one is conjugate to T 4 and the others to T.
60
at x = x0, u = u0. Conditions (16.16) mean that the curve F(x, u) = 0 has a singularity
at (x, u) = (x0, u0).
Therefore, we are looking for a plane cubic curve F(x, u) = 0 with three distinct
singularities. The possible singularities of a plane cubic curve can be completely classiﬁed.
If F is an irreducible polynomial, there is at most one singularity (a node or cusp). If
F = F1F2, with F1 linear in x and u and F2 quadratic and irreducible, there are precisely
two singularities (perhaps at inﬁnity), namely the points where F1 = F2 = 0. The only
way to get three singularities is to have F = F1F2F3, where the three factors are linear;
the three singularities are the points Fi = Fj = 0 for any two distinct i and j.
To reproduce the known m = 0 limit of F, the Fi must be (up to a scalar multiple and
a permutation of i) Fi = x −eiu −fi where fi are functions of m and τ only and vanish
at m = 0. Moreover, by adding constants (that is, functions of m and τ only) to x and u,
one can eliminate two of the three fi. Since we did not assign any physical meaning to x
we can take the freedom to shift it. However, we want to preserve u = ⟨Trφ2⟩. Therefore,
we will denote the shifted u by eu and will later determine the relation between them. To
keep the symmetry under permuting the ei, we shift x and u such that fi = ei2f. Then
the equation of the mass-deformed N = 4 theory becomes
y2 = (x −e1eu −e1
2f)(x −e2eu −e2
2f)(x −e3eu −e3
2f).
(16.17)
We still need to ﬁnd f and to determine eu in terms of u.
The relation between u and eu is determined by examining the theory at weak coupling;
i.e. in the limit τ →i∞.
In this limit we should reproduce our weak coupling curve
y2 = F0 = x2(x −u). This motivates us to change variables to
eu = u −1
2e1f
x →x −1
2e1u + 1
2e2
1f
(16.18)
in (16.17). The family of curves becomes
y2 = (x −c1u) (x + c2u −c2(c1 + c2)f) (x −c2u + c2(c1 −c2)f)
(16.19)
with c1 = 3
2e1 and c2 = 1
2(e3 −e2). In this form it is easy to study the weak coupling
limit. For a smooth limit, f0 = f(τ = i∞) should be ﬁnite.
Using c1(τ = i∞) = 1
61
and c2(τ = i∞) = 0, the exact curve (16.19) becomes y2 = F0 = x2(x −u) as required.
Therefore, in the form (16.19) the family of curves is expressed in terms of u = ⟨Trφ2⟩.
We can now relate f0 = f(τ = i∞) to the mass m. We do that by examining the
singularities of (16.19). The roots of the equation are at x1 = c1u and x2,3 = ±c2(−u +
(c1 ± c2)f). A singularity occurs when xi = xj (for any two distinct i and j). This occurs
for
u1 = 3
2e1f = c1f
u2,3 = ±1
2(e3 −e2)f = ±c2f.
(16.20)
In the weak coupling limit c1 ≈1, c2 ≈8q
1
2 and hence u1 ≈f0 and u2,3 ≈±8q
1
2 f0. We
interpret the singularity at u1 as associated with a massless elementary ﬁeld. It should be at
a = m/
√
2. For weak coupling and in the N = 4 normalization this is at u ≈1
2a2 = m2/4.
Therefore,
f0 = f(τ = i∞) = m2/4.
(16.21)
The other two singularities at u2,3 ≈±8q
1
2 f0 are interpreted as the two singularities
of the low energy pure gauge N = 2 theory. More precisely, we can now take the scaling
limit q →0, f0 = m2/4 →∞holding Λ2
0 = 2q
1
2 m2 ﬁxed. In this limit (16.19) becomes
y2 = (x −u)(x2 −Λ4
0)
(16.22)
which is exactly the curve of the expected low energy pure gauge N = 2 theory in the
N = 4 conventions with scale Λ0.
We still need to determine f(τ).
To do that we will consider the residues of the
diﬀerential form λ. As explained in section 15 (see the footnote preceding equation (15.4)),
they are independent of u and hence, on dimensional grounds, are proportional to m. The
proportionality factor must be independent of τ, since the residues are related to the central
extension in the N = 2 algebra, which is independent of τ. We will explain the general
theory of these residues in section 17, but for the moment, we give instead the following
indirect argument which shows that f is independent of τ.
Let us assume ﬁrst that f is independent of τ. Then, equation (16.17) has simple
modular properties. y, x, eu, ei and f have modular weights 6, 4, 2, 2 and 0 respectively.
62
Therefore the diﬀerential form λ determined by dλ/du ∼dx/y transforms like a diﬀerential
form of weight zero under SL(2, Z) and the same is true of its residues. We also know that
the residues do not diverge for τ →i∞(since in (16.21) we showed that at any rate the
assumption that f is constant is valid for τ →i∞). A modular function of weight zero
that is bounded at inﬁnity is a constant, so if f is constant, the residues are constants.
It is now trivial to determine the residues for arbitrary f. Indeed, on dimensional
grounds, the residues are proportional to m, but m only enters through the function
f(τ, m) = m2f1(τ). Hence, the residues are a constant times m
p
f1(τ). The residues,
therefore, are independent of τ if and only if f1 is a constant. The constant is known since
we have determined the behavior for τ →i∞:
f = 1
4m2.
(16.23)
We conclude that the curve governing the low energy behavior of the mass-deformed
N = 4 theory is
y2 = (x −e1eu −1
4e1
2m2)(x −e2eu −1
4e2
2m2)(x −e3eu −1
4e3
2m2)
(16.24)
with
u = ⟨Trφ2⟩= eu + 1
8e1m2.
(16.25)
This formula is completely SL(2, Z) invariant; the coeﬃcients are modular forms.
Since the formula is not limited to weak coupling, this SL(2, Z) invariance is a genuine,
new, strong coupling test of SL(2, Z) invariance of the N = 4 theory. (Also, we learn that
the N = 2-invariant bare mass preserves SL(2, Z).)
SL(2, Z) invariance may, however, be lost in various weak coupling limits. For in-
stance, for the weak coupling limit τ →i∞the natural variable is u = ⟨Trφ2⟩which
diﬀers from eu by an additive renormalization (16.25). Unlike eu, u does not transform like
a modular form. Furthermore, in the τ →i∞limit we deﬁned a scaling theory by taking
also m →∞holding Λ4
0 = 4m4e2πiτ ﬁxed. By SL(2, Z) we can ﬁnd other weakly coupled
theories and scaling limits in which τ →p/q with p/q an arbitrary rational number. The
theory in these limits is strongly coupled in the original variables – the elementary gauge
63
ﬁelds – but weakly coupled in dual variables, φd, which were interpreted as monopoles in
the original theory. The natural parameter is then ud = ⟨Trφd2⟩. It is related to u or eu
by a shift and a modular transformation. In a suitable limit with τ →p/q, m →∞one
gets a pure gauge N = 2 theory. Thus, the pure N = 2 theory that arises in the scaling
limits does not have SL(2, Z) symmetry; SL(2, Z) merely permutes the possible equivalent
scaling limits.
16.3. The curve for Nf = 4
In this subsection we determine the curve for the Nf = 4 theory with arbitrary masses
(m1, m2, m3, m4). Among other things we will establish triality and SL(2, Z) invariance.
We start by considering the situation for mi = (m, m, 0, 0). As we discussed in section
10, in this case we expect to ﬁnd three singularities with two massless particles in each.
According to our general discussion in section 11, this means that the monodromy around
any of them is conjugate to T 2.
This is exactly the situation we encountered in our
discussion of the curve for N = 4, so with these masses the curve is
y2 =
Y
i
(x −eieu −e2
i f).
(16.26)
Here eu is related to u = ⟨Trφ2⟩by a constant shift as in (16.18) and f is proportional to
m2 and a priori may depend on τ.
As for N = 4, since the residues of λ should be τ independent, f must be a constant.
In order to determine the constant we again consider this curve in the weak coupling limit
τ →i∞. Again, we shift x and eu as in (16.18) and take the limit q →0, f →∞with
qf 2 held ﬁxed. The low energy theory is that of the massless Nf = 2 theory. Indeed,
we ﬁnd the curve (13.3) with eΛ22 = Λ22/8 = 8q
1
2 f. We also ﬁnd a singularity at u ≈f
which we interpret as associated with a massless elementary quark and hence it should be
at a = m/
√
2. In the Nf = 4 normalization this means that it is at u ≈2a2 = m2. Hence,
f = m2.
We now turn to the theory with arbitrary mi.
We ﬁrst impose the global SO(8)
symmetry and construct its low dimension invariants. There is a unique quadratic invariant
R = 1
2
X
i
m2
i .
(16.27)
64
There are three linearly independent quartic invariants. We take them to be R2 and
T1 = 1
12
X
i>j
m2
i m2
j −1
24
X
i
m4
i
T2 = −1
2
Y
i
mi −1
24
X
i>j
m2
i m2
j + 1
48
X
i
m4
i
T3 = 1
2
Y
i
mi −1
24
X
i>j
m2
i m2
j + 1
48
X
i
m4
i
(16.28)
with P Ti = 0. The reason for writing them like that is that the Ti are permuted under
the triality automorphism of SO(8) (which acts on the masses as in equations (10.3) and
(10.4)); we anticipate (but do not assume) that triality is a symmetry of the theory. There
are four six order SO(8) invariants. We take them to be R3, RTi and
N = 3
16
X
i>j>k
m2
i m2
jm2
k −1
96
X
i̸=j
m2
i m4
j + 1
96
X
i
m6
i .
(16.29)
R and N are invariant under triality.
In trying to generalize the curve for mi = (m, m, 0, 0) to arbitrary m we impose that:
1) The limit of the curve as any masses go to zero is smooth and hence it is polynomial in
mi.
2) U(1)R (or equivalently dimensional analysis) constrains the powers of mi.
This is
achieved by assigning charges 4, 4, 6, 2 to eu, x, y, mi.
3) For mi = (m, m, 0, 0) we recover the curve (16.26).
Since for mi = (m, m, 0, 0) we have R̸ = 0, Ti = N = 0, the most general form of the
curve consistent with these conditions is
y2 = W1W2W3 + x
X
i
Tifi + eu
X
i
Tigi + R
X
i
Tihi + pN
(16.30)
with
Wi = x −eieu −e2
i R
(16.31)
and fi, gi, hi and p are functions of τ to be determined.
For mi = (m, m, 0, 0) the curve has three singularities at eui = eim2 with two massless
particles in each. Therefore, the discriminant of the curve ∆has three double zeros at
65
these values of eu. We now consider the situation with mi = (m+µ, m−µ, 0, 0). According
to the discussion in section 10, for non-zero µ one of the three singularities should split and
the other two can move but remain double zeroes. Our weak coupling limit above identiﬁed
the singularity at eu1 with the one at which elementary quarks are massless. Therefore,
this one should split. We will now determine some of the coeﬃcients by demanding that
the zero at eu2 moves but remains a double zero.
Since the curve is holomorphic in µ2, so is the discriminant ∆. For |µ| ≪|m| its
double zero at eu2 starts moving at order µ2 to eu2 = e2m2 + µ2λ . For it to remain a
double zero, the order µ2 term in ∆(eu = e2m2 + µ2λ) should vanish. It is straightforward
to calculate this term. It is proportional to
−e1e3(f2 + f3 −2f1) + e2(g2 + g3 −2g1) + (h2 + h3 −2h1) + p.
(16.32)
We get one constraint by setting (16.32) to zero. Repeating this at eu3 we get a similar
equation with the subscripts 2 and 3 interchanged. Four more equations (related by other
permutations of the subscripts) are obtained by studying the cases mi = (m, m, µ, µ), and
mi = (m, m, µ, −µ). To organize the equations, we break the symmetry between eu2 and eu3
by deciding that in the ﬁrst of these cases the zero at eu2 splits and in the other the zero at
eu3 splits. The opposite choice leads to similar results with e2 and e3 interchanged. Using
these six equations we determine the ten unknowns fi, gi, hi, p in terms of four unknowns
F, G, H, A:
f1 = A(e2 −e3) + F
f2 = A(e3 −e1) + F
f3 = A(e1 −e2) + F
gi = −fiei + G
hi = −fie2
i + H
p = −(e1 −e2)(e2 −e3)(e3 −e1)A.
(16.33)
Since P Ti = 0, the values of F, G, H do not aﬀect the curve and hence can be set to zero.
In order to determine the unknown function A(τ) we consider the µ dependence more
fully. One approach would be to study higher order terms in the expansion around µ = 0,
66
and require that the double zeroes of ∆remain double zeroes. Instead, we examine the
curve for µ = m. For this value there are three massless quarks, and we expect the two
unsplit double zeros to merge, giving ∆a fourth order zero (which we have previously
encountered in the Nf = 3 theory). ∆has this fourth order zero if and only if
A = (e1 −e2)(e2 −e3)(e3 −e1)
(16.34)
leading to the curve
y2 = W1W2W3 + A (W1T1(e2 −e3) + W2T2(e3 −e1) + W3T3(e1 −e2)) −A2N
(16.35)
again with
Wi = x −eieu −e2
i R
A = (e1 −e2)(e2 −e3)(e3 −e1)
R = 1
2
X
i
m2
i
T1 = 1
12
X
i>j
m2
i m2
j −1
24
X
i
m4
i
T2 = −1
2
Y
i
mi −1
24
X
i>j
m2
i m2
j + 1
48
X
i
m4
i
T3 = 1
2
Y
i
mi −1
24
X
i>j
m2
i m2
j + 1
48
X
i
m4
i
N = 3
16
X
i>j>k
m2
i m2
jm2
k −1
96
X
i̸=j
m2
i m4
j + 1
96
X
i
m6
i .
(16.36)
We see that our ﬁnal answer is modular invariant. To be precise, full SL(2, Z) in-
variance, which permutes the ei, is a symmetry if combined with Spin(8) triality, which
permutes the Ti. This is a strong indication that the full theory is dual in the way described
in sections 6 and 10.
Weak coupling and scaling limits
As for N = 4, the theory has inﬁnitely many weakly coupled limits related by SL(2, Z).
The obvious one is τ →i∞; others are at τ = p/q with p/q rational. The weakly coupled
variables are diﬀerent in the various limits (the monopoles in one limit are the quarks in
67
another limit). Correspondingly, u = ⟨Trφ2⟩is diﬀerent in the diﬀerent scaling theories.
Let us focus on τ →i∞. We deﬁne u and shift x in a way similar to (16.18)
u = eu + 1
2e1R
x →x −1
2e1u + 1
2e2
1R.
(16.37)
Substituting (16.37) in (16.35) we ﬁnd
y2 = (x2 −c2
2u2)(x −c1u) −c2
2(x −c1u)2 X
i
m2
i −c2
2(c2
1 −c2
2)(x −c1u)
X
i>j
m2
i m2
j
+ 2c2(c2
1 −c2
2)(c1x −c2
2u)m1m2m3m4 −c2
2(c2
1 −c2
2)2 X
i>j>k
m2
i m2
jm2
k
(16.38)
where, as before, c1 = 3
2e1 and c2 = 1
2(e3 −e2).
We can now analyze the renormalization group ﬂow from Nf = 4 to Nf < 4. In
sections 12-14 we have already veriﬁed the ﬂows from Nf = 3 to Nf = 0, 1, 2, so it is
suﬃcient here to consider the ﬂow from Nf = 4 to the massive Nf = 3 theory. To do this,
we take the limit τ →i∞, m4 →∞, keeping ﬁxed m1, m2, m3 and
Λ3 = 64q1/2m4.
(16.39)
(Recall that q1/2 is the one instanton factor. The reason for the factor of 64 is that in
section 14 we took Λ22 = Λ3m3 but the above discussion of (16.26) implies that the ﬂow
from Nf = 4 to massless Nf = 2 gives Λ22 = 64q1/2m3m4. Thus the 64 in (16.39) is
needed to agree with our previous deﬁnition of Λ3.) Taking this limit using c1 ≈1 and
c2 ≈8q
1
2 leads to
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
(16.40)
which is the same as the massive Nf = 3 curve (14.5).
As for the N = 4 theory, scaling limits around other weakly coupled points lead to
equivalent theories in terms of dual degrees of freedom.
68
