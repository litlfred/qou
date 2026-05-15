The dictionary in
[algebraic causal-action structure](#prop:algebraic-causal-action-structure)
gives a precise sense in which CFS [`finster2021`, `finster2024`] and
QOU share *structure* without sharing *implementation*. Every
component of the Finster variational data has an algebraic-side
twin on $A_q = H_n(R, q)$, and the twins satisfy the same formal
relations: the trace decomposes as integration against a measure
on the spectrum; the variational principle distinguishes a finite
active set; the active set plays the role of the locus where
physics happens. None of this requires crossing the
[Archimedean wall](#def:archimedean-realization-functor).

The mirror interpretation makes four CFS findings legible in QOU
language without endorsing any specific limit.

**Effective collapse [`finster2024`].** The Finster collapse mechanism
extracts nonlinear and stochastic corrections to the Schrödinger
equation as a small-momentum limit of the causal action. Its
algebraic-side mirror is the operator-selection LP rerun under a
shifted weight vector $t \to t + \delta t$: the active set
$\widehat{A}_q^{\,\mathrm{active}}$ jumps discretely as $\delta t$
crosses a slack-tight transition, and the resulting LP shadow-price
update is the categorical analogue of the collapse jump. This
collapse is fully deterministic on the algebraic side (it is an LP
re-optimisation); the stochastic appearance in CFS arises after
$\pi_\infty$ averages the discrete jumps into a continuous
measure flow.

**Baryogenesis [`finster2022`].** Finster–Jokel–Paganini realise
baryogenesis as an asymmetry in the regularised Dirac sea induced by
cosmological time dependence. Its algebraic-side mirror is the
asymmetric LP support on Borromean-baryon active blocks
([Borromean baryon](#conj:borromean-quark)): the LP optimal
$x^\star$ concentrates on the chirally-asymmetric Wedderburn
projectors, and the asymmetry is an immediate consequence of skein
chirality together with the LP optimality conditions. The
regularisation length $\varepsilon$ of CFS plays no role
algebraically; the asymmetry is purely combinatorial.

**Linear dynamics [`finster2021`].** The Finster linear dynamics for
spinorial wave functions arise from variation of the causal action in
a small-fluctuation regime around an optimal $\rho$. Their
algebraic-side mirror is the linearisation of the LP about
$(x^\star, y^\star)$: the tangent simplex at the optimum is governed
by the dual constraints $G^\top y \leq t$, and small perturbations of
the weight vector propagate as linear flows on the active set. These
are *exactly* the discrete dynamics computed by the Gröbner–Shirshov
reduction engine, transcribed into LP-tangent coordinates.

**Holographic mixing → Fock space [`dappiaggi2024`].** The
holographic-mixing reduction to standard Fock-space QED replaces the
universal measure by a stochastic operator-mixing rule that recovers
canonical commutation relations in a limit. Its algebraic-side
mirror is q-Schur–Weyl duality: the tensor power
$V^{\otimes n}$ already decomposes as
$\bigoplus_\lambda V^\lambda \otimes S^\lambda_q$ with $\lambda$ a
Young diagram, and the Markov trace over this decomposition reproduces
the canonical q-deformed bosonic and fermionic correlators directly,
without invoking stochastic mixing. The CFS holographic step appears
to be the post-wall image of QOU's pre-wall Schur–Weyl decomposition.

In each case the algebraic-side twin is *finite* and *combinatorial*,
proved in $R\otimes\mathbb{Q}$ from existing infrastructure. The
Finster results may be read as the post-wall continuum image of the
discrete LP active-set dynamics — but the QOU-side proof does not
require the limit to be taken.
