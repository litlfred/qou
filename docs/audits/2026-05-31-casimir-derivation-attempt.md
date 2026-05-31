# Audit: Casimir derivation attempt — what an actual derivation requires

**Date.** 2026-05-31
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**Result.** Derivation requires extending `prop:vacuum-epsilon` with mode-dependent weights, NOT just a single `ε`. The currently-formulated vacuum-epsilon does not suffice.

This audit responds to the critique that the 6th-sweep `π²/(2·[5]_q!_sym)` finding was template fitting, not a derivation. Below is what an actual derivation requires and why it is currently blocked.

## What standard-physics Casimir derivation does

The standard derivation has four steps:

1. **Mode enumeration.** EM modes between two parallel conducting plates have allowed wavevectors `(k_⊥, k_z)` with `k_z = nπ/d` (n = 1, 2, …) and `k_⊥` continuous in ℝ².

2. **Per-mode energy.** Each mode `n` has dispersion `ω_n(k_⊥) = c·√(k_⊥² + (nπ/d)²)` and zero-point energy `(1/2)·ℏ·ω_n(k_⊥)`.

3. **Sum + regularize.** Total energy per area:
   $$
     u(d) = \frac{\hbar c}{2}\int\!\!\frac{d^{2}k_{\perp}}{(2\pi)^{2}}\sum_{n=1}^{\infty}\sqrt{k_{\perp}^{2}+(n\pi/d)^{2}}
   $$
   This diverges; ζ-function regularize to extract the d-dependent finite piece.

4. **ζ-regularization yields `-π²ℏc/(720 d³)`.** The π²/720 emerges from `ζ(-3) = -1/120 = -1/5!`.

The critical fact: **steps 2 and 4 depend on the per-mode energy formula `ω_n(k_⊥)`, which is a function of n through `nπ/d`**. The "n³" in the Casimir sum comes from this n-dependence after k_⊥ integration.

## What the current vacuum-epsilon axiom gives

[`prop:vacuum-epsilon`](../../content/quantum-observable-universe/appendix-surreals/vacuum-epsilon.md) asserts:

$$
  \mathrm{Geom}(\unicode{9737}) = \varepsilon
$$

i.e., every unknot contributes the SAME infinitesimal `ε` to the geometric energy.

Under disjoint-union additivity (Hoefsmit probe, sweep 1):

$$
  \mathrm{Geom}_\varepsilon(N \cdot \unicode{9737}) = N \cdot \varepsilon / \hbar_q^2
$$

This gives the same energy for every unknot, **independent of the unknot's plate-mode index n**.

## The obstacle — vacuum-epsilon is mode-index-blind

Standard Casimir: the n-th mode has energy `ℏc·n·π/d` (a function of `n`). Sum gives `Σ n` (after k_⊥ integration), regularized to ζ(-1) for the energy or ζ(-3) for the next-order term.

QOU under vacuum-epsilon: every unknot has the same `ε`. Sum gives `N·ε` (no n-dependence). After standard-part, this is a *constant* total — does not reproduce the `1/d³` scaling.

**For QOU to derive Casimir, vacuum-epsilon must be extended to:**

$$
  \mathrm{Geom}_\varepsilon^{n}(\unicode{9737}_n) = \varepsilon_n
$$

where `ε_n` is a *family of infinitesimals* indexed by the mode `n` (or by some categorical structure equivalent to mode-counting between plates).

The natural family in surreal terms is `ε_n = n · ε` (linear in n) or `ε_n = ε / n` (1/n weighting) — both are infinitesimals with different birthday ranks.

## Why the 6 probe sweeps all failed to derive

Each probe was a template substitution:
- Take the classical formula
- Substitute classical quantities (n, n!, etc.) with q-deformed analogues
- Compute at substrate
- Compare to π²/720

None of the probes addressed the question "what determines the mode-dependent weighting `ε_n`?" — they all assumed a single ε and tried to recover the n-dependence from external structure. That's why they're fitting.

## What a real derivation needs (3 layers)

1. **Construct N_⊙(A, d) and `ε_n` together as a categorical object.** Each "plate mode" must be associated with a specific unknot configuration AND a specific infinitesimal weight. The map `n ↦ ε_n` must be derived from QOU structure, not postulated.

2. **Verify the regularization is q-equivariant.** The sum `Σ_n ε_n` should converge via some QOU-native mechanism. The 6 candidates tested (Carlitz, KKW, Macdonald, Heine, Tsumura, [5]_q!_sym) are all *post-hoc* choices — any could be right if you accept it; none is forced.

3. **Show the standard-part recovers `-π²ℏc/(720 d³)` at substrate.** This is the consistency check — if the derivation in steps 1-2 doesn't give the textbook answer at substrate, either the derivation is wrong or QOU predicts a measurable deviation.

## Honest current status

- **Sub-problem 1** (categorical N_⊙) — open, blocking everything downstream.
- **Sub-problem 3** (prefactor) — cannot be derived without sub-problem 1; all six probe sweeps were fitting.
- **Open question**: vacuum-epsilon needs extension to mode-indexed `ε_n` family. This is a substantive new conjecture beyond the current `prop:vacuum-epsilon`.

The conjecture's narrative claim "the standard-part recovers the textbook Casimir force per unit area exactly (see the conditional derivation below)" is **technically correct** for the conditional implication (modulo the `PlateModeCount` class hypothesis), but the unconditional derivation requires the open construction work.

## Recommended next step (if pursued)

Drop the focus on the prefactor and tackle sub-problem 1 directly:

> **New conjecture (proposed).** *There exists a categorical family `{ε_n}` of infinitesimals in `No`, indexed by `n ∈ ℕ`, with `ε_n → ε` in some surreal-limit sense and satisfying:*
>
> 1. `ε_n ∝ n · ε` (linear in n, matches `ℏω_n` energy of n-th mode)
> 2. `Σ_n ε_n` is summable in surreal-Borel sense
> 3. `st(Σ_n ε_n · (mode density of plates))` reproduces `-π²ℏc/(720 d³)`

This conjecture has at least a chance of derivation from existing QOU primitives (the family `{ε_n}` could come from `ε · [n]_q`, `ε · n`, or `ε · q^n`; the surreal-Borel summation is a known construction in the surreal-numbers literature).

Until this extension is constructed, the prefactor question is structurally underdetermined and any "derivation" is fitting.
