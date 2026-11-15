---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-064-powers-quasi-powers-and-riordan-arrays
section_title: "Powers, quasi-powers, and Riordan arrays"
section_number: null
pages: 403-408
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
385
Exception
Examples
Degenerate contributing points
9.39
Non-transverse intersection
10.69
Boundary directions
10.66
Vanishing numerator
12.18, 12.20
Table 12.4 Guide to non-generic examples.
in our asymptotic expansions typically do not vanish. Table 12.4 collects ex-
amples where the above assumptions fail to hold.
Non-transverse intersections may be arbitrarily complicated, and we cover
only a simple example. Similarly, we discuss one example with a degener-
ate contributing point. From the point of view of Fourier–Laplace integrals,
asymptotics in directions on boundaries of the cones dictating uniform behav-
ior are half of what they would be if the direction was interior to the cone. The
ﬁrst-order term in our asymptotic expansions of a sequence with generating
function F vanishes when the numerator of F is zero at its contributing singu-
larities. In this case, we can usually determine dominant asymptotic behavior
by computing higher order coeﬃcients in the expansion.
12.2 Powers, quasi-powers, and Riordan arrays
Let v(z) be a power series (or polynomial) and suppose that we want to esti-
mate the coeﬃcient [zr]v(z)k of a large power of v. This coeﬃcient equals the
coeﬃcient of zrwk in the power series expansion
F(z, w) =
1
1 −wv(z) ,
(12.1)
so we can determine asymptotics using the tools of ACSV. The combinatorial
constructions discussed in Section 2.2 of Chapter 2 show some ways in which
generating functions of this form arise. Another common application comes
from probability: if v(z) = P
r arzr, where ar = Pr(X j = r) for a family
{Xj} of independent, identically distributed random variables taking values in
Nd then v(z)n is the probability generating function for the partial sum S n =
Pn
j=1 Xj, and hence
P(S n = r) = [zr]v(z)n .
It has long been known that, under suitable hypotheses, such large powers
lead to Gaussian behavior. An early work on multivariate analytic combina-
torics [BR83] observed that this behavior is robust enough to hold not only
386
Combinatorial applications
for exact powers, but also for quasi-powers, meaning sequences of functions
{fn(z)} satisfying
fn(z) ∼Cng(z) · h(z)n
(12.2)
uniformly as z ranges over certain polydisks. Gaussian behavior of coeﬃ-
cients of quasi-powers is the basis for the GF-sequence method developed by
Bender, Richmond, and collaborators in a series of papers including [Ben73;
BR83; GR92; BR99]; see also the work of Hwang extending this to algebraic-
logarithmic singularities [Hwa96; Hwa98a; Hwa98b]. These papers give con-
ditions under which a multivariate generating function
F(z1, . . . , zd, w) =
∞
X
n=0
fn(z)wn
(12.3)
is a quasi-power in the sense of (12.2). They then show that if g and h are
analytic in a ∆-domain (recall Figure 3.1), if h has a unique dominant singu-
larity where the boundary of the region intersects the positive real axis, and
if the quadratic part of h is nondegenerate there, then, after a rescaling, the
coeﬃcients of fn(z) have a Gaussian limit distribution as n →∞.
Riordan arrays
An important combinatorial family of quasi-powers is the set of Riordan ar-
rays {ank : n, k ≥0} whose generating functions F(x, y) = P
n,k≥0 ankxnyk
satisfy
F(x, y) =
φ(x)
1 −yv(x)
(12.4)
for some analytic functions φ and v with φ(0) , 0. Just as (12.1) repre-
sents sums of independent, identically distributed random variables when v
is a probability generating function, the function (12.4) is a delayed renewal
sum [Dur04, Section 3.4], where an initial random variable X0 may be added
that is distributed diﬀerently from the others. Riordan arrays cover an enor-
mous number of examples arising in applications, including many lattice path
problems, and are useful for simplifying sums because of the Pascal-like re-
currences the terms satisfy – see [Mer+97; Spr94].
Remark 12.1. Some authors require that v(0) = 0 in (12.4), but we do not
make this assumption.
12.2 Powers, quasi-powers, and Riordan arrays
387
Deﬁne the functions
µ(v; x) := xv′(x)
v(x)
(12.5)
σ2(v; x) := x2v′′(x)
v(x)
+ µ(v; x) −µ(v; x)2 = xdµ(v; x)
dx
,
(12.6)
whose symbols are motivated by probability theory (see Section 12.8 below).
Theorem 12.2. Let (v(x), φ(x)) determine a Riordan array with generating
function (12.4). Suppose that v(x) has radius of convergence R ∈(0, ∞] and is
aperiodic with nonnegative coeﬃcients. If φ has radius of convergence at least
R then
(i) the function µ(v; x) is strictly increasing for x ∈(0, R), and its range
contains the interval J = (A, B), where A = µ(v; 0) and B = µ(v; R) are
deﬁned as one-sided limits;
(ii) there is an asymptotic expansion of the form
ars ≈x−rv(x)ss−1/2
∞
X
k=0
bk(r/s)s−k
(12.7)
uniformly as r/s varies over compact subsets of J, where x is the unique
positive real solution to µ(v; x) = r/s. The leading term in this expansion
is
ars ∼x−rv(x)s
φ(x)
p
2πsσ2(v; x)
.
(12.8)
Proof
Writing P(x, y) = φ(x) and Q(x, y) = 1−yv(x), we see that V is smooth
because Q and Qy never simultaneously vanish. Furthermore, the smooth crit-
ical point equations simplify to show that (x, 1/v(x)) is critical in the direction
(r, s) if and only if µ(v; x) = r/s. Lemma 6.41 shows that all points of the form
(x, 1/v(x)) for x ∈(0, R) are strictly minimal points. The Hessian determinant
appearing in the asymptotic expansion (9.2) simpliﬁes to σ2(v; x), so the result
follows from an application of Theorem 9.4 after we show that µ is strictly
increasing for x ∈(0, R). The latter result follows from (12.6).
□
Remark 12.3. If v has coeﬃcients of mixed sign, more complicated behavior
can occur – see Exercise 12.8.
Remark 12.4. Riordan arrays are often speciﬁed by a recursion of the form
an+1,k+1 =
∞
X
j=0
cjan,k+j ,
388 Combinatorial applications

where the generating function C(t) = a c it! is known explicitly but v(x)
is known only implicitly through the equation v(x) = xC(v(x)). Subtleties that
arise in computations when dealing with such implicitly defined v are discussed
in [Wil05].

Example 12.5 (Packing paths in paths). DoSli¢ [DoS19] derives the bivariate
generating function

F(x,y) = danny’ =

nk

J—x”

l-x-x"(1- x")y

for the number a,, of ways to maximally pack a path of length m in a path of
length n, using exactly k copies of the smaller path. This is a Riordan array
with d(x) = (1 — x”)/(1 — x) and v(x) = x(x), and ¢ and v have infinite radii
of convergence since they are both polynomials.

Taking derivatives shows that

x +207 +--+ + (m= 1x"!
Ttxeeype byl

,

BY; x) = m+

and yu increases from m to 2m — | as x increases from zero to infinity, cov-
ering all directions of combinatorial interest [DoS19, Proposition 2.1]. Thus,
when 2 = n/k remains in a compact sub-interval of (m,2m — 1) the Gaussian
asymptotic expansion (12.7) holds.

To determine the leading term in this expansion with respect to A, one can
compute a lexicographic Grébner basis of the ideal (u(v;x) — A,o7(v; x) -
S,@(x) — T) in Q(A)[x, S,T] to eliminate x and write o? and ¢ in terms of
A. For instance, when m = 3 we obtain the irreducible elimination polynomials

281 712
a
3

pS;a)=S? 4222-162 S)s + At 1623 + — A + 220

q(T; A) = (A-5)T? + BA 16)T +3.

In this case we can use the quadratic formula to express a? and ¢ explicitly
in terms of A, but for general m one must identify the correct branch of the
elimination polynomials implicitly. Note that the system p(S, A) = ps(S,A) =
PaA(S,A) = 0 has no solutions, so the two branches given by solving p(S, A)
for S do not meet. Because o? is a continuous function of A on the interval
[m, 2m — 1], and limy n+ o?(v; x) = lim,_,9- 7(v; x) = 0, the value of a? as
a function of 2 is the branch of p(S, A) = 0 passing through the point (S, 2) =
(0, m). The correct branch of g(S, A) = 0 for @ with respect to A is determined
analogously. 4

The condition in Theorem 12.2 that ¢ has at least as large a radius of con-
vergence as v is satisfied in many, but not all, applications.
12.2 Powers, quasi-powers, and Riordan arrays
389
Example 12.6 (Maximum number of distinct subsequences). Flaxman, Har-
row, and Sorkin [FHS04] study strings of length n over the alphabet {1, 2, . . . , d}
that contain as many distinct (not necessarily contiguous) subsequences of
length k as possible. Let ank denote the maximum number of distinct subse-
quences of length k that can be found in a single string of length n. Initial
segments S |n of the inﬁnite string S consisting of repeated blocks of the string
12 · · · d turn out always to be maximizers, meaning S |n has exactly ank distinct
subsequences of length k. The generating function for {ank} is then computed
to be
F(x, y) =
X
n,k
ankxnyk =
1
1 −x −xy(1 −xd) ,
meaning ank is a Riordan array with φ(x) = (1−x)−1 and v(x) = x+x2+· · ·+xd.
Assume for non-triviality that d ≥2. The singular variety V is the union of
the line x = 1 and the smooth curve y = 1/v(x), which meet transversely at the
double point (1, 1/d); see Figure 12.1 for an illustration with d = 3.
Figure 12.1 V in the case d = 3.
390
Combinatorial applications
The radius of convergence of φ, namely 1, is now less than the radius of
convergence of v, which is inﬁnity. Taking derivatives shows that
µ(v; x) =
1
1 −x −
dxd
1 −xd = 1 + 2x + 3x2 + · · · + dxd−1
1 + x + x2 + · · · + xd−1
,
so that µ increases from 1 to (d +1)/2 as x increases from 0 to 1. The Gaussian
asymptotics of (12.7) still hold, but only when λ = n/k remains in a compact
sub-interval of (1, d+1
2 ), and the computations to compute terms in this asymp-
totic expansion are analogous to those for Example 12.5 above.
Proposition 6.41 implies that there is a strictly minimal point in the positive
quadrant controlling asymptotics in any direction. When λ ≥(d + 1)/2 this
turns out to be the non-smooth point (1, 1/d), and Corollary 10.14 from Chap-
ter 10 implies that aλk,k ∼dk in this case. Note that this is trivial when λ ≥d
because any preﬁx of the inﬁnite string S with length at least dk will allow all
possible k-subsequences to occur, meaning ank = dk in this regime.
◁
