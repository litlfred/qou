---
doc_id: arxiv-1608.02961v3
doc_title: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte"
section_id: sec-001-21-equivariant-quantization
section_title: "Equivariant quantization"
section_number: 2.1
pages: 8-9
source_pdf: 1608.02961v3.pdf
source_sha256: ef3805c23133b8f2
doc_brief: "Perturbative and nonperturbative aspects of complex Chern-Simons Theory Tudor Dimofte — We present an elementary review of some aspects of Chern-Simons theory with complex gauge group SL(N, C)."
---
There are several things to notice about (2.14). Perhaps the most salient is that, unlike
in the case of Chern-Simons theory with compact gauge group [17, 53], the Hilbert space
is inﬁnite-dimensional. This is no surprise, since it comes from quantizing a noncompact
phase space. One may also recognize the C2k factor as being related to the standard Hilbert
space for SU (2) theory at (bare) level k. Indeed, if we ignore µ and consider functions
f(m) of an integer m∈ Z/(2kZ), such that f(m) = f(−m) as in (2.16), we ﬁnd exactly
|k|+1 independent valuesf(0),f (1),...,f (|k|) that determine a state in the ﬁnite-dimensional
Hilbert space of SU (2) Chern-Simons.
What is less obvious, in particular for general Σ, is that the inﬁnite-dimensional Hilbert
space of complex Chern-Simons theory admits an additional U(1)t symmetry, introduced in
[23]. The graded components of H[Σ] ( i.e. the subspaces of ﬁxed U(1)t charge) turn out
to be ﬁnite-dimensional, and in particular the subspace of zero charge is just the familiar
SU (2) Hilbert space.
The extra U(1)t symmetry comes from viewing P[M]≃M Hit(SU (2), Σ) as the Hitchin
moduli space. There is a canonical U(1)t metric isometry of the Hitchin moduli space that
rotates the CP1 of complex structures about an axis. In particular, it rotates ωJ = Im(Ω)
andωK into each other. This is an isometry of our quantization problem at least whens = 0,
8
since it preserves ωk,s=0, and leads to the desired symmetry of H[Σ]k,0. (Since the Hilbert
space, abstractly, does not depend on s, one might then hope to endow even spaces at s⁄= 0
with the symmetry.)
In the case Σ = T 2, it is easy to describe the U(1)t symmetry: when we view P[T 2]≃
T∗(S1×S1)/Z2≈ T∗Mﬂat(SU (2),T 2) as the cotangent bundle of the space of ﬂat SU (2)
connections, U(1)t simply rotates the cotangent ﬁbers. The U(1)t-invariant subspace of
H[T 2]k,s=0 simply consists of the functions f(µ,m ) that are independent of µ — i.e. the
SU (2) Hilbert space we found above. The full U(1)t action is trickier to describe in the
polarization we are using. Roughly, one observes that at s = 0 and b = 1 the variables x, ¯x
can be written as
x =zη−m, ¯x =zηm, (2.22)
where z = exp(πµ/k) and η = exp(iπ/k). Then, on functions of f(z,m ) that are analytic
in z, the U(1)t symmetry just acts as rotations z → eiθz. The subspaces of ﬁxed U(1)t
weight contain monomials in z. After imposing Weyl invariance, the graded dimension of
the Hilbert space becomes
dimU(1)tH[T 2]k,s=0 :=∑
w∈ZtwdimH[T 2]weightw
k,s=0 =|k| + 1 + 2|k|(t +t2 +t3 +...)
=|k| + 1 + 2|k|t
1−t.
(2.23)
