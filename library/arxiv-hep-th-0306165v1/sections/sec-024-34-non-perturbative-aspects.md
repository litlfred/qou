---
doc_id: arxiv-hep-th-0306165v1
doc_title: "which has many interesting connections with three-dimensi onal quantum gravity and ge- ometry of hyperbolic 3-manifolds. We show that, in the prese nce of a single knotted Wilson l"
section_id: sec-024-34-non-perturbative-aspects
section_title: "Non-perturbative Aspects"
section_number: 3.4
pages: 31-34
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting connections with three-dimensi onal quantum gravity"
---
We found the semi-classical expression for the partition fu nction Z(M ) and brieﬂy
discussed higher-order perturbative corrections. Howeve r, using the eﬀective quantum
mechanics one might hope to compute the entire series Z(M ), say, using the technique of
the geometric quantization [59,60,61,62,63]. The semi-cl assical result (3.34) is simply the
leading order approximation to the exact expression for Z(M ), which obeys
ˆAZ = 0 (3 .40)
In quantum theory, this operator equation represents the cl assical constraint A(l,m ) = 0,
cf. e.g. (3.15). Namely, the operator ˆA is obtained from the A-polynomial by replacing
l and m with the corresponding operators, ˆl and ˆm, whose commutation relations follow
from (3.5). We also note that Z(M ) automatically satisﬁes the Hamiltonian constraint,
ˆHZ = 0, which can be naturally interpreted as the Wheeler-DeWit t equation (1.11) in
three-dimensional Euclidean gravity.
As we explain in the later sections, the asymptotic behavior of the colored Jones
polynomial is very similar to the perturbative expansion (3 .38) – (3.39). This suggests a
close connection between the exact, non-perturbative part ition function of the SL(2,C)
Chern-Simons theory and a certain analytic continuation of the colored Jones polynomial,
Z(M )←→? JN (K,q ) (3 .41)
In particular, it is natural to speculate that the colored Jo nes polynomial is related to
the SL(2,C) partition function when the variable q is not a root of unity, cf. Table 1. A
further evidence for this relation comes from the recent wor k [69], where it was shown that
the colored Jones polynomial for certain knots obeys the q-diﬀerence equation (3.40). We
postpone further study of the expected relation (3.41) to fu ture work.
+M M_
Σ
Fig. 8: The manifold M is a connected sum of the 3-manifolds M+ and M−, joined
along their common boundary Σ.
30
The non-perturbative partition function Z(M ) has a number of nice properties that
follow directly from the path integral formulation (1.4). S uppose, for example, that M is a
connected sum of the 3-manifolds, M±, joined along the common sphere boundary Σ = S2
(see ﬁg. 8):
M =M+∪Σ M− (3.42)
Then, the Chern-Simons partition function Z(M ) is given by
Z(M ) = Z(M+)×Z(M−)
Z(S3) (3.43)
where Z(S3) denotes the partition function for a 3-sphere.
Similarly, one can compute Z(M ) for a homology 3-sphere M represented as a union
(3.42) of M+ and M− joined along a common torus boundary, Σ = T 2. Following the
discussion in section 2, to each M± we can associate a representation variety (the zero
locus of the corresponding A-polynomial):
L± = Hom (π1(M±);SL(2,C))/SL(2,C)
Moreover, sinceM± are 3-manifolds with a common torus boundary Σ = T 2, the inclusions
of Σ into M± induce the embeddings:
L±֒→C∗× C∗ = Hom (π1(Σ); SL(2,C))/SL(2,C)
The intersection points of L+ andL− are in one-to-one correspondence with the conjugacy
classes of representations of the fundamental group π1(M ) into SL(2,C). Therefore, we
expect that the partition function
Z(M ) =⟨Z(M+)|Z(M−)⟩ (3.44)
is dominated by the contribution from the intersection poin ts of L+ and L−.
The above discussion is reminiscent of the deﬁnition of the C asson invariant [70,71].
Indeed, using the A-polynomial we can deﬁne (and in many case s easily compute) the
SL(2,C) Casson invariant of M as the weighted sum of the intersection points of L+ and
L− inside C∗× C∗,
λSL(2, C)(M ) = #(L+∩L−) (3 .45)
31
Example. M = S3
Consider M = S3 with the standard Heegard splitting, M = M+ ∪Σ M−, where
Σ = T 2 and each M± is a copy of the solid torus. Since the boundaries of M± are glued
together with a relative SL(2, Z Z)-transformation,
(
γl
γm
)
− →
(
0 −1
1 0
)(
γl
γm
)
from (2.16) and (2.22) we get:
L+ = l − 1 , L − = m − 1
Clearly, the curves L+ and L− intersect at a single point, m = l = 1, so that we ﬁnd
the SL(2,C) Casson invariant λSL(2, C)(S3) = 1.
It would be interesting to ﬁnd a realization of the SL(2,C) Casson invariant in Chern-
Simons theory with fermionic symmetries, cf. [16].
Finally, let us point out that throughout the paper we mainly focus on the simplest case
of a single torus boundary, or a single Wilson loop W(l,m )(K). It would be interesting to
extend this discussion to links with several components and three-manifolds with arbitrary
boundary Σ (such generalizations will be brieﬂy discussed i n the next section). In a special
case, when a link consists of r unlinked components γk, we have:
Z(S3;γ1,R 1,...,γ r,R r)
Z(S3) =
r∏
k=1
Z(S3;γk,R k)
Z(S3) (3.46)
Suppose that r = 2 and R1 =R2, i.e. we have two oriented unlinked components, γ1 and
γ2, carrying the same representation R. Then, from the path integral formulation (1.4), it
follows that the partition function for the connected sum γ1#γ2 is related to the product
of the partition functions for the individual link componen ts,
Z(S3;γ1#γ2,R ) = Z(S3;γ1,R )×Z(S3;γ2,R )
Z(S3; unknot,R ) (3.47)
This factorization formula also follows from the property g) of the A-polynomial listed in
section 2.3.
32
