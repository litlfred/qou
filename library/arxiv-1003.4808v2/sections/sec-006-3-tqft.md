---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-006-3-tqft
section_title: "TQFT"
section_number: 3
pages: 13-15
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
doc_brief: "Quantum Field Theory and the Volume Conjecture — 14 sections: Preliminaries; The many dimensions of the volume ; Parametrized VC"
---
the “quantumG-invariants” of knots and links. This was supplied by quantum Chern-
Simons theory with compact gauge group G in [3], and reinterpreted via quantum
groups and R-matrices in [4]. Using either of these approaches, one may deﬁne a
quantum partition function
ZG(M,L ;{Ra}; ℏ) (2.31)
for a link L in any three-manifold M, where each component of the link is colored
with a diﬀerent representation Ra. The “polynomial” PG
R is obtained from this after
normalizing by the partition function of an empty manifold,
PG
{Ra}(M,L ;q) = ZG(M,L ;{Ra}; ℏ)
ZG(M; ℏ) , (q =e2ℏ). (2.32)
Thus, in the case of the colored Jones polynomial,
JN(K;q) = ZSU (2)(S3,K ;RN; ℏ)
ZSU (2)(S3; ℏ) . (2.33)
The integer k (appearing in q = e2ℏ = e
2πi
k ) is identiﬁed with the “level” or coupling
constant of the compact Chern-Simons theory. 8
The partition function (2.31) supplies the left-hand-side of the volume conjecture.
We then want to understand the asymptotics of ZG(M,L ;{Ra}; ℏ) in the limit ℏ→ 0,
with a parameter ua = ℏ(λ∗
a +ρ∗) held ﬁxed for each separate link component. The
answer should be given by perturbative, quantum Chern-Simons theory with complex
gauge group GC, evaluated on the link complement M\L, in the background of a ﬂat
connection with ﬁxed holonomy
ma = exp(ua) (2.34)
around the meridian of each excised link component. Denoting this perturbative Chern-
Simons partition function by
ZGC
pert(M\L;{ua}; ℏ) = exp
(
− 1
4ℏICS({ua})− δ
2 log ℏ +...
)
, (2.35)
we expect that
ZG(M,L ;{Ra}; ℏ)
ℏ→0
∼ ZGC
pert(M\L;{ua}; ℏ) . (2.36)
This discussion can also be rephrased in a somewhat more symmetric manner, using
link complements on both sides of the volume conjecture. It turns out that in compact
8To be completely precise, the integer k used throughout these lectures is the sum of the Chern-
Simons level and the dual Coxeter number of G.
12
Chern-Simons theory the partition function of a knot (or link) K ⊂ M colored by
representationRλ is equivalent to the partition function of the knot complementM\K
with ﬁxed meridian holonomy
m = exp
(
iπλ∗ +ρ∗
k
)
= exp (ℏ(λ∗ +ρ∗)) = exp(u). (2.37)
For the compact G theory to make sense, the eigenvalues of the matrix u/iπ must
clearly be rational. However, interesting asymptotics — potentially with exponential
growth as in (2.36) — occur when u is analytically continued away from such ratio-
nal values. This process of analytic continuation naturally lands one in the regime of
Chern-Simons theory with complex gauge group GC [11].
After so many generalizations, it may be unclear that the volume conjecture has
anything to do with volumes anymore. Indeed, for higher-rank gauge groups G, “vol-
ume” should not be a hyperbolic volume but rather the “volume” of a holonomy rep-
resentation
ϱ :π1(M\K)→GC. (2.38)
Even in the case ofG =SU (2) and knots in the three-sphere, one may run across cases
of non-hyperbolic knot complements. It was clear from the initial days of the volume
conjecture [2] that even in these cases the asymptotics of JN(K;q) could still be given
by an appropriate ﬂat (but non-hyperbolic/non-metric) SL(2, C) structure.
3 TQFT
We have just seen that the volume conjecture admits a multitude of generalizations, all
of which seem to be related to Chern-Simons quantum ﬁeld theory. The most complete
statement of the volume conjecture (2.36) involves Chern-Simons theory with compact
gauge group G on the left-hand side and Chern-Simons theory with complex gauge
group GC on the right:
combinatorics/rep. theory geometry
quantumG-invariants volumes of representations
JN(K;q), PG
Rλ(K;q), ←→ ϱ :π1(M\K)→GC,
ZG(M,K ;u; ℏ), etc. ZGC
pert(M\K;u; ℏ), etc.
q =e
2πi
k =e2ℏ, u =iπλ∗+ρ∗
k .
(3.1)
Chern-Simons theory is a topological quantum ﬁeld theory (TQFT). In addition to the
basic implication that partition functions such as ZG(M,K ;u; ℏ) or ZGC
pert(M\K;u; ℏ)
are topological invariants of colored knots and links in three-manifolds, the structure
of TQFT provides powerful methods for actually computing them in multiple ways. It
also shows why a general correspondence like (3.1) might be expected to hold.
13
