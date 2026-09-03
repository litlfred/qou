---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-026-65-a-formal-diﬀusion-operator-and-the-characteri
section_title: "A formal diﬀusion operator and the characterization of negligible amplitudes. Next, to"
section_number: 6.5
pages: 16-18
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
deﬁne the diﬀusion operator S, we need the two diﬀerential operators
(6.5.1)
∂w = ∂w −∂wθ
¯∂wθ
¯∂w,
∂θ =
1
¯∂wθ
¯∂w.
These operators come from the change of variables (z, w, ¯w) →(z, w, θ), but this is of no
real signiﬁcance to us here. What is, however, important is the property that they commute
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
17
(∂w∂θ = ∂θ∂w), and the formula for the commutator of ∂w and Mz−w (see (6.5.9) below). In
terms of the above diﬀerential operators, ∇simpliﬁes:
(6.5.2)
∇= ∂θ + 2mMz−w.
The diﬀusion operator S is deﬁned (rather formally) by
(6.5.3)
S := e(2m)−1∂w∂θ =
∞
X
j=0
1
j!(2m)j (∂w∂θ)j.
The relation with diﬀusion comes from thinking about ∂w∂θ as a generalized Laplacian, so that
S is the 1/(2m)forwardtime step for the corresponding generalized diﬀusion (or heat) equation.
Our analysis will not require the series expansion (6.5.3) to converge in any meaningful way.
It is supposed to act on asymptotic expansions of the type
(6.5.4)
a(z, w) ∼ma0(z, w) + a1(z, w) + m−1a2(z, w) + m−2a3(z, w) + . . .,
in the obvious fashion. Here, the functions aj(z, w) are assumed not to depend on the parameter
m. As for the meaning of an asymptotic expansion like (6.5.4), we should require that
a(z, w) =
k
X
j=0
m−j+1aj(z, w) + O(m−k).
Actually, we may even think that the left hand side represents the right-hand side more
abstractly in the sense of the abschnitts (partial sums)
a⟨k⟩(z, w) =
k
X
j=0
m−j+1aj(z, w),
so that a(z, w) need not be a well-deﬁned function, it would just be a stand-in for the sequence
of abschnitts a⟨k⟩(z, w), k = 1, 2, 3, . . .. In this sense, the meaning of Sa clariﬁes completely. We
observe from the way S is deﬁned that
(6.5.5)
[Sa⟨k⟩]⟨k⟩= [Sa]⟨k⟩.
and likewise for its inverse
(6.5.6)
[S−1a⟨k⟩]⟨k⟩= [S−1a]⟨k⟩.
Here, the inverse operator S−1 is given by the (rather formal) expansion
(6.5.7)
S−1 := e−(2m)−1∂w∂θ =
∞
X
j=0
(−1)j
j!(2m)j (∂w∂θ)j.
The important property of S, which is veriﬁed by a simple algebraic computation, is that
(6.5.8)
S∇= 2mMz−wS.
We include the calculation which gives (6.5.8), as it is elegant and quite simple. First, we note
that
∂j
wMz−w∂j
θ = −j∂θ(∂θ∂w)j−1 + Mz−w(∂θ∂w)j,
j = 1, 2, 3, . . .,
which follows from the calculation
(6.5.9)
∂j
wMz−w = −j∂j−1
w
+ Mz−w∂j
w,
j = 1, 2, 3, . . ..
18
ANTTI HAIMI AND HAAKAN HEDENMALM
Finally, we expand S∇:
S∇= e(2m)−1∂θ∂w∇= e(2m)−1 ∂θ∂w(∂θ + 2mMz−w)
=
+∞
X
j=0
1
j!(2m)j ∂j
w∂j
θ(∂θ + 2mMz−w) = ∂θ e(2m)−1∂θ∂w +
+∞
X
j=0
1
j!(2m)j−1 ∂j
w Mz−w ∂j
θ
= ∂θ e(2m)−1∂θ∂w −
+∞
X
j=1
1
(j −1)!(2m)j−1 ∂θ(∂θ∂w)j−1 +
+∞
X
j=1
1
j!(2m)j−1 Mz−w(∂θ∂w)j
= 2mMz−w em−1∂θ∂w = 2mMz−wS,
as needed.
The reason why we consider the diﬀusion operator S is outlined in the following proposition
(see [8]). As for notation, let R1 denote the algebra of all functions f(z, w) that are holomorphic
in z and C∞-smooth in w (near the diagonal z = w).
Proposition 6.2. Fix an integer k = 1, 2, 3 . . .. Suppose a(z, w) has the asymptotic expansion (6.5.4),
i.e., a ∼ma0 + a1 + m−1a2 + m−2a3 + . . ., where the functions aj ∈R1 are all independent of m. Then
the following are equivalent:
(i) We have that
[Sa]⟨k⟩∈Mz−wR1.
(ii) We have that
a⟨k⟩= [∇A]⟨k⟩,
for some function A(z, w) = Pk
j=0 m−jAj(z, w), where each aj ∈R1 is independent of m.
Proof. Suppose ﬁrst that (ii) holds. Then, by (6.5.5) and (6.5.8), we have that
(6.5.10)
[Sa]⟨k⟩= [Sa⟨k⟩]⟨k⟩= [S[∇A]⟨k⟩]⟨k⟩= [S∇A]⟨k⟩= Mz−w[2mSA]⟨k⟩= 2mMz−w[SA]⟨k+1⟩,
and (i) follows.
Next, we suppose instead that (i) holds, so that [Sa]⟨k⟩= Mz−wα for some function α(z, w) =
Pk
j=0 m1−jαj(z, w), where the αj(z, w) are independent of m, and holomorphic in z and C∞-
smooth in w near the diagonal z = w. We would like to ﬁnd an A of the form prescribed by
(ii). In view of the calculation (6.5.10), it is clear that if A can be found, then we must have
α = [2mSA]⟨k⟩= 2m[SA]⟨k+1⟩. Finally, by (6.5.6), we realize that A = (2m)−1[S−1α]⟨k⟩. Finally, we
plug in A := (2m)−1[S−1α]⟨k⟩and check that it is of the right form, with [∇A]⟨k⟩= a⟨k⟩. Indeed,
we see by applying S−1 from the left and the right on both sides of (6.5.8) using (6.5.5) and
(6.5.6) that
(6.5.11)
∇S−1 = 2mS−1Mz−w,
so that
[∇A]⟨k⟩= [(2m)−1∇S−1α]⟨k⟩= [S−1Mz−wα]⟨k⟩= [S−1Sa]⟨k⟩= a⟨k⟩,
as needed.
□
