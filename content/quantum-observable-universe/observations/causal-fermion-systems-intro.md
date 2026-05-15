Causal fermion systems (CFS), developed by Finster and collaborators
over the past two decades
[`finster2021`, `finster2022`, `finster2024`, `dappiaggi2024`], are a
parallel program for unifying quantum field theory with general
relativity by replacing the smooth spacetime continuum with operators
on a Hilbert space and a universal measure that minimises a causal
action. The framework derives effective linear dynamics for spinorial
wave functions, an effective collapse mechanism, a candidate
baryogenesis mechanism, and a holographic-mixing route to standard
Fock-space QED dynamics — all from variation of the causal action.

QOU and CFS share motivation and structure: both reject the smooth
continuum as fundamental, both posit a discrete or operator-algebraic
substrate, both define dynamics by an action principle, and both
attempt to derive Dirac dynamics and emergent geometry as
consequences. They differ in machinery. CFS works directly over the
complex numbers and uses Lebesgue measures on operator sets; the
emergent spacetime is the support of the universal measure $\rho$.
QOU works pre-Archimedean: states are categorical, traces are
$R$-valued for $R = \mathbb{Z}[q^{\pm 1/2}]$, particles are knots in
the exceptional divisors of the Bring's-surface fibre, and time
evolution is Gröbner–Shirshov reduction on $H_n(R, q)$.

The aim of this section is narrow. We do *not* claim that CFS is the
Archimedean realisation
([archimedean realization functor](#def:archimedean-realization-functor))
of QOU — that role is occupied by $\tau_{\mathrm{arch}}$, whose
established targets are scalar period invariants such as the
hyperbolic volume
([Kashaev volume conjecture](#conj:kashaev-volume-conjecture)) and
the classical dilogarithm
([dilogarithm archimedean limit](#conj:dilogarithm-archimedean-limit)).
What we show instead is that *on the algebraic side*, before any
limit is taken, QOU already implements a discrete, $R$-valued
analogue of the Finster causal-action variational principle: the Hecke
operator algebra $A_q = H_n(R, q)$ carries the q-Plancherel measure
$\tilde w_\lambda$, the Markov trace factors as integration against
$\tilde w_\lambda$, and the operator-selection LP
([operator-selection LP](#prop:operator-selection-lp))
plays the role of the variational principle, with the LP active set
furnishing the discrete analogue of $\mathrm{supp}(\rho)$. The
Archimedean limit of this structure is conjectural and would be a
*different* functor from $\tau_{\mathrm{arch}}$ — measure-valued
rather than scalar-valued.

Section roadmap. We first state the algebraic causal-action structure
on $A_q$ as a provable proposition assembled from existing QOU
infrastructure (Wedderburn decomposition, Markov trace, q-Plancherel
weight, LP duality). We interpret the proposition as a categorical
mirror of CFS. We then state the conjectural Archimedean lift
$\mu_{\mathrm{arch}}$ that would carry this discrete measure to a
Finster universal measure on a continuous operator algebra, and close
with a remark situating CFS as the post-wall shadow of the
measure-valued lift.
