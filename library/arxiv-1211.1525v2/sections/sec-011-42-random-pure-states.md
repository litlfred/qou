---
doc_id: arxiv-1211.1525v2
doc_title: "PARTIAL TRANSPOSE OF RANDOM QUANTUM STATES: EXACT FORMULAS AND MEANDERS"
section_id: sec-011-42-random-pure-states
section_title: "Random pure states"
section_number: 4.2
pages: 18-19
source_pdf: 1211.1525v2.pdf
source_sha256: 51ff1c8f90c025a4
toc_source: outline
---
the latter shows a connection to the meander polynomials.
4.2. Random pure states. We start with the case l = 1 of trivial environ-
ment space Cl; this corresponds to ρ being a random pure state.
Theorem 4.1. Let l = 1. Then the empirical eigenvalues distribution (4.1)
converges almost surely as n →∞to
(4.3)

1 −1
c

δ0 + 1
cµB√X1X2
in the weak topology of probability measures. Here, µB√X1X2 is the distri-
bution of B√X1X2, where the distribution of random variables X1 and X2
is the free Poisson distribution ν1,c as in (2.4), and B takes the value 1 or
−1 with probability 1/2, and they are all (classically) independent.
Before showing the proof let us make some remarks. First, when c < 1
the coefﬁcient of δ0 from the ﬁrst summand is negative, but this negativity
is canceled by the mass from the second summand. Secondly, the case
when l = c = 1 was considered by Aubrun [Aub12, Proposition 9.1] which
reads that the limiting distribution is the product of two independent random
PARTIAL TRANSPOSE OF RANDOM QUANTUM STATES
19
variables, each with the semicircular distribution SC0,1 (with mean 0 and
variance 1). Since if Y is a random variable with a semicircle law SC0,1
then its square Y 2 has the Poisson distribution ν1,1, this is a special case
of Theorem 4.1. However, one should be able to recover Theorem 4.1 via
this method as well. Also, analysis of Schmidt coefﬁcients of ψ, where
ρ = |ψ⟩⟨ψ| explains why the operator ρΓ has at most min(m, n)2 non-zero
eigenvalues for l = 1 and why the distribution (4.3) has the atom at zero.
Proof of Theorem 4.1. For a technical reason, we consider the following
rescaled empirical distribution:
(4.4)
c
mn
mn
X
i=1
λi.
Let p = 2q; we consider permutation α ∈Sp which contributes to (4.2) so
that permutation τ := πα belongs to the following geodesic:
id →τ →π2 = (1, 3, . . . , p −1)(2, 4, . . . , p).
Then the limit moment of (4.4) is equal to c×(4.2), which can be calculated
as follows:
c × (4.2) =
X
id→τ→π2
c#τ =

X
˜τ∈NC(q)
c#˜τ


2
.
Moreover,
X
˜τ∈NC(q)
c#˜τ =
X
˜τ∈NC(q)
Y
V ∈τ
c
coincides with the appropriate moment of the free Poisson distribution νc,1
(with rate c and jump size 1). Hence, for the even moments, square root of
the product of two classically independent free Poisson random variables
gives the right moments. However, since all the odd moments vanish, we
must add the factor B to recover our desired moments to get the limit dis-
tribution of (4.4). After rescaling back this distribution, the additional atom
(1 −1
c)δ0 does not change the moments mp of the measure for p = 1, 2, . . .
but takes care of the correct value of the moment m0 (the total mass of the
measure). This shows convergence in expected moments.
Almost sure convergence can be proven similarly as in the proof of The-
orem 3.1. Since the limit is compactly supported, the converges in moments
implies convergence in the weak sense.
□
