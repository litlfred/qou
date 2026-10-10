---
doc_id: arxiv-1001.2933v4
doc_title: "Analytic Continuation Of Chern-Simons Theory"
section_id: sec-008-2-7-other-real-forms
section_title: "Other Real Forms"
section_number: "2.7"
pages: 20-23
source_pdf: 1001.2933v4.pdf.txt
source_sha256: b02636c86d593c02
toc_source: inferred
---
2.7 Other Real Forms
Let H′ be a noncompact real form of the complex Lie group G = HC. (For example, if
H = SU(2), H′ might be SL(2, R).) We sometimes describe this more briefly by calling H′
a noncompact real form of H. Chern-Simons theory with gauge group H′is formally defined
by the familiar sort of integral
ZH′(k
′
) = Z
U′
DA′exp(ik′W(A
′
)), (2.32)
where now A′is a connection on an H′ bundle E′ → M and U
′
is the space of such connections, up to gauge transformation.
Since the complexification of H′is simply G = HC, the complexification of U
′
is the
familiar space UC of complex-valued connections. Consequently, U
′
can be viewed as an integration cycle in UC on which the usual Chern-Simons integral is an (oscillatory) convergent
integral. In this respect, it is no different from U, the space of connections modulo gauge
transformations for the compact Lie group H. Either U or U
′
can be regarded as a possible
integration cycle in UC for the Chern-Simons path integral. (U and U
′ are both fixed points
of real involutions acting on UC, as explained more fully in section 2.7.1.) As such, each can
be expressed as a linear combination of the usual Lefschetz thimbles Jσ.
Hence, the framework for analytic continuation of ZH′(k
′
) is the same as the framework
for analytic continuation of ZH(k). We seek to expand it as a linear combination with integer
coefficients of the functions ZH,σ(k) of eqn. (2.23):
ZH′(k
′
) = X
σ
n
′
σZH,σ(k). (2.33)
20

(The coefficients n
′
σ will have to jump in the usual way in crossing Stokes lines.) However,
there is a subtlety in the relation between the parameters in ZH′(k
′
) and ZH(k). This relation
is not k
′ = k but
k
′ + h′ = k + h, (2.34)
where h
′
is a constant6that has been computed in different ways [48, 50]. Like (2.28),
which can actually be viewed as a special case, (2.34) arises from a comparison between
the complexification of the integration measures used in defining ZH and ZH′. It is further
discussed in section 2.7.1.
Just as in the discussion of analytic continuation of ZH(k), we wish to pick a linear
combination of critical point cycles so that the formula (2.33) will agree with ZH′(k
′
) for
k
′ ∈ Z. The general analysis of this is similar to what it is for the case of compact gauge
group, but again there is some simplification for the case of a knot in S
3
. If we label
our knot by a finite-dimensional irreducible representation of H′(as opposed to a unitary
representation of H′, which would be infinite-dimensional), then it is natural to pick the same
integration cycle that we used in analytically continuing ZH(K, k). With the identification
of parameters k
′ + h′ = k + h, this leads to ZH′(K, k′
) = ZH(K, k). That relationship is
already known in perturbation theory, which is insensitive to the difference between H and
H′(except for a one-loop shift in the parameters [48]). That fact motivates our choice of
cycle.
Our discussion in section 2.6.1 can be viewed as a special case of this, since G = HC is
a noncompact real form of the compact Lie group H × H. The properties of Chern-Simons
theory with compact gauge group that we have used do not depend on whether the gauge
group is simple, so they hold for H × H.
2.7.1 Comparison Of Holomorphic Volume Forms
We will now briefly provide a context for eqn. (2.34).
The complex Lie group G = HC admits two real involutions that are important here: one
leaves fixed H and one leaves fixed H′. Similarly, writing hC, h, and h
′
for the Lie algebras of
HC, H, and H′, the space UC of hC-valued connections modulo gauge transformation admits
two relevant real involutions: one leaves fixed the space U of h-valued connections modulo
gauge transformations, and one leaves fixed the space U
′
of h
′
-valued connections modulo
gauge transformations.
6Decompose the Lie algebra of H′ as h′ = k ⊕ p, where k is the Lie algebra of a maximal compact
subgroup of H′, and p is its orthocomplement. After defining the dual Coxeter number h as the trace in h
′
of the square of a suitable element of h
′
, write h = h+ + h−, where h+ and h− come from traces in k and p,
respectively. Then h
′ = h+ − h−.
21

Accordingly, the complexification of either U or U
′ gives the same space UC. Now let
DA and DA′ be the path integral measures for the theories with gauge groups H and H′,
respectively. Either one of these can be analytically continued to a holomorphic volume
form on UC; we denote these holomorphic forms simply as DA and DA′. Our discussion of
analytic continuation has concerned the integration of these volume forms over various real
cycles in UC (or more precisely the integration of their pullbacks to the universal cover UbC
over cycles in UbC).
DA and DA′ are holomorphic volume forms on the same space, so their ratio is an
invertible holomorphic function of the complexified connection A. The relationship is
DA = DA′exp(i(h − h
′
)W(A)). (2.35)
This relationship is computed in [48] by comparing η-invariants for the theories with gauge
group H and H′. A different language is used there and in most of the literature. In this
language, a one-loop correction (coming from the η-invariant) shifts the effective ChernSimons coupling of the H theory by h and that of the H′
theory by h
′
. The ratio of the two
statements is (2.35).
The relation (2.34) is an immediate consequence of (2.35). Similarly (2.28) reflects the
fact that the ratio between the holomorphic volume forms on UC that we have called DA
and DA is
DA = DA exp(ihW(A)). (2.36)
Alternatively, (2.28) is the special case of (2.34) for G = HC regarded as a noncompact real
form of the compact Lie group H × H.
A finite-dimensional analog of the problem of comparing such holomorphic volume forms
would involve a complex manifold X with two different real structures. For example, X
could be the complex x-plane, with two real structures determined by the involutions x → x
and x → −x. If we set x = u + iv, the fixed set of the first involution is the u axis U, with
real volume form du, and the fixed point of the second is the v axis U
′
, with real volume
form dv. On the other hand, on X we have the natural holomorphic one-form dx = du+idv.
The analytic continuation of du from U to X is dx, and the analytic continuation of dv is
−idx. So the relation between the two analytically continued volume forms is dv = −idu.
In the context of the infinite-dimensional Chern-Simons path integral, such a comparison
between volume forms leads to an η invariant, as explained in [48, 51], and this η invariant
can be expressed in terms of the Chern-Simons function.
22






 























Re λ
C1
C2 C3
Figure 1: The complex λ plane, with the real axis from left to right. The hatched regions are the
three “good” regions in which the Airy integrand vanishes at infinity. The contour Ci, i = 1, 2, 3,
connects the i
th good region to the i + 1th
.
