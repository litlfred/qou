---
doc_id: arxiv-math-0410233v4
doc_title: "CUSP SHAPES UNDER CONE DEFORMA TION JESSICA S. PURCELL"
section_id: sec-013-41-convex-combinations-of-deformations
section_title: "Convex combinations of deformations"
section_number: 4.1
pages: 18-19
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "CUSP SHAPES UNDER CONE DEFORMATION JESSICA S. PURCELL — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
to an inﬁnitesimal deformation is the 1–form ω0. We want ω0 to have certain
desired properties.
By equation (4), we can decompose ω0 = (ω0)j in Vj as
(ω0)j = uj ωm + (xj + iyj) ωℓ,
with uj, xj, and yj in R, and where ωm and ωℓ were computed in [13].
In [14], it was shown that if the singular locus has just one co mponent,
then the entire cone deformation can be parameterized by the square of the
cone angle t = α2. In this case, u = u1 was determined explicitly in [14]:
u = −1/(4α2), where α is the cone angle at the core of the singular solid
torus V = V1.
When we have multiple components of the singular locus, we ma y not
necessarily be able to parameterize the cone deformation in this manner.
However, we do have the following information.
First, for each j in {1, . . . , n}, locally we have a deformation given by
changing the j-th cone angle only and leaving the others ﬁxed. This is a
deformation with only one component of the singular locus, s o the methods
of [14] apply, and this deformation can be parameterized by t = α2
j . Then
(ω0)j = − 1
4α2
j
ωm + (xjj + iyjj )ωℓ.
Changing the angle in the j-th tube Vj and leaving the others ﬁxed also
aﬀects the k-th tube Vk. Since there is no change of cone angle in this tube,
(ω0)k can be expressed as
(ω0)k = (xjk + iyjk )ωℓ.
Any of these j deformations may be scaled by a factor sj ≥ 0, and we
may take non-negative linear combinations. These correspo nd to new local
deformations, in which the rates of change of cone angles var y according to
the choice of the sj. In a neighborhood of the j-th component, write:
(22) ( ω0)j = − sj
4α2
j
ωm +
n∑
k=1
(skxkj + i skykj ) ωℓ.
Given a point ¯ s = ( s1, s2, . . . , sn), we may use these equations for ω0
to compute the forms η0 explicitly, and thus compute the boundary terms
bj = bj(¯s) explicitly. Hodgson and Kerckhoﬀ did the calculations wit hout
the extra ¯s (page 382 of [14]). When the ¯ s is put in, we obtain:
(23) bj(¯s)
Area(∂Vj ) = s2
j c +
(
(
∑
k
skxkj )2 + (
∑
k
skykj )2
)
a + sj(
∑
k
skxkj ) b.
Here the terms a, b, and c are constants in terms of R which agree with
those on page 383 of [14]. However, we are not immediately con cerned with
their values. More important, a is always negative, b and c always positive.
From the formula (23) we obtain the following information.
CUSP SHAPES UNDER CONE DEFORMATION 19
(1) bj(¯s) is quadratic in ¯s.
(2) If any sj = 0 for some ¯s, then bj(¯s) ≤ 0.
We also know that the sum of all the bj’s is strictly positive, provided
¯s ⁄= (0 , 0, . . . ,0), by equation (16), as well as the remark right after that
equation. We will use this information in §4.2.
