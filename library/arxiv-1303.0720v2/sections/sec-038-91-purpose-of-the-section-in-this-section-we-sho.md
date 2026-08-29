---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-038-91-purpose-of-the-section-in-this-section-we-sho
section_title: "Purpose of the section. In this section we show how the approximate local Bergman"
section_number: 9.1
pages: 33-35
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
kernels actually provide asymptotics for the weighted bianalytic Bergman kernel K2,mpointwise
near the diagonal.
9.2. The basic pointwise estimate. We let the potential Q, the point z0, the radius r, and the
cut-oﬀfunction χ0 be as in Subsections 6.1 and 6.3, with the additional requirement mentioned
in Subsection 7.2. In particular, we have that D(z0, r) ⋐Ω. We begin with a local weighted
bianalytic Bergman kernel mod(m−k−1),
K⟨k⟩
2,m(z, w) = b⟨2,k⟩(z, w) e2mQ(z,w),
where
(9.2.1)
b⟨2,k⟩:= m2b2
0 + mb2
1 + · · · + m−k+1b2
k+1
is a ﬁnite asymptotic expansion (here, it is assumed that z, w ∈D(z0, r) for the expression to
make sense). The “coeﬃcients” b2
j are biholomorphic separately in (z, ¯w) in D(z0, r) × D(z0, r),
and in principle they can be obtained from the criteria (7.7.5), but that is easy to say and hard
to do. The ﬁrst two “coeﬃcients” were derived in Subsection 7.9, and the formula for the third
“coeﬃcient” was mentioned as well. Let us write I⟨k⟩
2,m for the integral operator
I⟨k⟩
2,m[f](z) :=
Z
Ω
f(w)K⟨k⟩
2,m(z, w)χ0(w) e−2mQ(w)dA(w).
We quickly check that
(9.2.2)
P2,m
h
K⟨k⟩
2,m(·, w)χ0
i
(z) = I⟨k⟩
2,m[K2,m(·, z)](w),
where we recall that P2,m stands for the orthogonal projection L2(Ω, e−2mQ) →PA2
2,m, and K2,m
is as before the weighted bianalytic Bergman kernel on Ωwith weight e−2mQ. We would like
to show that K⟨k⟩
2,m and K2,m are close pointwise. By (9.2.2) and the triangle inequality, we have
that
(9.2.3)

K2,m(z, w) −K⟨k⟩
2,m(z, w)χ0(z)

 ≤

K2,m(w, z) −I⟨k⟩
2,m[K2,m(·, z)](w)

+

K⟨k⟩
2,m(z, w)χ0(z) −P2,m[K⟨k⟩
2,m(·, w)χ0](z)

.
34
ANTTI HAIMI AND HAAKAN HEDENMALM
9.3. Analysis of the ﬁrst term in the pointwise estimate. In the sequel, k is a ﬁxed nonegative
integer. To estimate the ﬁrst term on the right-hand side of (9.2.3), we use that K⟨k⟩
2,m is a local
reproducing kernel mod(m−k), which is expressed by (7.7.4). Before we go into that, we observe
that if u is biharmonic in D(z0, r), then
(9.3.1)
I⟨k⟩
2,m[u](z) =
Z
Ω
u(w)χ0(w)b⟨2,k⟩(z, w) e2mQ(z,w)−2mQ(w)dA(w)
=
Z
Ω
u(w)χ0(w)v(2)(z, w) e2mQ(z,w)−2mQ(w)dA(w)
+
Z
Ω
u(w)χ0(w)[M ¯∂wθ∇M ¯∂wθ∇X⟨k+2⟩]⟨k⟩(z, w) e2mQ(z,w)−2mQ(w)dA(w),
for z ∈D(z0, 1
3r), where X⟨k+2⟩is given by (7.7.6), and b⟨2,k⟩(z, w) is determined uniquely by
the criteria (7.7.5) together with the requirement that b⟨2,k⟩(z, w) should be bianalytic in each
of the variables (z, ¯w), as worked out in Subsections 7.7, 7.8, and 7.9. We rewrite (9.3.1) in the
following form:
(9.3.2)
I⟨k⟩
2,m[u](z) =
Z
Ω
u(w)χ0(w)v(2)(z, w) e2mQ(z,w)−2mQ(w)dA(w)
+
Z
Ω
u(w)χ0(w)[M ¯∂wθ∇M ¯∂wθ∇X⟨k+2⟩] e2mQ(z,w)−2mQ(w)dA(w)
−m−k
Z
Ω
u(w)χ0(w)(Yk + m−1Zk) e2mQ(z,w)−2mQ(w)dA(w),
where Yk, Zk are the expressions
Yk := M ¯∂wθ∂θM ¯∂wθ∂θXk + 2M ¯∂wθ

∂θM ¯∂wθMz−w + M2
¯∂wθMz−w∂θ

Xk+1.
and
Zk := M ¯∂wθ∂θM ¯∂wθ∂θXk+1.
Here, we recall that X⟨k+2⟩= Pk+1
j=0 m−jXj is a ﬁnite asymptotic expansion (or abschnitt). If we use
(6.2.1) to estimate the last term on the right-hand side of (9.3.2), and combine with Proposition
7.1 and (7.4.2), (7.7.3) (just write X⟨k+2⟩in place of A),
(9.3.3)
I⟨k⟩
2,m[u](z) = u(z) + O

r−1emQ(z)−δ0m∥u∥m
n
r∥¯∂wX⟨k+2⟩∥L∞(D(z0, 3
4 r)2)
+ [1 + ∥X⟨k+2⟩∥L∞(D(z0, 3
4 r)2)][1 + mr2∥¯∂wθ∥L∞(D(z0, 3
4 r)2)]
o
+ m−k−1
2 emQ(z)∥u∥m∥Yk + m−1Zk∥L∞(D(z0, 3
4 r)2)

,
for z ∈D(z0, 1
3r), where the implied constant is absolute. Given our standing assumptions,
all the involved norms are ﬁnite. If we accept an implied constant which may depend on the
triple (Q, z0, r), then we can compress (9.3.3) to
(9.3.4)
I⟨k⟩
2,m[u](z) = u(z) + O(m−k−1
2 emQ(z)∥u∥m),
z ∈D(z0, 1
3r),
for m ≥1. By a duality argument, (9.3.4) implies that
(9.3.5)

P2,m[K⟨k⟩
2,m(·, z)χ0] −K2,m(·, z)

m = O(m−k−1
2 emQ(z)),
z ∈D(z0, 1
3r).
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
35
If we apply this estimate (9.3.4) to the function u(z) = K2,m(z, w) (not the dummy variable w
used in the above integrals!), we ﬁnd that (for m ≥1)
(9.3.6)
I⟨k⟩
2,m[K2,m(·, w)](z) = K2,m(z, w) + O(m−k−1
2 emQ(z)K2,m(w, w)1/2)
= K2,m(z, w) + O(m−kemQ(z)+mQ(w)),
z ∈D(z0, 1
3r),
where again the implied constant depends on the triple (Q, z0, r). Note that in the ﬁrst step,
we used that ∥K2,m(·, w)∥2
m = K2,m(w, w), and in the last step the estimate of Corollary 8.3 (with
z0 replaced by z and with e.g. δ = 1
3r). If we switch the roles of z and w in (9.3.6), so that e.g.
w ∈D(z0, 1
3r) instead, we obtain an eﬀective estimate of the ﬁrst term on the right-hand side of
(9.2.3):
(9.3.7)
I⟨k⟩
2,m[K2,m(·, z)](w) = K2,m(w, z) + O(m−kemQ(z)+mQ(w)),
w ∈D(z0, 1
3r).
