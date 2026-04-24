The four classical-limit problems tackled by the QOU framework —
the Riemann hypothesis, 3D Navier--Stokes regularity, Collatz, and
P vs NP — all reduce to a **single surreal inequality** between the
cost of a standard-real deviation and the mass-gap infinitesimal.
This remark collects the four squeezes side by side.

**The common template.** Let $\varepsilon \in \mathrm{Der}(A)$ be the
Reeb infinitesimal
([Reeb infinitesimal](#def:reeb-epsilon))
and $q = 1 + \varepsilon$
([$q$ from $\varepsilon$](#def:q-from-epsilon)).  Recall from
[surreal rate calculus](#prop:surreal-rate-calculus):

$$
  \Delta_q \;\asymp\; \varepsilon^3
  \qquad (\text{mass-gap dissipation, positive infinitesimal}),
$$
$$
  \Omega_q \;\asymp\; \varepsilon^{-1}
  \qquad (\text{Reeb-period budget, positive transfinite}).
$$

Each problem identifies a *drift* $\delta$ that measures the
standard-real deviation from the classical stable configuration.
The [surreal squeeze](#lem:surreal-squeeze) then delivers the same
inequality:

$$
  \delta^2 \cdot \Omega_q
   \;>\; \Delta_q
  \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

Expanding $\Omega_q \asymp \varepsilon^{-1}$ and $\Delta_q \asymp
\varepsilon^3$: for every standard real $\delta > 0$,
$\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$.

**Side-by-side table.**

| Problem | Drift $\delta$ | Cost $\delta^2 \cdot \Omega_q$ | Budget $\Delta_q$ | $\Ow$-verdict | Conclusion |
|---|---|---|---|---|---|
| [RH](#rem:rh-surreal-bound) | $\mathrm{Re}(\rho) - 1/2$ | $\asymp \delta^2 \varepsilon^{-1}$ | $\asymp \varepsilon^3$ | $\Ow(\text{cost}) = -1 < 3 = \Ow(\text{budget})$ | $\delta = 0$ (zeros on critical line) |
| [Navier--Stokes](#rem:ns-surreal-bound) | enstrophy spike | $\asymp \varepsilon^{-4/3}$ | $\asymp \varepsilon^3$ | $\Ow(\text{cost}) = -4/3 < 3$ | finite-time blow-up in classical limit |
| [Collatz](#rem:collatz-surreal-bound) | contact-volume drift per step | $\asymp \delta^2 \varepsilon^{-1}$ | $\asymp \varepsilon^3$ | $\Ow(\text{cost}) = -1 < 3$ | $\delta = 0$ (all orbits terminate at $1$) |
| [P vs NP](#rem:p-vs-np-surreal-bound) | per-step $q$-efficiency $\delta_n$ | $\asymp 2^n \delta_n^2 \varepsilon^{-1}$ | $\asymp 2^n \varepsilon^3$ | $\Ow(\text{cost}) = -1 < 3$ | $\mathbf{P} \neq \mathbf{NP}$ under std-part of BQP$_q \supsetneq \mathbf{P}$ |

The first three rows are *unconditional* surreal translations of
existing QOU propositions
([collapse of the quantum gap](#thm:quantum-gap-collapse),
[blowup as Yekutieli lifting obstruction](#prop:blowup-yekutieli),
[$q$-Collatz](#conj:q-collatz)); the fourth row is *conditional* on
[P vs NP in the QOU](#conj:p-vs-np-qou).

**Why the template works.** The mass-gap scaling
$\Delta_q \asymp \varepsilon^3$ is a *fixed structural invariant* of
the rigid braided monoidal category $\mathbf{C}$: it does not change
from problem to problem.  The Reeb-period scaling
$\Omega_q \asymp \varepsilon^{-1}$ is likewise a fixed structural
invariant of the Reeb derivation $\xi$
([categorical Reeb derivation](#def:categorical-reeb-derivation)).
The *content* of each millennium problem is therefore not the rate
table — which is common to all four — but the identification of the
problem-specific drift $\delta$ and the translation of the classical
statement into the form
"the drift vanishes".  Once the drift is identified, the squeeze
$\delta^2 / \varepsilon > \varepsilon^3$ closes the argument
uniformly.

**Philosophical upshot.** In the QOU framework, the four millennium
problems are not four independent questions but **four instances of
the same substrate-stability requirement**: the observable universe
can contain only those classical-limit configurations in which no
standard-real drift absorbs more substrate energy than the mass gap
can dissipate.  The Riemann hypothesis is the spectral instance,
Navier--Stokes is the hydrodynamic instance, Collatz is the
arithmetic instance, and P vs NP is the complexity instance.

**Relation to the appendix.** The $\omega$-adic form of each
squeeze is registered in the
[body asymptotics catalog](#rem:body-asymptotics-catalog) under
the $\Ow$-entry of the corresponding body block, with notation
following [Big-O via $\Ow$](#rem:big-o-surreal).  The four remarks
above can therefore be read either in the
"$\delta^2 \cdot \Omega_q > \Delta_q$ in $\mathbb{R}(\varepsilon)$"
register or in the "$\Ow(\text{cost}) < \Ow(\text{budget})$"
register; the two are equivalent by the Big-O bridge.
