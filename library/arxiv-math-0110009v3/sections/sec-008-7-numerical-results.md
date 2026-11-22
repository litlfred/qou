---
doc_id: arxiv-math-0110009v3
doc_title: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003"
section_id: sec-008-7-numerical-results
section_title: "Numerical results"
section_number: 7
pages: 15-18
source_pdf: 0110009v3.pdf
source_sha256: bb0c97f2de33b0dd
toc_source: inferred
doc_brief: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003 — We develop an analogue for sphere packing of the linear programming bounds for error-correcting codes, and use it to prove upper bounds for the density of"
---
It is possible to get numerical results by using linear programming to
ﬁnd functions for use in Theorem 3.1, as was done for the kissing problem by
Odlyzko and Sloane in [OS]. The idea is to ﬁx one of f(0) and bf(0), and view
extremizing the other as an inﬁnite-dimensional linear programming problem.
One can try to approximate it with a ﬁnite-dimensional problem, and solve it
on a computer. Although we obtained some numerical results this way, it was
cumbersome and generally ineﬀective. Instead, we use the following approach.
First, consider trying to use our techniques to bound the density of an
isodual lattice. There is no reason for optimal sphere packings to be isodual
lattices, and for example in three dimensions they are known not to be, but it
is convenient to use this case as a stepping stone.
Proposition 7.1.
Suppose g : Rn →R is a radial, admissible function,
is not identically zero, and satisﬁes the following three properties:
(1) g(0) = 0,
(2) g(x) ≥0 for |x| ≥r, and
(3) bg = −g.
Then every isodual lattice in dimension n must contain a nonzero vector of
length at most r.
Proof of special case. For simplicity, we deal only with the case in which
g(x) > 0 for |x| ≫0. Let Λ ∼= Λ∗be an isodual lattice. By Poisson summation,
X
x∈Λ
g(x) =
X
x∈Λ∗
bg(x) = −
X
x∈Λ
g(x),
704
HENRY COHN AND NOAM ELKIES
so
X
x∈Λ
g(x) = 0.
In order for the sum not to be positive, the lattice Λ must contain some nonzero
vector of length at most r.
We can actually remove the hypothesis that g(x) > 0 for |x| ≫0 from the
proof of Proposition 7.1, by using a scaling trick, as in the proof of Theorem 3.2.
However, we omit the details, because the hypothesis holds in all our numerical
examples.
Notice that given any function f that proves a bound in Theorem 3.2,
we can produce a g that proves the same bound in Proposition 7.1, by taking
g = bf −f. Thus, the bound we get for isodual lattices is at least as good
as that for general sphere packings. In principle, it could be better, but in
practice we ﬁnd that it is not (as we explain below).
We can ﬁnd excellent functions for use in Proposition 7.1 as follows. Let
Lα
k(x) be the Laguerre polynomials orthogonal with respect to the measure
e−xxα dx on [0, ∞). Set α = n/2 −1, and deﬁne
gk(x) = Lα
k(2π|x|2)e−π|x|2
for k ≥0; we suppress the dependence on n in our notation.
These func-
tions form a basis for the radial eigenfunctions of the Fourier transform, with
eigenvalues (−1)k (see Section 4.23 and equation (4.20.3) of [Leb]).
To ﬁnd a function g for use in Proposition 7.1, we consider a linear com-
bination of g1, g3, . . . , g4m+3, and require it to have a root at 0 and m double
roots at z1, . . . , zm. (Counting degrees of freedom suggests that there should
be a unique such function, up to scaling.) We then choose the locations of
z1, . . . , zm to minimize the value r of the last sign change of g. To make this
choice, we do a computer search. Speciﬁcally, we make an initial guess for
the locations of z1, . . . , zm, and then see whether we can perturb them to de-
crease r. We repeat the perturbations until reaching a local optimum. Strictly
speaking, we cannot prove that it ever converges, or comes anywhere near the
global optimum. However, it works well in practice. At any rate this cannot
aﬀect the validity of our bounds, only their optimality given m. As we increase
m, this method should give better and better bounds, which should converge
to the best bounds obtainable using Proposition 7.1.
This method gives good functions for use in Proposition 7.1, but naturally
bounds on all sphere packings would be better than bounds only on isodual
lattices. We can turn these functions into functions satisfying the hypotheses
of Theorem 3.2, without changing r, as follows.
Let h be a linear combination of g0, g2, . . . , g4m+2 with double zeros at
z1, . . . , zm, such that g + h has a double zero at r. Then in the examples we
have computed, g + h has constant sign, which we can take to be positive. We
NEW UPPER BOUNDS ON SPHERE PACKINGS I
705
end up with a function f = −g + h that is nonpositive outside radius r, and
whose Fourier transform bf = g + h is nonnegative everywhere; furthermore,
f(0) = bf(0).
Thus, we can apply Theorem 3.2 to get the same bound for
general sphere packings that g proves for isodual lattices. Notice that it is not
clear a priori that f must satisfy all the hypotheses of Theorem 3.2, but it
happens in all of our numerical examples.
Figure 1 (from §1) and Table 3 (from Appendix C) illustrate the bounds
this method produces, using m = 6 as the number of forced double zeros
(except in dimension 7 and lower, where m = 5 suﬃces for the accuracy we
desire). We also list for comparison Rogers’ bound [Ro], which was previously
the best bound known in dimensions 4 through 36. The choices of forced double
roots are described in Table 4 (from Appendix C).
These bounds were calculated using a computer. However, the mathe-
matics behind the calculations is rigorous. In particular, we use exact rational
arithmetic, and apply Sturm’s theorem to count real roots and make sure we
do not miss any sign changes.
More precisely, we take the quantities 2πz2
i
to be rational numbers. That is convenient, because the functions gk(x) are
polynomials in 2π|x|2 with rational coeﬃcients (times Gaussians, which have
no sign changes). The one subtlety is that in constructing h, we want g + h to
have a double root at r, and 2πr2 is generally not rational. Instead of doing
this computation using ﬂoating point arithmetic, we replace 2πr2 by a nearby
rational number and then determine h exactly, using that value of r. To do so,
we must increase r slightly, but of course we can make the increase as small as
we wish.
In dimensions 8 and 24, we carried out the calculations for m = 11. The
resulting upper bounds are within factors of 1.000001 and 1.0007071 of equality,
respectively. More precisely, in dimension 8 we take
2πr2 = 12.56637375,
and in dimension 24 we take
2πr2 = 25.1342216.
The forced double roots we used to achieve these bounds are given in Tables 1
and 2.
i
1
2
3
4
5
6
2πz2
i
25.1328
37.6995
50.2678
62.8463
75.4579
88.2463
i
7
8
9
10
11
2πz2
i
101.3618
115.6443
131.0298
150.0861
174.2876
Table 1. Forced double roots for m = 11, n = 8.
706
HENRY COHN AND NOAM ELKIES
i
1
2
3
4
5
6
2πz2
i
37.705
50.285
62.893
75.578
88.454
101.737
i
7
8
9
10
11
2πz2
i
115.776
131.035
148.162
168.215
193.766
Table 2. Forced double roots for m = 11, n = 24.
Our numerical results lead us to the following conjectures.
Conjecture 7.2.
The smallest possible value of r in Proposition 7.1
equals that in Theorem 3.2, and for each optimal g from Proposition 7.1, there
exists an optimal f from Theorem 3.2 such that g = bf −f.
Conjecture 7.3.
There exist functions that satisfy the hypotheses of
Theorem 3.2 and solve the sphere packing problem in dimensions 2, 8, and 24.
Conjecture 7.4.
The numerical method described above gives bounds
that converge (as m →∞) to the optimal bounds obtainable using Theorem 3.2.
