# Poisson / theta resummation of the mass sum — scope + prune verdict

**Date:** 2026-06-17
**Branch:** `claude/bold-rubin-wahq2l`
**Status:** SCOPED + cheap formalize-first prune (REFUTED at the fixed-$n$ level)
**Parent:** [`docs/audits/2026-06-17-d14-theta-bar-side-and-nome-conflation.md`](../audits/2026-06-17-d14-theta-bar-side-and-nome-conflation.md)
(the Jacobi-triple-product / theta avenue on D14)
**Prune probe:** [`computations/probes/theta_poisson_mass_resummation_prune.py`](../../computations/probes/theta_poisson_mass_resummation_prune.py)
→ witness [`theta-poisson-mass-resummation-prune.witness.json`](../../computations/probes/theta-poisson-mass-resummation-prune.witness.json)

## The hypothesis

The Jacobi triple product makes a theta function `θ(z|τ) = Σ_{n∈ℤ} z^n q^{n²}`
Poisson-self-dual: its modular $S$-transform $\tau\mapsto-1/\tau$
(= D14, [`conj:modular-s-transform-q-q-tilde`](../../content/quantum-observable-universe/q-geometric-langlands/modular-s-transform-q-q-tilde.md))
exchanges the small-$|q|$ regime and the root-of-unity regime. The Kashaev
Volume Conjecture lives on the root-of-unity side. So the *deep* hope is:

> Can the framework's **mass observable** — the Markov-trace sum
> $\mathrm{tr}_M = \sum_{\lambda\vdash n} y_\lambda\chi^\lambda$ evaluated at the
> substrate — be written as (or Poisson-resummed into) a theta-type sum, so
> that the D14 $S$-transform bridges the substrate $q_0$ evaluation to the
> Volume-Conjecture root-of-unity asymptotic?

This is D14 Open-R&D item 2 ("verify the Volume Conjecture asymptotic on
$\tilde q_0$ matches the framework's bare-volume evaluation") in its strongest
form.

## Formalize-first prune (AGENTS.md §3.3)

Poisson/theta resummation applies **only** when the sum's $q$-exponent support
lies on a **quadratic lattice** `{a n² + b n + c : n∈ℤ}` (sparse support, gaps
growing linearly `~2an`). The prunable invariant: is a framework trace
polynomial's exponent support theta-shaped (constant positive second difference
of the sorted support)?

| object | exponent support | gaps | theta-compatible? |
|---|---|---|---|
| proton $J$ numerator | `{0,7,8,10,11,18}` | `7,1,2,1,7` | **no** |
| neutron $J$ numerator | `{0,1,2,9,11,18,19,20}` | `1,1,7,2,7,1,1` | **no** |
| theta truncation (control) | `{0,1,4,9,16}` | `1,3,5,7` | **yes** ✓ |

The control (`Σ_{n≤4} q^{n²}`) is correctly detected; the actual proton/neutron
Markov traces are **not** theta-shaped. Their exponents are content- /
hook-length-based (`q^{content(λ)}`, principal-specialization $n(\lambda)$),
which are *not* quadratic in a single lattice index. **Direct Poisson/theta
resummation of the fixed-$n$ mass observable is refuted.**

## Why — and where the theta structure actually lives

The refutation is structural, not a tuning accident:

1. **The mass observable is a finite sum at fixed $n$.** $\mathrm{tr}_M$ runs
   over $\lambda\vdash n$ for the fixed knot/atom — a *finite* index set. A
   theta function is an *infinite* lattice sum. There is no $n\to\infty$ lattice
   to Poisson-dualise at the observable level.

2. **Theta self-duality lives in the tower generating function**, $\sum_{n\ge0}
   z^n\,(\text{class function on }H_n(q))$, via the JTP / Cauchy identities
   (cheat-sheet §4; the $a_8(u)=\sum p(n)u^{5-n}$ partition-function appearance
   is a tower-level fact). The framework evaluates a *fixed* tower level at a
   *fixed* substrate — not the generating function.

3. **The root-of-unity / Volume-Conjecture side is the colored Jones**, a
   genuinely theta/modular object — but it is reached by the $\tilde q$ branch
   of D14, *not* by resumming the substrate mass sum.

## Verdict and parking

- **Not a near-term lever.** The fixed-$n$ mass observable does not Poisson-
  resum; the bridge would require reindexing the whole $H_n(q)$ tower so its
  generating function acquires a quadratic exponent — a large conjectural step
  with no current handle.
- **The concrete, surviving deliverable** of the theta avenue is the
  Task-2 Lean realization of D14 via the theta functional equation, bar-side
  (see parent audit). That stands on its own.
- **The one productive (but hard) continuation**, if revisited: work directly
  on the $\tilde q$ (root-of-unity) branch — relate the colored-Jones Volume-
  Conjecture asymptotic on $\tilde q_0$ to the bare hyperbolic volume already in
  the mass formula (`Vol(𝓑₃)·ρ/ℏ_q²`). That is a comparison of two *independent*
  objects, not a resummation identity, and belongs to the Volume-Conjecture
  thread, not here.

## Cross-references

- Parent audit (bar-side + nome trap): [`2026-06-17-d14-theta-bar-side-and-nome-conflation.md`](../audits/2026-06-17-d14-theta-bar-side-and-nome-conflation.md)
- D14 conjecture: [`conj:modular-s-transform-q-q-tilde`](../../content/quantum-observable-universe/q-geometric-langlands/modular-s-transform-q-q-tilde.md)
- Partition-function tower fact: [`docs/audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md`](../audits/2026-06-01-qbeta-habiro-a8-partition-function-match.md)
- Volume Conjecture: `conj:kashaev-volume-conjecture`
