---
doc_id: arxiv-1808.02836v2
doc_title: "On minimal ideal triangulations of cusped hyperbolic 3–manifolds"
section_id: sec-016-33-combinatorial-bounds-for-triangulations
section_title: "Combinatorial bounds for triangulations"
section_number: 3.3
pages: 18-19
source_pdf: 1808.02836v2.pdf
source_sha256: 0224a296253122a2
---
The set-up and notation of the previous subsection is continued. Let
nqtt(T ) = number of tetrahedra of type ∆qtt,
nqq(T ) = number of tetrahedra of type ∆qq,
ntt(T ) = number of tetrahedra of type ∆tt,
n/ 0(T ) = number of tetrahedra of type ∆/ 0,
nqqq(T ) = number of tetrahedra of type ∆qqq,
e(T ) = number of 0–even edges,
˜e(T ) = number of preimages of 0–even edges in~∆.
18
The number of tetrahedra in T is
|T| = nqtt(T ) +nqq(T ) +ntt(T ) +n/ 0(T ) +nqqq(T ).
For the remainder of this subsection, we write nqtt = nqtt(T ), etc.
Let ˆK be the complex in T spanned by all 0–even edges (i.e., the complex of all edges, faces and tetrahedra
of T containing only 0–even edges) and let K be the ideal complex obtained from ˆK by removing its vertices.
Let N be a small regular neighbourhood of K. Then ∂N is a normal surface; it meets each tetrahedron in
the same number and types of normal discs as Sϕ1∪ Sϕ2∪ Sϕ3 except for the tetrahedra of type ∆qqq, which
it meets in four distinct normal triangle types instead of three distinct normal quadrilateral types. The normal
coordinate of ∂N is thus obtained by taking the sum of the normal coordinates ofSϕ1, Sϕ2, and Sϕ3, and adding
to this the tetrahedral solution of each tetrahedron of type ∆qqq. (The tetrahedral solution is obtained by adding
all triangle coordinates of a tetrahedron and subtracting all quadrilateral coordinates; see, for instance, [23,
Section], or [36, Section 2.8]. Each tetrahedral solution has both positive and negative coordinates.) Hence
χ(Sϕ1) + χ(Sϕ2) + χ(Sϕ3) +nqqq = χ(∂N) = 2χ(N) = 2χ(K) =−2e + ntt + 2n/ 0,
where the rightmost equality is a consequence of the following computation: By deﬁnition, the Euler charac-
teristic of K equals minus the number of 0–even edges plus the number of triangles with only 0–even edges
minus the number of tetrahedra of type ∆/ 0(note that K is ideal and hence has no vertices). Since every triangle
occurs in exactly two tetrahedra, every tetrahedron of type ∆tt accounts for one half of a triangle with 0–even
edges and every tetrahedron of type ∆/ 0accounts for two triangles of 0–even edges. Hence, in total we have
χ(K) =−e + 1
2ntt + 2n/ 0− n/ 0=−e + 1
2ntt + n/ 0.
In particular, χ(Sϕ1) + χ(Sϕ2) + χ(Sϕ3) +nqqq is even. Rearranging the above equality gives
ntt + 2n/ 0− nqqq = 2e + χ(Sϕ1) + χ(Sϕ2) + χ(Sϕ3), (3.1)
and hence:
˜e = nqtt + 2nqq + 3ntt + 6n/ 0
= 2|T|− nqtt + ntt + 4n/ 0− 2nqqq
= 2|T|− nqtt− ntt + 4e + 2(χ(Sϕ1) + χ(Sϕ2) + χ(Sϕ3)). (3.2)
Lemma 14 Let M be a cusped hyperbolic 3–manifold of ﬁnite volume, and suppose thatϕ1, ϕ2∈ H1(ˆM,ˆM(0); Z2)
are non–trivial classes with ϕ1 + ϕ2 = ϕ3⁄= 0. Let T be a minimal triangulation, Sϕi be the canonical surface
dual to ϕi, and let ed denote the number of 0–even edges of degree d. Then
e3 = nqtt + ntt− 2(|T| + χ(Sϕ1) + χ(Sϕ2) + χ(Sϕ3)) +
∞
∑
d=5
(d− 4)ed. (3.3)
Proof Lemmata 8 and 9 imply that the smallest degree of an edge in T is three. One has ˜e = ∑ded and
e = ∑ ed. Inserting this into Equation (3.2) yields the desired equality.
