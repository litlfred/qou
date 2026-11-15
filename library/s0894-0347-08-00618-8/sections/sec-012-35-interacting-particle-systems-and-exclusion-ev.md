---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8"
section_id: sec-012-35-interacting-particle-systems-and-exclusion-ev
section_title: "Interacting particle systems and exclusion evolutions"
section_number: 3.5
pages: 20-21
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8 — 24 sections: Front matter; Introduction; A plethora of negative dependence"
---
process is one of the main models considered in the area of Probability Theory
known as Interacting Particle Systems. The idea is that particles move in continuous
time on a countable set S, in such a way that there is always at most one particle
per site. The motion of each particle would be a continuous time Markov chain on
S, except that transitions to occupied sites are forbidden. This process has been
used to model many situations, including biopolymers and traﬃc ﬂow. We refer to
[52, Chap. VIII] and [54, Part 3] for detailed treatments of this process.
The (ﬁnite) symmetric exclusion process generates a continuous time evolution
on the set Pn. The limiting measure under the symmetric exclusion evolution with
initial measure µ is the symmetrization µs of µ as deﬁned in §2.1. A problem that
has attracted some attention is the following (see, e.g., [52, 55]).
Problem 3.5. Find a natural negative dependence property that is preserved by
symmetric exclusion evolutions.
Since the limiting distribution of the evolution as t →∞is the symmetrization
of the initial distribution deﬁned in (2), any such property would have to be pre-
served by this symmetrization procedure. In order for a solution to Problem 3.5 to
be useful in settling Conjecture 2.2, the negative dependence property should be
satisﬁed by non-random/deterministic distributions and should imply NA. Prob-
lem 3.5 is also motivated by a theorem of Harris [52, Theorem 2.14] that provides a
general criterion for the preservation of positive dependence for Markov processes.
Theorems 3.1 and 3.3 of [55] give negative dependence properties that are preserved
by the symmetric exclusion evolution. However, one can make an argument that
neither of these is ideal – the ﬁrst is too weak, while the second is too strong. In
[55, Theorem 3.2] it was proved that NA is not preserved by the symmetric exclu-
sion process. The examples that we construct in §7 further show that in fact none
of the properties NLC, h-NLC, Rayleigh/h-NLC+, CNA, CNA+ deﬁned in §2.1
is preserved by such evolutions. This is a consequence of the following criterion
established by Pemantle in [65, Theorem 2.7] (see also [72, Proposition 3.6]) for the
ultra log-concavity of rank sequences of symmetric polynomials in Pn:
Theorem 3.7 ([65]). For 0 ≤k ≤n let ek(z1, . . . , zn) be the k-th elementary
symmetric function on {z1, . . . , zn} and consider the polynomial
f(z1, . . . , zn) =
n

k=0
akek(z1, . . . , zn),
where ak ≥0, 0 ≤k ≤n. The following are equivalent:
(1) f satisﬁes the conclusion of Conjecture 2.4; that is, it has an ULC rank
sequence (cf. Deﬁnition 2.8);
(2) f has either (and then all) of the following ﬁve properties: NLC, h-NLC,
Rayleigh/h-NLC+, CNA, and CNA+.
In §5 we show that the strongly Rayleigh property is preserved by (ﬁnite) sym-
metric exclusion evolutions and thus provide an answer to Problem 3.5. We then
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
541
prove that the distribution at time t > 0 for the (not necessarily ﬁnite) symmetric
exclusion process is CNA+ whenever the initial distribution is a product measure,
which conﬁrms Conjecture 2.2.
Symmetric strongly Rayleigh measures are described in the following theorem.
Recall that a (possibly inﬁnite) matrix A is said to be totally non-negative of order
p, or TPp for short, if for any k ≤p all its k × k minors are non-negative [49]. If A
has all non-negative minors, then A is called totally non-negative, or TP for short.
Theorem 3.8 (Exchangeable Strongly Rayleigh Case). Suppose µ ∈Pn has a
symmetric generating polynomial and rank sequence {rk}n
k=0. The following are
equivalent:
(a) The generating polynomial of µ is stable, i.e., µ is strongly Rayleigh.
(b) All zeros of the univariate polynomial n
k=0 rkzk are real.
(c) The inﬁnite Toeplitz matrix (ri−j)∞
i,j=0 is TP, where rk = 0 if k /∈{0}∪[n].
Proof. The equivalence (b) ⇔(c) is a classical result due to Aissen, Schoenberg
and Whitney [1], while the equivalence (a) ⇔(b) is a consequence of the Grace-
Walsh-Szeg¨o coincidence theorem (see Theorem 4.6 below).
□
