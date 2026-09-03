---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-027-66-the-local-asymptotics-for-the-weighted-bergma
section_title: "The local asymptotics for the weighted Bergman kernel: the corrective algorithm. We"
section_number: 6.6
pages: 18-20
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
recall from Subsection 6.3 that the kernel Mm(z, w) given by (6.3.1) is a local reproducing
kernel mod(e−δ0m) (see Proposition 6.1). The kernel Mm(z, w) is automatically holomorphic in
z ∈D(z0, r), and we would like to correct it so that it becomes conjugate-holomorphic in w,
while maintaining the approximate reproducing property. In view of the negligible amplitude
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
19
calculation (6.4.4), the approximate reproducing property (with a worse precision) will be kept
if we replace Mm by the kernel
K⟨k⟩
m (z, w) := b⟨k⟩(z, w) e2mQ(z,w),
where
(6.6.1)
b⟨k⟩:= mb0 + b1 + · · · + m−k+1bk
is a ﬁnite asymptotic expansion (where each term bj is independent of m), with
(6.6.2)
b⟨k⟩= 2m
π
¯∂wθ + ¯∂wθ [∇X]⟨k⟩.
Here, X ∼X0 + m−1X1 + m−2X2 + . . . is an asymptotic expansion in m (where every Xj is
independent of m), and each Xj(z, w) should be holomorphic in z and C∞-smooth in w. Then
K⟨k⟩
m (z, w) is a local reproducing kernel mod(m−k) as a result of perturbing by the abschnitt of
a negligible amplitude (multiplied by e2mQ(z,w)). We want to add the condition that b⟨k⟩(z, w)
be conjugate-holomorphic in w, to obtain a local Bergman kernel mod(m−k). This amounts to
asking that bj(z, w) is holomorphic in ¯w. The way this will enter into the algorithm is that such
functions are uniquely determined by their diagonal restrictions.
It is convenient to express (6.6.2) is the form
(6.6.3)
b⟨k⟩
¯∂wθ = 2m
π + [∇X]⟨k⟩.
For convenience of notation, we think of b⟨k⟩as the abschnitt of an asymptotic expansion
b ∼mb0 + b1 + m−1b2 + . . .. Proposition 6.2 tells us how to solve (6.6.3): we just apply the
diﬀusion operator S to both sides and check that the abschnitts coincide along the diagonal
z = w. More concretely, b⟨k⟩solves (6.6.3) for some X if and only if

S
 b
¯∂wθ

−2m
π
⟨k⟩
∈Mz−wR1,
which is the same as
(6.6.4)

S
m−1b
¯∂wθ
⟨k+1⟩
−2
π ∈Mz−wR1.
When we expand the condition (6.6.4), we ﬁnd that it is equivalent to having
(6.6.5)
b0
¯∂wθ
−2
π ∈Mz−wR1,
and
(6.6.6)
j
X
i=0
1
i!2i (∂w∂θ)i
( bj−i
¯∂wθ
)
∈Mz−wR1,
j = 1, . . ., k.
From the Taylor expansion (6.2.3), we see that
¯∂wθ(z, w) −∂z ¯∂wQ(z, w) ∈Mz−wR1,
so that (6.6.5) is equivalent to
b0(z, w) −2
π∂z ¯∂wQ(z, w) ∈Mz−wR1.
20
ANTTI HAIMI AND HAAKAN HEDENMALM
Taking the restriction to the diagonal, we obtain that b0(z, z) = 2
π∆Q(z), and as the diagonal
z = w is a uniqueness set for functions that are holomorphic in (z, ¯w), the only possible choice
is
b0(z, w) := 2
π∂z ¯∂wQ(z, w).
The rest of the functions bj are obtained in explicit form using (6.6.6). To illustrate how this
works, we show how to obtain b1. By (6.6.6) with j = 1, we have
(6.6.7)
b1
¯∂wθ
+ 1
2∂w∂θ
(
b0
¯∂wθ
)
∈Mz−wR1.
We plug in the expression for b0 which we obtained above, and restrict (6.6.7) to the diagonal
z = w:
b1(z, z)
∆Q(z, z) = −1
2∂w∂θ
( 2
π∂z ¯∂wQ(z, w)
¯∂wθ
)

w:=z
.
After some necessary simpliﬁcations, this leads to the formula
b0(z, z) = 1
2π∆log ∆Q(z),
and the only possible choice for b0(z, w) which is holomorphic in (z, ¯w) is the polarization of
the above,
b0(z, w) = 1
2π∂z ¯∂w log[∂z ¯∂wQ(z, w)].
We note that the expressions for bj(z, w) are well-deﬁned and holomorphic in (z, ¯w) on the
bidisk D(z0, r) × D(z0, r), at least for j = 0 and j = 1. This will be the case for all other indices
j as well, because the expressions for b1
j(z, w) will only involve polynomial expressions in
some derivatives of ∂z ¯∂wQ(z, w) possibly divided by a positive integer power of ∂z ¯∂wQ(z, w).
This allows us to work with the local Bergman kernel K⟨k⟩(z, w) in the context of the bidisk
D(z0, r) × D(z0, r).
