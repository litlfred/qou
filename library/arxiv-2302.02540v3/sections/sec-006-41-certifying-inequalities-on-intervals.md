---
doc_id: arxiv-2302.02540v3
doc_title: "Linear programming bounds for hyperbolic surfaces"
section_id: sec-006-41-certifying-inequalities-on-intervals
section_title: "Certifying inequalities on intervals"
section_number: 4.1
pages: 7-8
source_pdf: 2302.02540v3.pdf
source_sha256: 0dfe07df944902ec
toc_source: outline
doc_brief: "Linear programming bounds for hyperbolic surfaces — We adapt linear programming methods from sphere packings to closed hy- perbolic surfaces and obtain new upper bounds on their systole, their"
---
produce our bounds, the end results are rigorous. The reason is that we work with rational
zeros and polynomials with rational coefficients, so the linear systems involved are solved
exactly over the rational numbers. The polynomials we get thus have actual double zeros
rather than approximate ones.
To ascertain thatf(x) =p(x 2)e−x2/2≥0 for everyxin a given interval [a,b], we apply
Sturm’s theorem to count the number of distinct roots ofpin that interval and make sure
that there are no more than the number of imposed double zeros. This implies that neither
pnorfchanges sign on the interval, and it then suffices to check thatpis strictly positive
at some point or that its second derivative is strictly positive at a double zero.
We will also sometimes need to certify inequalities involving transcendental functions
over intervals. In these cases, we approximate the transcendental functions with trun-
cated Taylor series and apply Sturm’s theorem to these approximation. The functions we
consider either have positive or alternating Taylor coefficients, allowing us to know if the
approximations are from below or above.
In some cases, we need to find the minimum of a functionh(x) =r(x)e −x/2 on an
interval [a,b], whereris a polynomial. Sinceh ′(x) = (r′(x)−r(x)/2)e −x/2 we can use
8 MAXIME FORTIER BOURQUE AND BRAM PETRI
Sturm’s theorem to verify thathhas at most one critical point on the interval. If it has
one, then it suffices to verify thatr ′(a)−r(a)/2>0 andr ′(b)−r(b)/2<0 so that the
critical point is a local maximum. The minimum ofhis then at one of the endpoints, and
this is also true if there is no critical point in the interval.
