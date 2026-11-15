---
doc_id: s0894-0347-00-00337-4
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(00)00337-4"
section_id: sec-008-23-various-formulas-for-the-kernel-j
section_title: "Various formulas for the kernel J"
section_number: 2.3
pages: 12-14
source_pdf: S0894-0347-00-00337-4.pdf
source_sha256: 1c6848281fc2804c
toc_source: outline
---
tion of x, the function J(x, y) is entire in x and y. We shall now obtain several
denominator–free formulas for the kernel J.
Proposition 2.6.
J(x, y; θ) =
∞
X
m=0
(−1)m
(x + y + m + 2)m
Γ(x + m + 2)Γ(y + m + 2)
θ
x+y
2
+m+1
m!
.
(2.14)
Proof. Straightforward computation using a formula due to Nielsen (see Section
5.41 of [43] or [14], formula 7.2.(48)).
Proposition 2.7. Suppose x + y > −2. Then
J(x, y; θ) = 1
2
Z 2
√
θ
0
(Jx(z) Jy+1(z) + Jx+1(z) Jy(z)) dz.
Proof. Follows from a computation done in the proof of Proposition 2.3,
∂
∂θ J(x, y; θ) =
1
2
√
θ
(Jx Jy+1 + Jx+1 Jy) ,
Jx = Jx(2
√
θ) ,
ASYMPTOTICS OF PLANCHEREL MEASURES
493
and the following corollary of (2.14):
J(x, y; 0) = 0 ,
x + y > −2 .
Remark 2.8. Observe that by Proposition 2.7 the operator
∂J
∂θ is a sum of two
operators of rank 1.
Proposition 2.9.
J(x, y; θ) =
∞
X
s=1
Jx+s Jy+s ,
Jx = Jx(2
√
θ).
(2.15)
Proof. Our argument is similar to an argument due to Tracy and Widom; see the
proof of the formula (4.6) in [36]. The recurrence relation (2.8) implies that
J(x + 1, y + 1) −J(x, y) = −Jx+1 Jy+1 .
(2.16)
Consequently, the diﬀerence between the left-hand side and the right-hand side of
(2.15) is a function which depends only on x −y. Let x and y go to inﬁnity in
such a way that x −y remains ﬁxed. Because of the asymptotics (2.9) both sides
in (2.15) tend to zero and, hence, the diﬀerence actually is 0.
In the same way as in [36] this results in the following
Corollary 2.10. For any a ∈Z, the restriction of the kernel J to the subset {a, a+
1, a + 2, . . . } ⊂Z deﬁnes a nonnegative trace class operator in the ℓ2 space on that
subset.
Proof. By Proposition 2.9, the restriction of J on {a, a+1, a+2, . . .} is the square of
the kernel (x, y) 7→Jx+y+1−a(2
√
θ). Since the latter kernel is real and symmetric,
the kernel J is nonnegative.
Hence, it remains to prove that its trace is ﬁnite.
Again, by Proposition 2.9, this trace is equal to
∞
X
s=1
s (Ja+s+1(2
√
θ))2.
This sum is clearly ﬁnite by (2.9).
Remark 2.11. The kernel J resembles a Christoﬀel–Darboux kernel and, in fact,
the operator in ℓ2(Z) deﬁned by the kernel J is an Hermitian projection operator.
Recall that K = L(1 + L)−1, where L is of the form
L =
 0
A
−A∗
0

.
One can prove that this together with Lemma 2.5 imply that J is an Hermitian
projection kernel. However, in contrast to a Christoﬀel–Darboux kernel, it projects
to an inﬁnite–dimensional subspace.
Note that in [17] the restriction of the kernel J to Z+ was obtained as a limit of
Christoﬀel–Darboux kernels for Charlier polynomials.
494
A. BORODIN, A. OKOUNKOV, AND G. OLSHANSKI
2.4. Commuting diﬀerence operator. Consider the diﬀerence operators ∆and
∇on the lattice Z,
(∆f)(k) = f(k + 1) −f(k) ,
(∇f)(k) = f(k) −f(k −1) .
Note that ∇= −∆∗as operators on ℓ2(Z). Consider the following second order
diﬀerence Sturm–Liouville operator:
D = ∆◦α ◦∇+ β ,
(2.17)
where α and β are operators of multiplication by certain functions α(k), β(k). The
operator (2.17) is self–adjoint in ℓ2(Z). A straightforward computation shows that
(2.18)

Df

(k) = (−α(k + 1) −α(k) + β(k))f(k)
+ α(k)f(k −1) + α(k + 1)f(k + 1) .
It follows that if α(s) = 0 for a certain s ∈Z, then the space of functions f(k)
vanishing for k < s is invariant under D.
Proposition 2.12. Let [J]s denote the operator in ℓ2({s, s+1, . . .}) obtained by re-
stricting the kernel J to {s, s+1, . . .}. Then the diﬀerence Sturm–Liouville operator
(2.17) commutes with [J]s provided
α(k) = k −s,
β(k) = −k(k + 1 −s −2
√
θ)
√
θ
+ const .
Proof. Since [J]s is the square of the operator with the kernel Jk+l+1−s, it suﬃces
to check that the latter operator commutes with D, with the above choice of α and
β. But this is readily checked using (2.18).
This proposition is a counterpart of a known fact about the Airy kernel; see [36].
Moreover, in the scaling limit when θ →∞and
k = 2
√
θ + x θ1/6,
s = 2
√
θ + ς θ1/6,
the diﬀerence operator D becomes, for a suitable choice of the constant, the diﬀer-
ential operator
d
dx ◦(x −ς) ◦d
dx −x(x −ς),
which commutes with the Airy operator restricted to (ς, +∞). The above diﬀeren-
tial operator is exactly that of Tracy and Widom [36].
Remark 2.13. Presumably, this commuting diﬀerence operator can be used to ob-
tain, as was done in [36] for the Airy kernel, asymptotic formulas for the eigenvalues
of [J]s, where s = 2
√
θ + ς θ1/6 and ς ≪0. Such asymptotic formulas may be very
useful if one wishes to reﬁne Theorem 4 and to establish convergence of moments
in addition to convergence of distribution functions. For individual distributions of
λ1 and λ2 the convergence of moments was obtained, by other methods, in [3, 4].
