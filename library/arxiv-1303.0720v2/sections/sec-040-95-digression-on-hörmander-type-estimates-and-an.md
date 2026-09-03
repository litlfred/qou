---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-040-95-digression-on-hörmander-type-estimates-and-an
section_title: "Digression on Hörmander-type estimates and an obstacle problem. We should like to"
section_number: 9.5
pages: 35-37
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
apply Proposition 9.1 with φ := mQ. Then we need the assumptions of the proposition to be
valid:
(9.5.1)
∆Q > 0
and
1
2∆Q∆log ∆Q > −m
on Ω.
The latter criterion apparently gets easier to fulﬁll as m grows. In the analytic case q = 1 only
the criterion ∆Q > 0 is needed, and in fact, it can be relaxed rather substantially (see [2] for the
36
ANTTI HAIMI AND HAAKAN HEDENMALM
polynomial setting). Basically, what happens is that we may sometimes replace the potential
Q by its subharmonic minorant ˇQ given by
ˇQ(z) := sup
n
u(z) : u ∈Subh(Ω), and u ≤Q on Ω
o
,
where Subh(Ω) denotes the cone of subharmonic functions; see Theorem 4.1 [2] for details
(in the polynomial setting). In principle, the Bergman kernel should be well approximated
by the local Bergman kernel if ˇQ = Q in a neighborhood of the given point z0. From the
conceptual point of view, what is important is that for an analytic function f, the expression
1
m log | f| is subharmonic (and in fact in the limit as m grows to inﬁnity we can approximate
all subharmonic functions with expressions of this type). In our present bianalytic setting,
1
m log | f| need not be subharmonic, but we still suspect that it approximately subharmonic for
large m. So we expect that (9.5.1) can be relaxed to ˇQ = Q near the point z0 plus (if needed)
some suitable replacement of the second (curvature type) criterion of (9.5.1).
9.6. Analysis of the second term in the pointwise estimate II. As we apply Proposition 9.1
to φ = mQ, the result is the following.
Proposition 9.2. Let Ωbe a domain in C and suppose Q : Ω→R is C4-smooth with both ∆Q > 0 on
Ωand
κ := sup
Ω
1
2∆Q∆log 1
∆Q < +∞.
Assume that f ∈L2
loc(Ω). Then there exists a (norm-minimal) solution v0 to the problem ¯∂2v0 = f with
Z
Ω
|v0|2e−2mQdA ≤
1
4m(m −κ)
Z
Ω
| f|2 e−2mQ
[∆Q]2 dA,
provided that m > κ and that the right-hand side is ﬁnite.
We now apply the above proposition with
f(z) := ¯∂2
z[χ0(z)K⟨k⟩
2,m(z, w)] = K⟨k⟩
2,m(z, w) ¯∂2χ0(z) + 2[ ¯∂χ0(z)][ ¯∂zK⟨k⟩
2,m(z, w)]
=
n
b⟨2,k⟩(z, w) ¯∂2χ0(z) + 2[ ¯∂χ0(z)][ ¯∂zb⟨2,k⟩(z, w)]
o
e2mQ(z,w),
and calculate that
| f(z)|e−mQ(z) ≤
n
| ¯∂2χ0(z)b⟨2,k⟩(z, w)| + 2| ¯∂χ0(z) ¯∂wb⟨2,k⟩(z, w)|
o
em Re[2Q(z,w)−Q(z)]
≤
n
| ¯∂2χ0(z)b⟨2,k⟩(z, w)| + 2| ¯∂χ0(z) ¯∂zb⟨2,k⟩(z, w)|
o
emQ(w)−δ0m,
where as before δ0 =
1
18r2ǫ0 and it is assumed that w ∈D(z0, 1
3r0). Under the assumptions on Q
stated in Proposition 9.2, we obtain from that proposition (recall the deﬁnition of (9.4.1)) and
the above calculation that
(9.6.1)

K⟨k⟩
2,m(·, w)χ0 −P2,m[K⟨k⟩
2,m(·, w)χ0]

m
≤
[ǫ0]−1
2m1/2(m −κ)1/2 emQ(w)−δ0mn
∥¯∂2χ0∥L2(Ω) ∥b⟨2,k⟩∥L∞(D(z0, 3
4 r)2) + 2∥¯∂χ0∥L2(Ω)∥¯∂zb⟨2,k⟩∥L∞(D(z0, 3
4 r)2)
o
= O

(mǫ0)−1emQ(w)−δ0mn
r−1∥b⟨2,k⟩∥L∞(D(z0, 3
4 r)2) + ∥¯∂zb⟨2,k⟩∥L∞(D(z0, 3
4 r)2)
o
,
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
37
where the implied constant is absolute and w ∈D(z0, 1
3r0), and we assume that m ≥2κ.
If we accept a constant which depends on the triple (Q, z0, r), then we can simplify (9.6.1)
signiﬁcantly:
(9.6.2)

K⟨k⟩
2,m(·, w)χ0 −P2,m[K⟨k⟩
2,m(·, w)χ0]

m = O(memQ(w)−δ0m),
because the two norms of b⟨2,k⟩and ¯∂zb⟨2,k⟩grow like O(m2). Finally, we combine this norm
estimate (9.6.2) with control on the point evaluation at z (see Proposition 8.1):
(9.6.3)

K⟨k⟩
2,m(z, w)χ0(z) −P2,m[K⟨k⟩
2,m(·, w)χ0](z)

 = O(m3/2emQ(z)+mQ(w)−δ0m),
z, w ∈D(z0, 1
3r).
