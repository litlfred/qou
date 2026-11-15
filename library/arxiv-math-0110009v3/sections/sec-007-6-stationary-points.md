---
doc_id: arxiv-math-0110009v3
doc_title: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003"
section_id: sec-007-6-stationary-points
section_title: "Stationary points"
section_number: 6
pages: 12-15
source_pdf: 0110009v3.pdf
source_sha256: bb0c97f2de33b0dd
toc_source: inferred
doc_brief: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003 — We develop an analogue for sphere packing of the linear programming bounds for error-correcting codes, and use it to prove upper bounds for the density of"
---
We do not know how to use Theorem 3.1 to match the best density bound
known in high dimensions, that of Kabatiansky and Levenshtein [KL]. How-
ever, it provides a new proof of the second-best bound known, due to Leven-
shtein [Lev]:

A< Ina
~ (n/2)!24""
where j; is the smallest positive zero of the Bessel function Jj. (For more
information about the asymptotics of this bound and how it compares with
other bounds, see page 19 of [CS], but note that equation (42) is missing the
exponent in 7’ /2°) We will show how to use a calculus of variations argument
to find functions that prove that bound. This approach is analogous to that
used by Levenshtein. Yudin [Y] has also given a proof of Levenshtein’s bound
that seems reminiscent of our general approach, but not identical.

To construct a function f for use in Theorem 3.1, we begin by supposing
that there is a function g such that f(x) = (1— |2|?)g(x)?, so that f auto-
matically satisfies the inequality f(x) < 0 for |x| > 1. (We write g instead of
g for convenience later.) Assume that g is radial, and has support in the ball
of radius R about the origin; we discuss these assumptions later. Notice that
nothing in our setup requires f to be nonnegative, so we must check for this
property later.
NEW UPPER BOUNDS ON SPHERE PACKINGS I
701
We have bf = g ∗(g + Lg), where ∗denotes convolution and
L =
1
4π2
n
X
j=1
∂2
∂t2
j
,
so that under the Fourier transform, L corresponds to multiplication by −|x|2.
We require f(0) = 1, i.e.,
R
Rn g = 1. We want to maximize bf(0), subject to
this constraint. Notice that
bf(0) =
Z
Rn g(0 −t)(g + Lg)(t) dt =
Z
Rn g(t)(g + Lg)(t) dt =
Z
Rn g(g + Lg),
because g is radial (and hence even).
Perturb g to g+h, where h has integral zero (so that f(0) does not change)
and has support in the ball of radius R. Then the ﬁrst order change in bf(0) is
Z
Rn(gh + hg + gLh + hLg) = 2
Z
Rn h(g + Lg)
(where the equality comes from integration by parts).
In order to have this vanish whenever
R
Rn h = 0, the function g +Lg must
be constant (within the support of g), so for some constant c we have
g + Lg = cχR,
where χR is the characteristic function of the ball of radius R about 0. Then
it follows from Proposition 2.1 that
(1 −|x|2)bg(x) = c(R/|x|)n/2Jn/2(2πR|x|).
Now 2πR must be a zero of Jn/2 for the right-hand side to vanish at
|x| = 1, and c is determined (given R) by
1 =
Z
Rn g =
Z
Rn g + Lg =
Z
Rn cχR = cRnπn/2/(n/2)! .
(The function g + Lg has the same integral as g, because integration by parts
shows that Lg has integral 0.)
In fact, we take 2πR to be the ﬁrst positive root jn/2 of Jn/2, in order
to make bf nonnegative everywhere. To check that it is indeed nonnegative
everywhere then, we use the equation
bf = g ∗(g + Lg) = g ∗(cχR).
If g is nonnegative everywhere, then so is bf. We can now determine g explicitly:
We know that g+Lg = cχR. The diﬀerential operator 1+L takes a radial
function u(|t|) to
u′′(|t|)
4π2
+ n −1
4π2|t|u′(|t|) + u(|t|).
702
HENRY COHN AND NOAM ELKIES
It follows from this and the diﬀerential equation satisﬁed by the Bessel func-
tions that
Jα(2π|t|)/|t|α
is in the kernel of 1 + L, if α = n/2 −1. From that, one can check that
g(t) =

−
Rα
Jα(2πR)
Jα(2π|t|)
|t|α
+ 1

χR(t).
One can check that the minimum of Jα(2π|t|)/|t|α occurs at
|t| = jn/2/(2π) = R,
so g is nonnegative everywhere, as desired, since Jα(2πR) = Jα(jn/2) < 0 (the
roots of the functions Jα and Jα+1 = Jn/2 are interlaced).
Thus, we have constructed a function f satisfying the hypotheses of The-
orem 3.1. It has f(0) = 1 and
bf(0) =
Z
Rn g(g + Lg) = c
Z
Rn g = c = (n/2)!
πn/2Rn.
Because R = jn/2/(2π), this function proves Levenshtein’s sphere packing
bound:
Proposition 6.1.
The function
f(x) = Jn/2(jn/2|x|)2
(1 −|x|2)|x|n
satisﬁes the hypotheses of Theorem 3.1, and leads to the upper bound
jn
n/2
(n/2)!24n
for the densities of n-dimensional sphere packings.
This function does not optimize the bound in Theorem 3.1, but it does
optimize it within the class of functions whose Fourier transforms have sup-
port in the ball of radius jn/2/π about the origin. This was ﬁrst proved by
Gorbachev [Go]. For another proof, see [C].
It is not a coincidence that this proves exactly the same bound as in
Levenshtein’s paper [Lev]. Levenshtein studies spherical codes with minimal
angular separation θ, and derives his sphere packing bound from letting θ →0.
Under that limit, the functions he uses in the linear programming bounds for
spherical codes become our Bessel function example. This can be proved using
the limit
(6.1)
lim
j→∞j−αP (α,β)
j

cos z
j

= (z/2)−αJα(z),
which is 10.8 (41) in [EMOT].
NEW UPPER BOUNDS ON SPHERE PACKINGS I
703
The functions we have obtained are not optimal in any dimension above 1.
There are two reasons for this. First, we restricted our attention to functions
such that bf has compact support, and as we have seen in Section 5, that cannot
be true if we are to get sharp bounds.
Second, and more importantly, we
implicitly considered only functions such that bf is positive within its support.
The problem is that if bf vanishes somewhere, then the perturbations h must
be chosen so as not to push bf below zero. We made no attempt to do so, and
therefore could not ﬁnd any stationary points for which bf has zeros within its
support. We have seen in Section 5 that zeros are essential for sharp bounds.
Unfortunately, it seems diﬃcult to adapt the stationary point argument
to deal with these diﬃculties. One approach is to assume that bf has zeros at
certain locations, and look at only the perturbations h that, up to ﬁrst order,
do not push bf below zero. Although we can set up such problems, we have not
been able to solve them.
