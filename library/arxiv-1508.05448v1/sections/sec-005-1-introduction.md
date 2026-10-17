---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-005-1-introduction
section_title: "Introduction"
section_number: 1
pages: 10-34
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
toc_source: outline
---
Introduction
The idea of concentration of measure was ﬁrst introduced by Milman in the asymp-
totic theory of Banach spaces [Milman and Schechtman, 1986]. The phenomenon
occurs geometrically only in high dimensions, or probabilistically for a large number
of random variables with suﬃcient independence between them. For an overview of
the history and some standard results, see [Ledoux, 2005].
A illustrative geometric example of concentration of measure occurs for the stan-
dard n-sphere Sn in Rn+1. If we let µn denote the uniform measure on Sn, then for
large enough n, µn is highly concentrated around the equator.
To see exactly what we mean by ”highly concentrated”, let us consider any mea-
surable set A on Sn such that µn(A) ≥1/2. Then, if we let d(x, A) be the geodesic
distance between x ∈Sn and A, we deﬁne the expanded set
At = {x ∈Sn ; d(x, A) < r}
At contains all points of A in addition to any points on Sn with a geodesic distance
less than r from A. The precise inequality that can be obtained says that
µn(Ar) ≥1 −e−(n−1)r2/2
2
In other words ”almost” all points of the sphere are within distance of
1
√n from our
set A. Obviously as n →∞, this quantity because inﬁnitesimal. This example is due
to Gromov, and more discussion can be found in [Gromov, 1980].
Gromov’s work on concentration on the sphere was inspired by L´evy’s work [L´evy
and Pellegrino, 1951] on concentration of functions. Suppose we have a function F,
which is continuous on Sn with a modulus of continuity given by ωF(t) = sup{|F(x)−
F(y)| : d(x, y) ≤t}. Let mF be a median for F, which by deﬁnition means that
µn(F ≥mF) ≥1/2 and µn(F ≤m) ≥1/2. Then we have
µn({|F −mF| ≥ωF(t)}) ≤2e−(n−1)t2
While these geometric examples give a nice introduction to the phenomenon, in
this work we will mainly be interested in concentration of measure in a probabilis-
tic setting. Let us give a simple example that will give some intuition about how
concentration of measure comes up in probability.
Suppose we have independent
random variables X1, X2, . . . , Xn. Suppose that they take the values 1 and −1, each
with probability 1/2. For each n ≥1, let Sn = Pn
i=1 Xi. Since E(Xi) < ∞(in fact
E(Xi) = 0), the strong law of large numbers tells us that Sn/n converges almost
surely to E(Xi) as n →∞. Remember that this means that
P

lim
n→∞
Sn
n = E(Xi)

= 1
Moreover, by the central limit theorem, we know that
 Sn
√n

d−→N(0, σ2)
where σ2 is the variance of each Xi, which in this case is 1. This shows us that the
ﬂuctuations of Sn are of order n. However, notice that |Sn| can take values as large
as n. If we measure Sn using this scale, then Sn
n is essentially zero. The actual bound
3
looks like
P
|Sn|
n
≥r

≤2e−nr2/2
for r > 0. See [Talagrand, 1996] for a proof. As Talagrand points out, concentration
of measure appears in a probabilistic setting by showing that one random variable
that depends in a smooth enough way on many other independent random variables
is close to constant, provided that it does not depend too much on any one of the
independent random variables. As we will see later in this work, it turns out that this
idea still holds true if we have a random variable that depends on a large number of
”almost” independent random variables. We will later see an instance of a random
variable that depends on many weakly correlated random variables. It requires a
little more work to prove concentration of measure, but often, it is still possible.
This work is divided into chapters. Chapter 2 introduces Talagrand’s Gaussian
concentration of measure inequality, Talagrand’s isoperimetric inequality, Ledoux’s
concentration of measure on Markov chains, and the Euler-Maclaurin formula. A
statement and proof of each theorem (with the exception of the Euler-Maclaurin for-
mula) is also given, to make this work as self-contained as possible. In later chapters,
we will see new applications of each of these results. Chapter 3 introduces several
new results using Ledoux’s concentration of measure inequality on reversible Markov
chains. We are able to generalize a method ﬁrst used by Chatterjee and Ledoux [Chat-
terjee and Ledoux, 2009] to prove concentration of measure for two diﬀerent random
operator compressions. We also show how to use this method to obtain concentration
of measure bounds for the length of the longest increasing subsequence of a random
walk evolving under the asymmetric exclusion process. To give more meaning to our
ﬂuctuation bounds, we also derive a lower bound for the length of this longest increas-
ing subsequence. It turns out that we can use Talagrand’s isoperimetric inequality
to do this, even though our random variables have weak correlations. In Chapter
4, we discuss a method for calculating the mixed matrix moments in the Ginibre
random matrix ensemble using techniques from spin glasses. In addition, we use the
4
mixed matrix moments to compute asymptotics of the overlap functions (introduced
by Chalker and Mehlig [Chalker and Mehlig, 1998]) for eigenvectors corresponding
to eigenvalues near the edge of the unit circle.
We propose an adiabatic method
for computing explicit formulas for the eigenvector overlap functions. In Chapter 5,
we use the Euler-Maclaurin formula to prove a q-deformed Stirling’s formula. We
demonstrate a use of the q-Stirling’s formula to obtain asymptotics for point counts
in a four square problem. We also discuss techniques and algorithms to simulate a
Mallows random permutation.
5
2
Concentration of Measure
Results and other Necessary
Background
2.1
Talagrand’s Gaussian Concentration of Mea-
sure Inequality
Michel Talagrand has made numerous contributions to the theory of concentration
of measure. The ﬁrst concentration of measure result that we will present applies to
Lipschitz functions of Gaussian random variables, so we will refer to it henceforth
as Talagrand’s Gaussian concentration of measure inequality, to distinguish it from
other results of Talagrand that we will use. Before stating the theorem, recall that a
Lipschitz function F on RM, with Lipschitz constant A, satisﬁes
|F(x) −F(y)| ≤A∥x −y∥
where ∥x −y∥is the Eucliean distance between x and y. The following theorem is
due to Talagrand [Talagrand, 2003]
Theorem 2.1.1. Consider a Lipschitz function F on RM, with Lipschitz constant
A. Let x1, . . . , xM denote independent standard Gaussian random variables, and let
6
x = (x1, . . . , xM). Then for each t > 0, we have
P(|F(x) −EF(x)| ≥t) ≤2 exp

−t2
4A2

(2.1)
Proof. For this proof, we will assume that F is not only Lipschitz, but also twice
diﬀerentiable. This is the case in most applications of this theorem, and if it is not
the case, we can regularize F by convoluting with a smooth function to solve the
problem. We begin with a parameter s and consider a function G on R2M deﬁned as
G(z1, . . . , z2M) = exp (s(F(z1, . . . zM) −F(zM+1, . . . , z2M)))
Let u1, . . . u2M be 2M independent standard Gaussian random variables. Let v1, . . . v2M
also be 2M random variables (independent of the u1, . . . , uM) such that ﬁrst M
(v1, . . . , vM) are independent standard Gaussians and such that the second M vari-
ables (vM+1, . . . , v2M) are copies of the ﬁrst M v′s, in order. (i.e. vi = vi+M if i ≤M.)
Notice that due to the independence of the u’s and the ﬁrst M v’s, we have
Euiuj −Evivj = 0
except when j = i + M or i = j + M, in which case we have
Euiuj −Evivj = 0 −1 = −1
We consider a function f(t) = (f1, . . . f2M)(t) given by
fi(t) =
√
tui +
√
1 −tvi
Note that f(0) = v and that f(1) = u. Also, consider
φ(t) = EG(f(t))
7
so that
φ′(t) = E
2M
X
i=1
d
dtfi(t)∂G
∂xi
(f(t))
To simplify φ′(t), recall the Gaussian integration by parts formula. For Gaussian
random variables y, y1, . . . , yn, and a function F (of moderate growth at inﬁnity), we
have
EyF(y1, . . . , yn) =
n
X
i=1
E(yyi)E∂F
∂xi
(y1, . . . , yn)
(See [Talagrand, 2003] Appendix 6 for a proof).
Using the fact that
d
dtfi =
1
2
√
tui −
1
2√1 −tvi
and applying Gaussian integration by parts, gives
φ′(t) =
2M
X
i,j=1
E
 1
2
√
tui −
1
2√1 −tvi

(
√
tuj +
√
1 −tvj)E ∂2G
∂zi∂zj
f(t)
Using the independence of the u’s and the v’s, we have that
E
 1
2
√
tui −
1
2√1 −tvi

(
√
tuj +
√
1 −tvj) = 1
2(Euiuj −Evivj)
which we have already determined is equal to 0 unless j = i + M or i = j + M (in
which case it is −1), so we have
φ′(t) = −E
X
i=1M
∂2G
∂zi∂zi+M
(u(t))
Computing the second derivative gives
∂2G
∂zi∂zi+M
(z) = −s2 ∂F
∂xi
(z1, . . . , zM)∂F
∂xi
(zM+1, . . . , z2M)G(z)
8
Since F is Lipschitz, we know that for all x ∈RM,
M
X
i=1
∂F
∂xi
x
2
≤A2
so we can use the Cauchy-Schwarz inequality to get
φ′(t) ≤s2A2φ(t)
Notice that φ(0) = 1 (since at t = 0 the u’s disappear and the second half of the v’s
cancel the ﬁrst half). Hence we have
φ′(t)/φ(t) ≤s2A2
so
log(φ(t)) ≤s2A2t + C
or
φ(t) ≤es2A2t
and
φ(t) ≤exp(s2A2)
Recalling that fi(1) = ui, this tells us that
E exp(s(F(u1, . . . , uM) −F(uM+1, . . . , u2M)) ≤es2A2
By independence of the u’s, we have that
E exp(s(F(u1, . . . , uM) −F(uM+1, . . . , u2M)))
= E exp(s(F(u1, . . . , uM)E exp(−sF(uM+1, . . . , u2M))
(2.2)
9
By Jensen’s inequality, we know that
E exp(−sF(uM+1, . . . , u2M)) ≥exp(−sEF(uM+1, . . . , u2M))
for s > 0.
Putting this all together, we have
E exp s(F(x) −EF(x)) ≤es2A2
where x is a length M vector of independent standard Gaussian random variables.
By Markov’s inequality
P(F(x) −EF(x) ≥t) = P(s(F(z) −E(F(z)) ≥st) ≤e−stEes(F−EF)
Letting s = t/2A2, we have
P(F(z) −EF(z) ≥t) ≤exp

−t2
4A2

We can then apply the same inequality to −F and we will have our result.
It is worth noting that the method used to prove this result is quite important. Ta-
lagrand [Talagrand, 2003] refers to this method of proof as the ”smart path method”.
This method can be applied to a variety of problems. Notice that we found a ”path”
(namely our function f), which took us between the situation that we wanted to study
and a simpler situation. Beyond choosing an appropriate path, the only real work left
to do was to get bounds on the derivatives along the path. Talagrand points out that
although this method leads to an elegant proof, the choice of path is highly important
and nontrivial. Often the choice is not obvious and can be found only after a careful
study of the structure of the problem.
10
2.2
Talagrand’s Isoperimetric Inequality
The concentration of measure inequality presented in this section is also due to Tala-
grand. In [Talagrand, 1995], a theory of isoperimetric inequaliies on product spaces
is developed. The theorem presented here is just one of the many isoperimetric in-
equalities proved and applied in that work. Once the necessary notions of distance
are deﬁned and the theorem proved, the applications of the theorem are vast and
obtained quickly. Before stating the theorem, we need to set up our product space
and deﬁne a special notion of distance on the space.
We will begin with a probability space which we will denote by (Ω, F, P). To give
an idea of what we mean when we talk about a product probability space, we will
give an example of the product of two probability spaces.
Suppose that we have two probability spaces given by (Ω1, F1, P1) and (Ω2, F2, P2).
We want to form a product space which is the ”product” of these two probability
spaces. For ease of notation, we will usually just denote the product space by Ω1×Ω2,
leaving the sigma algebras and the measures implicit. Our new measure space is just
the cross product Ω1 × Ω2. The new sigma algebra is given by the tensor product
F1⊗F2. We deﬁne the product measure P1×P2 by (P1×P2)(F1×F2) = P1(F1)P2(F2)
for all F1 ∈F1 and F2 ∈F2. We can then deﬁne a product of n probability spaces
by extending this notion.
Given our probability space (Ω, F, P), we will be considering the product space
Ωn.
Given A ⊆Ωn, Talagrand’s isoperimetric inequality gives us bounds on the
measure of the set of points that are within a speciﬁed distance of this set A. Before
we can state the inequality, we need to develop a notion of distance.
For x ∈Ωn and A ⊂Ωn, we deﬁne Talagrand’s convex distance to be
dT(x, A) = min


t : ∀{αi}, ∃y ∈A such that
n
X
i=1
αi1{xi̸ = yi} ≤t
 n
X
i=1
α2
i
! 1
2



11
The similarity between dT(x, A) and Hamming’s distance
dH(x, A) = inf
y∈A
n
X
i=1
1(xi̸ = yi)
should be noted. Notice that if all αi = n−1/2, then Talagrand’s convex distance
is always at least as large as n−1/2 times the Hamming distance. One of the main
reasons that we use dT(x, A) instead of dH(x, A), is that dT(x, A) not only allows
us to weight the summands diﬀerently, it allows us to choose weights that explicitly
depend on the values of the xi. This ﬂexibility allows the inequality to be applied to
a much wider range of problems.
A second (and equivalent) way of deﬁning Talagrand’s convex distance is by
dT(x, A) = sup
(
zα : zα = inf
y∈A
n
X
i=1
αi(x)1(xi̸ = yi) and
N
X
i=1
α2
i (x) ≤1
)
(2.3)
To gain a bit of understanding about the convex distance, let us look at a simple
example. Suppose that we are working in one dimension. Let x ∈R and let our set
A just be {y}, the set containing only the point y ∈R. Then
dT(x, {y}) = min{t ≥0 : ∀α ∈R>0,
α1(x̸ = y) ≤t∥α∥}
=



1
if y̸ = x
0
if y = x
Given A ⊂ωn, we deﬁne
At = {x ∈Ωn : dT(x, A) ≤t}
In other words, At is the set of all points that are within a distance t of A. The
following inequality can be found in [Talagrand, 1995] and tells us that for a set A of
”reasonable size”, P(At) is close to 1.
12
Theorem 2.2.1. For every A ⊂Ωn, we have
Z
Ωn exp
1
4d2
T(x, A)

dP(x) ≤
1
P(A)
(2.4)
and consequently
P(dT(x, A) > t) ≤e−t2/4
P(A)
(2.5)
and
P(At) ≥1 −e−t2/4
P(A)
(2.6)
It should be noted that the proof given here more closely follows the proof as
given in [Steele, 1997] as opposed to [Talagrand, 1995]. The method is basically the
same as Talagrand’s original proof although some components are presently slightly
diﬀerently and appear in a diﬀerent order.
Before we can begin the proof of the theorem, we need a deeper understanding
and a diﬀerent characterization of the convex distance. We will begin by deﬁning a
set UA(x). Elements of this set will be elements of Rn containing only 0’s and 1’s. We
will begin with the set U ′
A(x), which is the set of all vectors uy = (1(x1̸ = y1), 1(x2̸ =
y2), . . . , 1(xn̸ = yn)) for y ∈A. We then let UA(x) be the set which includes all of
these vectors in addition to all vectors we can obtain from U ′
A(x) by switching some
of the 0’s to 1’s. In other words, u ∈UA(x) if and only if u−uy ≥0 for all y ∈A. We
then deﬁne the set VA(x) to be the convex hull of UA(x). By convex hull, we mean
the set of all convex combinations of vectors in UA(x). We then have the following
dual characterization of dT(x, A).
Proposition 2.2.2.
dT(x, A) = min{∥v∥2 : v ∈VA(x)}
Proof. Begin with
min
y∈A
n
X
i=1
αi1(xi̸ = yi)
13
Using the deﬁnition of UA(x), this is
min
u∈UA(x)
n
X
i=1
αiui
Using the fact that the minimum of a linear functional on a convex set is equal to
the minimum over the set of extreme points, we have that the above is equal to
min
v∈VA(x)
n
X
i=1
αivi
Next, we apply the Cauchy-Schwarz inequality to get
≤
min
v∈VA(x)
( n
X
i=1
α2
i
)1/2 ( n
X
i=1
vi
)1/2
=
( n
X
i=1
α2
i
)
min{∥v∥2 : v ∈VA(x)}
Recalling Talagrand’s convex distance,
dT(x, A) = min


t : ∀{αi}, ∃y ∈A such that
n
X
i=1
αi1{xi̸ = yi} ≤t
 n
X
i=1
α2
i
! 1
2



we immediately have
dT(x, A) ≤min{∥v∥2 : v ∈VA(x)}
by our last inequality.
Now we need to prove the reverse inequality. By the linear functional characteri-
zation of the Euclidean norm, there is an α with ∥α∥2 = 1 such that for all v ∈VA(x),
we have
n
X
i=1
αivi ≥min{∥v∥2 : v ∈VA(x)}
14
By deﬁnition of VA(x), this implies that for all y ∈A, we have
n
X
i=1
αi1(xi̸ = yi) ≥min{∥v∥2 : v ∈VA(x)}
Using equation (2.2), this immediately applies the reverse inequality
Now that this result is established, we can prove Talagrand’s isoperimetric in-
equality.
Proof. (of Theorem 2.2.1) To prove the theorem, we will use induction on the dimen-
sion of the product space. To prove the base case, we will start with n = 1. In this
case we have
dT(x, A) = min{∥v∥2 : v ∈VA(x)}
which is



1
: x /∈A
0
: x ∈A
Plugging this into the integral from Talagrand’s theorem, we have
Z
Ω
exp
1
4d2
T(x, A)

dP(x) = e0
Z
A
dP(x) + e1/4
Z
Ac dP(x)
= P(A) + e1/4(1 −P(A))
If we can show that this quantity is ≤1/P(A), the base case will be proved. This
will be relatively easy to show, using a little bit of calculus. For ease of notation, let
p = P(A). Then (multiplying on both sides of the equation by p), we need to prove
that
p2 + e1/4p(1 −p) ≤1
To prove this, we will take derivatives to ﬁnd the p that maximizes p2+e1/4p(1−p)−1.
15
Taking the derivative and solving for p gives p ≈2.26. Hence, on the interval [0, 1],
p2 + e1/4p(1 −p) obtains its maximum at 1. At p = 1, the inequality is satisﬁed, so
the base case is proved.
Now we will proceed with the inductive step. Assume that for any A ⊆Ωn, we
have
Z
Ωn exp
1
4dT(x, A)2

dP(x) ≤
1
P(A)
where P(A) now represents our product measure on Ωn.
We need to check and
make sure that the inequality holds for dimension n + 1. We start with an arbitrary
A ⊆Ωn+1. We will begin by writing Ωn+1 as Ωn × Ω. Let x ∈Ωn and ω ∈Ω. Then
(x, ω) ∈Ωn+1. We will consider two diﬀerent sets. Following Steele, we will deﬁne
the following as the ω section of A, given by
A(ω) = {x : (x, ω) ∈A} ⊂Ωn
and the projection of A, given by
B =
[
ω∈Ω
A(ω) = {x : ∃(x, ω) ∈A} ⊂Ωn
To prove the theorem, we will show that dT(x, A) (in n+1 dimensions) can be bounded
in terms of the convex distances for the ω sections and the projections. To do this,
we prove the following lemma.
Lemma 2.2.3. For all 0 ≤t ≤1 and A(ω) and B as deﬁned above, we have
d2
T((x, ω), A) ≤t(d2
T(x, A(ω))) + (1 −t)(dT(x, B))2 + (1 −t)2
(2.7)
Using the alternative characterization of dT from Proposition 2.2.2, we can ﬁnd
vectors v1 ∈VA(ω)(x) and v2 ∈VB(x) such that dT(x, A(ω) = ∥v1∥and dT(x, B) =
∥v2∥.
16
First we note that (v1, 0) ∈VA(x, ω). To see this, use the fact that since v1 ∈
VA(ω)(x), we know that v(i)
1
(the ith component of v1) is equal to 1(xi̸ = yi) for
some y ∈A(ω) for all i.
Then, if y ∈A(ω), we know that (y, ω) ∈A.
Hence,
vn+1
1
= 1(ω̸ = ω) = 0.
Next, we note that (v2, 1) ∈VA(x, ω). This follows immediately from the fact that
starting from a vector in U ′
A(x, ω), we can always change 0’s to 1’s and remain in
UA(x, ω), and hence in VA(x, ω).
Since VA(x, Ω) is convex,
t(v1, 0) + (1 −t)(v2, 1) = (tv1 + (1 −t)v2, 1 −t)
is also in VA(x, Ω). Notice that by our alternative characterization of dT, ∥(tv1 + (1 −
t)v2, 1 −t)∥is an upper bound on dT((x, ω), A).
∥(tv1 + (1 −t)v2, 1 −t)∥2 =
n
X
i=1
(tv(i)
1 + (1 −t)v(i)
2 )2 + (1 −t)2
≤t∥v1∥2
2 + (1 −t)∥v2∥2
2 + (1 −t)2
Using dT(x, A(ω)) = ∥v1∥and dT(x, B) = ∥v2∥, we have proved the lemma.
Keeping ω ﬁxed, deﬁne In(ω) to be the n-fold integral given by
In(ω) =
Z
Ωn exp
1
4d2
T((x, ω), A)

dP(x)
Using Lemma 2.2.3, we have that
In(ω) ≤
Z
Ωn exp
1
4(td2
T(x, A) + (1 −t)d2
T(x, B) + (1 −t)2)

dP(x)
= exp
(1 −t)2
4
 Z
Ωn exp
 t
4d2
T(x, A)

exp
1 −t
4
d2
T(x, B)

dP(x)
(2.8)
17
Recall that Holder’s inequality says that
Z
|fg| dµ ≤
Z
|f|p dµ
1/p Z
|g|p dµ
1/q
Applying this to (2.7) with p = 1/t and q = 1/(1 −t) gives
In(ω) ≤exp
(1 −t)2
4
 Z
Ωn exp
1
4d2
T(x, A)

dP(x)
t Z
Ωk
exp
1
4d2
T(x, B)

dP(x)
1−t
Now, by the induction hypothesis, we have
In(ω) ≤exp
(1 −t)2
4
 
1
P(A(ω))
t 
1
P(B)
1−t
=
1
P(B)
P(A(ω))
P(B)
−t
exp
(1 −t)2
4

(2.9)
Since A(ω) ⊂A(B), we know that P(A(ω)) ≤P(B). In order to complete the proof
of the theorem, we need the following lemma.
Lemma 2.2.4. For all 0 ≤r ≤1, we have
inf
0≤t≤1 r−t exp
1
4(1 −t)2

≤2 −r
The proof of this lemma is essentially a calculus exercise, but we will give an
outline. Taking the derivative of r−t exp
  1
4(1 −t)2
with respect to t gives
−exp
1
4(1 −t)2

r−t(ln(r) + 1/2(1 −t)
Optimizing in t gives t = 1+2 ln(r), which can be shown to be a minimum. Plugging
back into r−t exp
  1
4(1 −t)2
gives
r−1+2 ln(r) exp(1/4(1 −1 −ln(r))2)
18
After some simpliﬁcation, we get that the above
= r2 ln(r)+1
To show that r2 ln(r)+1 ≤2 −r, we just need to show that r + r2 ln(r)+1 ≤2. Using
calculus, one can show that r + r2 ln(r)+1 is decreasing on 0 ≤r ≤1 and therefore, the
inequality is true. This concludes the proof of the lemma.
Applying this lemma to equation (2.8) gives
In(ω) ≤
1
P(B)

2 −P(A(ω))
P(B)

This can now be integrated with respect to ω, which gives
Z
Ωn+1 exp
1
4dT((x, ω), A)

dP(x)dP(ω) ≤
1
P(B)

2 −P(A)
P(B)

=
1
P(A)
P(A)
P(B)

2 −P(A)
P(B)

Notice that if we can prove that
P(A)
P(B)

2 −P(A)
P(B)

≤1
then our proof will be complete. Letting x = P(A)
P(B), we want to determine for which
x, x(2 −x) ≤1, or equivalently, for which x, x2 −2x + 1 ≥0. Since this factors as
(x −1)2, this inequality is true for all x, which completes the proof.
As previously mentioned, although the setup and proof of this theorem took a fair
amount of work, most applications of the theorem are elegant and quick. See [Steele,
1997] for a discussion and explanation of common applications. In addition, we will
see an application in a later chapter.
19
2.3
Ledoux’s Concentration of Measure on Reversible
Markov Chains
A concentration of measure result proved by Ledoux [Ledoux, 2005] turns out to
be a key foundational piece for some of the results of chapter 3. Before stating the
result, we provide a few deﬁnitions. Following the notation in [Ledoux, 2005], we
will let (Π, µ) denote a Markov chain on a ﬁnite or countable set X.
A Markov
chain is a stochastic process which moves between elements of X according to the
following rules: if the chain is at a given x ∈X, the next position in the chain is
chosen according to a ﬁxed probability distribution Π(x, ·). In other words, given a
starting position x ∈X, the probability to move from x to y is Π(x, y). We call X
the state space and Π the transition matrix. Markov chains satisfy a ”memoryless”
property. This property (called the Markov property) is stated in mathematical terms
as follows.
For notational purposes, let S = (Π, µ), so that St is the current state of the chain
at some discrete time t > 0. Then for all x, y ∈X and events Kt−1 = ∩t−1
i=0{Si = xi}
satisfying P(Kt−1 ∩{St = x}) > 0, we have
P(St+1 = y | Kt−1 ∩{St = x}) = P(St+1 = y | St = x) = Π(x, y)
A simple explanation of this property is that the future depends only on the present,
not on the past. For a complete discussion of Markov chains and more properties, see
[Levin et al., 2009].
Furthermore, for this application, we require that the Markov chain be irreducible.
A Markov chain is irreducible if for any x, y ∈X, there exists an integer t > 0, such
that Πt(x, y) > 0. By the notation Πt(x, y), we mean that P(St = y | S0 = x). In
other words, there is a positive probability of going from any state to any other state.
20
A probability measure µ on X is called an invariant (or stationary) measure if
X
x∈X
µ(x)Π(x, y) = µ(y)
for all y ∈X. Regarding Π as a matrix (where Π(x, y) is the (i, j)th entry) and µ as
a vector, this is equivalent to the condition
µ = µΠ
which perhaps gives a more intuitive idea of the measure. This is the µ that we will
refer to in the notation (Π, µ) for the Markov chain.
A Markov chain is reversible if
µ(x)Π(x, y) = µ(y)Π(y, x)
for all x, y ∈X. This is often called the detailed balance condition.
From now on, we will assume that (Π, µ) is a reversible Markov chain with tran-
sition matrix Π and invariant measure µ. For functions f and g on X, the Dirichlet
form associated to (Π, µ) is given by
E(f, g) := ⟨(I −Π)f, g⟩µ
In particular,
E(f, f) = 1
2
X
x,y∈X
[f(x) −f(y)]2µ(x)Π(x, y)
For a proof of this fact, see [Levin et al., 2009].
We will notate the eigenvalues of Π in decreasing order by
1 = η1 > η2 ≥· · · ≥η|X| ≥−1
21
Notice that 1 must be an eigenvalue of Π, since (letting e temporarily represent a
vector of all 1’s)
Πe = e
using the fact that the sum along each row and column of Π is 1. To see why the rest
of the eigenvalues must have magnitude less than 1, note that if |ηk| > 1 for some k,
then Πnvk = ηn
kvk for an eigenvector vk. If |ηk|n is large, this contradicts the fact that
all entries of Π are between 0 and 1.
The spectral gap of the Markov chain is deﬁned by λ1 := 1 −η2. The spectral
gap relates to the Dirichlet form via the Poincare inequality, which says that for all
functions f on X,
λ1Varµ(f) ≤E(f, f)
In order to work with Ledoux’s concentration of measure result, we need to deﬁne a
triple norm on functions f on X. Let
∥|f∥|2
∞= 1
2 sup
x∈X
X
y∈X
|f(x) −f(y)|2Π(x, y)
We are now in a position to state Ledoux’s concentration of measure result on Markov
chains [Ledoux, 2005].
Theorem 2.3.1. Let (Π, µ) be a reversible Markov chain on X with a spectral gap
given by λ1 > 0. Then, whenever ∥|F∥|∞≤1, F is integrable with respect to µ and
for every r ≥0,
µ

{F ≥
Z
Fdµ + r}

≤3e−r√
λ1/2
Proof. We will begin by assuming that F is a bounded function on X with mean 0
and ∥|F∥|∞≤1. We will let
Λ(λ) =
Z
eλFdµ
22
for λ > 0. By deﬁnition,
E(eλF/2, eλF/2) = 1
2
X
x,y∈X
[eλF(x)/2 −eλF(y)/2]2Π(x, y)µ({x})
which, by symmetry is equal to
X
F(y)<F(x)
[eλF(x)/2 −eλF(y)/2]2Π(x, y)µ({x})
=
X
F(y)<F(x)
eλF(x) + eλF(y) −2eλ/2(F(x)+F(y))Π(x, y)µ({x})
Using the fact that F(y) < F(x) in the region we are summing over, the above is
≤
X
F(y)<F(x)
2eλF(x) −2eλ/2(F(x)+F(y)Π(x, y)µ({x})
=
X
F(y)<F(x)
2eλF(x)(1 −eλ/2(F(y)−F(x)))Π(x, y)µ({x})
Taylor expanding the exponential to second order gives
≤
X
F(y)<F(x)
2eλF(x)(1−(1+λ/2(F(y)−F(x))+(λ/2F(y)−λ/2F(x))2/2Π(x, y)µ({x})
The ﬁrst order term cancels by symmetry once we go back to summing over the whole
x, y ∈X, leaving us with
X
x,y∈X
eλF(x)(λ/2F(y) −λ/2F(x))2Π(x, y)µ({x})
= λ2
2 ∥|F∥|2
∞
Z
eλFdµ
23
so we have showed that
E(eλF/2, eλF/2) ≤∥|F∥|2
∞
Z
eλFdµ
The Poincare inequality says that
λ1Varµ(f) ≤E(f, f)
Using this, and the fact that
λ1Var(eλF/2) = λ1(Λ(λ) −Λ2(λ/2))
we have that
λ1(Λ(λ) −Λ2(λ/2)) ≤λ2∥|F∥|2
∞Λ(λ)
Recalling that ∥|F∥|2
∞≤1 by assumption, we have the inequality
Λ(λ) −Λ
λ
2
2
≤λ2
λ1
Λ(λ)
Solving for Λ(λ) gives
Λ(λ) ≤
1
1 −λ2
λ1
Λ
λ
2
2
Now we use the same inequality on the Λ
  λ
2

term and iterate n times, leaving us
with
Λ(λ) ≤
n−1
Y
k=0
 
1
1 −
λ2
4kλ1
!2k
Λ
 λ
2n
2n
We now let n →∞.
The product will converge provided that λ < √λ1.
This
assumption does not cause any problems as we only required that λ be nonnegative.
Recall that Λ(λ) =
R
eλFdµ and that F is bounded, so Λ(λ) = 1 + o(λ). This gives
24
Λ(λ/2n)2n →1 as n →∞. Hence we are left with
Λ(λ) ≤
∞
Y
k=0
 
1
1 −
λ2
4kλ1
!2k
If we now set λ = 1
2
√λ1, we have
λ
√λ1
2

≤
∞
Y
k=0

1
1 −
1
4k+1

≤3
Recall this tells us that
Z
eλFdµ ≤3
Markov’s inequality states that for a nonnegative integrable random variable X and
and r > 0,
P(X > a) ≤E(X)
a
Applying this to the above equation, we have
P(e
q
λ1F
2
> er) ≤3/er
so
P(
√λ1F
2
> r) ≤3/er
giving
P(F > r) ≤3e−
√
λ1
2
r
(2.10)
This is essentially the result we wanted to prove, except that to begin with, we
assumed that F was a mean zero function and bounded. To get rid of the mean 0
condition, we can simply replace F in the beginning of the proof with F ′ = F −E(F),
giving us a mean zero function and our desired result. To relax the boundedness
condition, we approximate F by Fn = min(|F|, n). Notice this still satisﬁes ∥|F∥|2
∞≤
1. Choose an m such that P(|F| ≤m) ≥1/2 for all n and an r such that 3e−r√λ1/2 <
25
1/2. Since
P(Fn > r) ≤3e−
√
λ1
2
r
we must have
Z
Fndµ ≤m + r
Then, by the monotone convergence theorem, we have
Z
|F|dµ < ∞
We can then apply (2.1) to min(max(F, −n), n) and let n →∞to get the ﬁnal result.
In chapter 3, we will see multiple ways that this theorem can be applied to get
concentration of measure results for a variety of interesting quantities merely by
choosing an appropriate Markov chain with a known spectral gap.
