---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-024-63-approximate-local-reproducing-and-bergman-ker
section_title: "Approximate local reproducing and Bergman kernels. In [8], the point of departure is"
section_number: 6.3
pages: 14-16
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
an approximate reproducing identity for functions in A2
m. To state the result, we deﬁne the
kernel
(6.3.1)
Mm(z, w) := 2m
π e2mQ(z,w) ¯∂wθ(z, w).
This kernel is for obvious reasons only deﬁned in some ﬁxed neighborhood of the diagonal.
We shall be concerned with the (small) bidisk D(z0, r)×D(z0, r) where Mm(z, w) is well-deﬁned,
by our assumptions (A:i)–(A:iv) above.To extend the kernel beyond the bidisk, we multiply
by a smooth cut-oﬀfunction χ0(w), and think of the product as 0 oﬀthe support of χ0 (also
where Mm(z, w) is undeﬁned). The function χ0(w) is C∞-smooth with 0 ≤χ0 ≤1 throughout
C, and vanishes oﬀD(z0, 3
4r), while it has χ0 = 1 on D(z0, 2
3r), and is a function of the distance
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
15
|w −z0|. We ask in addition that the norm ∥¯∂χ0∥L2(Ω) is bounded by an absolute constant, which
is possible to achieve. We will use the simpliﬁed notation
(6.3.2)
∥u∥m := ∥u∥L2(Ω,e−2mQ) =
 Z
Ω
|u|2e−2mQdA
1/2
.
Proposition 6.1. We have that for all u ∈A2
m,
u(z) =
Z
Ω
u(w)χ0(w)Mm(z, w) e−2mQ(w)dA(w) + O(r−1∥u∥memQ(z)−mδ0),
z ∈D(z0, 1
3r),
where we write δ0 := 1
18r2ǫ0 > 0. The implied constant is absolute.
To develop the necessary intuition, we supply the easy proof.
Proof of Proposition 6.1. Since the Cauchy kernel 1/(πz) is the fundamental solution to ¯∂, we
have by Cauchy-Green theorem (i.e., integration by parts) that
(6.3.3)
u(z) = χ0(z)u(z) =
Z
Ω
1
π(z −w)
¯∂w

u(w)χ0(w) e2m(z−w)θ(z,w)
dA(w)
=
Z
Ω
u(w)χ0(w)Mm(z, w) e−2mQ(w)dA(w)
+ 1
π
Z
Ω
u(w)
¯∂wχ0(w)
z −w e2m(z−w)θ(z,w)dA(w),
z ∈D(z0, 1
3r).
It will be enough to show that the last term on the right-hand side of (6.3.3) (the one which
involves ¯∂wχ) belongs to the error term. By (6.2.1) and the Cauchy-Schwarz inequality, we
have that
(6.3.4)
1
π
Z
Ω

u(w)
¯∂wχ0(w)
z −w e2m(z−w)θ

dA(w) ≤
Z
Ω

u(w)
¯∂wχ0(w)
z −w

 emQ(z)−mQ(w)−1
2 m∆Q(z)|w−z|2dA(w)
≤∥u∥memQ(z)
 Z
Ω

¯∂wχ0(w)
z −w

2
e−m∆Q(z)|w−z|2dA(w)
1/2
≤3
r ∥¯∂χ0∥L2(Ω)∥u∥memQ(z)e−1
18 mr2∆Q(z),
again for z ∈D(z0, 1
3r), and the desired conclusion is immediate.
□
We will interpret Proposition 6.1 as saying that the function Mm(z, w) is an local reproducing
kernel mod(e−δm), with δ = δ0 > 0. More generally, a function Lm(z, w) deﬁned on D(z0, r) and
holomorphic in z is a a local reproducing kernel mod(e−δm) if
u(z) =
Z
Ω
u(w)χ0(w)Lm(z, w) e−2mQ(w)dA(w) + O(∥u∥memQ(z)−mδ),
z ∈D(z0, 1
3r),
holds for large m and all u ∈A2
m. Here and in the sequel, it is implicit that δ should be positive.
Analogously, a function Lm(z, w) deﬁned on D(z0, r) and holomorphic in z is a a local reproducing
kernel mod(m−k) if
u(z) =
Z
Ω
u(w)χ0(w)Lm(z, w) e−2mQ(w)dA(w) + O(∥u∥mm−kemQ(z)),
z ∈D(z0, 1
3r),
holds for large m and all u ∈A2
m. We speak of approximate local reproducing kernels when
it is implicit which of the above senses applies. The Bergman kernel Km(z, w) is of course
an approximate local reproducing kernel in the above sense (no error term!), and it has the
additional property of being holomorphic in ¯w. This suggests the term approximate local Bergman
kernel for an approximate local reproducing kernel, which is holomorphic in ¯w. Starting with
the local reproducing kernel Mm, Berman, Berndtsson, and Sjöstrand supply an algorithm to
16
ANTTI HAIMI AND HAAKAN HEDENMALM
correct Mm and obtain as a result an approximate local Bergman kernel mod(m−k) for any given
positive integer k. It is a nontrivial step – which actually requires additional assumptions on
the potential Q – to show that the approximate local Bergman kernels obtained algorithmically
in this fashion are indeed close to the Bergman kernel Km near the diagonal. This is achieved
by an argument based on Hörmander’s L2-estimates for the ¯∂-operator. In this section, we only
present the corrective algorithm.
