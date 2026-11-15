---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology"
section_id: sec-069-128-summary
section_title: "Summary"
section_number: 12.8
pages: 408-409
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
toc_source: outline
doc_brief: "An Introduction to Geometric Topology — 86 sections: Front matter; Introduction; Part 1. Hyperbolic geometry"
---
We have proudly completed the proof of Theorem 12.1.1. We state that
theorem again here:
Theorem 12.8.1. A closed orentable 3-manifold has a geometric structure
modelled on one of the following six geometries:
S3, R3, S2 × R, H2 × R, Nil, g
SL2
if and only if it is a Seifert manifold of the appropriate commensurability class,
as prescribed by Table 12.1. It has a Sol geometric structure if and only if it
is a torus (semi-)bundle of Anosov type.
We can deduce that the eight geometries are mutually exclusive:
Proposition 12.8.2. Two closed 3-manifolds admitting diﬀerent geometries
are not diﬀeomorphic, and not even commensurable.
Proof. We already know that the six Seifert geometries form six distinct
commensurability classes. A manifold of type Sol is not Seifert by Proposition
11.4.14. A closed hyperbolic manifold is neither Seifert nor Sol because its
fundamental group is inﬁnite and does not contain an inﬁnite normal abelian
subgroup by Corollary 5.1.10 (as opposite to the other geometries, see Propo-
sition 10.4.3).
Two manifolds having diﬀerent geometries cannot be commensurable,
since a common ﬁnite cover would inherit both geometries.
□
In fact one can tell the geometry of the manifold directly from its funda-
mental group.
Proposition 12.8.3. Let M be a closed manifold modelled on one X of the
eight geometries; this ﬂowchart shows how to determine X from π1(M):
• if π1(M) is ﬁnite, then X = S3; otherwise
• if π1(M) is virtually cyclic, then X = S2 × R; otherwise
• if π1(M) is virtually abelian, then X = R3; otherwise
• if π1(M) is virtually nilpotent, then X = Nil; otherwise
• if π1(M) is virtually solvable, then X = Sol; otherwise
• if π1(M) contains a normal cyclic group K, then:
– if a ﬁnite-index subgroup of the quotient lifts, then X = H2 ×R,
– otherwise X = g
SL2;
• otherwise X = H3.
Proof. The virtually abelian cases were settled in Section 10.3.10. The
Nil and Sol geometries were considered by Corollaries 12.5.8 and 12.7.7.
If X = H2 × R or g
SL2 then π1(M) surjects onto π1(S) for some closed
hyperbolic surface S. This implies that π1(M) is not solvable, for otherwise
