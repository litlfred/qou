---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-016-b-real-valued-gaussian-kernel
section_title: "Real-Valued Gaussian Kernel"
section_number: B
pages: 8-8
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
Together with the polynomial kernel, the Gaussian kernel
is extensively used in machine learning and signal processing
applications. It serves as a deviation measure between samples,
hence, providing reliable estimates for known regions of the
input space (dictionary), while vanishing for inputs that deviate
from the dictionary. The Gaussian kernel can be extended
to operate on quaternion samples by accommodating the
quaternion norm in its argument. Recall that ∥q∥=

q Hq,
so that the real-valued Gaussian kernel K RG can be deﬁned as
K RG(x, y) = exp
"
−AR (x −y)H (x −y)
#
,
(13)
where AR > 0 is the kernel parameter.
We next use Deﬁnition 4 to show that K RG is positive
deﬁnite in the quaternion domain. First, observe that for an
arbitrary, non-zero, vector x ∈Hn the quadratic form xHKx
is real. Indeed, due to the symmetry of the real matrix K we
have
2ℑ{xHKx} = xHKx −(xHKx)H = xHKx −(xHKx) = 0.
Now, by expanding the vector x = xr + ixi + jx j + kxk
within ℜ{xHKx} using its real and imaginary parts, we can
write
ℜ{xHKx} = xT
r Kxr + xT
i Kxi + xT
j Kx j + xT
k Kxk.
Since K is positive deﬁnite in the real domain, the arbitrary
components xR, xi, x j, xk are real-valued, and the quadratic
form xHKx is positive, we have xHKx = ℜ{xHKx} > 0,
proving the positive deﬁniteness of the real Gaussian kernel
K RG in H.
Fig. 2.
Real (left) and i-imaginary (right) parts of KQG. The colourmap is
dark blue for −7 · 10−4, white for 0, and red for 7 · 104, with a logarithmic
RGB interpolation.
