---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-009-221-analytic-continuation
section_title: "Analytic continuation"
section_number: 2.2.1
pages: 18-20
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
For a generic 3-manifold M with boundary Σ = T 2, constructing the quantum operators
ˆAi(ˆl, ˆm) may be a diﬃcult task. However, when M is the complement of a knot K in the
3-sphere,
M = S3 /integerdivideK, (2.35)
there is a simple way to ﬁnd the ˆAi’s. Indeed, according to (1.17) these operators annihilate
the polynomial knot invariants PG,R(K;q), which are deﬁned in terms of Chern-Simons
theory with compact gauge group G,
ˆAi(ˆl, ˆm) PG,R(K;q) = 0. (2.36)
The operator ˆli acts on the set of polynomial invariants{PG,R(K;q)} by shifting the highest
weight λ = (λ1,...,λ r) of the representation R by the i-th basis elements of the weight
lattice Λ wt, while the operator ˆ mj acts simply as multiplication by qλj /2. Let us brieﬂy
explain how this comes about.
In general, the moduli space Mﬂat (GC, Σ) is a complexiﬁcation of Mﬂat (G, Σ). The
latter is the classical phase space in Chern-Simons theory w ith compact gauge group G and
– 17 –
can be obtained from Mﬂat (GC, Σ) by requiring all the holonomies to be “real,” i.e. inG.
Similarly, restricting to real holonomies in the deﬁnition ofL produces a Lagrangian sub-
manifold inMﬂat (G, Σ) that corresponds to a quantum state |M⟩ in Chern-Simons theory
with compact gauge group G. In the present example of knot complements, restricting to
such “real” holonomies means replacing TC by T in (2.28) and taking purely imaginary
values of ui and vi in equations (2.30). Apart from this, the quantization prob lem is es-
sentially the same for gauge groups G and GC. In particular, the symplectic structure
(2.32) has the same form (with imaginary ui andvi in the theory with gauge group G) and
the quantum operators ˆAi(ˆl, ˆm) annihilate both PG,R(K;q) and Z (α)(M ; ℏ,u ) computed,
respectively, by Chern-Simons theories with gauge groups G and GC.
In order to understand the precise relation between the para meters in these theories, let
us consider a Wilson loop operator, WR(K), supported on K⊂ S3 in Chern-Simons theory
with compact gauge group G. It is labeled by a representation R =Rλ of the gauge group
G, which we assume to be an irreducible representation with hi ghest weight λ∈ t∨. As we
already mentioned earlier ( cf. eq. (1.13)), the path integral in Chern-Simons theory on S3
with a Wilson loop operator WR(K) computes the polynomial knot invariant PG,R(K;q),
withq =e2ℏ . Using (2.19), we can represent this path integral as ⟨R|M⟩, where|R⟩ is the
result of the path integral on a solid torus containing a Wils on loop WR(K), and |M⟩ is
the path integral on its complement, M .
In the semi-classical limit, the state |R⟩ corresponds to a Lagrangian submanifold of
Mﬂat (G,T 2) = ( T× T)/W deﬁned by the ﬁxed value of the holonomy m =eu on a small
loop around the knot, where u is given by (1.14). The relation between m =eu, which is an
element of the maximal torus T of G, and the representation Rλ is given by the invariant
quadratic form−Tr (restricted to t). Speciﬁcally,
m = exp( ℏλ∗)∈ T, (2.37)
where λ∗ is the unique element of t such that λ∗(x) =−Trλx for all x∈ t. In (1.15), we
analytically continue this relation to m∈ TC.
For a given value of m =eu, equations (2.30) have a ﬁnite set of solutions lα, labeled
by α. Only for one particular value of α is the perturbative GC invariantZ (α)(M ; ℏ,u )
related to the asymptotic behavior of PG,R(K;q). This is the value of α which maximizes
Re
(
S(α)
0 (M ;u)
)
. For this α, we have (1.15):
Z (α)(M ; ℏ,u )
Z(S3; ℏ) = asymptotic expansion of PG,R(K;q). (2.38)
For hyperbolic knots and u suﬃciently close to 0, this “maximal” value of α is always
α = geom.
It should nevertheless be noted that the analytic continuat ion described here is not
as “analytic” as it sounds. In particular, the limit (1.14) i s very subtle and requires much
care. As explained in [22], in taking this limit it is importa nt that values of q =e2ℏ avoid
roots of unity. If one takes the limit with ℏ−1∈ 1
iπ Z, which corresponds to the allowed
values of the coupling constant in Chern-Simons theory with compact gauge group G, then
– 18 –
one can never see the exponential asymptotics (1.8) with Im ( S(ρ)
0 ) > 0. The exponential
growth characteristic to Chern-Simons theory with complex gauge group emerges only in
the limit with ℏ =u/λ∗ and u generic.
