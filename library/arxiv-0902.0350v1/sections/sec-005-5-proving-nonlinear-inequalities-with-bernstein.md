---
doc_id: arxiv-0902.0350v1
doc_title: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE"
section_id: sec-005-5-proving-nonlinear-inequalities-with-bernstein
section_title: "Proving nonlinear inequalities with Bernstein bases"
section_number: 5
pages: 12-16
source_pdf: 0902.0350v1.pdf
source_sha256: 4591687132c93973
doc_brief: "A REVISION OF THE PROOFOF THE KEPLER CONJECTURE — The Kepler conjecture asserts that no packing of congruent balls in three-dimensional Euclidean space has density greater than that of the"
---
ThehardestcomputationalpartoftheoriginalproofoftheKeplerconjecture
is the verification of a list of about a thousand nonlinear inequalities. This
section presents a technique aimed at proving them, based on polynomial
approximation and Bernstein bases. We feel that this approach better fits
the requirements of formal proof, as outlined in Section 4.2. We hope to
refine the method to cover all Flyspeck inequalities.
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 13
Weexhibitthemethodonasingleinequality calc-586468779. Theoriginal
proof contains the following definitions [9]:
pt :=−π
3 + 4 arctan
√
2
5
δoct := π− 4 arctan
√
2
5
2
√
2
∆(y) := 1
2
⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐
0 1 1 1 1
1 0 y2
3 y2
2 y2
1
1 y2
3 0 y2
4 y2
5
1 y2
2 y2
4 0 y2
6
1 y2
1 y2
5 y2
6 0
⏐⏐⏐⏐⏐⏐⏐⏐⏐⏐
a0(y) :=y1y2y3 + 1
2(y2
1y2 +y1y2
2 +y2
1y3 +y2
2y3 +y1y2
3
+y2y2
3−y1y2
4−y2y2
5−y3y2
6)
a1(y) := a0(y1,y 5,y 6,y 4,y 2,y 3)
a2(y) := a0(y2,y 4,y 6,y 5,y 1,y 3)
a3(y) := a0(y4,y 5,y 3,y 1,y 2,y 6)
γ(y) :=−δoct
6
√
∆(y) + 2
3
3∑
i=0
arctan
√
∆(y)
ai(y) .
The statement of the inequality is:
(1) ∀y∈ [2, 2.51]6.γ (y)≤ pt.
Define the difference of two intervals by[a1,b 1]− [a2,b 2] = [a1−b2,b 1−a2].
Interval arithmetic is used to prove the inequalities in the original proof. It
suffers from thedependency problem: the minimum and maximum of the
formulax−x are overestimated because[a,b ]−[a,b ] = [a−b,b−a], although
x−x is clearly 0. Subdividing [a,b ] into [a, a+b
2 ] and [a+b
2 ,b ], and then re-
evaluating the formula yields an improved result. However, depending on
the problem, the number of required subdivisions can be very large. This is
why checking some inequalities takes a very long time.
5.1. F rom geometrical functions to polynomials. Fortunately, better
methods than interval arithmetic are available, if the function under consid-
eration is polynomial. A quick look atγ tells us that (1) is not polynomial,
since it has occurrences of√·, 1/·, and arctan. Can it nevertheless be re-
duced to a polynomial problem? Two strategies come to mind:
First, algebraic laws such as√a≤ b⇔ a≤ b2 (if b≥ 0) and a
b ≤ c⇔
a≤bc (if b >0) can often be used to eliminate occurrences of√· and 1/·.
The list of trigonometric identities is endless. For our example, Vega’s rule
14 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
arctana+arctanb = arctan a+b
1−ab seems useful. Unfortunately, this technique
quite often yields huge expressions that are difficult to deal with by virtue of
their sheer size. Also, an algebraic transformation to a polynomial problem
may simply be impossible (we suspect that this is the case for (1)).
A second technique is based on replacingγ with a polynomialg that domi-
nates it, but is still smaller thanpt. Clearly, if there exists ag such that
(2) ∀y∈ [2, 2.51]6.γ (y)≤g(y)
and
(3) ∀y∈ [2, 2.51]6.g (y)≤ pt,
then by transitivity (1) holds.
Such a polynomialg can be obtained by replacing√·, 1/· and arctan with
polynomial approximations. We only need to ensure that we use upper
approximations for positive occurrences and lower approximations for neg-
ative ones. Only occurrences whose arguments contain variables need to be
replaced, since e.g.
√
2 is a (constant) polynomial itself.
In the definition ofγ the function arctan occurs positively, so it is replaced
by an upper approximation arctan. The term
√
∆(y)
ai(y) is first unfolded to√
∆(y) · 1
ai(y). Both the square root and reciprocal occur positively again
here, so they can be replaced by upper approximationssqrt and rcp, re-
spectively. This yieldsarctan(sqrt(∆(y))· rcp(ai(y))) in all four summands.
There remains only√· occurring negatively after−δoct
6 , which is to be re-
placed by a lower approximationsqrt.
We choose the following approximations:
arctan(t) := arctan
√
2
5 + 25
27
(
t−
√
2
5
)
rcp(t) := 1
4− 37t
1600 + t2
1000− 13t3
640000 + t4
6400000
sqrt(t) := 8
√
2 + 3
64(π− 4 arctan
√
2
5 )
(t− 128)
sqrt(t) := 8
√
2 + 1
16
√
2(t− 128).
These approximations are valid on the domain (1). For example,
∀t∈ ∆([2, 2.51]6).
√
t≤ sqrt(t).
A REVISION OF THE PROOF OF THE KEPLER CONJECTURE 15
This can be established by elementary means, knowing that∆([2, 2.51]6)⊆
[128; 501]. The latter can be shown automatically by the method outlined
in the next subsection.
In summary, we arrive at the following definition ofg:
g(y) :=−δoct
6 sqrt(∆(y)) + 2
3
3∑
i=0
arctan(sqrt(∆(y))· rcp(ai(y))).
In form, it is almost identical to the definition ofγ. Our construction of
g therefore ensures (2). Moreover, the approximations were chosen (using
polynomial interpolation) in a way such that
(4) γ(2, 2, 2, 2, 2, 2) =g(2, 2, 2, 2, 2, 2) = pt.
This is important, because otherwise (3) cannot hold.
5.2. Bounding polynomials. In order to prove (1), it remains to be shown
that g(y)≤ pt. This can be done with the help of Bernstein polynomials.
We briefly outline the case of a single variablex here.
The ith Bernstein basis polynomial of orderk is defined as
Bk
i (x) :=
(k
i
)
xi(1−x)k−i.
For a polynomialp and a vectorb∈ Rk, if
p(x) =
k∑
i=0
bi· Bk
i (x),
then b is called theBernstein representationof p. In this case
∀x∈ [0; 1].p (x)≤ max
i
bi.
This property is tremendously useful: it gives us an upper bound on p,
namely the largest coefficient ofp’s Bernstein representation. By a change
of variable we can reduce any interval to[0, 1]. The generalization to the
multivariate case is straightforward [6], [49].
In order to bound a polynomial it thus suffices to convert it into Bernstein
representation. This can be done by a matrix multiplication (the Bernstein
basis of orderk forms a basis of the vector space of all polynomials of degree
up tok). For practical purposes it is however crucial to use a more efficient
algorithm (cf. [6], [49]).
Note that g contains irrational coefficients. This is a consequence of re-
quirement (4) and cannot be avoided. However, we were able to choose
16 HALES, HARRISON, MCLAUGHLIN, NIPKOW, OBUA, AND ZUMKELLER
the approximation polynomials in a way such that the transcendental parts
can be factored out (hence the occurrence ofπ− 4 arctan
√
2
5 in the defini-
tion of sqrt). As can be easily checked with symbolic algebra software, the
polynomial p(y) :=
√
2(g(y)− pt) has rational coefficients! It can thus be
converted to a Bernstein representation without rounding, using the algo-
rithm presented in [49]. With this method the only divisions are by powers
of 2, which can be efficiently represented using dyadic numbers.
The polynomialp consists of 12945 monomials and has total degree 18. A
prototype implementation in Haskell returns 0 as the maximum for p in
about half a minute. Thus
√
2(g(y)− pt)≤ 0 and g(y)≤ pt.
