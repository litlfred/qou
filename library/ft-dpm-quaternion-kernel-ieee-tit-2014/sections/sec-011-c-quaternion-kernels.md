---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-011-c-quaternion-kernels
section_title: "Quaternion Kernels"
section_number: C
pages: 5-6
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
The introduced quaternion-valued feature spaces allow us
to adopt the standard regression formulation, that is,
ˆy =
N

i=1
ai K(x, xi), ai ∈H.
The following lemma states properties of quaternion posi-
tive deﬁnite kernels.
Lemma 2: Let K = Kr +i Ki + j K j +kKk be a quaternion
kernel, then
(a) K is Hermitian iff Kr is symmetric positive deﬁnite and
Ki = −K T
i , K j = −K T
j and Kk = −K T
k .
(b) If
K
is Hermitian,
K
is positive deﬁnite iff the
real-valued matrix representation4 of its Gram matrix is
positive deﬁnite.
Proof:
(a) The Hermitian condition of the quaternion
kernel K = K H can be expressed in terms of its real an
imaginary parts as
Kr + i Ki + j K j + kKk = K T
r −i K T
i −j K T
j −kK T
k .
Therefore, since {1, i, j, k} is a linearly-independent basis
of H, the above relationship is true if and only if the cor-
responding terms are equal coordinate-wise, that is:
Kr = K T
r , Ki = −K T
i , K j = −K T
j , Kk = −K T
k .
(b) Let us now re-state the matrix deﬁnition (Deﬁnition 3)
of positive deﬁniteness vHKv > 0, ∀v ∈Hm \ {0} as
ℜ{vHKv} > 0
(6)
ℑ{vHKv} = 0.
(7)
where K ∈Hm×m is the Gram matrix corresponding to an
arbitrary collection of m points {x1, . . . , xm} ⊂X. Observe
that Eq. (6) is a necessary and sufﬁcient condition for a
Hermitian quaternion kernel K to be positive deﬁnite, since (7)
always holds due to the Hermitian property of the kernel:
2ℑ{vHKv} = vHKv −(vHKv)H = vHKv −(vHKv) = 0.
To analyse (6) in terms of real and imaginary parts of the
quaternion kernel, we expand the vector v = vr +ivi + jv j +
kvk and the kernel matrix K = Kr + iKi + jK j + kKk using
their real and imaginary parts and rewrite Eq. (6) as
ℜ{vHKv} = vT
r Krvr + vT
i Krvi + vT
j Krv j + vT
k Krvk
+2vT
i Kivr + 2vT
j K jvr + 2vT
k Kkvr
+2vT
i K jvk + 2vT
j Kkvi + 2vT
k Kiv j > 0.
(8)
Observe that Eq. (8) can be written as a quadratic positive-
deﬁnite form rT
v Qrv ≥0, where
rv =
⎛
⎜⎜⎝
vr
vi
v j
vk
⎞
⎟⎟⎠,
Q =
⎛
⎜⎜⎝
Kr −Ki −K j −Kk
Ki
Kr
−Kk
K j
K j
Kk
Kr
−Ki
Kk −K j
Ki
Kr
⎞
⎟⎟⎠
are respectively an R4m representation of v and the real-valued
matrix representation of the Gram matrix of K.
We have therefore proved that the positive deﬁniteness
condition of a quaternion kernel can be veriﬁed through the
positive deﬁniteness of its real-valued matrix representation
and vice versa.
4See [45, p. 91] for the real matrix representation of quaternions.
