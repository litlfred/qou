---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-005-4-linear-programming
section_title: "Linear programming"
section_number: 4
pages: 6-7
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
Like the linear programming bounds of Cohn and Elkies [CE03] for the density of sphere
packings, for each of the five invariants sys, kiss,λ 1,m 1, andN small, our criterion will take
the following form:
Suppose thatfis an admissible function such thatfand bfsatisfy certain
linear inequalities over certain intervals. Thenfand bfproduce a bound on
the given invariant that holds for every closed hyperbolic surface (satisfying
certain conditions) in a given genus.
This is called “linear programming” because the inequalities are linear in the sense that
any positive linear combination of functions that satisfy the inequalities still satisfies the
inequalities. However, the function to be optimized (the resulting bound) is not linear inf.
Moreover, the space we are optimizing over is infinite-dimensional and there are infinitely
many inequalities to check (one at each point in the specified intervals). For these reasons,
classical linear programming algorithms do not work well, which led Cohn and Elkies to
devise the following strategy (adapted here to our setting).
The idea is to consider functionsfof the formf(x) =p(x 2)e−x2/2 wherepis a poly-
nomial. Such a function is automatically admissible since its Fourier transform takes the
form bf(y) =q(y 2)e−y2/2 for some polynomialq, hence defines an entire function with super-
exponential decay in any horizontal strip. Moreover, the mapp7→qis linear. In fact, it is
LINEAR PROGRAMMING BOUNDS FOR HYPERBOLIC SURF ACES 7
diagonal with entries (−1)n with respect to the basis of generalized Laguerre polynomials
L(−1/2)
n , which in turn are related to the Hermite polynomialsH 2n by
L(−1/2)
n (x2) = (−1)n
22nn!H2n(x).
The upshot of the linearity of the mapp7→qis that it is possible to impose linear equations
on bothfand bfsimultaneously. All one has to do is solve a linear system of equations to
find the coefficients ofpandq. The conditions we impose are thatfand bfhave double
zeros at certain pointsx 1,...,x m andy 1,...,y n respectively.
The reason for imposing double zeros is that it prevents local changes of sign and with
enough double zeros at appropriate locations we are usually able to find some functions
fand bfthat satisfy the required inequalities. This is done by hand through trial and
error. Once we have found such suitable zeros, we try to wiggle them to decrease the
resulting bound (using standard optimization routines fromSciPy), then add more double
zeros to the right of the previous ones and repeat. When we increase the genus for a given
invariant, we restart this procedure but take as input a subset of the double zeros found
for the previous genus.
For sphere packing bounds this optimization scheme over double zeros appears to con-
verge quickly to a unique optimal functionfin each dimension. We have not found this to
be the case for hyperbolic surfaces. One important difference is that for sphere packings,
Cohn and Elkies assume thatfand bfhave the same double zeros and the situation is fairly
symmetric. This is not the case with the Selberg trace formula and the actual optimizers
for our problems appear to have only finitely many zeros in some cases (but not their
Fourier transform). Indeed, imposing more zeros forfusually makes our bounds worse
and the zeros have a tendency to fly off to infinity or collide when we run the optimizer.
The strategy we have described above is the one we use in low genus (or for small systole).
In high genus (or for large systole), our asymptotic bounds are obtained by using special
test functions related to Bessel functions and optimizing over certain parameters.
