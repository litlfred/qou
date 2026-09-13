---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-004-4-general-derivation-derivation-for-theorem-21
section_title: "General Derivation: Derivation for Theorem 2.1"
section_number: 4
pages: 5-7
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
We wish to obtain bounds on virial coeﬃcients using those which come from cluster
coeﬃcients, in order to gain an estimate of the lower bound for the radius of convergence of
the virial expansion. The derivation loosely follows the method used by Ruelle in [Rue69]
and that of Lebowitz and Penrose in [Leb64]. The starting point is the cluster expansion
bound, which is given in the form:
|nbn|≤ ann−1
n! bn (4.1)
Wherea andb are positive functions of temperature deﬁned by the particular bound we use.
The starting point is the relationship in (3.2), (implicitly) deﬁning virial coeﬃcients in
terms of cluster coeﬃcients:
cn = β−1
2πi
∮
C
dz
nzρn−1 (4.2)
In order to get an upper bound on |cn|, we need to bound|ρ| from below. To do this we use
the bound:
|ρ−z|≤
∞∑
n=2
|nbn||z|n (4.3)
We then substitute in for the upper bounds we have on the cluster coeﬃcients:
|ρ−z|≤ a
∞∑
n=2
nn−1
n! (b|z|)n (4.4)
We deﬁne the function: f(x) :=
∞∑
n=1
nn−1
n! xn and write (4.4) conveniently as:
|ρ−z|≤ a(f(b|z|)−b|z|) (4.5)
Using the reverse triangle inequality, we obtain:
|ρ|≥| z|(1 +ab)−af(b|z|) (4.6)
Letb|z| =se−s and observe that, from the assumed generic bound on the cluster expansion,
b|z|≤ e−1 in order for
∞∑
n=1
nbnzn to converge. se−s is an increasing function on (0, 1) and it
takes values in (0,e−1) as required. We then have the bound in terms of s:
|ρ|≥ b−1se−s(1 +ab)−af(se−s) (4.7)
6 S. J. TATE
We have chosen the functionse−s since it is the inverse function off. This can be understood
from Lagrange Inversion (shown in appendix) and is a result in [Cor97] . We thus have the
expression:
|ρ|≥ b−1se−s(1 +ab)−as (4.8)
We thus seek to maximise the right hand side to get the best possible bound. We notice
that in the ranges∈ (0, 1) we have a zero ats = 0 and another whenb−1e−s(1+ab)−a = 0
i.e. when es = 1 + 1
ab, so at s = ln
(
1 + 1
ab
)
. It is positive for s∈ (0, ln
(
1 + 1
ab
)
). We seek
the value of s to maximise this function in this range.
Remark 2. This approach to estimating a lower bound for the radius of convergence for
the virial expansion, takes a value of |z| some distance away from its maximal value for con-
vergent cluster expansions. We expect density to increase with fugacity and so the maximal
density for which the cluster expansions remain convergent appears to be greater than that
for the virial expansion. This is not true in general and is a weakness of this approach.
If we deﬁne:
r(s) :=s(e−s(1 +ab)b−1−a) (4.9)
and take the derivative to search for an extremum in this range.
r′(s) = (e−s(1 +ab)b−1−a)−se−s(1 +ab)b−1 (4.10)
if we ﬁnd when r′(s) = 0 in (4.10), then we solve:
(1−s)e−s = ab
1 +ab (4.11)
Substituting γ = 1−s, we get the equation for γ:
γeγ = eab
1 +ab (4.12)
The LambertW -function, as is explained in [Cor97], is the inverse ofγeγ and so we can write
(4.9) in terms of γ and substitute γ forW (µ), where µ := eab
1+ab. If we write ˜r(γ(s)) :=r(s).
We thus get:
˜r(γ) = (1−γ)(eγ 1 +ab
eb −a)
=a(eγ 1 +ab
eab −γeγ 1 +ab
eab − 1 +γ)
=a( 1
γ− 2 +γ)
=a(W (µ)− 1)2
W (µ) (4.13)
Where we use (4.12) to cancel: γeγ 1+ab
eab = 1 and eγ 1+ab
eab = 1
γ .
We evaluate the integral (4.2) along the contour described by the circle |z| = constant,
where the constant is determined by the manipulations above. This leaves us with the
integral:
|cn|≤ β−1
2nπ
∮
C
dz
|z||ρ|n−1 (4.14)
This gives us bounds on the coeﬃcients cn as:
|cn|≤ β−1
n
(
a−1 W (µ)
(W (µ)− 1)2
)n−1
(4.15)
VIRIAL EXPANSION BOUNDS 7
This gives us the radius of convergence of the virial expansion satisfying:
RVir≥a(W (µ)− 1)2
W (µ) (4.16)
