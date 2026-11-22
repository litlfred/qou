---
doc_id: arxiv-math-0110009v3
doc_title: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003"
section_id: sec-006-5-conditions-for-a-sharp-bound
section_title: "Conditions for a sharp bound"
section_number: 5
pages: 10-12
source_pdf: 0110009v3.pdf
source_sha256: bb0c97f2de33b0dd
toc_source: inferred
doc_brief: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003 — We develop an analogue for sphere packing of the linear programming bounds for error-correcting codes, and use it to prove upper bounds for the density of"
---
In one dimension, we have already seen how to use Theorem 3.1 to solve
the (admittedly trivial) sphere packing problem. Based on numerical evidence
and analogy with the kissing problem, we conjecture that it can also be used
to get sharp bounds in dimensions 2, 8, and 24. For reasons to be explained
shortly, it is more convenient to work with Theorem 3.2 instead of Theorem 3.1,
so we shall do so; we can convert everything to the framework of Theorem 3.1
by rescaling the variables.
In each of dimensions 1, 2, 8, and 24, the densest known packing is a lattice
packing, given by a lattice that is homothetic to its dual. This lattice is Z in
dimension 1, the A2 root lattice (i.e., the hexagonal lattice) in dimension 2, the
E8 root lattice in dimension 8, and the Leech lattice in dimension 24. See [CS]
for information about these lattices. Each of these lattices except A2 actually
equals its dual, but that is not true for A2. However, we can rescale A2 so that
the rescaled lattice is isodual, i.e., isometric with its own dual (in this case,
via a rotation).
NEW UPPER BOUNDS ON SPHERE PACKINGS I 699

Suppose A is any lattice of covolume 1, such as an isodual lattice, and f
is a radial function giving a sharp bound on A via Theorem 3.2 (ie., r is the
length of the shortest nonzero vector of A). By Poisson summation, we have

YS fo = YS fla).

xed aeA*

Given the inequalities on f and f, the only way this equation can hold is if f
vanishes on A \ {0} and f vanishes on A* \ {0}. This puts strong constraints
on f and f. When A is isodual, the vector lengths in A and A* are the same,
so f and f must both vanish on A \ {0}.

Of course, there are similar constraints on f for a sharp bound in Theo-
rem 3.1 (as opposed to Theorem 3.2), but we prefer to work with this context,
since the isodual normalizations are more pleasant, and are the standard nor-
malizations for Eg and the Leech lattice.

It is natural to try to guess f from our knowledge of its roots. For example,
in one dimension we could try

f(x) =(1-2*) J] (-2) - 4a (zy.

k>2

which clearly satisfies f(x) < 0 for |x| > 1 and has the right zeros. In fact, one
can compute its Fourier transform and check that f is nonnegative everywhere
(it has support [—1, 1] and is positive in (—1, 1)), so it solves the sphere packing
problem in dimension 1, in a different way from the function in the previous
section.

Unfortunately, it seems difficult to generalize this approach to higher di-
mensions. One can generalize this function by replacing the sine function with
a Bessel function (see Proposition 6.1), but that does not yield a sharp bound
in dimensions greater than 1. Attempts to write down a product with zeros at
the right places for a sharp bound lead to products that seem intractable.

One important thing to note is that for a sharp bound above dimension 1,
it is not possible for f to have compact support, as it does in the examples
involving sine and Bessel functions. If it did, then f could not have sufficiently
densely-spaced zeros. To be precise, if f is a radial function with support in
the ball B(0, R) of radius R about the origin, then the common value f(r) on
vectors of radius r satisfies

f(r) = fermen dt,
B(0,R)
where x is any vector with |2| = 1. This defines an entire function of r, and
for all complex r,
[F(r)| < Parr |F(o)| at,

B(0,R)
700 HENRY COHN AND NOAM ELKIES

so f is a function of exponential type, and Jensen’s formula implies that f can
have at most linearly spaced zeros (see Section 15.20 of [Ru]). However, the
nonzero vectors in the Leech lattice have lengths 2k for integers k > 1, and
those in Eg have lengths /2k for integers k > 0. The function f must vanish
at those vector lengths, and these roots are too densely spaced for f to have
compact support. Of course, f also cannot have compact support (because f
vanishes on A* \ {0}).

One might wonder whether the restriction to radial functions is misleading:
perhaps a nonradial function could be constructed more naturally. We cannot
rule out that possibility, but consider it unlikely. Even if f is not radial, a
sharp bound implies that f and f must vanish on concentric spheres centered
at the origin and passing through the nonzero points of A and A*, respectively.
The simplest reason is that if f proves that A is optimal, then it proves the
same for every rotation of A. Alternatively, after rotational symmetrization
f and f must vanish on these spheres, and the inequalities on their values
then imply that they must have vanished before symmetrization (the average
of nonnegative values vanishes if and only if the values all do). It would seem
strange for f to vanish on these spheres without being radial, but of course we
cannot rule it out.
