---
doc_id: arxiv-2601.05136v2
doc_title: "State integrals for the quantized SL 2 ( C ) Chern-Simons invariant"
section_id: sec-010-the-action-and-state-sums
section_title: "The action and state sums"
section_number: null
pages: 9-10
source_pdf: 2601.05136v2.pdf
source_sha256: cee15456257d3028
toc_source: outline
---
Following [McP25a, Section 6] we deﬁne the action functional of a diagram. Consider the functions
(3.4)
Ω+
N(µ|t1, t2, t3, t4) := ϕN(t4 −t1) + ϕN(t2 −t3)
−ϕN(t2 −t1 −µ/N + 1 −1/N) −ϕN(t4 −t3 + µ/N)
−2πiµ(t2 + t3 −t1 −t4 −µ/N)
Ω−
N(µ|t1, t2, t3, t4) := −ϕN(t1 −t4 + 1 −1/N) −ϕN(t3 −t2 + 1 −1/N)
+ ϕN(t1 −t2 + µ/N) + ϕN(t3 −t4 −µ/N + 1 −1/N)
+ 2πiµ(t2 + t3 −t1 −t4 −µ/N)
These are logarithmic versions of the braiding kernels of [McP25a, Section 5]. As discussed there
t 7→exp Ωϵ
N(µ|t) is a quasi-periodic function of each ti. The periodicity constants are related to
the segment equations of Section 2.3, i.e. to the gluing equations of the octahedral decomposition.
Fix an oriented framed knot K and an open diagram D of K. Assign each internal segment
a complex variable ti, assign the boundary segments 0, and ﬁx a complex number µ (later, a log-
meridian of K). Construct a function SN(D, µ|t) of the variables ti by taking a sum over crossing
functions
t2
t4
t1
t3
→1
N Ω+
N(µ|t1, t2, t3, t4)
(3.5)
t1
t3
t2
t4
→1
N Ω−
N(µ|t1, t2, t3, t4)
(3.6)
