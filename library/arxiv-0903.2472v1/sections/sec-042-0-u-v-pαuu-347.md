---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-042-0-u-v-pαuu-347
section_title: "(u) = V (p(α)(u),u ) (3.47)"
section_number: 0
pages: 40-42
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
for some α. In particular, lα(u) as given by (3.46) and m =eu obey (2.51).
To analyze generic critical points of V , observe that the critical point equations take
the form
2 ∂
∂pj
V (p,u ) =−
N∑
i=1
ǫiGji log(1+exp(gi(p, 2u)+iπǫi))+ ∂
∂pj
f (p, 2u, 0) = 0 ∀j, (3.48)
where Gji = ∂
∂pj
gi(p, 2u) are some constants and the functions ∂
∂pj
f (p, 2u, 0) are linear.
Again, the cuts of the logarithm must match the singularitie s of the quantum dilogarithm.
Exponentiating (3.48), we obtain another set of conditions
rj(x,m ) = 1 ∀j, (3.49)
where
rj(x,m ) = exp
(
2 ∂
∂pj
V (p,u )
)
=
∏
i
(1−egi)−ǫiGji exp
( ∂
∂pj
f
)
(3.50)
are all rational functions of the variables xj =epj and m =eu. Note that an entire family
of points {p + 2πin| n∈ ZN −1} maps to a single x, and that all branch cut ambiguities
disappear in the simpler equations (3.49). Depending on arg (ℏ) and the precise form of f ,
solutions to (3.49) either “lift” uniquely to critical poin ts of the potential V , or they lift to
a family of critical points at which V diﬀers only by integer multiples of 2 πiu.
Now, the system (3.49) is algebraic, so its set of solutions d eﬁnes a complex aﬃne
variety
R ={(x1,...,x N −1,m )∈ CN|rj(x1,...,x N −1,m ) = 0 ∀j}, (3.51)
which is closely related to the representation variety L given by A(l,m ) = 0. Both gener-
ically have complex dimension one. Noting that s(x1,...,x N −1,m ) = exp
(∂
∂uV
)
is also a
rational function, we can deﬁne a rational map φ : CN→ C2 by
φ(x1,...,x N −1,m ) = (s(x1,...,x N −1,m ),m ). (3.52)
The claim in [27] that one critical point of V always corresponds to the geometric branch
ofL means that φ(R) (taking an algebraic closure) always intersects L nontrivially, along
a subvariety of dimension 1. Thus, some irreducible compone nt of φ(R), coming from
an irreducible component of R, must coincide with the entire irreducible component of L
containing the geometric branch. Every solution x = x(m) in this component of R corre-
sponds to a branch of the A-polynomial. Moreover, if such a so lution x(α) (corresponding
– 39 –
to branch α) can be lifted to a real critical point p(α)(u) of V , then one must have relations
(3.46) and (3.47).
This simple algebraic analysis shows that some solutions of (3.49) will cover an entire
irreducible component of the curve L deﬁned by A(l,m ) = 0. We cannot push the general
argument further without knowing more about the reducibili ty ofR. However, we can look
at some actual examples. Computing V (p,u ) for thirteen hyperbolic manifolds with a sin-
gle torus boundary, 17 we found in every case that solutions of (3.49) completely co vered all
non-abelian branches α⁄= abel; in other words, φ(R) =L′, withL′ ={A(l,m )/(l−1) = 0}.
For six of these manifolds, we found unique critical points p(u) corresponding to every non-
abelian branch of L at arg( ℏ) = iπ. Motivated by these examples, it is natural to state the
following conjecture:
Conjecture 2 : Every critical point of V corresponds to some branch α, and all α⁄= abel
are obtained in this way. Moreover, for every critical point p(α)(u) (corresponding to some
branchα) we have (3.46)-(3.47) and to all orders in perturbation theory:
Z (α)(M ; ℏ,u ) =
√
2
∫
Cα
N∏
i=1
Φ ℏ
(
gi(p, 2u) +ǫi(iπ + ℏ)
) ǫi
e
1
2ℏ f (p,2u,ℏ)−u
N −1∏
j=1
dpj√
4πℏ
, (3.53)
whereCα is an arbitrary contour with ﬁxed endpoints which passes thr ough p(α)(u) and no
other critical point.
A slightly more conservative version of this conjecture mig ht state that only those α
that belong to the same irreducible component of L as the geometric branch, α = geom,
are covered by critical points of V . Indeed, the “abelian” branch with label = 1 is not
covered by the critical points of V and it belongs to the separate component ( l− 1) of the
curve A(l,m ) = 0. It would be interesting to study the relation between cr itical points
of V and irreducible components of L further, in particular by looking at examples with
reducible A-polynomials aside from the universal ( l− 1) factor.
The right-hand side of (3.53) is the proposed state integral model for the exact per-
turbative partition function of SL(2, C) Chern-Simons theory on a hyperbolic 3-manifold
M with a single torus boundary Σ = T 2. (A generalization to 3-manifolds with an arbi-
trary number of boundary components is straightforward.) T his state integral model is a
modiﬁed version of Hikami’s invariant (3.16). Just like its predecessor, eq. (3.53) is based
on an ideal triangulation {∆ i}N
i=1 of a hyperbolic 3-manifold M and inherits topological
invariance from the pentagon identity (3.40) of the quantum dilogarithm.
However, in writing (3.53) we made two important modiﬁcatio ns to Hikami’s invariant
(3.16). First, we introduced contours Cα running across the sadle points pα, which now
encode the choice of a classical solution in Chern-Simons th eory. Second, in (3.53) we
17Namely, the complements of hyperbolic knots 41(k21), 52(k32), 12n242 (31, (-2,3,7)-pretzel knot),
61(k41), 63(k643), 72(k42), 73(k520), 74(k628), 10132(K59), 10139(K522), and 11n38(K513), as well
as the one-punctured torus bundles L2R and LR3 over S1 (also knot complements, but in a manifold other
than S3).
– 40 –
introduced an extra factor of
√
8πℏe−u, which is needed to reproduce the correct asymptotic
behavior ofZ (α)(M ; ℏ,u ). To understand this correction factor, we must look at the h igher-
order terms in the expansion of Z (α)(M ; ℏ,u ). By using (3.26), one can continue the saddle
point approximations described above to arbitrary order in ℏ. The result has the expected
form (1.8),
Z (α)(M ; ℏ,u ) = exp
(
1
ℏS(α)
