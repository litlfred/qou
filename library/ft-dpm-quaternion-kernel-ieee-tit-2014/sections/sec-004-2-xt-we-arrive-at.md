---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "5736 IEEE TRANSACTIONS ON INFORMATION THEORY , VOL. 60, NO. 9, SEPTEMBER 2014 Quaternion Reproducing Kernel Hilbert Spaces:"
section_id: sec-004-2-xt-we-arrive-at
section_title: "(x)]T we arrive at"
section_number: 2
pages: 7-8
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
doc_brief: "5736 IEEE TRANSACTIONS ON INFORMATION THEORY , VOL. 60, NO. 9, SEPTEMBER 2014 Quaternion Reproducing Kernel Hilbert Spaces: — The existence and uniqueness conditions of quater- nion reproducing"
---
KQP (x, y) = φH(x)φ(y). (12)
Finally, by combining (12) and Deﬁnition 3 we have
∫
X2
θ∗(x)KQP (x, y)θ(y)dxdy
=
∫
X2
θ∗(x)φH(x)φ(y)θ(y)dxdy
(a)
=
∫
X
θ∗(x)φH(x)dx
∫
X
φ(y)θ(y)dy
=
⎥∫
X
φ(x)θ(x)dx
⎦H ∫
X
φ(y)θ(y)dy
=
‖‖‖‖
∫
X
φ(x)θ(x)dx
‖‖‖‖
2
≥ 0,
where θ(·) is assumed to be Lebesgue integrable and bounded
on the compact set X ⊊H n, while the identity (a)= is a
consequence of Fubini’s theorem [10].
TOBAR AND MANDIC: QUATERNION REPRODUCING KERNEL HILBERT SPACES 5743
Fig. 1. Real (left) and i-imaginary (right) parts of KQP . The colourmap is
dark blue for −13· 103, white for the interval [−10, 10], and red for 13 · 103
with a logarithmic RGB interpolation.
Remark 9: Note from Eqs. (10) and (11) that, owing to
its imaginary part, the quaternion cubic kernel K QP pro-
vides enhanced data representation over the real-valued cubic
kernel K RP . Therefore, K QP has the ability to learn the
relationship between input variables, while preserving the
mathematical simplicity of polynomial kernels.
Fig. 1 visualises KQP for the scalar case x = 1, y = yr +
iyi + jy j + kyk ∈ H, which gives KQP (1, y) = 2(1 + y)
(1 + ‖y‖2).A s KQP (1, y) is symmetric, we only plot the
region (yr, yi, yj, yk) ∈[ −15, 15]×[ −15, 15]×{ 0}×{ 0}.
B. Real-Valued Gaussian Kernel
Together with the polynomial kernel, the Gaussian kernel
is extensively used in machine learning and signal processing
applications. It serves as a deviation measure between samples,
hence, providing reliable estimates for known regions of the
input space (dictionary), while vanishing for inputs that deviate
from the dictionary. The Gaussian kernel can be extended
to operate on quaternion samples by accommodating the
quaternion norm in its argument. Recall that ‖q‖ =
√
q H q,
so that the real-valued Gaussian kernel KRG can be deﬁned as
KRG (x, y) = exp
⎥
−AR (x − y)H (x − y)
⎦
, (13)
where AR > 0 is the kernel parameter.
We next use Deﬁnition 4 to show that KRG is positive
deﬁnite in the quaternion domain. First, observe that for an
arbitrary, non-zero, vector x ∈ H
n the quadratic form xH Kx
is real. Indeed, due to the symmetry of the real matrix K we
have
2ℑ{xH Kx}= xH Kx − (xH Kx)H = xH Kx − (xH Kx) = 0.
Now, by expanding the vector x = xr + ixi + jx j + kxk
within ℜ{xH Kx} using its real and imaginary parts, we can
write
ℜ{xH Kx}= xT
r Kxr + xT
i Kxi + xT
j Kx j + xT
k Kxk.
Since K is positive deﬁnite in the real domain, the arbitrary
components xR, xi, x j, xk are real-valued, and the quadratic
form xH Kx is positive, we have xH Kx =ℜ { xH Kx} > 0,
proving the positive deﬁniteness of the real Gaussian kernel
KRG in H.
Fig. 2. Real (left) and i-imaginary (right) parts of KQG . The colourmap is
dark blue for −7 · 10−4, white for 0, and red for 7 · 104, with a logarithmic
RGB interpolation.
