---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "5736 IEEE TRANSACTIONS ON INFORMATION THEORY , VOL. 60, NO. 9, SEPTEMBER 2014 Quaternion Reproducing Kernel Hilbert Spaces:"
section_id: sec-005-c-quaternion-valued-gaussian-kernel
section_title: "Quaternion-Valued Gaussian Kernel"
section_number: C
pages: 8-10
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
doc_brief: "5736 IEEE TRANSACTIONS ON INFORMATION THEORY , VOL. 60, NO. 9, SEPTEMBER 2014 Quaternion Reproducing Kernel Hilbert Spaces: — The existence and uniqueness conditions of quater- nion reproducing"
---
Recent complex-valued extensions of kernel estimation
algorithms [17], [18] consider a complex-valued positive def-
inite version of the real Gaussian kernel [47]. A quaternion
version of such a kernel is
K
QG (x, y) = exp
⎥
−AQ
⎥
x − y∗⎦T ⎥
x − y∗⎦⎦
, (14)
where AQ > 0 is the kernel parameter.
Observe that the differences between KQG and KRG are in
that KQG is a function of x − y∗ (rather than x − y, hence
allowing for the positive deﬁniteness of the kernel), while
the transpose (instead of the Hermitian) operator allows its
argument to be a full quaternion.
By denoting ˜e
R =ℜ {x − y∗} and ˜eI =ℑ {x − y∗}, we write
x − y∗ =˜eR +˜eI and expand KQG according to
KQG (x, y) = exp
⎥
−AQ (˜eR +˜eI )T (˜eR +˜eI )
⎦
= exp
⎥
−AQ
⎥
˜eT
R ˜eR +˜eT
I ˜eR +˜eT
R ˜eI +˜eT
I ˜eI
⎦⎦
= exp
⎥
−AQ
⎥
‖˜eR‖2 − ‖˜eI ‖2 + 2˜eT
R ˜eI
⎦⎦
= eδ
⎥
cos‖/Delta1‖+ /Delta1
‖/Delta1‖sin ‖/Delta1‖
⎦
,
where δ =− AQ
⎥
‖˜eR‖2 − ‖˜eI ‖2
⎦
and /Delta1=− 2AQ ˜eT
R ˜eI .
Unlike the real Gaussian kernel KRG , KQG is not globally
bounded since its norm grows exponentially with ‖˜eI ‖2 =
‖ℑ{x}+ℑ {y}‖2 (as AQ > 0). This highlights both advantages
and disadvantages regarding t he implementation of kernel
estimation algorithms: KQG has the ability to model data with
large dynamics and to boost the speed of learning due to its
exponential growth; however, an incorrect choice of parame-
ters will lead to unbounded estimates. From the point of view
of a physically-meaningful representation, the real Gaussian
kernel K
RG is better suited for interpolation applications as it
can be regarded as a measure of similarity of samples (like the
triangular kernel in similarity -based modelling [48]), whereas
the quaternion Gaussian kernel K
QG is useful for extrapolating
nonlinear features.
Fig. 2 shows KQG for the scalar case y = 0, x = xr +ix i +
jx j + kxk ∈ H, which gives δ =− AQ(x2
r − x2
i − x2
j − x2
k ),
/Delta1=− 2AQ xr(ix i + jx j + kxk).A s KQG (x, 0) is symmetric,
we only plot the region (xr, xi, x j, xk) ∈[ − 15, 15]×
[−15, 15]×{ 0}×{ 0} where AQ = 0.05.
5744 IEEE TRANSACTIONS ON INFORMATION THEORY , VOL. 60, NO. 9, SEPTEMBER 2014
VI. K ERNEL RIDGE REGRESSION IN QUATERNION RKHS
We validated the proposed QRKHS, together with the intro-
duced quaternion kernels, in the kernel ridge regression (KRR)
setting presented in Section VI-A against both scalar and
vector-valued real kernels; these results complement previous
quaternion kernel applications which considered linear (quater-
nion) kernels only [31]. Section VI-B illustrates the prediction
of body sensor signals and shows that the introduced quater-
nion cubic kernel outperforms the real vector-kernel (ensemble
of four real cubic kernels), while having the same degrees of
freedom and similar computational complexity. Section VI-C
considers the nonlinear channel equalisation problem using
real Gaussian and quaternion Gaussian kernels, and both linear
and widely-linear estimators, in order to validate the quater-
nion Gaussian kernel generalisation (extrapolation) properties
and robustness to overﬁtting. This second experiment also
explains how to choose the parameters of the quaternion
Gaussian kernel using available measurements.
A. Introduction to Kernel Ridge Regression
Consider the collection of a vailable measurement pairs
C
N ={ (xi, yi)}i=1:N ∈ X × Y corresponding to the input and
output of a nonlinear system. The aim of KRR is to model
the relationship between the input x and the output y of such
as y s t e mb y
ˆy = ⟨ω,φ x⟩, (15)
whereby both the (ﬁxed) element ω and the transformation φx
lie on a QRKHS H0 with inner product ⟨·,·⟩. To avoid the
need for the optimisation in the high-dimensional space H0,
we restrict the search for the optimal weight to a reduced-
dimensional QRKHS H = span{φxi , i = 1,..., N} ⊊ H0,
referred to to as the empirical feature space [41]. In this way,
the optimal ω ∈ H can be expressed as
ω =
N∑
i=1
aiφxi ,
and therefore the estimate (15) takes the form
ˆy =
N∑
i=1
ai
⟨
φxi ,φ x
⟩
=
N∑
i=1
ai K(xi, x),
where K is the generating kernel of the QRKHS H for
which existence and uniqueness is guaranteed by the Riesz
representation theorem (Thm. 1). As a consequence, the search
for the optimal weights ω is simpliﬁed into the problem of
ﬁnding the coefﬁcients a =[ a
1,..., aN ]∈ HN .
Using the regularised least-squares criterion for ﬁnding
the optimal vector a given the observations CN ,a n dt h e
regularisation parameter ρ ∈ R+, we arrive at the optimisation
problem
a = arg min
a∈HN
N∑
j=1
‖‖‖‖
‖y
j −
N∑
i=1
ai K(xi, x j)
‖‖‖‖
‖
2
+ ρ ‖a‖2 ,
for which the solution can be found in a closed form using
the HR calculus [30], and is given by
a = (KH K + ρI)−1KH Y, (16)
Fig. 3. Inertial body sensor setting. [Left] Fixed coordinate system (red),
sensor coordinate system (blue) and Euler angles (green). [Right] A3 D
inertial body sensor at the right wrist.
where Y =[ y1,..., yN ]T , I is the identity matrix, and K is
the Gram matrix evaluated over the set of training samples
given by Kij = K(xi, x j).
We next present two applications of KRR operating in a
QRKHS with the kernels presented in Section V, and refer to
the input samples of the training set CN as support vectors .
The algorithms were implemented in MATLAB® using the
Quaternion Toolbox for MATLAB® [46].
B. Multivariate Body Motion Tracking: Cubic Kernels
We implemented KRR algorithms using real, vector and
quaternion cubic kernels to perform a one-step-ahead predic-
tion of the trajectory of limbs in Tai Chi sequences. Data sets
for training and validation of the algorithms corresponded to
different realisations of Tai Chi movements.
1) Data Acquisition and Preprocessing: Four accelerome-
ters (placed at wrists and ankl es) recorded the three Euler
angles (Fig. 3), giving a total of 12 signals {θs}s=1,..,12
taking values in the range [−π,π ]. The recorded signals
were discontinuous in {−π,π } and thus unsuitable for the
application of continuous kernels, hence the angles data were
conditioned through the mapping θs ↦→ (sin θs, cos θs).T h e s e
new features also made it possible for the data to be resampled
if needed.
Each of the scalar mappings θs ↦→ sin θs, θs ↦→ cos θs
is non-injective (and non-invertible) and therefore does not
allow for the angle signal θs to be recovered. However, the
considered 2D map θs ↦→ (sin θs, cos θs) ∈ R2 is bijective and
therefore invertible, hence, allowing us to recover the original
angle signal θs. Additionally, the proposed map also allows
us to preserve the dynamics of the signal. As illustrated in
Fig. 4, sine and cosine preserve data variation successfully
only when they behave in a linear-like fashion
5;h o w e v e r ,
as such trigonometric functions are shifted versions of one
another, by considering them together the signals dynamics
are well preserved.
The data corresponding to the so-mapped 12 angles were
then represented by a 24-dimensional real signal, or equiv-
alently, a six-dimensional quaternion signal. Therefore, by
considering two delayed samples as regressors, the input and
output pairs were respectively elements of H
12 and H6.
5Recall that for θ ≈ 0, sin(θ) ≈ θ and cos(1.5π + θ) ≈ θ.
TOBAR AND MANDIC: QUATERNION REPRODUCING KERNEL HILBERT SPACES 5745
Fig. 4. Raw angle measurements and considered features. [Top] Original
discontinuous angle recording and [Bottom] the corresponding continuous
sine and cosine mapping. Observe that i n the right (left) circle only cosine
(sine) preserves the dynamics of the angle signal accurately.
Fig. 5. Body sensor signal tracking: Angle features (sin θ, cosθ) and KRR
estimates.
2) Choice of Cubic Kernels: The kernel ridge regression
algorithms were implemented f eaturing real-, vector-, and
quaternion-valued cubic kernels. The real kernel used was
the standard cubic kernel in Eq. (10) for p = 3, that is, 6
KRP (x, y) =
⎥
1+⟨x, y⟩ℜ
⎦3, whereas the vector-kernel chosen
was
KM(x, y) =
⎛
⎜⎜
⎜⎝
⟨x, y⟩
3
ℜ⎥
1 + ⟨x, y⟩ℜ
⎦3
⎥
10 + ⟨x, y⟩ℜ
⎦3
⎥
100 + ⟨x, y⟩ℜ
⎦3
⎞
⎟⎟
⎟⎠
since its subkernels are a basis of the space of cubic poly-
nomials on ⟨x, y⟩
ℜ and performed better that other basis
considered (see Appendix A for comments on the choice of
these subkernels).
Finally, we chose the quaternion kernel KQP (x, y) =⎥
1+xH x
⎦⎥
1+xH y
⎦⎥
1+yH y
⎦
introduced in Eq. (11) to validate
the quaternion kernel regression concept.
3) Results: We chose a regularisation parameter ρ = 5
as this suited all three algorithms and in particular allowed
6Recall that ⟨x, y⟩ℜ =ℜ {⟨x, y⟩}.
Fig. 6. Performance of KRR algorithms for body sensor signal tracking as
a function of the number of support vectors.
Fig. 7. Computation time of KRR algorithms for body sensor signal tracking.
the multikernel not to suffer from overﬁtting. Fig. 5 shows
the cosine and sine of one coordinate θ and their kernel
estimates for 90 randomly chosen support vectors. Fig. 6
shows the averaged prediction mean square error (MSE) over
30 independent realisations , as a function of the number of
support vectors for the same regularisation parameter. The
support vectors and the validation set (50 samples) were
randomly chosen, without repetition, for all realisations.
Observe that the scalar real kernel algorithm is outperformed
by both the multikernel and quaternion ones due to their higher
degrees of freedom. Moreover, note that the performance of
the quaternion cubic kernel became progressively better than
that of its real-valued counterpart as the number of support
vectors (and therefore training samples) increased. The better
performance of K
QP for a larger number of support vectors
can be explained by the inability of KRP to model cross-
coupling between data components and the cross-coordinate
terms, for which the quaternion cubic kernel is perfectly well
suited (see Remark 9).
Finally, Fig. 7 shows the computation time for all three
algorithms. In line with Table I, the complexities of the vector
and quaternion kernels were found to be similar and greater
than that of the real kernel.
