---
doc_id: 04procbryden
doc_title: "Some computations of Ohtsuki series"
section_id: sec-005-3-computer-calculations-of-ohtsuki-series
section_title: "Computer calculations of Ohtsuki series"
section_number: 3
pages: 9-9
source_pdf: 04procbryden.pdf
source_sha256: 8baffbc6542c34a5
doc_brief: "Some computations of Ohtsuki series — We present some computational data on Ohtsuki series for a two pa- rameter family of integer homology spheres obtained by surgery around what we call ‘2–strand"
---
Using (3), ZK(M ±
(( S
T ))) can be computed for all theK −1 diﬀerent Kth
roots of unity, q = qs = exp 2πis
K (1 ≤ s<K ) for ﬁxed S, T and prime
K. From these values, the coeﬃcients am,K(M ±
(( S
T ))) ∈ Z can be found
in (1) where we assume that they vanish past the ( K − 2)th. Namely,
one solves the following linear system of size K − 1,
ZK |q=qs =
K−2∑
m=0
am,K.(qs − 1)m , (5)
where the dependence on the manifold has been omitted from the no-
tation. The integrality of the solutions provides a check on the errors in
the computations of the individual WRT invariants at diﬀerent roots
of unity.
There a number of computational challenges here.
