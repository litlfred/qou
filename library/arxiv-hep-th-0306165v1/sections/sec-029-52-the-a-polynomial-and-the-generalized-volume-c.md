---
doc_id: arxiv-hep-th-0306165v1
doc_title: "which has many interesting connections with three-dimensi onal quantum gravity and ge- ometry of hyperbolic 3-manifolds. We show that, in the prese nce of a single knotted Wilson l"
section_id: sec-029-52-the-a-polynomial-and-the-generalized-volume-c
section_title: "The A-Polynomial and the Generalized Volume Conjectur e"
section_number: 5.2
pages: 38-41
source_pdf: 0306165v1.pdf
source_sha256: 4f187debec912a24
doc_brief: "Three-Dimensional Quantum Gravity — We study three-dimensional Chern-Simons theory with compl ex gauge group SL(2, C), which has many interesting connections with three-dimensi onal quantum gravity"
---
Incomplete hyperbolic structures on knot complements come in continuous families.
For example, if K is a hyperbolic knot in the 3-sphere, then the moduli space of hyperbolic
metrics on M = S3\K has at least one component of complex dimension one. Apart fr om
a special point representing the cusped 3-manifold, a gener ic point in this moduli space
corresponds to an incomplete hyperbolic structure on M with a conical singularity or some
other kind of degeneration along the knot K, see e.g. [64] for more details.
A convenient way to describe the space of incomplete hyperbo lic structures on M =
S3\K is to identify a hyperbolic structure with a SL(2,C) structure. Then, the moduli
17 Notice, that our normalization of the Chern-Simons invaria nt agrees with [52,55], but diﬀers
from the normalization used in [36] by a factor of 2 π2.
37
space of SL(2,C) structures is described by the character variety which, i n turn, is given
by the zero locus of the A-polynomial [46],
A(l,m ) = 0 (5 .5)
where l and m are the complex-valued ‘eigenvalues’ of the holonomies (2. 10) around the
longitude and the meridian of a knot. In these variables, the point in the moduli space
representing the complete metric on M is located at ( l,m ) = ( −1, 1). The change of
the volume and the Chern-Simons invariant is described, res pectively, by the diﬀerential
1-forms (3.30) and (3.31) on the curve (5.5):
d Vol(M ) = 2
(
− log|l|d(argm) + log|m|d(argl)
)
d CS(M ) =− 1
π2
(
log|m|d log|l| + (argl)d(argm)
) (5.6)
Therefore, if K is a hyperbolic knot, the right-hand side of the volume conje cture
(5.4) has a natural generalization. For a given knot K, we can consider a family of
(incomplete) hyperbolic metrics on M and regard Vol( M ) and CS (M ) as functions on
the curve A(l,m ) = 0 obtained by integrating (5.6), cf. ﬁg. 7,
Vol(l,m ) = Vol(K) + 2
∫ (
− log|l|d(argm) + log|m|d(argl)
)
CS (l,m ) = CS (K)− 1
π2
∫ (
log|m|d log|l| + (argl)d(argm)
) (5.7)
Here, Vol(K) and CS (K) refer to the volume and the Chern-Simons invariant of the
complete hyperbolic metric on the knot complement (more gen erally, the Gromov norm of
K).
In order to ﬁnd a suitable generalization of the left-hand si de of the volume conjecture
(5.4), let us look at the path integral deﬁnition of the color ed Jones polynomial. In quantum
ﬁeld theory, the colored Jones polynomial evaluated at the k-th root of unity appears as
the normalized 18 expectation value of a Wilson line in the SU (2) Chern-Simons theory [3],
JN (K,e 2πi/k ) =⟨TrRj P exp
∮
K
A⟩ (5.8)
18 Here, the word “normalized” refers to a factor of ZSU (2)(S3) in the denominator of the path
integral. In the following section we will introduce anothe r version of the colored Jones polyno-
mial, often used in the mathematical literature, where JN (K, q) is further normalized relative to
JN (unknot, q).
38
where k stands for the (renormalized) value of the level, and Rj is an irreducible spin- j
representation of SU (2) of dimension N = 2j + 1. Therefore, the left-hand side of the
volume conjecture (5.4) can be interpreted as a classical li mit of the Chern-Simons-Witten
invariant (5.8), such that
k→∞ , N →∞ , N
k = 1 (5 .9)
In physics, Wilson lines represent trajectories of massive point-like particles. Inter-
acting with gravity such particles produce conical defects in the geometry of space-time,
so that the deﬁcit angle is proportional to the mass of the par ticle [13]. These heuristic
arguments suggest that, in the present context, a Wilson lin e (5.8) should be associated
with a conical singularity along the knot K, with a deﬁcit angle ∼ N/k. On the other
hand, deformations of the hyperbolic structure on M with a conical singularity along the
knot K are parametrized by the curve (5.5), with |m| = 1. Therefore, one might expect
log(m)∼ 2πi
(
1− N
k
)
(5.10)
These considerations suggest that the proper modiﬁcation o f the left-hand side of the
volume conjecture (5.4), that includes deformations of the hyperbolic structure on M ,
should be obtained by replacing (5.9) with a more general dou ble-scaling limit,
k→∞ , N →∞ , a ≡ N
k = ﬁxed (5 .11)
The ratio, a = N/k, which is kept ﬁxed in this limit, does not need to be a rationa l
number. In fact, the relation (5.10) suggests that, in order to compare with the volume
and the Chern-Simons invariant computed from the A-polynom ial, the parameter a must
be treated as a continuous complex variable. Moreover, rati onal values of a (except for
a = 1) are special, in a sense that the asymptotic behavior of th e colored Jones polynomial
“jumps” in such cases. Again, this suggests to consider gene ric values of a. Since the
colored Jones polynomial is deﬁned for all values of q, not only for the roots of unity, a
natural way to realize this is to keep N integer, and take k = N/a to be non-integer 19.
Then, by analogy with (5.4), we expect the following conject ure to be true:
19 Alternatively, one could consider an analytic continuatio n of JN (K, q) to non-integer values of
the color, N . Even though eventually this possibility may play an import ant r´ ole in the connection
with the SL(2,C) Chern-Simons theory, it seems less obvious at present. Se e however [83], which
may be relevant here. I wish to thank D. Thurston for pointing out this reference and for helpful
discussions on related topics.
39
The Generalized V olume Conjecture: In the limit (5.11), the N -colred Jones
polynomial has the following asymptotic behavior:
lim
N,k →∞
logJN (K,e 2πi/k )
k = 1
2π
(
Vol(l,m ) +i2π2CS (l,m )
)
(5.12)
where Vol(l,m ) andCS (l,m ) are the functions (5.7) on the zero locus of the A-polynomial ,
evaluated at the point
m =− exp(iπa) (5 .13)
This identiﬁcation of the parameters agrees with the expect ed relation (5.10), where we
ﬁxed the exact numerical factor by considering speciﬁc exam ples, see below.
Note, that the generalized volume conjecture (5.12) presen ts a 1-parameter family of
relations, which include the well-known volume conjecture (5.4) as a special case, m = 1.
Below, we demonstrate that (5.12) is true for the ﬁgure-eigh t knot.
