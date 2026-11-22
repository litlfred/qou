---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-009-a-vector-valued-rkhs-matrix-valued-kernels
section_title: "Vector-Valued RKHS (Matrix-Valued Kernels)"
section_number: A
pages: 5-5
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
Unlike the original RKHS theory, where the elements
of the feature space are (scalar) real-valued functions,
the
feature
space
can
be
constructed
using
the
basis
{(x) : X −→Rn, x ∈X}, therefore yielding a vector-valued
RKHS (VRKHS) with matrix-valued reproducing kernels
K(x, y) =  H(x)(y) ∈Rn×n. The VRKHS theory was
introduced in [39] and [40], and recent results exploiting this
concept includes multi-category classiﬁcation and multivariate
regression [19], [20].
The matrix-valued kernel concept is particularly useful in
multivariate regression, whereby the desired output is vector-
valued. For illustration, consider the problem of learning the
mapping y = f (x) ∈Rn, using3 ˆy =  H(x)M where (·)
forms the basis of the VRKHS HV . Following the classic
kernel regression paradigm, M can be approximated accord-
ing to the signal subspace principle [41], and the available
measurements {(xi, yi)}i=1:N , by 
M = N
i=1 (xi)Ai, where
the (vector) weights {Ai}i=1:N ⊂Rn are set according to the
chosen optimisation criteria. Consequently, the estimate can
be expressed as
ˆy =
N

i=1
 H(x)(xi)Ai =
N

i=1
K(x, xi)Ai
where (·)H denotes the conjugate transpose (Hermitian) oper-
ator and K(x, xi) ∈Rn×n and Ai ∈Rn×1.
The vector-valued RKHS is physically meaningful in that it
assumes that the dimensionality of the feature space is given
by the dimensionality of the output of the regression problem.
However, the matrix-valued nature of the resulting kernels hin-
ders the implementation of multichannel regression, because
both the number of kernel evaluations and multiplications grow
quadratically with the size of the output vector. Indeed, as
the kernel K(xi, x) is symmetric, it contains (n2+n)
2
different
entries and the product K(xi, x)Ai involves n2 multiplications.
The fact that, within matrix-valued kernel regression, the
dimension of the feature space is dictated by the dimension of
the output contradicts the fundamental concept of using feature
spaces (of a different dimension) to explain the observed
relationship in the data. See Table I for the computational
complexity of other higher-dimensional kernel algorithms.
We next review another real-valued higher dimensional
approach for kernel regression, referred to as multikernel or
vector kernel, which allows for the use of multiple kernels.
As desired, the dimensionality of the vector kernel is set as a
design parameter, and does not depend on the the number of
channels of the input/output data.
