---
doc_id: arxiv-math-0110009v3
doc_title: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003"
section_id: sec-010-appendix-a-technicalities-about-density
section_title: "Technicalities about density"
section_number: Appendix A
pages: 20-21
source_pdf: 0110009v3.pdf
source_sha256: bb0c97f2de33b0dd
toc_source: inferred
doc_brief: "arXiv:math/0110009v3 [math.MG] 3 Sep 2003 — We develop an analogue for sphere packing of the linear programming bounds for error-correcting codes, and use it to prove upper bounds for the density of"
---
In this appendix, we provide precise statements and references for what it
means for a packing to have a density and whether there is a maximally dense
packing. Much of our discussion closely follows Section I of [K].
Let P be any sphere packing in Rn. We say that P has density ∆if for
all p ∈Rn, we have
∆= lim
r→∞
vol(B(p, r) ∩P)
vol B(p, r)
,
where B(p, r) is the ball of radius r centered at p, and B(p, r) ∩P consists of
those parts of the balls in P that lie within B(p, r). It is proved in [Gr] that
if this limit exists for one p, then it exists for all p and is equal for all p. We
say that the packing has uniform density if the limit exists uniformly for all p.
In that case, [Gr] shows that for every compact set R that is the closure of its
interior and every point p,
∆= lim
r→∞
vol((rR + p) ∩P)
vol rR
,
where of course rR + p denotes R scaled by a factor of r and translated by p.
NEW UPPER BOUNDS ON SPHERE PACKINGS I
709
Although not every packing has a density, every packing has an upper
density, deﬁned by
∆= lim sup
r→∞
sup
p∈Rn
vol(B(p, r) ∩P)
vol B(p, r)
.
It is proved in [Gr] that the supremum of all upper densities is achieved by a
uniformly dense packing.
Periodic packings are the most convenient ones for our purposes. Using the
above results, it is easy to see that they come arbitrarily close to the greatest
possible density, as follows. Suppose ∆is the maximum packing density in Rn,
and let P be a uniformly dense packing of density ∆. Let R be the fundamental
parallelotope of any lattice Λ ⊂Rn. We know that
∆= lim
r→∞
vol(rR ∩P)
vol rR
.
Let ε > 0. If we choose r large enough, then the total volume of the spheres
in P that lie entirely within rR is within ε vol rR of ∆vol rR, because only
a negligible fraction of the spheres can intersect the sides of rR.
Deﬁne a
periodic packing P′ by taking all the spheres of P that lie entirely within rR,
and also including all translations of them by rΛ. Then this periodic packing
has density at least ∆−ε.
