---
doc_id: arxiv-2111.06645v3
doc_title: ""
section_id: sec-034-102-optimal-truncation-and-smoothed-optimal-trun
section_title: "Optimal truncation and smoothed optimal truncation"
section_number: 10.2
pages: 74-75
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α7→ Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
One of the main numerical aspects concerns smoothed optimal truncation, which was originally
an appendix to an earlier draft of this paper but has now been relegated to a planned independent
publication [45] because the methods are applicable to many problems outside the realm of
quantum topology. This is a method for the numerical summation of factorially divergent series
when only a finite number of coefficients are known and we do not have information about the
possible analytic continuation of the Borel transform, which is the method usually used.
We already explained in Section 4.1 the naive optimal truncation, Φ( h)opt of a factorially
divergent series Φ(h) = P∞
n=0Anhn, defined simply as PN
n=0Anhn where N is the approxi-
mate value of n at which the term Anhn takes on its minimum absolute value, given explicitly
by N =|B/h| if An grows like n!B−n. The idea of smoothed optimal truncation is very sim-
ply to replace Φ(h)opt by a “smoothed” version Φ(h)smooth which is defined as Φ(h)opt +εN(h)
where the exponentially small correction term εN(h) depends on the cutoff parameter N in such
a way that Φ(h)smooth does not jump when one changes N by 1. This means simply that we
requireεN−1(h)−εN(h) =Anhn. Of course, if we knew how to solve this equation exactly, then
the function Φ(h)smooth would be completely independent of N and would give us a canonical
way to lift the power series Φ(h) to an actual function. This is not the case, but ifAn has a known
asymptotic expansion, which is true for all of the series in this paper (see Section 3.4) then we
can define εN(h) asymptotically as the product of e−N and a power series in 1/n chosen in such
a way that the desired equality εN−1(h)−εN(h) = Anhn is true asymptotically to all orders
in 1/n. The details of how to do this if An has the asymptotic form B−nP∞
ℓ=0cℓΓ(n +κ−ℓ) for
some real number κ and some numerical coefficients cℓ (as in equations (3.16), (3.17) or (3.18))
are given in [45] and will not be repeated here. The only thing that is of importance to us here
is that the result of the smoothing gives an evaluation of Φ(h) that is independent of all choices
(and hence gives a predicted “right” definition of the corresponding function) up to an error
that is exponentially small with a better exponent than that given by naive optimal truncation.
Specifically, the new error is e−N(1+|C|)−N rather than simply e−N as before if, as is always the
case for us, the coefficients cℓ themselves grow factorially like ℓ!C−ℓ. Examples of this dramatic
numerical improvement were given in Section 4.3, where in one case the error in evaluating
Knots, Perturbative Series and Quantum Modularity 75
a series Φ(h) was of the order of 10−29 using naive optimal truncation but of the order of 10−56
using smoothed optimal truncation.
