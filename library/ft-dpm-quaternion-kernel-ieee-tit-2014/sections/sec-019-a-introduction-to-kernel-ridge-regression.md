---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-019-a-introduction-to-kernel-ridge-regression
section_title: "Introduction to Kernel Ridge Regression"
section_number: A
pages: 9-9
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
Consider the collection of available measurement pairs
CN = {(xi, yi)}i=1:N ∈X × Y corresponding to the input and
output of a nonlinear system. The aim of KRR is to model
the relationship between the input x and the output y of such
a system by
ˆy = ⟨ω, φx⟩,
(15)
whereby both the (ﬁxed) element ω and the transformation φx
lie on a QRKHS H0 with inner product ⟨·, ·⟩. To avoid the
need for the optimisation in the high-dimensional space H0,
we restrict the search for the optimal weight to a reduced-
dimensional QRKHS H = span{φxi, i = 1, . . . , N} ⊊H0,
referred to to as the empirical feature space [41]. In this way,
the optimal ω ∈H can be expressed as
ω =
N

i=1
aiφxi,
and therefore the estimate (15) takes the form
ˆy =
N

i=1
ai

φxi, φx

=
N

i=1
ai K(xi, x),
where K is the generating kernel of the QRKHS H for
which existence and uniqueness is guaranteed by the Riesz
representation theorem (Thm. 1). As a consequence, the search
for the optimal weights ω is simpliﬁed into the problem of
ﬁnding the coefﬁcients a = [a1, . . . , aN] ∈HN.
Using the regularised least-squares criterion for ﬁnding
the optimal vector a given the observations CN, and the
regularisation parameter ρ ∈R+, we arrive at the optimisation
problem
a = arg min
a∈HN
N

j=1
!!!!!y j −
N

i=1
ai K(xi, x j)
!!!!!
2
+ ρ ∥a∥2 ,
for which the solution can be found in a closed form using
the HR calculus [30], and is given by
a = (KHK + ρI)−1KHY,
(16)
Fig. 3.
Inertial body sensor setting. [Left] Fixed coordinate system (red),
sensor coordinate system (blue) and Euler angles (green). [Right] A 3D
inertial body sensor at the right wrist.
where Y = [y1, . . . , yN]T , I is the identity matrix, and K is
the Gram matrix evaluated over the set of training samples
given by Kij = K(xi, x j).
We next present two applications of KRR operating in a
QRKHS with the kernels presented in Section V, and refer to
the input samples of the training set CN as support vectors.
The algorithms were implemented in MATLAB® using the
Quaternion Toolbox for MATLAB® [46].
