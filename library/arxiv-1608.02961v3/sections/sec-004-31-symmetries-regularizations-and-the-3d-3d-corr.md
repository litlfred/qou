---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte"
section_id: sec-004-31-symmetries-regularizations-and-the-3d-3d-corr
section_title: "Symmetries, regularizations, and the 3d-3d correspondence"
section_number: 3.1
pages: 12-13
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
In principle, the 3d-3d correspondence itself may suﬃce to resolve the diﬃculties with cutting
and gluing in complex Chern-Simons theory. 6 The correspondence assigns to a closed 3-
manifold M and a Lie algebra g of type ADE (and a bit of extra discrete data) a three-
dimensional ﬁeld theory TG[M] with the property that that
partition function of TG[M] on squashed lens space L(k, 1)b
=GC Chern-Simons partition functionZ[M]k,s with is =k 1−b2
1+b2 . (3.3)
where g = Lie(G). When GC = SL(N, C), the theory TGC[M] is the eﬀective low-energy
worldvolume theory of N M5 branes compactiﬁed on M; the branes wrap M× R3 in the
M-theory geometry T∗M× R5. Similarly, the correspondence assigns to a three-manifold
M with boundary Σ a boundary condition TG[M] for the four-dimensional theory TG[Σ] of
classS [62, 63].
Typically TG[M] is an N = 2 superconformal theory, though both supersymmetry and
conformal invariance might be broken. Unfortunately, it is not completely understood what
conditions on M guaranteeN = 2 superconformal theories. We assume for the present
heuristic argument that we do haveN = 2 superconformal theories.
The basic idea, then, would be to replace GC Chern-Simons theory on M with TGC[M],
which is a much more powerful object. Even when the Chern-Simons partition functions
Z[M]k,s (equivalently, lens-space partition functions of TG[M]) are ill-deﬁned, the theory
TG[M] itself should still make sense. Moreover, the theories TG[M] obey cutting and gluing
rules. Gluing M =N1∪ΣN2 corresponds to “sandwiching” the four-dimensional theoryTG[Σ]
between boundary conditions TG[N1] and TG[N2], and colliding the boundaries together to
produce a new eﬀective theory TG[N1∪Σ N2]. In this way, we reproduce the structure
of a three-dimensional TQFT. If we should ever want to recover Chern-Simons partition
functions, we just place the superconformal theories on a lens space L(k, 1)b.
There are two practical diﬃculties with this proposal that will hopefully be overcome
soon. First, the full theories TG[M] are not actually known for most manifolds, for any
nonabelian G. A construction using ideal triangulations was outlined in [14, 38] (also [64,
65]); however, that construction produces subsectors of the full theories TG[M] that are
missing some branches of vacua, the same way partition functions of Chern-Simons theory on
hyperbolic manifolds are “missing” abelian ﬂat connections. Examples of complete theories
TG[M] for a handful of manifolds (including a hyperbolic one) were postulated in [44], and
theories for lens spaces M =L(p,r ) were studied in [44, 23, 24].
The second diﬃculty, or potential shortcoming, is that zeroes and inﬁnities still remain
in the actual Chern-Simons partition functions. Here, however, another solution presents
itself: the theories TG[M] often have extra symmetries; and parameters associated to these
symmetries (twisted masses or fugacities) can be used to reﬁne the squashed-lens-space
L(k, 1)b partition functions of TG[M] — thus literally regularizing the Chern-Simons zeroes
and inﬁnities.
6We will not review the 3d-3d correspondence here. For recent reviews and discussions, especially in the
context of Chern-Simons theory and TQFT, see [60, 44, 23, 24] as well as the related [61].
12
We already met one such symmetry in Section 2.1: the U(1)t that gave an equivariant
quantization of the Hilbert spaceH[Σ]k,s=0. Via the 3d-3d correspondence, this Hilbert space
is mapped to the BPS Hilbert space of the 4d class- S theory TG[Σ] on R×L(k, 1)b=1. This
4d theory has an additional R-symmetry U(1)t that commutes with the supercharge used to
deﬁne the “BPS” Hilbert space, and provides the U(1)t grading.
Similarly, the three-dimensional theory TG[Σ×S1] (obtained by compactifying TG[Σ] on
a circle) has N = 4 rather than N = 2 supersymmetry. The larger R-symmetry group of
theN = 4 theory contains U(1)t, and including its twisted mass in partition functions leads
to ﬁnite answers that encapsulate the graded dimension (2.23).
Theories TG[M] for Seifert-ﬁbered three-manifolds M should also retain this U(1)t sym-
metry. In this case, it can ultimately be traced back to an exceptional isometry 7 of the
M-theory geometry T∗M× R5. An simple example of such a manifold is a lens space
M =L(p,r ), whose reﬁned partition functions were analyzed in [24], and put precisely into
the factorized form (3.1) — with the factors 1 /|Stab(α)| = 1/∞ now regularized.
When M is generic ( e.g. hyperbolic) this exceptional U(1)t symmetry is, unfortunately,
absent. It was nevertheless proposed in [44] that there exists yet another symmetry U(1)t′
in any theory TG[M], related to the standard U(1) R-symmetry of three-dimensionalN = 2
theories — as well as to categoriﬁcation of colored knot polynomials. This U(1)t′ was used to
regularize Chern-Simons partition functions for the trefoil and ﬁgure-eight knot complements
(Seifert-ﬁbered and hyperbolic manifolds, respectively), producing sums of the form (3.1)
that included all ﬂat connections, even abelian ones.
