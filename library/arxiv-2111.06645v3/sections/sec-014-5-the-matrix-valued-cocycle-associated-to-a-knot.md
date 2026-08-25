---
doc_id: arxiv-2111.06645v3
doc_title: ""
section_id: sec-014-5-the-matrix-valued-cocycle-associated-to-a-knot
section_title: "The matrix-valued cocycle associated to a knot"
section_number: 5
pages: 30-31
source_pdf: 2111.06645v3.pdf
source_sha256: 2a4826bd1c2f0823
doc_brief: "Knots, Perturbative Series and Quantum Modularity — We introduce an invariant of a hyperbolic knot which is a map α7→ Φα(h) from Q/Z to matrices with entries in Q[[h]] and with rows and columns"
---
Let us define, for a fixed knot K (suppressed from the notation as usual), matrix γ∈ SL2(Z)
and number x∈ Q ∖

γ−1(∞)
	
, an (r + 1)× (r + 1) matrix Wγ(x) by
Wγ(x) = J(γx)−1ejγ(x)J(x), (5.1)
whereej is the automorphy factor defined in (4.14). (This formula makes sense because the
matrix J is conjecturally invertible, and even unimodular, as discussed in (5.8) below.) This
function has remarkable properties. On the one hand, the refined quantum modularity conjecture
as presented above can now be rewritten as the asymptotic statement
Wγ(X)≈ bΦa/c
 2πi
c(cX +d)
−1
(5.2)
for X∈ Q tending to infinity with bounded denominator. In particular, unlike the completely
discontinuous function J(x) in terms of which it is defined, Wγ(X) has an asymptotic behavior
at infinity that depends only on X as a real number and not on its numerator and denomi-
nator separately, and in Section 5.2 we will present very strong evidence that this is true not
only asymptotically at infinity, but also for finite values of the argument, so that Wγ(x) be-
comes a smooth (and in fact real analytic) function of its argument away from the singularity
at x =γ−1(∞). On the other hand, the cocycle property (4.15) of ej immediately implies that
Knots, Perturbative Series and Quantum Modularity 31
the function γ7→Wγ(·) is a cocycle for the group PSL 2(Z) acting on the multiplicative group of
almost-everywhere-defined invertible matrix-valued functions on P1(Q), meaning that it satisfies
Wγγ′(x) =Wγ(γ′x)Wγ′(x) (5.3)
for all γ and γ′ in PSL2(Z). But this cocycle property then immediately extends by continuity
to imply that Wγ on R is also a PSL 2(Z)-cocycle, but now in the space of piecewise smooth
matrix-valued functions on P1(R). We can then use the smoothness to define a canonical lift of
each of the formal power series Φ (σ,σ′)
α (h) to an actual function of h, simply by requiring (5.2)
to be an exact rather than merely an asymptotic equality.
These various properties will be described in detail in this section. The first subsection treats
the elementary properties (behavior under complex conjugation, determinant, and inverse) of
the matrices J(x) andWγ(x). The discussion of the smoothness properties and the lifting of the
perturbative series Φ(σ,σ′)
α (h) to well-defined functions ofh will be given in Section 5.2, while the
brief final subsection treats the expected equality between the cocycle Wγ(x) and the cocycle
constructed in the companion paper [44] using state integrals, which gives the real explanation
for its smoothness and even analyticity.
