---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-015-a-polynomial-kernel-the-quaternion-cubic-example
section_title: "Polynomial Kernel: The Quaternion Cubic Example"
section_number: A
pages: 7-8
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
The polynomial kernel is standard in kernel-based estima-
tion due to its robustness and ease of implementation. For real-
and complex-valued samples xr, yr, the polynomial kernel is
given by
K P(xr, yr) =
	
1 + xT
r yr

p
where p ∈N is referred to as the order of the kernel. On the
other hand, the real-valued polynomial kernel of quaternion
samples x, y K RP : X2 →R, that is, the polynomial kernel of
the real-valued representations of x and y, can be expressed as
K RP(x, y) =
	
1 + ⟨x, y⟩ℜ

p =
	
1 + ℜ{xHy}

p
(10)
where ⟨x, y⟩ℜis the inner product in Rn and ℜ{q} denotes the
real part of the quaternion q.
The extension to quaternion-valued polynomial kernels is
not straightforward, as for the quaternion vectors x and y the
factorisation
	1 + xHy
p = φH(x)φ(y)
may not be possible due to the noncommutativity of the
quaternion ring, and therefore the positive deﬁniteness of such
kernel cannot be guaranteed in this manner.
For p = 3, we next propose a quaternion polynomial kernel
which admits factorisation as an inner product, thus ensuring
the required positive deﬁniteness.
Consider the quaternion cubic kernel KQ P : X2 →H
given by
KQ P(x, y) =
	
1 + xHx

	
1 + xHy

	
1 + yHy

.
(11)
To show that KQ P is positive semideﬁnite, we shall ﬁrst
consider its factorisation of the form KQ P(x, y) = φH(x)φ(y).
Indeed,
KQ P(x, y) = 	1 + xHx
	1 + yHy
+
	
1 + xHx

xHy
	
1 + yHy

= 	1 + xHx
H	1 + yHy
+
	
x
	
1 + xHx

H	
y
	
1 + yHy

= φH
1 (x)φ1(y) + φH
2 (x)φ2(y),
where φ1(x) = 1 + xHx and φ2(x) = x
	
1 + xHx

. Therefore,
by setting φ(x) = [φT
1 (x) φT
2 (x)]T we arrive at
KQ P(x, y) = φH(x)φ(y).
(12)
Finally, by combining (12) and Deﬁnition 3 we have

X2 θ∗(x)KQ P(x, y)θ(y)dxdy
=

X2 θ∗(x)φH(x)φ(y)θ(y)dxdy
(a)
=

X
θ∗(x)φH(x)dx

X
φ(y)θ(y)dy
=

X
φ(x)θ(x)dx
 H 
X
φ(y)θ(y)dy
=
!!!!

X
φ(x)θ(x)dx
!!!!
2
≥0,
where θ(·) is assumed to be Lebesgue integrable and bounded
on the compact set X ⊊Hn, while the identity (a)
= is a
consequence of Fubini’s theorem [10].
Fig. 1.
Real (left) and i-imaginary (right) parts of KQP. The colourmap is
dark blue for −13 · 103, white for the interval [−10, 10], and red for 13 · 103
with a logarithmic RGB interpolation.
Remark 9: Note from Eqs. (10) and (11) that, owing to
its imaginary part, the quaternion cubic kernel KQ P pro-
vides enhanced data representation over the real-valued cubic
kernel K RP. Therefore, KQ P has the ability to learn the
relationship between input variables, while preserving the
mathematical simplicity of polynomial kernels.
Fig. 1 visualises KQ P for the scalar case x = 1, y = yr +
iyi + jy j + kyk ∈H, which gives KQ P(1, y) = 2(1 + y)
(1 + ∥y∥2). As KQ P(1, y) is symmetric, we only plot the
region (yr, yi, y j, yk) ∈[−15, 15] × [−15, 15] × {0} × {0}.
