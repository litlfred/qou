---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-023-b-quaternion-widely-linear-ridge-regression
section_title: "Quaternion Widely-Linear Ridge Regression"
section_number: B
pages: 12-13
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
Strictly-linear models assume that the minimum mean
square estimator (MMSE) E{x|s} of a vector x given an
observation vector s is, regardless of the real or quaternion
nature of the vectors, given by7
ˆx = As,
(19)
where A is a coefﬁcient matrix. On the other hand, widely-
linear quaternion models exploit the linear dependency
between the vector x and each of the components of the
regressor s = sr +isi + js j +ksk, yielding an estimator which
is linear in each of these components.
Alternatively, by considering the involutions of s, given
by [50]
si = −isi = sr −isi + js j + ksk
s j = −js j = sr + isi −js j + ksk
sk = −ksk = sr + isi + js j −ksk,
we can express the widely-linear estimator in the form [51]:
ˆx = As + Bsi + Cs j + Dsk = Wsa,
7We have maintained the notation s and x for consistency with the nonlinear
channel equalisation simulation.
where
W = [A, B, C, D],
sa =
⎡
⎢⎢⎣
s
si
s j
sk
⎤
⎥⎥⎦
are the so-called augmented quantities.
This way, the widely-linear estimator is theoretically equiv-
alent to the quadrivariate real-valued estimator and is the
best linear estimator in H [52]. For complex widely-linear
algorithms, see [53], [54].
In the ridge-regression setting, the weights W are computed
in the regularised least-squares sense based on a set of avail-
able observation pairs {(sn, xn), n = 1, . . . , N}, that is
W = (SHS + ρI)−1SHX,
where ρ > 0 is a regularization factor, and S = [s1, . . . , sN ]
and X = [xT
1 , . . . , xT
N]T are the matrices of available observa-
tions.
The widely-linear ridge regression can also be regarded
as an approximation of the widely-linear Wiener ﬁlter [52],
where the correlation matrix and the autocorrelation vector
are approximated using the available data.
