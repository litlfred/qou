---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-035-c1-symplectic-gluing
section_title: "C.1. Symplectic gluing"
section_number: null
pages: 40-41
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
viewed, both classically and quantum mechanically, as a process of sy mplectic reduction.
Suppose we have a one-cusped manifold M with a triangulationT ={∆ i}N
i=1. Classically,
each tetrahedron ∆ i comes with a phase space
P∂ ∆ i = {ﬂat SL(2, C) connections on ∂∆ i}
≈ {(Zi,Z ′
i,Z ′′
i )∈ C\(2πiZ)|Zi +Z ′
i +Z ′′
i =iπ},(C.1)
with (holomorphic) symplectic structure
(C.2) ω∂ ∆ i =dZ∧dZ′′,
and a Lagrangian submanifold
9
L∆ i = {ﬂat SL(2, C) connections that extend to ∆ i}
= {eZ ′′
+e−Z− 1 = 0} ⊂P∂ ∆ i(C.3)
When gluing the tetrahedra together, we ﬁrst form a product
(C.4) L× =L∆ 1×···L ∆ N ⊂ P × =P∂ ∆ 1×···×P ∂ ∆ N.
The edge constraints XI :=∑ N
i=1
(
GIiZi + G′
IiZ ′
i + G′′
IiZ ′′
i
)
− 2πi from (
2.3) are functions on
the product phase space P×, and can be used as (holomorphic) moment maps to generate
N− 1 independent translation actions tI. Recall [ NZ85] that the logarithmic meridian
and longitude holonomies ( u,v ) are also functions on P×, which Poisson-commute with all
9Explicitly,P∂ ∆ i is a space of ﬂat connections on a 4-punctures sphere with parabo lic holonomy at the
four punctures; while L∆ i is the subspace with trivial holonomy — hence connections that exte nd into the
bulk of the tetrahedron. See, e.g., Section 2 of [ DGG].
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 41
the edges XI, and so are ﬁxed under these translations. Then the phase space of M is a
symplectic quotient,
P∂M = {ﬂat SL(2, C) connections on ∂M≃T 2} ≈ {(u,v )∈ C}
= P×
//
(tI),(C.5)
and the A-polynomial of M (more properly, components of the A-polynomial for which the
triangulation is regular) is the result of pulling the Lagrangian L× through the quotient,
(C.6) LM = “L×
//
(tI)” ≈ {AM (ev,e u) = 0} ⊂ P∂M .
This is quite easy to check using equations (
4.5) and ( 4.6).
