---
doc_id: arxiv-1203.6551v1
doc_title: "On the number of hyperbolic 3-manifolds of a given volume"
section_id: sec-001-5-higher-order-terms-in-the-neumann-zagier-asymp
section_title: "Higher order terms in the Neumann-Zagier asymptotic formula"
section_number: 5
pages: 13-15
source_pdf: 1203.6551v1.pdf
source_sha256: a8e84f8ed63dbcca
doc_brief: "On the number of hyperbolic 3-manifolds of a given volume — The work of Jørgensen and Thurston shows that there is a ﬁnite number N (v) of orientable hyperbolic 3-manifolds with any given volum e v."
---
Let M be a cusped hyperbolic 3-manifold with horospherical torus cross s ection
T , and chose meridian and longitude generators for H1(T ) = Z2 as in section 2.
Let u, v denote the logarithms of the holonomies of the meridian and longitude
respectively, chosen so that u = v = 0 at the complete hyperbolic structure on M .
Then −v has a power series expansion
− v =
∞∑
n=1
cnun, (5.1)
where cn = 0 for all even n and c1 = −τ where τ is our cusp shape parameter. 2
Then Neumann and Zagier [ 38, equation (62), p328]) derive the following as-
ymptotic formula for the decrease in volume ∆ V during Dehn ﬁlling for ( p, q) Dehn
ﬁlling on one cusp T of the cusped hyperbolic 3-manifold M :
∆ V = |Im (c1)|π2
|z|2 − 2π4 Im
[ c3
z4
]
+ O
( 1
|z|6
)
, (5.2)
where z = p + qτ .
If we write z = reiθ , then this becomes
∆ V = |Im (τ )|π2
r2 − 2π4
r4 Im
[
c3e−4iθ ]
+ O
( 1
r6
)
. (5.3)
We now give some calculations for the manifolds studied in the previous sec-
tions.
Example 5.1. For m004, Neumann and Zagier ([ 38, p331]) show that c1 =
2√−3 = −τ and c3 = 2√−3
3 , and obtain the following asymptotic formula:
∆ Vm004(p, q) = 2
√
3π2
p2 + 12q2 − 4
√
3(p4 − 72p2q2 + 144q4)π4
3(p2 + 12q2)4 + O
( 1
(p2 + 12q2)3
)
.
(5.4)
Writing z = p + τ q = reiθ as above, this simpliﬁes to
∆ Vm004 = 2
√
3π2
r2 − 4π4 cos(4θ)√
3r4 + O
( 1
r6
)
. (5.5)
2In [ 38], a non-standard orientation convention for meridian and l ongitude was used; this
was pointed out in [ 37]. Replacing the basis in [ 38] by meridian, − (longitude) corresponding to
u, − v gives our version of the Neumann-Zagier formula.
14 HODGSON AND MASAI
Example 5.2. Let W L denote the Whitehead link complement as drawn in
Figure 2 (and in [ 27], [ 37]), with the standard topological choice of meridians
and longitudes. Then Hodgson-Meyerhoﬀ-Weeks [ 27, Figure 8 with p = q = 1]
show that the hyperbolic Dehn ﬁllings W L(1, 1)(m, l) and W L(−5, 1)(m, −l −m/2)
have equal volumes since they have homeomorphic 2-fold covers, w henever m, l are
relatively prime integers with m a multiple of 4.
Now W L(1, 1) and W L(−5, 1) are homeomorphic to m004 and m003 respec-
tively. In fact, using SnapPy or Snap, there are isometries taking W L(1, 1)(m, l)
to m004(m, l) and W L(−5, 1)(m, −l − m/2) to m003(m/2 − l, 2l). Hence we have
Vol(m004(m, l)) = Vol(m003(a, b)) (5.6)
for hyperbolic Dehn ﬁllings such that ( a, b) = ( m/2 − l, 2l) and ( m, l) = (2 a+ b, b/2)
for pairs of relatively prime integers with m a multiple of 4.
Since the volume is a real analytic function on hyperbolic Dehn surger y space
(using u as coordinate, as in [ 38]), it follows that (5.6) holds for all large real values
of ( p, q). Hence we can deduce the asymptotic formula for decrease in volu me for
m003:
∆ Vm003(a, b) = ∆ Vm004(2a + b, b/2)
=
√
3π2
2 (a2 + ab + b2) − π4 (
−18b2(2a + b)2 + (2a + b)4 + 9b4)
64
√
3 (a2 + ab + b2)4 + . . .
(5.7)
Introducing polar coordinates reiθ = a + bω, this simpliﬁes to
∆ Vm003(a, b) =
√
3π2
2r2 − π4
4
√
3
cos(4θ)
r4 + O
( 1
r6
)
. (5.8)
Example 5.3. For the Whitehead link sister m125, Aaber and Dunﬁeld [ 1]
study the Neumann-Zagier asymptotic expansion of volume for Deh n ﬁllings. If u, v
denote the logarithms of holonomies of the meridian and longitude for the geometric
basis for cusp 0 of m125, then they show [ 1, p1019] that
− v = iu + −3 + i
48 u3 + . . . (5.9)
so c1 = −τ = i and c3 = −3+i
48 in our notation. This gives the following asymptotic
formula for decrease in volume for surgeries on cusp 0:
∆ Vm125(p, q) = π2
|z|2 − 2π4 Im
[ −3 + i
48z4
]
+ O
( 1
|z|6
)
, (5.10)
where z = p + qτ = p − qi.
More explicitly:
∆ Vm125(p, q) = π2
p2 + q2 − π4(p4 − 12p3q − 6p2q2 + 12pq3 + q4)
24 (p2 + q2)4 + O
( 1
(p2 + q2)3
)
.
(5.11)
Example 5.4. For the Whitehead link complement W L (as drawn in Figure
2) we can compute the asymptotic expansion for ∆ V using the work of Neumann-
Reid [ 37]. Let u, v denote the logarithms of holonomies of the standard meridian
and longitude for the link complement. Then [ 37] shows that
u = log x + log(x + 1) − log(x − 1) and v = 4 log x − 2πi,
ON THE NUMBER OF HYPERBOLIC 3-MANIFOLDS OF A GIVEN VOLUME 15
where x ∈ C is a suitable simplex parameter. From these equations we obtain
eu = x(x + 1)
(x − 1) where x = ie−v/ 4.
This gives a quadratic equation for x with the relevant solution given by
x = 1
2
( √
−6eu + e2u + 1 + eu − 1
)
= ie−v/ 4,
and so
−v = −4 log
( −i
2
( √
−6eu + e2u + 1 + eu − 1
) )
= (−2 + 2i)u + iu3
6 + O(|u|5). (5.12)
Hence c1 = −τ = (−2 + 2i) and c3 = i
6 in our previous notation.
This gives the following asymptotic formula for decrease in volume for Dehn
ﬁlling on one cusp of W L:
∆ VW L(p, q) = 2π2
|z|2 − 2π4 Im
[ i
6z4
]
+ O
( 1
|z|6
)
, (5.13)
where z = p + qτ = p + q(2 − 2i). Hence
∆ VW L(p, q) = 2π2
p2 + 4pq + 8q2 − π4 (
p2 − 8q2) (
p2 + 8pq + 8q2)
3 (p2 + 4pq + 8q2)4 + . . . . (5.14)
We can convert from the standard peripheral curves for W L to the geometric
peripheral curves on m129 using: W L(p, q) = m129(a, b) where a = p + 2q, b = −q
or p = a + 2b, q = −b. Then the new cusp shape parameter for m129 is τ ′ = −2i
and
∆ Vm129(a, b) = ∆ VW L(a + 2b, −b)
= 2π2
a2 + 4b2 − π4 (
a4 − 24a2b2 + 16b4)
3 (a2 + 4b2)4 + . . . (5.15)
