---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-000-c-quaternion-kernels
section_title: "Quaternion Kernels"
section_number: C
pages: 5-7
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
The introduced quaternion-va lued feature spaces allow us
to adopt the standard regression formulation, that is,
ˆy =
N∑
i=1
ai K(x, xi), ai ∈ H.
TOBAR AND MANDIC: QUATERNION REPRODUCING KERNEL HILBERT SPACES 5741
The following lemma states properties of quaternion posi-
tive deﬁnite kernels.
Lemma 2: Let K = Kr +iK i + jK j +kK k be a quaternion
kernel, then
(a) K is Hermitian iff K r is symmetric positive deﬁnite and
Ki =− K T
i ,K j =− K T
j and K k =− K T
k .
(b) If K is Hermitian, K is positive deﬁnite iff the
real-valued matrix representation4 of its Gram matrix is
positive deﬁnite.
Proof: (a) The Hermitian condition of the quaternion
kernel K = K H can be expressed in terms of its real an
imaginary parts as
Kr + iK i + jK j + kK k = K T
r − iK T
i − jK T
j − kK T
k .
Therefore, since {1, i, j, k} is a linearly-independent basis
of H, the above relationship is true if and only if the cor-
responding terms are equal coordinate-wise, that is:
Kr = K T
r , Ki =− K T
i , K j =− K T
j , Kk =− K T
k .
(b) Let us now re-state the matrix deﬁnition (Deﬁnition 3)
of positive deﬁniteness vH Kv > 0,∀v ∈ Hm \{ 0} as
ℜ{vH Kv} > 0( 6 )
ℑ{vH Kv}= 0. (7)
where K ∈ Hm×m is the Gram matrix corresponding to an
arbitrary collection of m points {x1,..., xm}⊂ X.O b s e r v e
that Eq. (6) is a necessary and sufﬁcient condition for a
Hermitian quaternion kernel K to be positive deﬁnite, since (7)
always holds due to the Hermitian property of the kernel:
2ℑ{vH Kv}= vH Kv − (vH Kv)H = vH Kv − (vH Kv) = 0.
To analyse (6) in terms of real and imaginary parts of the
quaternion kernel, we expand the vector v = vr + ivi + jv j +
kvk and the kernel matrix K = Kr + iKi + jK j + kKk using
their real and imaginary parts and rewrite Eq. (6) as
ℜ{vH Kv}= vT
r Kr vr + vT
i Kr vi + vT
j Kr v j + vT
k Kr vk
+2vT
i Ki vr + 2vT
j K j vr + 2vT
k Kk vr
+2vT
i K j vk + 2vT
j Kkvi + 2vT
k Ki v j > 0. (8)
Observe that Eq. (8) can be written as a quadratic positive-
deﬁnite form rT
v Qrv ≥ 0, where
rv =
⎛
⎜⎜⎝
vr
vi
v j
vk
⎞
⎟⎟⎠, Q =
⎛
⎜⎜⎝
Kr −Ki −K j −Kk
Ki Kr −Kk K j
K j Kk Kr −Ki
Kk −K j Ki Kr
⎞
⎟⎟⎠
are respectively an R4m representation of v and the real-valued
matrix representation of the Gram matrix of K .
We have therefore proved that the positive deﬁniteness
condition of a quaternion kernel can be veriﬁed through the
positive deﬁniteness of its real-valued matrix representation
and vice versa.
4See [45, p. 91] for the real matrix representation of quaternions.
D. Connections Between High-Dimensional Kernels
We next show that the matrix-valued, vector-valued, and
quaternion-valued kernels are not alternative representations
of the same mapping; they are different classes of kernels
and generate different featur e spaces. For the matrix-valued
kernel this follows from its dimension, which is given by the
number of data channels of the output. Consequently, a matrix
kernel cannot be designed to have an arbitrary dimension as
its quaternion- and vector-valued counterparts.
We now discuss whether a quaternion kernel and the par-
ticular case of a 4D vector kernel are two representations of
the same mapping. Although these share the same number of
degrees of freedom (four) and computational complexity, we
show that these are different mappings through the following
theorem.
Theorem 3: Let K and −→K be arbitrary quaternion- and
vector-kernels given by
K = K
r + iK i + jK j + kK k ∈ H
−→K =[ K1 K2 K3 K4]T ∈ R4,
where the real and imaginary parts of K , and the subkernels
of −→K are scalar, real-valued, functions.
The following statements about the R4 representation of K
and the quaternion representation of −→Ka r e t r u e :
(a) K′=[ Kr Ki K j Kk]T ∈ R4 is not a vector-kernel ,
(b) −→K ′= K1 + iK 2 + jK 3 + kK 4 ∈ H is not a Hermitian
positive deﬁnite quaternion-kernel .
Proof: The proof follows from the properties of vector and
quaternion kernels stated in Lemmas 1 and 2.
(a) Quaternion kernels are Hermitian and positive deﬁnite;
consequently, according to Lemma 2(a) the imaginary parts
of K given by K
i, K j, Kk are not symmetric. Therefore, based
on Lemma 1, the array K′=[ Kr Ki K j Kk] is not a vector-
kernel (since its subkernels are not symmetric and positive
deﬁnite).
(b) As −→K is a vector-kernel, Lemma 1 states that
K1, K2, K3 are symmetric and positive deﬁnite. Therefore,−→K ′ = K1 + iK 2 + jK 3 + kK 4 is not Hermitian due to
Lemma 2(b). □
We now state the main consequence of Theorem 3.
Although the R4 representation of the QRKHS generated by
a quaternion kernel K of the form
HR =
⎧
⎪⎪⎨
⎪⎪
⎩
⎛
⎜⎜⎝
ℜ f (x)
ℑ
i f (x)
ℑj f (x)
ℑk f (x)
⎞
⎟⎟⎠ ∈ R4, s.t. f (x) =
∞∑
n=1
an K(xn, x)
⎫
⎪⎪⎬
⎪⎪
⎭
(9)
where a
n ∈ H, x ∈ X, is indeed an RKHS (its evaluation
functional is bounded), its real vector-valued reproducing
kernel is not given by the R4 representation of the quaternion
kernel K′=[ Kr Ki K j Kk] of K ∈ H, because K′ is not a
vector kernel in R4.
Remark 8: The vector-valued representation of a QRKHS
in Eq. (9) is a VRKHS, however, ﬁnding its associated vector-
valued kernel is not trivial.
5742 IEEE TRANSACTIONS ON INFORMATION THEORY , VOL. 60, NO. 9, SEPTEMBER 2014
TABLE I
NUMBER OF OPERATIONS REQUIRED TO EVA L UAT E T H ETERM AK (xs, x) FOR AN n-DIMENSIONAL OUTPUT AND A SINGLE SUPPORT VECTOR xs .
THE COMPARISON IS PRESENTED FOR REAL -VALUED (SCALAR ), QUATERNION -VALUED (SCALAR ), VECTOR -VALUED (R4-VALUED ), AND
MATRI X-VALUED (Rn×n –A CCORDING TO THE OUTPUT )K ERNELS .T HE TERMS κR,κ Q DENOTE RESPECTIVEL Y REAL AND QUATERNION KERNEL
EV ALUATIONS WHILE μR,μ Q DENOTE SCALAR MULTIPLICATIONS .T HE COMPUTATIONAL COMPLEXITY DUE TO SUMMATIONS IS OMITTED AS IT IS
NEGLIGIBLE COMPARED TO MULTIPLICATIONS AND KERNEL EV ALUATIONS
E. Computational Complexity
Table I illustrates the computational complexity of kernel
regression algorithms for scalar, quaternion, multikernel and
matrix-kernel approaches. Observe that scalar kernels are
simplest, whereas the complexity of matrix kernels grows
quadratically with the dimension of the signal.
In order to compare the complexity associated to vector- and
quaternion-valued kernels, observe that (i) μ
R involves four
pure real multiplications (real kernels, quaternion weights)
while μQ involves 16 (quaternion valued kernels and weights),
and (ii) the quaternion kernel evaluation can be seen as the
evaluation of four real functions. Consequently, by assuming
κQ ∼ 4κR,μ Q ∼ 4μR, Table I shows that the computational
complexities of both kernel and quaternion kernel algorithms
are of the same order.
Therefore, the implementation of both vector and quaternion
kernels can beneﬁt from exploiting the similarity among sub-
kernels, as well as from an efﬁcient framework to perform
quaternion operations [46].
V. D ESIGN OF QUATERNION -VALUED MERCER KERNELS
Theorem 2 gives the justiﬁcation for the design and imple-
mentation of nonlinear kernel algorithms operating in QRKHS
to simplify into the choice of a positive-semideﬁnite kernel.
We next introduce and analyse the properties of some speciﬁc
kernels of quaternion variable and justify their use within
quaternion SVR algorithms.
A. Polynomial Kernel: The Quaternion Cubic Example
The polynomial kernel is standard in kernel-based estima-
tion due to its robustness and ease of implementation. For real-
and complex-valued samples x
r, yr , the polynomial kernel is
given by
K P(xr, yr) =
⎥
1 + xT
r yr
⎦p
where p ∈ N is referred to as the order of the kernel. On the
other hand, the real-valued polynomial kernel of quaternion
samples x, y KRP : X2 → R, that is, the polynomial kernel of
the real-valued representations of x and y, can be expressed as
KRP (x, y) =
⎥
1 + ⟨x, y⟩ℜ
⎦p =
⎥
1 +ℜ {xH y}
⎦p (10)
where ⟨x, y⟩ℜ is the inner product in Rn and ℜ{q} denotes the
real part of the quaternion q.
The extension to quaternion-valued polynomial kernels is
not straightforward, as for the quaternion vectors x and y the
factorisation ⎥1 + xH y⎦p = φH (x)φ(y)
may not be possible due to the noncommutativity of the
quaternion ring, and therefore the positive deﬁniteness of such
kernel cannot be guaranteed in this manner.
For p = 3, we next propose a quaternion polynomial kernel
which admits factorisation as an inner product, thus ensuring
the required positive deﬁniteness.
Consider the quaternion cubic kernel KQP : X2 → H
given by
KQP (x, y) =
⎥
1 + xH x
⎦⎥
1 + xH y
⎦⎥
1 + yH y
⎦
. (11)
To show that KQP is positive semideﬁnite, we shall ﬁrst
consider its factorisation of the form KQP (x, y) = φH (x)φ(y).
Indeed,
KQP (x, y) = ⎥1 + xH x⎦⎥1 + yH y⎦
+
⎥
1 + xH x
⎦
xH y
⎥
1 + yH y
⎦
= ⎥1 + xH x⎦H⎥1 + yH y⎦
+
⎥
x
⎥
1 + xH x
⎦⎦H⎥
y
⎥
1 + yH y
⎦⎦
= φH
