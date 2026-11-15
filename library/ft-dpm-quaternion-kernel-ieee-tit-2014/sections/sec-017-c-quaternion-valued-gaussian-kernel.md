---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-017-c-quaternion-valued-gaussian-kernel
section_title: "Quaternion-Valued Gaussian Kernel"
section_number: C
pages: 8-9
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
Recent complex-valued extensions of kernel estimation
algorithms [17], [18] consider a complex-valued positive def-
inite version of the real Gaussian kernel [47]. A quaternion
version of such a kernel is
KQG(x, y) = exp
"
−AQ
	
x −y∗
T 	
x −y∗
#
,
(14)
where AQ > 0 is the kernel parameter.
Observe that the differences between KQG and K RG are in
that KQG is a function of x −y∗(rather than x −y, hence
allowing for the positive deﬁniteness of the kernel), while
the transpose (instead of the Hermitian) operator allows its
argument to be a full quaternion.
By denoting ˜eR = ℜ{x −y∗} and ˜eI = ℑ{x −y∗}, we write
x −y∗= ˜eR + ˜eI and expand KQG according to
KQG(x, y) = exp
"
−AQ (˜eR + ˜eI )T (˜eR + ˜eI )
#
= exp
"
−AQ
"
˜eT
R˜eR + ˜eT
I ˜eR + ˜eT
R˜eI + ˜eT
I ˜eI
##
= exp
"
−AQ
"
∥˜eR∥2 −∥˜eI∥2 + 2˜eT
R ˜eI
##
= eδ

cos ∥
∥+

∥
∥sin ∥
∥
 
,
where δ = −AQ
"
∥˜eR∥2 −∥˜eI ∥2#
and 
 = −2AQ˜eT
R˜eI .
Unlike the real Gaussian kernel K RG, KQG is not globally
bounded since its norm grows exponentially with ∥˜eI ∥2 =
∥ℑ{x} + ℑ{y}∥2 (as AQ > 0). This highlights both advantages
and disadvantages regarding the implementation of kernel
estimation algorithms: KQG has the ability to model data with
large dynamics and to boost the speed of learning due to its
exponential growth; however, an incorrect choice of parame-
ters will lead to unbounded estimates. From the point of view
of a physically-meaningful representation, the real Gaussian
kernel K RG is better suited for interpolation applications as it
can be regarded as a measure of similarity of samples (like the
triangular kernel in similarity-based modelling [48]), whereas
the quaternion Gaussian kernel KQG is useful for extrapolating
nonlinear features.
Fig. 2 shows KQG for the scalar case y = 0, x = xr +ixi +
jx j + kxk ∈H, which gives δ = −AQ(x2
r −x2
i −x2
j −x2
k),

 = −2AQxr(ixi + jx j + kxk). As KQG(x, 0) is symmetric,
we only plot the region (xr, xi, x j, xk)
∈
[−15, 15] ×
[−15, 15] × {0} × {0} where AQ = 0.05.
