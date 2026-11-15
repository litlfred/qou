---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-020-b-multivariate-body-motion-tracking-cubic-kernel
section_title: "Multivariate Body Motion Tracking: Cubic Kernels"
section_number: B
pages: 9-10
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
We implemented KRR algorithms using real, vector and
quaternion cubic kernels to perform a one-step-ahead predic-
tion of the trajectory of limbs in Tai Chi sequences. Data sets
for training and validation of the algorithms corresponded to
different realisations of Tai Chi movements.
1) Data Acquisition and Preprocessing: Four accelerome-
ters (placed at wrists and ankles) recorded the three Euler
angles (Fig. 3), giving a total of 12 signals {θs}s=1,..,12
taking values in the range [−π, π]. The recorded signals
were discontinuous in {−π, π} and thus unsuitable for the
application of continuous kernels, hence the angles data were
conditioned through the mapping θs →(sin θs, cos θs). These
new features also made it possible for the data to be resampled
if needed.
Each of the scalar mappings θs →sin θs, θs →cos θs
is non-injective (and non-invertible) and therefore does not
allow for the angle signal θs to be recovered. However, the
considered 2D map θs →(sin θs, cos θs) ∈R2 is bijective and
therefore invertible, hence, allowing us to recover the original
angle signal θs. Additionally, the proposed map also allows
us to preserve the dynamics of the signal. As illustrated in
Fig. 4, sine and cosine preserve data variation successfully
only when they behave in a linear-like fashion5; however,
as such trigonometric functions are shifted versions of one
another, by considering them together the signals dynamics
are well preserved.
The data corresponding to the so-mapped 12 angles were
then represented by a 24-dimensional real signal, or equiv-
alently, a six-dimensional quaternion signal. Therefore, by
considering two delayed samples as regressors, the input and
output pairs were respectively elements of H12 and H6.
5Recall that for θ ≈0, sin(θ) ≈θ and cos(1.5π + θ) ≈θ.
Fig. 4.
Raw angle measurements and considered features. [Top] Original
discontinuous angle recording and [Bottom] the corresponding continuous
sine and cosine mapping. Observe that in the right (left) circle only cosine
(sine) preserves the dynamics of the angle signal accurately.
Fig. 5.
Body sensor signal tracking: Angle features (sin θ, cos θ) and KRR
estimates.
2) Choice of Cubic Kernels: The kernel ridge regression
algorithms were implemented featuring real-, vector-, and
quaternion-valued cubic kernels. The real kernel used was
the standard cubic kernel in Eq. (10) for p = 3, that is,6
K RP(x, y) =
	
1+⟨x, y⟩ℜ

3, whereas the vector-kernel chosen
was
KM(x, y) =
⎛
⎜⎜⎜⎝
⟨x, y⟩3
ℜ
	
1 + ⟨x, y⟩ℜ

3
	
10 + ⟨x, y⟩ℜ

3
	
100 + ⟨x, y⟩ℜ

3
⎞
⎟⎟⎟⎠
since its subkernels are a basis of the space of cubic poly-
nomials on ⟨x, y⟩ℜand performed better that other basis
considered (see Appendix A for comments on the choice of
these subkernels).
Finally, we chose the quaternion kernel KQ P(x, y) =
	
1+xHx

	
1+xHy

	
1+yHy

introduced in Eq. (11) to validate
the quaternion kernel regression concept.
3) Results: We chose a regularisation parameter ρ = 5
as this suited all three algorithms and in particular allowed
6Recall that ⟨x, y⟩ℜ= ℜ{⟨x, y⟩}.
Fig. 6.
Performance of KRR algorithms for body sensor signal tracking as
a function of the number of support vectors.
Fig. 7. Computation time of KRR algorithms for body sensor signal tracking.
the multikernel not to suffer from overﬁtting. Fig. 5 shows
the cosine and sine of one coordinate θ and their kernel
estimates for 90 randomly chosen support vectors. Fig. 6
shows the averaged prediction mean square error (MSE) over
30 independent realisations, as a function of the number of
support vectors for the same regularisation parameter. The
support vectors and the validation set (50 samples) were
randomly chosen, without repetition, for all realisations.
Observe that the scalar real kernel algorithm is outperformed
by both the multikernel and quaternion ones due to their higher
degrees of freedom. Moreover, note that the performance of
the quaternion cubic kernel became progressively better than
that of its real-valued counterpart as the number of support
vectors (and therefore training samples) increased. The better
performance of KQ P for a larger number of support vectors
can be explained by the inability of K RP to model cross-
coupling between data components and the cross-coordinate
terms, for which the quaternion cubic kernel is perfectly well
suited (see Remark 9).
Finally, Fig. 7 shows the computation time for all three
algorithms. In line with Table I, the complexities of the vector
and quaternion kernels were found to be similar and greater
than that of the real kernel.
