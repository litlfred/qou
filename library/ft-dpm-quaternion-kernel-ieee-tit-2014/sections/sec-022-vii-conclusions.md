---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-022-vii-conclusions
section_title: "CONCLUSIONS"
section_number: VII
pages: 12-12
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
We have investigated the existence of quaternion reproduc-
ing kernel Hilbert spaces (QRKHS), as well as the advan-
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
APPENDIX
A. Basis of Cubic Polynomials in ⟨x, y⟩ℜ
We show that the polynomials ⟨x, y⟩3
ℜ,
	
1 + ⟨x, y⟩ℜ

3,
	
10 + ⟨x, y⟩ℜ

3,
	
100 + ⟨x, y⟩ℜ

3 are a basis of the space
of cubic polynomials in ⟨x, y⟩ℜ. For simplicity we denote

 = ⟨x, y⟩ℜ.
For [α, β, γ, δ]T ∈R4, we need to ﬁnd [a, b, c, d]T ∈R4
such that
a
3 + b
	
1 + 

3 + c
	
10 + 

3 + d
	
100 + 

3
= α
3 + β
2 + γ 
 + δ.
(17)
Upon expanding the left-hand side of Eq. (17) and factoris-
ing it with respect to the basis [
3, 
2, 
, 1], we obtain
a
3 + b	1 + 

3 + c	10 + 

3 + d	100 + 

3
= a
3 + b
	
1 + 3
 + 3
2 + 
3
+ c
	
103 + 300
 + 30
2 + 
3
+ d
	
1003 + 3 × 1002
 + 300
2 + 
3
= 
3(a + b + c + d) + 
2(3b + 30c + 300d)
+ 
(3b+300c+3×1002d)+1(b+103c+1003d)
(18)
A comparison of the right-hand sides of Eqs. (17) and (18)
gives the linear equation
⎛
⎜⎜⎝
1 1
1
1
0 3 30
300
0 3 300 3 × 1002
0 1 103
1003
⎞
⎟⎟⎠
⎛
⎜⎜⎝
a
b
c
d
⎞
⎟⎟⎠=
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
independent basis of the set of cubic polynomials in 
 (the
independence property can be veriﬁed by [α, β, γ, δ] = 0 ⇒
[a, b, c, d] = 0).
Other linearly-independent bases of real cubic polynomials
on 
 were also considered, including {1, 
, 
2, 
3} and
{(b0 + 
)3, (b1 + 
)3, (b2 + 
)3, (b3 + 
)3} for different
parameters b0, b1, b2, b3 ∈R+. We have found that the chosen
basis (subkernels) provided the best results, in the MSE sense,
in the prediction setting considered.
