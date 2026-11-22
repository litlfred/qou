---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8"
section_id: sec-018-5-preservation-of-negative-dependence-by-symmetr
section_title: "Preservation of negative dependence by symmetric exclusion processes"
section_number: 5
pages: 31-33
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8 — 24 sections: Front matter; Introduction; A plethora of negative dependence"
---
by symmetric exclusion processes
In this section we study some consequences of the results in §4 for symmetric
exclusion processes and provide an answer to the problem of ﬁnding a natural
negative dependence property that is preserved by such evolutions (Problem 3.5).
Let us ﬁrst describe these processes in more detail. A conﬁguration of particles
on a countable set S is a point η on the Boolean lattice 2S, which we identify with
{0, 1}S, so η(i) = 1 means that site i is occupied, while η(i) = 0 means that it is
vacant. One is given a non-negative symmetric kernel Q = (qi,j)i,j∈S satisfying
(16)
sup
i

j
qi,j < ∞.
The corresponding exclusion process ηt is the Markov process on {0, 1}S in which
η →τi,j(η) at rate qi,j, where τi,j is the transposition that interchanges the coordi-
nates η(i) and η(j). Note that if η(i) = η(j) (i.e., the two sites are both occupied or
both empty), this transposition has no eﬀect, while if η(i)̸ = η(j), the transposition
has the eﬀect of moving the particle from the occupied site to the vacant site. In the
language of semigroups and generators, the semigroup T(t) on C({0, 1}S) deﬁned
by T(t)F(η) = EηF(ηt) has a generator
LF(η) = 1
2

i,j
qi,j[F(τi,j(η)) −F(η)]
for functions F that depend on ﬁnitely many coordinates. Condition (16) guaran-
tees that the process is well deﬁned and uniquely determined by Q.
One can give a more probabilistic description of the symmetric exclusion process
in terms of Poisson processes. Recall that a Poisson process N(t) with rate λ > 0
is a random increasing step function with jumps of size one, in which the times
between jumps are independent exponentially distributed random variables τk with
parameter λ: P(τk > t) = e−λt.
Now take a collection Ni,j(t) of independent
Poisson processes indexed by unordered pairs i, j (Ni,j(t) with rate qi,j) and apply
the transposition τi,j to η at the jump times of Ni,j(t). We will denote probabilities
for the process with initial conﬁguration η by P η.
Negative correlation inequalities have played an important role in the develop-
ment of the theory of symmetric exclusion processes. For example, Proposition 1.7
of [52, Chap. VIII] implies that
(17)
P η(ηt ≡1 on A) ≤

i∈A
P η(ηt(i) = 1),
A ⊆S.
This inequality was used in an essential way in the characterization of stationary
distributions of the process; see Theorem 1.44 in op. cit. and the end of this section.
Inequality (17) was generalized by Andjel in [2] to
P η(ηt ≡1 on A ∪B) ≤P η(ηt ≡1 on A)P η(ηt ≡1 on B),
A, B ⊆S, A ∩B = ∅,
(18)
and used to prove an ergodic theorem. For further applications of correlation in-
equalities in this setting; see the references and discussion in [55].
552
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
In that paper, one of us conjectured that the distribution of ηt at time t with
deterministic initial conﬁguration η is negatively associated. Even the special case
P η(ηt ≡1 on A, ηt ≡0 on B) ≥P η(ηt ≡1 on A)P η(ηt ≡0 on B),
A, B ⊆S, A ∩B = ∅
(19)
remained open (note that in (19), one of the events is increasing while the other is
decreasing). Surprisingly, despite the similarity between (18) and (19), neither the
proof of (18) in [2], nor a somewhat diﬀerent one given in [55], extends to prove
(19). We are now able to prove this conjecture; see Theorem 5.2 below. The latter
is actually a consequence of a yet stronger property for ﬁnite symmetric exclusion
processes that we will now establish.
Proposition 5.1. Suppose that S is ﬁnite and the initial distribution η0 of a sym-
metric exclusion process on {0, 1}S is strongly Rayleigh. Then so is the distribution
of ηt for all t > 0.
Proof. First, we observe that it suﬃces to prove the statement in case qi,j̸ = 0 for
only one pair i, j. To see this, suppose T1(t) and T2(t) are semigroups for ﬁnite state
Markov chains on the same state space with generators L1 and L2 respectively, and
let T(t) be the semigroup with generator L1 + L2. The Trotter product formula
(see [27, p. 33]) gives
T(t) = lim
n→∞
&
T1(t/n)T2(t/n)
'n.
It follows that if a closed set of probability measures M on the state space has the
property that µ ∈M implies µTi(t) ∈M for i = 1, 2 and t > 0, then µ ∈M
implies µT(t) ∈M for t > 0. Now write the generator of the symmetric exclusion
process as the following sum, corresponding to transitions at individual pairs of
sites:
L =

i,j
Li,j,
where
Li,jF(η) = 1
2qi,j[F(τi,j(η)) −F(η)].
Repeated application of the preceding observation with M = the set of probability
measures on {0, 1}S with stable generating polynomials, implies that the statement
of the proposition is correct for the process with generator L if it is correct for the
process with generator Li,j for each i, j.
In the case of a single non-zero qi,j, the generating polynomial of the distribution
of ηt is given by αf(z) + (1 −α)f(τi,j(z)), where α = P(Ni,j(t) is even) and f is
the generating polynomial for the initial distribution. Therefore, the result follows
from Theorem 4.20.
□
Recall from §2.4 that if S is a countably inﬁnite set, a probability measure on
{0, 1}S is strongly Rayleigh if every projection onto a ﬁnite subset of S is strongly
Rayleigh. Note that this property is preserved by weak convergence of measures.
Theorem 5.2. Suppose that S is countable and the initial distribution η0 of a
symmetric exclusion process on {0, 1}S is strongly Rayleigh. Then the distribution
of ηt is strongly Rayleigh, and hence CNA+, for all t > 0.
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
553
Proof. Since stability (the strongly Rayleigh property) implies negative association
by Theorem 4.9, the result follows from Proposition 5.1 when S is ﬁnite. For general
S, approximate the exclusion process on S by processes on ﬁnite subsets Sn of S
that increase to S, by taking the transposition rates for the process on Sn to be
qi,j if i, j ∈Sn and zero otherwise. By the Trotter-Kurtz semigroup convergence
theorem (see [27, p. 28]), the processes on Sn converge to the process on S, so the
result holds on S as well. (See [52, §I.3] for details.)
□
Remark 5.1. In particular, Theorem 5.2 proves Conjecture 2.2 and shows that its
conclusion remains valid if the initial conﬁguration is a product measure (since any
such measure is obviously strongly Rayleigh; cf. Deﬁnition 2.11 and §2.4).
We conclude this section with an application of Theorem 5.2 to the extremal sta-
tionary distributions for an irreducible symmetric exclusion process. Theorem 1.44
of [52, Chap. VIII] states that these are exactly {µα : α ∈H}, where
(a) H =
(
α : S →[0, 1] : 
j qi,j[α(j) −α(i)] = 0 for each i
)
are the harmonic
functions for Q with values in [0, 1], and
(b) µα = limt→∞ναT(t), where να is the product measure on {0, 1}S satisfying
να{η : η ≡1 on A} =

i∈A
α(i),
A ⊆S.
Very little is known about µα other than
(I) µα = να if and only if α is constant, and
(II) µα{η : η(i) = 1} = α(i) for each i ∈S.
As a consequence of Theorem 5.2, we can now add
(III) µα is negatively associated for each α ∈H.
Remark 5.2. If S is ﬁnite and qi,j > 0 for all i, j, then as we noted in §3.5 the
limiting distribution of ηt as t →∞is the symmetrization of the initial distribution.
In §7 we construct examples of measures in Pn, n ≥20, that are CNA+ but do
not have ULC rank sequences. By Theorem 3.7 in §3.5, these counterexamples to
Conjectures 2.3–2.5 show that none of the properties NLC, h-NLC, Rayleigh/h-
NLC+, CNA, or CNA+ is preserved by the symmetrization procedure (2), and by
[55, Theorem 3.2], the same can be said about the NA property. Therefore, the
analog of Proposition 5.1 fails for all the aforementioned properties.
Remark 5.3. The analog of Theorem 5.2 for asymmetric exclusion processes is false.
A simple example is obtained by taking S = {1, 2} in which only transitions from
state 1 to state 2 are allowed. If the initial distribution gives probability 1
4 to each
of the conﬁgurations in {0, 1}S, then the limiting distribution as t →∞is given by
µ({11}) = µ({00}) = 1
4, µ({10}) = 0, and µ({01}) = 1
2. This measure is not NA.
