---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-006-c-nonlinear-channel-equalisation-real-and-quater
section_title: "Nonlinear Channel Equalisation: Real and Quaternion"
section_number: C
pages: 10-13
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
Gaussian Kernels
We next validated the real and quaternion Gaussian kernels
for the problem of nonlinear channel equalisation.
5746 IEEE TRANSACTIONS ON INFORMATION THEORY , VOL. 60, NO. 9, SEPTEMBER 2014
1) Channel Model: The transmission channel was modelled
as a linear (moving average) ﬁlter with a memoryless nonlin-
earity stage corrupted by noise:
yn = a1xn + a2xn−1
sn = yn + a3y2
n + ϵn,
where {xn}n∈N is the transmitted message (input to the
channel), {yn}n∈N is an unobserved latent process, {ϵn}n∈N
is a noise process, and {sn}n∈N is the received signal (output
of the channel). This model has been previously considered
for the validation of kernel learning algorithms including
KRR [49], kernel LMS [13], and its complex-valued exten-
sions [16], [17]. The aim of channel equalisation is to identify
the original message {x
n}n∈N from the noisy measurements
{sn}n∈N.
We focused on the quadrivariate case, that is, xn, yn,ϵn,
sn ∈ R4, and assumed that the components of the input
vector (message) xn are jointly Gaussian, i.e. xn ∼ N(0,/Sigma1),
and uncorrelated with the (also Gaussian) noise ϵn ∼
N(0,/Sigma12). The quadriavariate real signals xn, sn ∈ R4 were
then expressed as univariate quaternion sequences xn, sn ∈ H.
The model parameters were randomly chosen and had the
values
/Sigma1=
⎡
⎢⎢⎣
1.2624 −0.3541 −0.1457 −0.5030
−0.3541 0 .8487 −0.1730 0 .0402
−0.1457 −0.1730 0 .4553 −0.3892
−0.5030 0 .0402 −0.3892 1 .4336
⎤
⎥⎥⎦,
a1 = 0.7466 + i0.3733 − j0.28 + k0.1867
a2 = 0.4564 + i0.1521 − j0.6085 + k0.4564
a3 = 0.5341 + i0.3204 + j0.1068 − k0.6409.
With this choice of parameters, both the original mes-
sage and the received signals were noncircular quaternion
sequences [24], [26].
2) Kernel Parameter Design: Within the KRR setting, once
the optimal weights a are computed via Eq. (16), the estimate
is linear in the kernel evaluations. Accordingly, empirical
criteria for kernel design were used to set the kernel parameters
so that the kernel evaluations (entries of the kernel evaluation
matrix K) remained bounded, while at the same time captured
enough data variance. We set the parameters of the Gaussian
kernels to be A
R = 6 · 10−3 (real) and AQ = 10−4
(quaternion) by analysing the second moment of the kernel
evaluations over a 200-sample realisation of the process st ,
thus ensuring boundedness and s ufﬁcient variability. Fig. 8
analyses the features used for setting kernel parameters and
shows the histogram of the kernel evaluations corresponding
to the choice of parameters.
3) Validation: The ability of the different kernels to both
(i) learn the relationship between the available input-output
samples and (ii) generalise the estimates to new datasets of
similar dynamics, was next assessed. Both kernels were also
compared to the strictly- and widely-linear quaternion ridge
regression. See Appendices B and C for an introduction to
quaternion widely-linear estimation and the models used for
this experiment.
Fig. 8. Choice of kernel parameters (red) AR and AQ based on the second
moment of the kernel evaluations and histograms corresponding to the chosen
parameters.
Fig. 9. Training MSE of ridge regressi on algorithms for channel equalisation.
Fig. 9 shows the training MSE averaged over 30 realisations
as a function of the number of support vectors. The train-
ing MSE was computed from the estimate of a 200-sample
sequence which contained the support (training) vectors .
Observe that for more than 50 support vectors, the widely-
linear ridge regression algorithm outperformed its strictly
linear counterpart. Also note that the training performance
of the quaternion Gaussian kernel was similar to that of
the widely-linear ridge regression algorithm [24]. The real
Gaussian KRR offered the best t raining performance, which
improved monotonically with the number of support vectors.
The validation MSE, also averaged over 30 realisations, is
shown in Fig. 10 as a function of the number of support
vectors. To compute the validation MSE, the support samples
(together with the training samples) and the estimated signal
corresponded to different realisations of 100 samples each,
this way, the validation MSE assesses the ability of the regres-
sion algorithms to generalise the input-output dependency.
Observe that, on average, th e quaternion Gaussian kernel
provided the best estimates, outperforming not only the linear
ridge regression algorithms, but also to the standard, real-
valued, Gaussian kernel.
The unbounded nature of the quaternion-valued Gaussian
kernel allowed for the extrapolation of the nonlinear behaviour
TOBAR AND MANDIC: QUATERNION REPRODUCING KERNEL HILBERT SPACES 5747
Fig. 10. Validation MSE of ridge re gression algorithms for channel
equalisation.
learned in the training stage. This property is not found in the
real Gaussian kernel, which serves as a similarity measure and
is therefore better suited for data interpolation.
Due to the enhanced modelling ability arising from the
terms in their imaginary parts, the quaternion-valued kernels
were less prone to overﬁtting than the real-valued kernels,
as shown in both experiments. Furthermore, the superior
performance of the quaternion SVR approach highlights the
advantage of using high-di mensional feature spaces.
VII. C
ONCLUSIONS
We have investigated the existence of quaternion reproduc-
ing kernel Hilbert spaces (QR KHS), as well as the advan-
tages of quaternion kernels over vector-kernels. This has
been achieved based on (i) a rigorous derivation and analysis
of quaternion versions of the Riesz representation and the
Moore-Aronszajn theorems, and (ii) an account of the dif-
ferences between vector and quaternion kernels in terms of
both positive deﬁniteness requirements and their associated
RKHSs. As a consequence, the design and implementation
of kernel estimation algorithms operating on a novel class of
high-dimensional quaternion-valued feature spaces has been
simpliﬁed into the choice of a positive-deﬁnite (quaternion)
kernel, in a way analogous to that of the real- and complex-
valued cases. The improved performance of the quaternion-
valued cubic and exponential kernels has been demonstrated
in the kernel ridge regression setting, for the 3D body motion
tracking and nonlinear channel equalisation applications. The
quaternion-valued kernels have been shown to outperform
their real- and vector-valued counterparts in the mean square
sense, and we have demonstrated their ability to capture the
inherent data relationships in a more accurate and physically-
meaningful way, while being robust to overﬁtting. For rigour,
the existence and uniqueness results have also been provided
with the aim to readily serve as a basis for further quaternion-
valued extensions of existing kernel algorithms.
A
PPENDIX
A. Basis of Cubic Polynomials in ⟨x, y⟩ℜ
We show that the polynomials ⟨x, y⟩3
ℜ ,
⎥
1 + ⟨x, y⟩ℜ
⎦3,⎥
10 + ⟨x, y⟩ℜ
⎦3,
⎥
100 + ⟨x, y⟩ℜ
⎦3 are a basis of the space
of cubic polynomials in ⟨x, y⟩ℜ . For simplicity we denote
/Delta1= ⟨x, y⟩ℜ .
For [α, β, γ, δ]T ∈ R4, we need to ﬁnd [a, b, c, d]T ∈ R4
such that
a/Delta13 + b
⎥
1 + /Delta1
⎦3 + c
⎥
10 + /Delta1
⎦3 + d
⎥
100 + /Delta1
⎦3
= α/Delta13 + β/Delta12 + γ/Delta1+ δ. (17)
Upon expanding the left-hand side of Eq. (17) and factoris-
ing it with respect to the basis [/Delta13,/Delta12,/Delta1,1], we obtain
a/Delta13 + b⎥1 + /Delta1⎦3 + c⎥10 + /Delta1⎦3 + d⎥100 + /Delta1⎦3
= a/Delta13 + b
⎥
1 + 3/Delta1+ 3/Delta12 + /Delta13⎦
+ c
⎥
103 + 300/Delta1+ 30/Delta12 + /Delta13⎦
+ d
⎥
1003 + 3 × 1002/Delta1+ 300/Delta12 + /Delta13⎦
= /Delta13(a + b + c + d) + /Delta12(3b + 30c + 300d)
+ /Delta1(3b+300c+3×1002d)+1(b+103c+1003d) (18)
A comparison of the right-hand sides of Eqs. (17) and (18)
gives the linear equation
⎛
⎜⎜⎝
11 1 1
0 3 30 300
0 3 300 3 × 1002
011 0 3 1003
⎞
⎟⎟⎠
⎛
⎜⎜⎝
a
b
c
d
⎞
⎟⎟⎠ =
⎛
⎜⎜⎝
α
β
γ
δ
⎞
⎟⎟⎠
with an invertible matrix on the left-hand side.
As a consequence, the proposed basis is a linearly-
independent basis of the set of cubic polynomials in /Delta1(the
independence property can be veriﬁed by [α, β, γ, δ]= 0 ⇒
[a, b, c, d]= 0).
Other linearly-independent bases of real cubic polynomials
on /Delta1were also considered, including {1,/Delta1,/Delta12,/Delta13} and
{(b0 + /Delta1)3,( b1 + /Delta1)3,( b2 + /Delta1)3,( b3 + /Delta1)3} for different
parameters b0, b1, b2, b3 ∈ R+. We have found that the chosen
basis (subkernels) provided the best results, in the MSE sense,
in the prediction setting considered.
B. Quaternion Widely-Linear Ridge Regression
Strictly-linear models assume that the minimum mean
square estimator (MMSE) E{x|s} of a vector x given an
observation vector s is, regardless of the real or quaternion
nature of the vectors, given by
7
ˆx = As, (19)
where A is a coefﬁcient matrix. On the other hand, widely-
linear quaternion models exploit the linear dependency
between the vector x and each of the components of the
regressor s = s
r +isi + jsj +ksk , yielding an estimator which
is linear in each of these components.
Alternatively, by considering the involutions of s,g i v e n
by [50]
si =− isi = sr − isi + jsj + ksk
sj =− js j = sr + isi − jsj + ksk
sk =− ksk = sr + isi + jsj − ksk,
we can express the widely-linear estimator in the form [51]:
ˆx = As + Bsi + Csj + Dsk = Wsa,
7We have maintained the notation s and x for consistency with the nonlinear
channel equalisation simulation.
5748 IEEE TRANSACTIONS ON INFORMATION THEORY , VOL. 60, NO. 9, SEPTEMBER 2014
where
W =[ A, B, C, D], sa =
⎡
⎢⎢⎣
s
si
sj
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
able observation pairs {(sn, xn), n = 1,..., N},t h a ti s
W = (SH S + ρI)−1SH X,
where ρ> 0 is a regularization factor, and S =[ s1,..., sN ]
and X =[ xT
1 ,..., xT
N ]T are the matrices of available observa-
tions.
The widely-linear ridge regression can also be regarded
as an approximation of the widely-linear Wiener ﬁlter [52],
where the correlation matrix and the autocorrelation vector
are approximated using the available data.
