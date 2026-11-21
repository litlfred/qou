---
doc_id: arxiv-1504.07260v3
doc_title: "Fricke S-duality in CHL models"
section_id: sec-028-a3-witten-index-of-the-quantum-symmetry
section_title: "A.3 Witten index of the quantum symmetry"
section_number: null
pages: 41-44
source_pdf: 1504.07260v3.pdf
source_sha256: 707cb014400a3f05
toc_source: outline
doc_brief: "Fricke S-duality in CHL models — We consider four dimensional CHL models with sixteen spacetime supersym- metries obtained from orbifolds of type IIA superstring on K3×T 2 by a ZN symmetry acting"
---
Witten index of the quantum symmetry
Let C be a non-linear sigma model on K3, g be a symmetry preserving the N = (4, 4)
superconformal algebra and let us assume that the orbifold theory C′ = C/⟨g⟩is consistent,
i.e. the twisted sectors satisfy the level-matching condition (λ = 1). In this section, we
compute the twined Witten index of the quantum symmetry Q. By deﬁnition of Q, this is
given by
IC′
Qk =
N
X
t=1
e
2πikt
N sdim(H⟨g⟩
gt ) ,
(A.17)
where Hgt denotes the space of gt-twisted Ramond-Ramond ground states (i.e. with con-
formal weights (1
4, 1
4)), H⟨g⟩
gt is its g-invariant subspace and sdimH⟨g⟩
gt is the superdimension
(Z2-graded by (−1)F+ ˜F ) of H⟨g⟩
gt . By the standard orbifold construction, sdimH⟨g⟩
gt is given
by
sdimH⟨g⟩
gt = 1
N
N
X
v=1
IC
gt,gv ,
(A.18)
where
IC
gt,gv := TrRR,Hgt(gv(−1)F+ ˜F qL0−c
24 ¯q
¯L0−c
24 ) ,
(A.19)
is the gt-twisted gv-twined Witten index. The index IC
gt,gv is a specialization to z = 0 of
the twisted twining elliptic genus φgt,gv(τ, z). In turn, the twisted-twining elliptic genus
φgt,gv(τ, z) can be obtained from the untwisted one φ1,g(t,v,N)(τ, z) by a modular transfor-
mation. By specializing to z = 0, the dependence on τ drops and we have simply the
identity
IC
gt,gv = IC
g(v,t,N) .
(A.20)
– 40 –
Using (3.19), we can now prove (3.20):
IC′
Qk =
N
X
t=1
e
2πikt
N
1
N
N
X
v=1
IC
gt,gv =
N
X
t=1
e
2πikt
N
1
N
N
X
v=1
IC
g(v,t,N)
=
N
X
t=1
e
2πikt
N
1
N
N
X
v=1
X
u|(t,v,N)
m(u)u
=
N
X
t=1
e
2πikt
N
X
u|(t,N)
m(u) u
N
N
X
v=1
δ(v mod u)
=
N
X
t=1
e
2πikt
N
X
u|(t,N)
m(u) =
X
u|N
m(u)
N
X
t=1
e
2πikt
N δ(t mod u)
=
X
u|N
m(u)
N/u
X
l=1
e
2πikl
N/u =
X
u|N
m(u)N
u δ(k mod N/u)
=
X
n|(k,N)
m(N/n)n .
(A.21)
Finally, let us consider the analysis of the Witten index for case where λ > 1. In this
case, the orbifold of C by g is not consistent and λ is the smallest power such that gλ
gives rise to a consistent orbifold. Failure of the level matching condition implies that the
twining genus φg(τ, z) is modular up to a phase. This implies that the twining Witten index
IC
g = φ(τ, 0) must vanish. The same argument applies to gk, for any k with (λ, k)̸ = λ
IC
gk = 0
if (λ, k)̸ = λ .
(A.22)
As a consequence, a cycle of length a in the cycle shape of g can have non-zero multiplicity
m(a)̸ = 0 only if a is a multiple of λ. To show this, consider by absurd that there is some
cycle of length b such that m(b)̸ = 0 and (b, λ) < λ. Without loss of generality, we can
assume that b is the smallest such cycle. Then, we have the contradiction
0 = IC
gb =
X
u|(b,N)
um(u) = bm(b) ,
(A.23)
where the last equality follows because all u < b with m(u)̸ = 0 are multiple of λ and
therefore cannot divide b.
Let Q
a| N
λ a ˜m(a) be the cycle shape of gλ. Since all cycle lengths in the cycle shape of
g are multiple of λ, we have the relation
˜m(a) = λm(λa) ,
(A.24)
which allows us to reconstruct the cycle shape of g when the cycle shape of gλ is known.
Since the orbifold by gλ is consistent, then (3.15) holds and
IC′ :=
X
a| N
λ
N
λa ˜m(a) ∈{0, 24}
(A.25)
– 41 –
where IC′ is the Witten index of the orbifold C′ = C/⟨gλ⟩. Using (A.24) we have
X
a| N
λ
N
λa ˜m(a) =
X
a| N
λ
N
λaλm(λa) = λ
X
b|N
N
b m(b).
(A.26)
so that
X
b|N
N
b m(b) = IC′
λ
.
(A.27)
By assumption, (3.15) is not satisﬁed by g, so that IC′̸ = 0, C′ is a K3 model and
X
b|N
N
b m(b) = 24
λ .
(A.28)
As explained in appendix A.2, we are interested in a symmetry g′ in the orbifold theory C′
that acts by
e
2πia
N gE−1
g
,
(A.29)
on the gλ-invariant gλa-twisted sector H⟨gλ⟩
gaλ . Here, E−1
g
∈Z/λZ is determined by E−1
g Eg ≡1
mod λ. Such an element always exist because (Eg, λ) = 1. Furthermore, g has order λ on
H⟨gλ⟩
gaλ , so that gE−1
g
is well-deﬁned. The standard orbifold formula gives
IC′
g′k =
N/λ
X
a=1
e
2πiak
N
λ
N
N/λ
X
v=1
IC
gλa,gλv+E−1
g
k .
(A.30)
By (A.22), IC′
g′k vanishes unless k is a multiple of λ, i.e.
IC′
g′k = 0
if (λ, k)̸ = λ .
(A.31)
By the same reasoning as for g, we obtain that the cycle shape Q
a|N am′(a) of g′ contains
only cycles with length multiple of λ and that the cycle shape Q
a|N a ˜m′(a) of g′λ is given
by the analogue of (A.24)
˜m′(a) = λm′(λa) .
(A.32)
The twining indices IC′
g′jλ, j = 1, . . . , N/λ are given by
IC′
g′jλ =
N/λ
X
a=1
e
2πiajλ
N
λ
N
N/λ
X
v=1
IC
gλ(a,v+E−1
g
j,N/λ) =
N/λ
X
a=1
e
2πiajλ
N
λ
N
N/λ
X
v=1
IC
gλ(a,v,N/λ) .
(A.33)
By the same computation as in the λ = 1 case, we obtain
IC′
g′jλ =
X
n|(j,N/λ)
˜m( N
λn)n .
(A.34)
This implies that
˜m′(n) = ˜m( N
λn) ,
(A.35)
– 42 –
that is
m′(λn) = m(N/n) ,
(A.36)
or, equivalently,
m′(a) = m(Nλ
a ) .
(A.37)
