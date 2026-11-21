---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-010-b-multikernel-learning
section_title: "Multikernel Learning"
section_number: B
pages: 5-5
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
The multikernel concept also uses a VRKHS as feature
space and redeﬁnes the inner product [21] so as to only
3For x ∈X, (x) ∈R|X|×n, and the coefﬁcient M ∈R|X|×1, where |X| is
the (possibly inﬁnite) cardinality of X. Observe that R|X|×1 is the space of lin-
ear mappings between the empirical feature space

(x) ∈R|X|×n, x ∈X

and Rn.
preserve the diagonal elements of the matrix-valued prod-
uct  H. This yields a vector-valued kernel −→
K (x, y) =
diag
	
 H(x)(y)

∈RL, where L is the number of sub-
kernels. The regression estimate corresponding to this vector-
valued kernel can be expressed by
ˆy =
N

i=1
AT
i
−→
K (x, xi),
where Ai
∈
RL×n, ˆy
∈
Rn. Additionally, by denot-
ing the entries of the vector-valued kernel (subkernels)
as −→
K
= [K1, K2, . . . , KL]T , and the coefﬁcients Ai
=
[ai,1, ai,2, . . . , ai,L]T , it is possible to express the vector
product as a summation, giving the estimate in the explicit
multiple-kernel (multikernel) format
ˆy =
L

j=1
N

i=1
aij K j(x, xi),
where aij ∈Rn and K j(x, xi) ∈R.
The structure of the multikernel concept is intuitive
and
its
ability
to
capture different
types
of
nonlinear
behaviour
from
the
input
data
has
been
documented
in [21], [22], [42], and [43]. Furthermore, the approach is
ﬂexible, since the number of subkernels does not depend on
the dimension of the input or output data (L is not necessarily
equal to n), but is only set as a design parameter based on
the observed nonlinear features of the data and the available
computational power.
The following lemma gives a sufﬁcient condition designing
for vector-kernels.
Lemma 1: −→
K
= [K1, K2, . . . , KL]T is a valid vector-
valued kernel if all its subkernels are positive deﬁnite scalar
kernels.
Proof: The proof follows from the construction of the
vector-kernel. If every subkernel Ki is positive deﬁnite, then
there exists a mapping ψi such that Ki(x, y) = ψ H
i (x)ψi(y).
As a consequence, by denoting  = [ψ1, . . . , ψL] the array
of the mappings ψi, we have −→
K (x, y) = diag
	
 H(x)(y)

,
that is, a vector-valued kernel.
□
Lemma 1 represents the backbone of the multikernel con-
cept: in multiple kernel learning [42], the output is approxi-
mated by a sum of partial approximations using subkernels,
hence, the estimate can be seen as an ensemble of estimators
in which each stage (subkernel) is responsible of estimating
one type of nonlinearity. An example of multikernel regression
which employs an LMS update strategy to predict wind can
be found in [21], where each subkernel within the multikernel
approach accounts for different dynamical properties of the
3D wind. For additional insight into multikernel learning
see [22], [42], [44].
