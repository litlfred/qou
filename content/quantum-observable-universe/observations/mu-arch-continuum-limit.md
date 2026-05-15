**Conjecture ($\mu_{\mathrm{arch}}$ Lagrangian-universality match).**
*Under the joint Faddeev / Kerov–Vershik scaling $n \to \infty$,
$q \to 1$, $n\lvert 1 - q\rvert \to \infty$, on the shared free-
probability spectral limit
$\Omega_q^{\infty}$ ([q-Plancherel asymptotic skeleton](#prop:q-plancherel-asymptotic-skeleton)),
the Finster causal Lagrangian
$\mathcal{L}_{\mathrm{CFS}}(x, y)$ — a max-of-pair-products
symmetric functional of $\mathrm{spec}(x \cdot y)$
[`finster2024`, §2] — agrees with the Plancherel-weighted character
generating function*
$$
  Z_{\mathrm{Pl}}(x \cdot y)
  \;:=\;
  \sum_{\lambda} \tilde w_\lambda \, \chi_\lambda(x \cdot y),
$$
*after the traceful projection
$\Pi_{\mathrm{tr}}$ ([CFS as traceful projection of QOU](#prop:cfs-as-traceful-projection-of-qou))
identifies CFS data with QOU's commutative spectral shadow.*

**What this narrowed conjecture buys.** Everything except the
Lagrangian form is now established or near-established:

| Clause of $\mu_{\mathrm{arch}}$ | Status |
|---|---|
| Operator-algebra embedding $H_\infty(q) \hookrightarrow L(\mathcal{H})$ | *Established* — [`prop:algebraic-gns-embedding`](#prop:algebraic-gns-embedding), Jones–Wenzl 1985–88 |
| Measure convergence $\tilde w_\lambda \to \mu_\infty^{(q)}$ | *Near-established* — [`prop:q-plancherel-asymptotic-skeleton`](#prop:q-plancherel-asymptotic-skeleton); q-deformed Kerov–Vershik conjectural piece only |
| Type II$_1$ / free-probability universality class | *Established* — Voiculescu–Biane; same class for both QOU and CFS carriers |
| Trace = Plancherel integral of central characters | *Provable* — [`prop:algebraic-causal-action-structure`](#prop:algebraic-causal-action-structure) part (1) |
| Active set $\widehat{A}_q^{\,\mathrm{active}} \to \mathrm{supp}(\rho)$ | *Conditional* on measure convergence; otherwise structurally automatic |
| **Lagrangian form: $\mathcal{L}_{\mathrm{CFS}} \stackrel{?}{=} Z_{\mathrm{Pl}}$** | **Genuinely conjectural** |

**The two outcomes.** The conjecture bifurcates into two possibilities,
each scientifically informative:

*(i) The Lagrangians agree.* Finster's max-of-pair-products extremal
functional reduces, on the free-probability spectral limit, to the
Plancherel-weighted character generating function. In this case
$\mu_{\mathrm{arch}}$ is a theorem (modulo the q-deformed Kerov–Vershik
input): CFS is the post-wall continuum realisation of QOU's
trace-projection $\Pi_{\mathrm{tr}}$, and the two frameworks describe
the same effective continuum physics.

*(ii) The Lagrangians disagree.* The two frameworks share carrier
algebra, universality class, and measure-theoretic data, but extract
different real-valued functionals from the same spectral input. The
emergent continuum dynamics are *different* even though the
underlying operator algebra and spectral measure are the same — a
genuine theory-bifurcation. QOU's Plancherel-weighted dynamics would
describe one continuum theory; Finster's causal-action dynamics
another. The substrate parameter $q_0 \approx 1.11$ would then
select between them based on which Lagrangian gives the observed
particle masses.

**Either outcome is interesting.** Case (i) is a substantial
unification — QOU and CFS would be two presentations of the same
post-wall theory. Case (ii) is a sharp falsifiability: the
QOU trace-projection dynamics could be tested against Finster's
predictions for collapse rates, baryogenesis asymmetry, or
holographic-mixing Fock-space corrections [`finster2024`,
`finster2022`, `dappiaggi2024`]. Disagreement would not refute
either framework but would localise the empirical difference to a
single functional-form question on the free-probability limit.

**What is no longer in the conjecture.**

- The operator-algebra embedding (clause 1 of the previous version):
  promoted to [`prop:algebraic-gns-embedding`](#prop:algebraic-gns-embedding).
- The measure convergence (clause 2): promoted to
  [`prop:q-plancherel-asymptotic-skeleton`](#prop:q-plancherel-asymptotic-skeleton),
  modulo the q-deformed Kerov–Vershik input which is independently
  cited.
- The active-set convergence (clause 4): structurally automatic once
  measure convergence holds, since LP active sets are continuous
  functions of the weight vector under non-degeneracy.

**Lean encoding.** Stated as a class with a single content field —
the Lagrangian-match equation — together with the structural
preconditions on the free-probability spectral limit. Per CLAUDE.md
§3b-cond, downstream Lean theorems requiring the match carry the
class as an explicit hypothesis; the only `sorry` in any downstream
chain lives in the conjectural instance.

**Distinction from $\tau_{\mathrm{arch}}$.** As before, $\tau_{\mathrm{arch}}$
is scalar-valued (Kashaev volumes, dilogarithm periods). The
measure-valued $\mu_{\mathrm{arch}}$, after this revision, is *almost
entirely provable* — it factors as
$\Pi_{\mathrm{tr}}$ (provable) followed by the Lagrangian match
(the residual conjecture).
