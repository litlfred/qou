---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-004-generating-functions-and-asymptotics
section_title: "Generating functions and asymptotics"
section_number: null
pages: 23-27
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
5
The algebraic form of a generating function is intimately related to recur-
sions – and exact formulae – for its coeﬃcient sequence ar, as well as combi-
natorial decompositions for the objects enumerated by ar. In a complementary
manner, the analytic properties of a generating function correspond to esti-
mates of ar.
1.1 Generating functions and asymptotics
In this text we are chieﬂy concerned with the asymptotic behavior of ar as
r →∞in certain directions. To discuss the behavior of sequences as their
indices go oﬀto inﬁnity, we introduce some standard asymptotic notation.
Deﬁnition 1.2 (asymptotic notation). If f and g are real-valued functions then
we write
• f = O(g) if and only if lim sup
x→x0
| f(x)/g(x)| < ∞,
• f = o(g) if and only if lim
x→x0 f(x)/g(x) = 0,
• f ∼g if and only if lim
x→x0 f(x)/g(x) = 1,
• f = Ω(g) when g = O(f), and
• f = Θ(g) when both f = O(g) and g = O( f),
for some value x0 understood in context, typically 0 or +∞.
As n →∞the function f(n) is said to be rapidly decreasing if f(n) =
O

n−K
for every K > 0, exponentially decaying if f(n) = O(e−cn) for some
c > 0, and super-exponentially decaying if f(n) = O(e−cn) for every c > 0.
Remark. An alternative deﬁnition is that f = O(g) when there exists C > 0
and an open neighborhood N of x such that f(x) ≤Cg(x) for all x ∈N. In this
case C is called an implied constant. One may increase C and decrease N and
still maintain the inequality, so implied constants are not unique, even if they
are chosen to give a tight inequality.
Example 1.3. As n →∞the function f(n) = 1/n! decays super-exponentially,
while 2−n decays exponentially and e−√n approaches zero but does not decay
exponentially.
◁
An asymptotic scale is a sequence {gj : j ∈N} of functions satisfying gj+1 =
o(g j) for all j ≥0. An asymptotic expansion (also called asymptotic series or
asymptotic development)
f ≈
∞
X
j=0
c jgj
6
Introduction
for a function f in terms of an asymptotic scale {gj : j ∈N} and constants
cj ∈C is said to hold if
f −
M−1
X
j=0
c jgj = O(gM)
(1.2)
for every M ≥1.
Remark. It is possible that c j = 0 for all j. For example, this will happen if
gj(n) = n−j and f is exponentially decaying. In this case there is no leading
term in the expansion. Otherwise, the leading term of an asymptotic expan-
sion is the ﬁrst non-zero term ckgk in the expansion.
Example 1.4. Stirling’s famous approximation to the factorial can be reﬁned
to give an asymptotic series
n! ≈
n
e
n √
2πn
X
ℓ≥0
cℓn−ℓ
with coeﬃcient sequence {cℓ} beginning 1, 1/12, 1/288, −139/51840, . . . .
◁
Example 1.5. Let f ∈C∞(R) be a smooth real function deﬁned on a neighbor-
hood of zero, so that cn = f (n)(0)/n! is the nth term in its Taylor expansion. If f
is not analytic then this expansion may not converge to f, and may even diverge
for all non-zero x, but Taylor’s Theorem with remainder always implies
f(x) =
M−1
X
n=0
cnxn + cMξM
for some ξ > 0 bounded close to the origin. This proves that
f ≈
X
n≥0
cnxn
is always an asymptotic expansion for f near zero.
◁
Remark. Following Poincar´e, many authors use the symbol ∼to denote both
asymptotic equivalence of functions and asymptotic series expansions. How-
ever, this overloading of notation can lead to inconsistencies. We thus follow
texts such as [dBru81] in using ≈for asymptotic expansions.
Exercise 1.1. Let f(x) = ex. Prove that f(x) ∼1 as x →0 but f(x)̸ ≈1 as an
asymptotic expansion in powers of x at x = 0.
All these notations hold in the multivariate case as well, except that if the
limit value z0 is inﬁnity then a statement such as f(z) = O(g(z)) must also
specify how z approaches the limit. A direction is a ray in Rd deﬁned by all
1.1 Generating functions and asymptotics
7
positive multiples of a ﬁxed non-zero vector, which can also be viewed as
an element of (d −1)-dimensional real projective space RPd−1. Often we will
parametrize directions of interest by taking r →∞while ﬁxing or bounding
the normalized vector ˆr := r/|r|, where, as introduced above,
|r| = |r1| + |r2| + · · · + |rd|.
Sometimes we shall loosely refer to “the direction r”, by which we mean the
direction parametrized by ˆr, or the ray determined by r.
Deﬁnition 1.6. A multivariate asymptotic expansion
fr ≈
∞
X
j=0
c jgj(r)
holds on a compact set of directions D ⊆RPd−1 if each cj ∈C, each gj =
o(gj+1), and fr −PM−1
j=0 gj(r) = O(gM) for each M as r →∞with ˆr ∈D. This
asymptotic expansion is a uniform asymptotic expansion on D if the implied
constants can be chosen independently of the sequence r as long as ˆr ∈D.
Example 1.7. In Chapter 9 we shall derive the result
 r + s
s
!
∼(r + s)(r+s)
rrss
r
r + s
2πrs
for all r, s > 0 as (r, s) →∞with r/(r + s) and s/(r + s) remaining bounded
and away from 0. This gives the ﬁrst term of an asymptotic series which is
uniform provided r/s and s/r are bounded away from 0, with all terms in the
series varying smoothly with direction. Because of our restrictions on r/s, this
asymptotic series can be expressed in terms of the asymptotic scale
gj(r, s) = (r + s)(r+s)
rrss
r
r + s
rs
(r + s)−j ,
an asymptotic scale involving decreasing powers s−j of s, or an asymptotic
scale involving decreasing powers r−j of r. Note that this multivariate asymp-
totic approximation is not uniform for all real directions: for instance, if r = 0
then
r+s
s

= 1 for all s.
◁
Remark. Throughout this book, we typically use f(z) and an instead of F(z)
and ar when dealing with the univariate case.
As we will see in Chapter 3, the generating function f(z) for a univariate
sequence {an : n ∈N} leads, almost automatically, to asymptotic estimates for
8
Introduction
an as n →∞. To estimate an when its generating function f is known, we
begin with Cauchy’s integral formula
an = 1
2πi
Z
C
z−n−1 f(z) dz .
(1.3)
Equation (1.3) represents an by a complex contour integral on a suﬃciently
small circle C around the origin, and one may apply complex analytic methods
to obtain an asymptotic estimate. The necessary knowledge of residues and
contour shifting may be found in an introductory complex variables text such
as [Con78b; BG91], with a particularly nice treatment of univariate saddle
point integration found in [Hen88; Hen91]. In particular, the singularities of
f(z) play a large role in characterizing asymptotic behavior.
The situation for multivariate arrays is nothing like the situation for uni-
variate arrays. In 1974, when Bender published his review article [Ben74] on
asymptotic enumeration, the literature on asymptotics of multivariate generat-
ing functions was in its infancy. Bender’s concluding section urges research in
this area:
Practically nothing is known about asymptotics for recursions in two variables even
when a generating function is available. Techniques for obtaining asymptotics from
bivariate generating functions would be quite useful.
In the 1980s and 1990s, a small body of results was developed by Bender,
Richmond, Gao, and others, giving the ﬁrst partial answers to asymptotic ques-
tions for multivariate generating functions. The ﬁrst paper to concentrate on
extracting asymptotics from multivariate generating functions was [Ben73], al-
ready published at the time of Bender’s survey, but the seminal paper is [BR83].
The authors work under the hypothesis that F has a singularity of the form
A/(zd −g(x))q on the graph of a smooth function g, for some real exponent
q, where x denotes (z1, . . . , zd−1). They show, under appropriate further hy-
potheses on F, that the probability measure µn one obtains by renormalizing
{ar : rd = n} to sum to 1 converges to a multivariate normal distribution when
appropriately rescaled. Their method, which we call the GF-sequence method,
is to break the d-dimensional array {ar} into a sequence of (d −1)-dimensional
slices and consider the sequence of (d −1)-variate generating functions
fn(x) =
X
r:rd=n
arxr .
They show that, asymptotically as n →∞,
fn(x) ∼Cng(x)h(x)n
(1.4)
