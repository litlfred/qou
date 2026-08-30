---
doc_id: arxiv-math-9905032v2
doc_title: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS"
section_id: sec-019-23-various-formulas-for-the-kernel-j-recall-that
section_title: "Various formulas for the kernel J. Recall that since Jx is an"
section_number: 2.3
pages: 16-17
source_pdf: 9905032v2.pdf
source_sha256: ba933d4cb484964b
doc_brief: "ASYMPTOTICS OF PLANCHEREL MEASURES FOR SYMMETRIC GROUPS — We consider the asymptotics of the Plancherel mea- sures on partitions of n as n goes to inﬁnity."
---
entire function of x, the function J(x, y) is entire in x and y. We shall
now obtain several denominator–free formulas for the kerne l J.
Proposition 2.6.
J(x, y; θ) =
∞∑
m=0
(−1)m (x + y + m + 2)m
Γ( x + m + 2)Γ( y + m + 2)
θ
x+y
2 +m+1
m! .(2.14)
Proof. Straightforward computation using a formula due to Nielsen ,
see Section 5.41 of [39] or [12], formula 7.2.(48) .
Proposition 2.7. Suppose x + y > −2. Then
J(x, y; θ) = 1
2
∫ 2
√
θ
0
(Jx(z) Jy+1(z) + Jx+1(z) Jy(z)) dz
Proof. Follows from a computation done in the proof of Proposition 2 .3
∂
∂θ J(x, y; θ) = 1
2
√
θ
(Jx Jy+1 + Jx+1 Jy) , J x = Jx(2
√
θ) ,
and the following corollary of (2.14)
J(x, y; 0) = 0 , x + y > −2 .
Remark 2.8. Observe that by Proposition 2.7 the operator ∂ J
∂θ is a
sum of two operators of rank 1.
Proposition 2.9.
J(x, y; θ) =
∞∑
s=1
Jx+s Jy+s , J x = Jx(2
√
θ).(2.15)
Proof. Our argument is similar to an argument due to Tracy and Widom,
see the proof of the formula (4.6) in [32]. The recurrence rel ation (2.8)
implies that
J(x + 1, y + 1) − J(x, y) = −Jx+1 Jy+1(2.16)
ASYMPTOTICS OF PLANCHEREL MEASURES 17
Consequently, the diﬀerence between the left-hand side and the right-
hand side of (2.15) is a function which depends only on x − y. Let x
and y go to inﬁnity in such a way that x − y remains ﬁxed. Because of
the asymptotics (2.9) both sides in (2.15) tend to zero and, h ence, the
diﬀerence actually is 0.
In the same way as in [32] this results in the following
Corollary 2.10. For any a ∈ Z, the restriction of the kernel J to the
subset {a, a + 1, a + 2, . . .} ⊂ Z determines a nonnegative trace class
operator in the ℓ2 space on that subset.
Proof. By Proposition 2.9, the restriction of J on {a, a + 1, a + 2, . . .}
is the square of the kernel ( x, y) ↦→Jx+y+1−a(2
√
θ). Since the latter
kernel is real and symmetric, the kernel J is nonnegative. Hence, it
remains to prove that its trace is ﬁnite. Again, by Propositi on 2.9, this
trace is equal to
∞∑
s=1
s (Ja+s+1(2
√
θ))2.
This sum is clearly ﬁnite by (2.9).
Remark 2.11. The kernel J resembles a Christoﬀel–Darboux kernel
and, in fact, the operator in ℓ2(Z) deﬁned by the kernel J is an Her-
mitian projection operator. Recall that K = L(1 + L)−1, where L is of
the form
L =
[
0 A
−A∗ 0
]
On can prove that this together with Lemma 2.5 implies that J is an
Hermitian projection kernel. However, in contrast to a Chri stoﬀel–
Darboux kernel, it projects to an inﬁnite–dimensional subs pace.
