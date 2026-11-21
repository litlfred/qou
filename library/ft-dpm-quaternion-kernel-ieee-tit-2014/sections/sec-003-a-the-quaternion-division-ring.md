---
doc_id: ft-dpm-quaternion-kernel-ieee-tit-2014
doc_title: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions"
section_id: sec-003-a-the-quaternion-division-ring
section_title: "The Quaternion Division Ring"
section_number: A
pages: 2-2
source_pdf: FT_DPM_Quaternion_Kernel_IEEE_TIT_2014.pdf
source_sha256: aa2f1eb73610a81b
toc_source: inferred
doc_brief: "Quaternion Reproducing Kernel Hilbert Spaces: Existence and Uniqueness Conditions — The existence and uniqueness conditions of quater- nion reproducing kernel Hilbert spaces (QRKHS) are established"
---
The quaternion set H is a four-dimensional vector space
over the real ﬁeld R spanned by the linearly independent
basis {1, i, j, k} [29]. Accordingly, any element q ∈H can
be written as a linear combination q = a1 + bi + cj + dk,
where a, b, c, d ∈R.
The sum and the scalar multiplication are deﬁned in an
element-wise fashion as in R4, that is
⎛
⎜⎜⎝
a1
b1
c1
d1
⎞
⎟⎟⎠+
⎛
⎜⎜⎝
a2
b2
c2
d2
⎞
⎟⎟⎠=
⎛
⎜⎜⎝
a1 + a2
b1 + b2
c1 + c2
d1 + d2
⎞
⎟⎟⎠
α(a, b, c, d) = (αa, αb, αc, αd),
α ∈R
(1)
where the notation (a, b, c, d) = (a, b, c, d)T = a1 + bi +
cj + dk ∈H is used for convenience of presentation.
Remark 1: The pair (H, +) is an Abelian group [10], for
which the addition operation is deﬁned in (1) and the additive
identity is 0 = (0, 0, 0, 0) ∈H.
The quaternion multiplication (or Hamilton product) is a
bilinear mapping H × H →H, (p, q) →pq, deﬁned by
pq =
⎛
⎜⎜⎝
a1
b1
c1
d1
⎞
⎟⎟⎠
⎛
⎜⎜⎝
a2
b2
c2
d2
⎞
⎟⎟⎠=
⎛
⎜⎜⎝
a1a2 −b1b2 −c1c2 −d1d2
a1b2 + b1a2 + c1d2 −d1c2
a1c2 −b1d2 + c1a2 + d1b2
a1d2 + b1c2 −c1b2 + d1a2
⎞
⎟⎟⎠.
(2)
Remark 2: The quaternion product deﬁned in (2) distributes
over the sum, i.e. ∀p, q,r ∈H
p(q + r) = pq + pr
(p + q)r = pr + qr.
It is also possible to express the quaternion multiplication
using the basis expansion representation, that is, (a11 +
b1i + c1 j + d1k)(a21 + b2i + c2 j + d2k), and applying the
multiplication rule
i2 = j2 = k2 = i jk = −1.
Note that the basis element 1 = (1, 0, 0, 0) ∈H is the
multiplicative identity, meaning that q1 = 1q = q, ∀q ∈H,
and is therefore omitted in the basis representation, q = a +
bi + cj + dk. We refer to the factor of (1, 0, 0, 0) as real part
of q, denoted by ℜ{q} = a, and to the remaining factors as
the imaginary part of q, denoted by ℑ{q} = (0, b, c, d).
For any given element q ∈H, q̸ = 0, its multiplicative
inverse q−1 ∈H \ {0} is given by
q−1 =
q∗
∥q∥2 ,
where q∗= (a, −b, −c, −d) denotes the conjugate of q,
and ∥q∥= √q∗q = √qq∗=
√
a2 + b2 + c2 + d2 denotes
the norm in H deﬁned as the Euclidean norm in R4; as a
consequence, qq−1 = q−1q = 1, ∀q̸ = 0. By using the
conjugate operator, the real and imaginary parts of q ∈H
can be written respectively as
ℜ{q} = q + q∗
2
,
ℑ{q} = q −q∗
2
.
Remark 3: The pair (H, ·) equipped with the identity ele-
ment is a monoid under multiplication, while the inclusion of
the multiplicative inverse makes (H\{0}, ·) a group [33], [34].
Remark 4: Since (H, +) is an Abelian group (Remark 1),
(H, ·) is a group (Remark 3), and the quaternion product
distributes over the sum (Remark 2), the triplet (H, +, ·) is
a non-commutative division ring [34].
Despite the lack of commutativity in H, its division ring
properties establish the basis for the design of estimation
algorithms. Furthermore, H is one of the four normed division
algebras over the real ﬁeld, the other three being the real
ﬁeld R, the complex ﬁeld C, and the non-associative unitary
octonion ring O (see the Frobenius theorem [35]).
