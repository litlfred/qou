---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes"
section_id: sec-005-71-relative-complexity-of-unitaries
section_title: "Relative Complexity of Unitaries"
section_number: 7.1
pages: 14-16
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to Spacetime.” The"
---
The standard inner product metric for unitaries is similar to the inner product metric
for states. In fact if we think of unitaries as the wave functions of maximally entangled
systems then it is the inner product for such states. The inner product distance between
U and V is,
d(UV ) = arccos |TrU†V| (7.15)
where Tr means the normalized trace deﬁned so that TrI = 1. For the same reasons that
I discussed earlier, the inner product distance is not a useful measure of how diﬃcult it is
to go from U to V by small steps. A much better measure is relative complexity.
Given two unitaries the relative complexityC(U,V ) is deﬁned as the minimum number of
gates (in the allowed gate set) satisfying,
U =gngn−1....g1V (7.16)
to within tolerance ϵ. The relative complexity of U and the identity may be deﬁned to be
13
the complexity of U.
C(U)≡C (U,I ). (7.17)
Figure 6 shows how the relative complexity can be thought of in terms of a discrete
curve from V to U.
Figure 6: Relative-C
Because the curve deﬁning C(U,V ) is the shortest such path, we can think of it as a
geodesic, but NOT a geodesic with respect to the inner product metric. It is a geodesic
with respect to relative complexity. The geometry deﬁned by relative complexity is very
diﬀerent from the geometry deﬁned by the inner product distance.
Relative complexity is a metric
Relative complexity satisﬁes the four deﬁning conditions to be a metric.
1.C≥ 0.
2.C(U,V ) = 0 iﬀ U = V
14
3.C(U,V ) =C(V,U )
4.C(U,V )≤C (V,W ) +C(W,V ) (Triangle Inequality)
In fact it is a particular kind of metric called right-invariant.
Suppose that
U = (gngn−1.......g1) V (7.18)
Then for any W it follows that,
UW = (gngn−1.......g1) VW. (7.19)
In other words the relative complexity of U and V is the same as that of UW and VW.
C(U,V ) =C(UW,VW ) (all W ) (7.20)
This is what it means for C to be right-invariant.
On the other hand if we multiply from the left,
WU = (Wgngn−1.......g1W†) WV. (7.21)
But (Wgngn−1.......g1W†) generally is not a product of n allowed gates. ThereforeC is not
left-invariant5.
It should be obvious from these remarks that quantum complexity is really a branch of
geometry—right-invariant geometry6
Most of the mathematical literature on the subject is about left-invariant geometry but
of course this is just a matter of convention.
