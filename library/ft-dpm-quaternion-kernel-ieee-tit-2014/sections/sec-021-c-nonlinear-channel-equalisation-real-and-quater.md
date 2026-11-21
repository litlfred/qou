---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-021-c-nonlinear-channel-equalisation-real-and-quater
section_title: "Nonlinear Channel Equalisation: Real and Quaternion"
section_number: C
pages: 10-12
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
Gaussian Kernels
We next validated the real and quaternion Gaussian kernels
for the problem of nonlinear channel equalisation.
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
the original message {xn}n∈N from the noisy measurements
{sn}n∈N.
We focused on the quadrivariate case, that is, xn, yn, ϵn,
sn ∈R4, and assumed that the components of the input
vector (message) xn are jointly Gaussian, i.e. xn ∼N(0, ),
and uncorrelated with the (also Gaussian) noise ϵn
∼
N(0, 2). The quadriavariate real signals xn, sn ∈R4 were
then expressed as univariate quaternion sequences xn, sn ∈H.
The model parameters were randomly chosen and had the
values
 =
⎡
⎢⎢⎣
1.2624 −0.3541 −0.1457 −0.5030
−0.3541 0.8487 −0.1730 0.0402
−0.1457 −0.1730 0.4553 −0.3892
−0.5030 0.0402 −0.3892 1.4336
⎤
⎥⎥⎦,
a1 = 0.7466 + i0.3733 −j0.28 + k0.1867
a2 = 0.4564 + i0.1521 −j0.6085 + k0.4564
a3 = 0.5341 + i0.3204 + j0.1068 −k0.6409.
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
kernels to be AR
= 6 · 10−3 (real) and AQ
= 10−4
(quaternion) by analysing the second moment of the kernel
evaluations over a 200-sample realisation of the process st,
thus ensuring boundedness and sufﬁcient variability. Fig. 8
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
Fig. 8.
Choice of kernel parameters (red) AR and AQ based on the second
moment of the kernel evaluations and histograms corresponding to the chosen
parameters.
Fig. 9. Training MSE of ridge regression algorithms for channel equalisation.
Fig. 9 shows the training MSE averaged over 30 realisations
as a function of the number of support vectors. The train-
ing MSE was computed from the estimate of a 200-sample
sequence which contained the support (training) vectors.
Observe that for more than 50 support vectors, the widely-
linear ridge regression algorithm outperformed its strictly
linear counterpart. Also note that the training performance
of the quaternion Gaussian kernel was similar to that of
the widely-linear ridge regression algorithm [24]. The real
Gaussian KRR offered the best training performance, which
improved monotonically with the number of support vectors.
The validation MSE, also averaged over 30 realisations, is
shown in Fig. 10 as a function of the number of support
vectors. To compute the validation MSE, the support samples
(together with the training samples) and the estimated signal
corresponded to different realisations of 100 samples each,
this way, the validation MSE assesses the ability of the regres-
sion algorithms to generalise the input-output dependency.
Observe that, on average, the quaternion Gaussian kernel
provided the best estimates, outperforming not only the linear
ridge regression algorithms, but also to the standard, real-
valued, Gaussian kernel.
The unbounded nature of the quaternion-valued Gaussian
kernel allowed for the extrapolation of the nonlinear behaviour
Fig. 10.
Validation MSE of ridge regression algorithms for channel
equalisation.
learned in the training stage. This property is not found in the
real Gaussian kernel, which serves as a similarity measure and
is therefore better suited for data interpolation.
Due to the enhanced modelling ability arising from the
terms in their imaginary parts, the quaternion-valued kernels
were less prone to overﬁtting than the real-valued kernels,
as shown in both experiments. Furthermore, the superior
performance of the quaternion SVR approach highlights the
advantage of using high-dimensional feature spaces.
