---
doc_id: arxiv-1508.07379v2
doc_title: "Convergence of Mayer and Virial expansions and the Penrose t ree-graph identity"
section_id: sec-001-2-model-and-results
section_title: "Model and Results"
section_number: 2
pages: 3-7
source_pdf: 1508.07379v2.pdf
source_sha256: c3dbf93d1cac198e
doc_brief: "Convergence of Mayer and Virial expansions and the Penrose t ree-graph identity — We establish new lower bounds for the convergence radius of the Ma yer series and the Virial series of a continuous"
---
2.1 Model
We consider a continuous system of classical particles in th e d-dimensional Euclidean space Rd.
Denote by xi ∈ Rd the position vector of the ith particle of the system and by ‖xi‖ its Euclidean
norm. We suppose hereafter that particles interact through a pair potential V : Rd → R ∪ {+∞}
such that V (−x) = V (x) and we set shortly R∗ .= R ∪ {+∞}. Given a conﬁguration ( x1, . . . , x n) ∈
Rdn of the system such that n particles are present, the energy U (x1, . . . , x n) of this conﬁguration
is deﬁned as
U (x1, . . . , x n) =
∑
1≤i<j≤n
V (xi − xj)
We work in the Grand Canonical Ensemble, where the statistic al mechanics of the system is gov-
erned by the following partition function
Ξ Λ (λ, β ) =
∞∑
n=0
λ n
n!
∫
Λ
dx1 . . .
∫
Λ
dxne−βU (x1,...,x n) (2.1)
where Λ ⊂ Rd is typically a d-dimensional cube with center in the origin, λ ∈ (0, +∞) is the activity
of the system and β ∈ (0, +∞) is the inverse temperature.
The connection with thermodynamics is obtained by taking th e logarithm of the partition func-
tion. Namely, the pressure PΛ (β, λ ) and the density ρΛ (β, λ ) of the system at ﬁxed values of the
thermodynamic parameters inverse temperature β , fugacity λ and volume Λ, are given by
PΛ (β, λ ) = 1
β |Λ | log Ξ Λ (λ, β ) (2.2)
ρΛ (β, λ ) = λ
|Λ |
∂
∂λ log Ξ Λ (λ, β ) (2.3)
It is a long known fact [12] that log Ξ Λ (λ, β ) can be expanded as a power series of the fugacity.
Namely,
1
|Λ | log Ξ Λ (λ, β ) = λ +
∞∑
n=2
Cn(β, Λ) λ n (2.4)
The series above is the so-called Mayer series and its coeﬃci ents Cn(β, Λ), known nowadays as
Mayer coeﬃcients , admit the following explicit expression.
Cn(β, Λ) = 1
|Λ |
1
n!
∫
Λ
dx1 . . .
∫
Λ
dxn
∑
g∈Gn
∏
{i,j }∈Eg
[
e−βV (xi−xj) − 1
]
(2.5)
where Gn denotes the set of all connected graphs with vertex set {1, 2, . . . , n } (a.k.a. labeled
connected graphs with n vertices) and Eg denotes the edge set of g ∈ G n.
Clearly, via Mayer series one can write both pressure (2.2) a nd density (2.3) as expansions in power
of the fugacity λ.
Some conditions on the potential V must be imposed to have hope to control the series. Stability
and temperedness are commonly considered as minimal condit ions to guarantee a good statistical
mechanics behavior of the system (see, e.g., [18] and [6]).
3
Deﬁnition 1 (Stability) A pair potential V is said to be stable if
B := sup
n≥2
sup
(x1,...,x n)∈Rdn
− 1
n U (x1, . . . , x n) < +∞ (2.6)
We call B the stability constant of the pair potential V .
Deﬁnition 2 (T emperedness) A pair potential V is said to be tempered if there exists r0 ≥ 0
such that ∫
‖x‖≥r0
|V (x)| dx < ∞ (2.7)
Observe that the stability constant of any tempered potenti al V is non-negative.
As mentioned in the introduction, the best rigorous upper bo und on |Cn(β, Λ) | so far (and hence
the best lower bound on the convergence radius of the Mayer se ries) for stable and tempered pair
potentials is that obtained by Penrose and Ruelle in 1963 [15 , 19].
Theorem 0 (Penrose Ruelle 1963) Let V be a stable and tempered pair potential with stability
constant B. Then the n-order Mayer coeﬃcient Cn(β, Λ) deﬁned in (2.5) is bounded by
|Cn(β, Λ) | ≤ e2βB (n−1)nn−2 [C(β )]n−1
n! (2.8)
where
C(β ) =
∫
Rd
dx |e−βV (x) − 1| (2.9)
Therefore the Mayer series (2.4) converges absolutely, unif ormly in Λ , for any complex λ inside
the disk
|λ| < 1
e2βB +1C(β ) (2.10)
I.e. the convergence radius R of the Mayer series admits the following lower bound
R ≥ RPR
.= 1
e2βB +1C(β ) (2.11)
Observe that the non-negative quantity C(β ) deﬁned in (2.9) is ﬁnite if V is stable and tempered
(see e.g. [18]).
2.2 Results
As said in the introduction, the bound on the absolute value o f the nth-order Mayer coeﬃcient
Cn(β, Λ) appearing in Theorem 0 has been obtained “indirectly” usi ng the method of Kirkwood-
Salzburg equations. Our main result is the following Theore m 1 below which improves strongly
Theorem 0 via a direct bound on Cn(β, Λ) by using the old Penrose tree-graph identity proposed
in [16].
4
Theorem 1 Let V be a stable and tempered pair potential with stability const ant B. Then the
n-order Mayer coeﬃcient Cn(β, Λ) is bounded by
|Cn(β, Λ) | ≤ eβBn nn−2 [ ˆC(β )]n−1
n! (2.12)
where
ˆC(β ) =
∫
Rd
[
1 − e−β |V (x)|
]
dx (2.13)
Therefore the Mayer series converges absolutely, uniformly in Λ , for any complex λ inside the disk
|λ| < 1
eβB +1 ˆC(β )
(2.14)
I.e. the convergence radius R of the Mayer series admits the following lower bound
R ≥ R∗ .= 1
eβB +1 ˆC(β )
(2.15)
Observe that, according to the deﬁnitions (2.9) and (2.13), we have 0 ≤ ˆC(β ) ≤ C(β ).
Remark 1 . The improvement given by Theorem 1 respect to Theorem 0 is tw ofold. First, the
factor eβB +1 in (2.15) replaces the factor e2βB +1 in (2.11). Second, the factor ˆC(β ) in (2.15) replaces
the factor C(β ) in (2.11) and clearly, recalling their deﬁnitions (2.13) a nd (2.9) respectively, we
have ˆC(β ) ≤ C(β ) where the equality only holds if V is non-negative (purely repulsive). Moreover
observe that while ˆC(β ) grows at most linearly in β , the factor C(β ) can grow exponentially with β
(for V with an attractive part). So, the ratio R∗/R PR always greater than one, is the product of two
factors, eβB and [ ˆC(β )/C (β )], both growing exponentially fast with β when V has a negative part.
Due to this exponential behavior in β , our improvement on the Penrose-Ruelle bound is rather
astonishing for attractive potentials (i.e. those with str ictly positive stability constant B) at non
small β (i.e. low temperatures). To give an idea, for the Lennard-Jo nes gas at inverse temperature
β = 1, using the value BLJ = 8 . 61 for its stability constant (see [9]), our lower bound is at least
8. 5 × 104 larger than the Penrose-Ruelle lower bound, while for β = 10 is at least 7 . 26 × 1043 larger
than the Penrose-Ruelle lower bound. On the other hand, for β small the exponential eβB is near
to one and ˆC(β ) becomes very close to C(β ) so that our improvement is much less sensitive at high
temperatures. Finally, for purely repulsive pair potentia ls (i.e. those with stability constant B = 0)
our bound coincides with the Penrose-Ruelle bound since in t his case eβB = 1 and ˆC(β ) = C(β ).
Remark 2 . As mentioned above, the density of the system ρΛ (β, λ ) given in (2.3) can also be
written, via (2.4), in terms of a power series of the fugacity λ. This series allows to express the
fugacity λ as a power series of the density ρΛ which, plugged into (2.4), gives the so-called Virial
series (see, e.g., [12]), i.e., the pressure as a function of the density and temperature, or, in other
words, the equation of state of the system. In 1964 Lebowitz a nd Penrose [8] (provided the following
lower bound on the convergence radius R of the Virial series of a gas of particles interacting via a
stable and tempered pair potential.
R ≥ R LP
.= g(e2βB )
e2βB ˆC(β )
(2.16)
5
with
g(u) = max
0<w<1
[(1 + u)e−w − 1]w
u
The authors deduced such a bound, via Lagrange inversion, fr om the Penrose-Ruelle bounds (2.8) of
the Mayer coeﬃcients (see also [7] for an alternative method that deal directly with the coeﬃcients of
the Viral series written in terms of two-connected graphs). If one redoes the calculations performed
by Lebowitz and Penrose using the new upper bound (2.12) for t he absolute value of the nth-order
Mayer coeﬃcient (with ˆC(β ) in place of C(β ) and eβB in place of e2βB ), then one immediately
obtains the following lower bound for the convergence radiu s R of the Viral series
R ≥ R ∗ .= g(eβB )
eβB ˆC(β )
(2.17)
Observing that 0 . 1448 ≤ g(u) ≤ e−1 for u ∈ [1, ∞) (see, e.g., Remark 2 below Theorem 1 in [13]),
we have that the ratio R∗/ RLP between the new lower bound (2.17) for the convergence radiu s
of the Viral series and the old Lebowitz-Penrose bound given in (2.16) is of the same order of
magnitude of the ratio R∗/R P R calculated above.
The proof of Theorem 1 relies on a non trivial tree-graph ineq uality on the absolute value of the
integrand of the r.h.s. of (2.5) (the so-called Ursell funct ions) as far as stable pair potentials are
considered. This new tree-graph inequality, an additional result of the present paper which we
consider interesting per se , can be stated as follows.
Proposition 1 Let V be a stable pair potential with stability constant B. Then, for any n ≥ 2 and
any (x1, . . . , x n) ∈ Rdn, the following inequality holds
|
∑
g∈Gn
∏
{i,j }∈Eg
(e−βV (xi−xj) − 1)| ≤ eβBn ∑
τ∈Tn
∏
{i,j }∈Eτ
(1 − e−β |V (xi−xj)|) (2.18)
where Tn denotes the set of all trees with vertex set [n] (a.k.a. labeled trees with n vertices).
The proofs of Proposition 1 and Theorem 1 are given in section s 3 and 4 respectively.
3 Proof of Proposition 1
In this section we set [ n] := {1, ..., n } and En := {{i, j } : i, j ∈ [n], i < j }. We recall also that Gn
is the set of all connected graphs with vertex set [ n] (i.e labeled connected graphs with n vertices)
and Tn is the set of all trees with vertex set [ n] (i.e labeled trees with n vertices). Given g ∈ G n, we
denote Eg its edge set. Given g ∈ G n and g′ ∈ G n such that Eg ⊂ Eg′, we say that g is a subgraph
of g′ and write g ⊂ g′. Note that the pair ( Gn, ⊂) is a partially ordered set. Given g, g ′ ∈ G n such
that g ⊂ g′, we denote [ g, g ′] = {g′′ ∈ G n : g ⊆ g′′ ⊆ g′}. In other words [ g, g ′] is an interval in
(Gn, ⊂). Given a set S, we denote by |S| its cardinality.
6
