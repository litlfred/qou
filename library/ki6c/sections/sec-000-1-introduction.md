---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-4
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Introduction
In [12, 13] Kashaev deﬁned the Kashaev invariant ⟨L ⟩N ∈C of a link L for N = 2, 3, · · ·
by using the quantum dilogarithm. In [14] he conjectured that, for any hyperbolic link L,
2π
N log ⟨L ⟩N goes to the hyperbolic volume of S3−L as N →∞, and veriﬁed the conjecture
for some simple knots, by formal calculations. In 1999, H. Murakami and J. Murakami
[18] proved that the Kashaev invariant ⟨L ⟩N of any link L is equal to the N-colored
Jones polynomial JN(L; e2π√−1/N) of L evaluated at e2π√−1/N, where JN(L; q) denotes the
invariant obtained as the quantum invariant of links associated with the N-dimensional
irreducible representation of the quantum group Uq(sl2).
Further, as an extension of
Kashaev’s conjecture, they conjectured that, for any knot K, 2π
N log |JN(K; e2π√−1/N)| goes
to the (normalized) simplicial volume of S3 −K. This is called the volume conjecture. As
a complexiﬁcation of the volume conjecture, it is conjectured in [19] that, for a hyperbolic
link L,
JN(L; e2π√−1/N)
∼
N→∞eNς(L),
where we put
ς(L) =
1
2π√−1
(
cs(S3 −L) +
√
−1 vol(S3 −L)
)
,
The ﬁrst author was partially supported by JSPS KAKENHI Grant Numbers 24340012, 16H02145 and 16K13754. The
second author was partially supported by JSPS KAKENHI Grant Number 15K04878.
1
and “cs” and “vol” denote the Chern-Simons invariant and the hyperbolic volume. Fur-
thermore, it is conjectured [9] (see also [3, 10, 35]) from the viewpoint of the SL(2, C)
Chern-Simons theory that the asymptotic expansion of JN(K; e2π√−1/k) of a hyperbolic
knot K as N, k →∞ﬁxing u = N/k is presented by the following form,
JN(K; e2π√−1/k)
∼
N,k→∞
u=N/k: ﬁxed
eNςN 3/2 ω ·
(
1 +
∞
∑
i=1
κi ·
(2π√−1
N
)i)
(1)
for some scalars ς, ω, κi depending on K and u, though they do not discuss the Jones
polynomial in the Chern-Simons theory in the case of vanishing quantum dimension,
which is discussed in [29]. Further, the ﬁrst author showed in [20] that, when K is the 52
knot, the asymptotic expansions of the Kashaev invariant is presented by the following
form,
⟨K ⟩N = eNς(K)N 3/2 ω(K) ·
(
1 +
d
∑
i=1
κi(K) ·
(2π√−1
N
)i + O
(
1
N d+1
))
,
(2)
for any d, where ω(K) and κi(K)’s are some scalars.
The volume conjecture has been rigorously proved for some particular knots and links
such as torus knots [15] (see also [4]1), the ﬁgure-eight knot (by Ekholm, see also [1]2),
Whitehead doubles of (2, p)-torus knots [36], positive iterated torus knots [27], the 52 knot
[16, 20], and some links [8, 11, 26, 27, 28, 36]; for details see e.g. [17].
The aim of this paper is to extend the formula (2) to the knots with 6 crossings, that
is, we show the following theorem. In particular, this means that the volume conjecture
holds for these knots.
Theorem 1.1. The asymptotic expansions of the Kashaev invariant ⟨K ⟩N of the knots
K with 6 crossings are presented by the form (2) for any d, where ω(K) and κi(K)’s are
some constants depending on K.
The knots with 6 crossings are the 61, 62 and 63 knots, and all of them are hyperbolic.
Their ς(K) are presented by
ς(61) = ς(61) = 0.5035603... + √−1 · 1.08078... ,
ς(62) = 0.700414... −√−1 · 0.934648... ,
ς(63) = 0.906072... .
We note that their ω(K) and κi(K)’s are also their invariants; in particular, we will show
that their ω(K) are presented by
ω(61) = ω(61) = −0.52139... −√−1 · 0.071732... ,
ω(62) = −0.42920... + √−1 · 0.20337... ,
1A detailed asymptotic expansion of the colored Jones polynomial for torus knots is given in [4].
2A detailed proof of the volume conjecture for the ﬁgure-eight knot was given in [1] and the term N3/2 in (1) and (2)
was also veriﬁed there.
2
ω(63) = 0.416927... .
We note that the values of ς(63) and ω(63) are real, since the 63 knot is amphicheiral.
It is shown [22] that 2√−1 ω2(K) for these knots is equal to the twisted Reidemeister
torsion associated with the action on sl2 of the holonomy representation of the hyperbolic
structure. We also remark that Dimofte and Garoufalidis [2] deﬁne a formal power series
from an ideal tetrahedral decomposition of a knot complement, which is expected to be
equal to the asymptotic expansion of the Kashaev invariant of the knot.
We show proofs of the theorem for the 61, 62, 63 knots in Sections 3.1, 4.1, 5.1 respec-
tively. An outline of the proofs is as follows. From the deﬁnition of the Kashaev invariant,
the Kashaev invariant of K is presented by a sum. We rewrite the sum by an integral by
the Poisson summation formula (Proposition 2.3). When we apply the Poisson summation
formula, the right-hand side of the Poisson summation formula consists of inﬁnitely many
summands, and we show that we can ignore them except for the one at 0 in the sense
that they are of suﬃciently small order at N →∞. Further, by the saddle point method
(Proposition 2.6), we calculate the asymptotic expansion of the integral, and obtain the
presentation of the theorem.
A non-trivial part of the proof is to apply the saddle point method, whose concrete
procedure is quite diﬀerent from the proof for the 52 knot in [20]. In this part, we need
to calculate the asymptotic behavior of an integral of the following form as N →∞,
∫
∆′ exp
(
N
(
V (t, s, u) −ς
))
dt ds du,
for a certain function V (t, s, u) which depends on N, where V (t, s, u) converges to ˆV (t, s, u)
as N →∞, and ς is a critical value of ˆV (t, s, u). Here, ˆV (t, s, u) is the potential function
of the hyperbolic structure of the knot complement. As we mention in Remark 2.7, the
above calculation is reduced to the calculation of the following case,
∫
∆′ exp
(
N
( ˆV (t, s, u) −ς
))
dt ds du.
The domain ∆′ of the integral is a compact domain in R3, and its boundary is included
in the following domain
{
(t, s, u) ∈C3 

 Re
( ˆV (t, s, u) −ς
)
< 0
}
.
(3)
The critical value ς is given by a critical point (t0, s0, u0), and it is located near ∆′ in
C3. In order to apply the saddle point method, we need to show that we can move ∆′
into imaginary direction by a homotopy in such a way that the new domain ∆′
1 contains
(t0, s0, u0), and ∆′
1 −{(t0, s0, u0)} is included in (3), and the boundary of ∆′ always stays
in (3) when we apply the homotopy. We note that, when we restrict the domain (3) to a
suﬃciently small neighborhood of (t0, s0, u0), the resulting space is homotopy equivalent
to a 2-sphere. The existence of the above homotopy means that the boundary of ∆′ is
homotopic to this 2-sphere in the domain (3). It is a non-trivial task to see that they are
homotopic in the domain (3), since it is not easy to see the topological type of the domain
3
(3) directly. We give such a homotopy concretely in Sections 3.5, 4.5, 5.5 for the 61, 62,
63 knots respectively. This part of the proof is quite non-trivial; in fact, we note that we
can not make such a homotopy for the 72 knot as shown in [21].
By the method of this paper, the asymptotic behavior of the Kashaev invariant is
discussed for the hyperbolic knots with 7 crossings in [21] and for some hyperbolic knots
with 8 crossings in [24].
The paper is organized as follows. In Section 2, we review deﬁnitions and basic prop-
erties of the notation used in this paper. In Sections 3, 4, 5, we show proofs of Theorem
1.1 for the 61, 62, 63 knots respectively. In Appendices A, B, C and D, we show proofs of
some lemmas used in Sections 3, 4, 5.
The authors would like to thank Tudor Dimofte, Kazuo Habiro, Hitoshi Murakami,
Toshie Takata and Dylan Thurston for helpful comments.
