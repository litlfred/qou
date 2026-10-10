> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# Kashaev limit for the pair-gen term — investigation

**Date:** 2026-05-05
**Branch:** `claude/categorical-mass-divergence-audit` (PR #534)
**Refs:**
- [`prop:rho-k-graded-expansion`](../../content/quantum-observable-universe/braids-and-knots/rho-k-graded-expansion.md)
- [`prop:atomic-braid-mass`](../../content/quantum-observable-universe/particle-interactions/atomic-braid-mass.md)
- [`thm:knot-mass-formula-unified`](../../content/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.md)
- [`computations/wedderburn_pair_volumes.py`](../../computations/wedderburn_pair_volumes.py)
- [`computations/rho-k-pair-gen-v2-wedderburn.witness.json`](../../computations/rho-k-pair-gen-v2-wedderburn.witness.json)

## Setup

The unified ρ_K graded expansion proposes a pair-gen term

$$
  \rho_K^{\text{pair-gen}} \cdot m_e \cdot |\text{tr}_M(\beta_K)|
  \;=\;
  \alpha \, z^2 \!\!\sum_{i<j}\!\! \ln\bigl|\hat V_i \hat V_j\bigr|_{\text{Wedderburn}}
$$

as the parallel of the single-gen term $\alpha \sum_i \ln|\hat V_i^\text{full}|$
(proven empirically at $0.18\%$ in `prop:atomic-braid-mass`). The parallel
is supposed to follow from the Kashaev limit of the six-term theorem's

$$
  T_3 \;=\; -z^2 \!\!\sum_{i<j}\!\! \mathrm{Li}_2^q(-|\hat V_i \hat V_j|),
$$

just as $\alpha \sum \ln|\hat V_i|$ is supposed to be the Kashaev limit of
$T_2 = -\sum_i \mathrm{Li}_2^q(-|\hat V_i|)$.

## Empirical findings

### 1. The supposed Kashaev integration identity does not hold numerically

The claimed identity
$\int_0^V (\ln_q(1+t)/t) \, dt = -\mathrm{Li}_2^q(-V)$
fails at $V = 0.14$ (typical atomic per-generator volume) for the
standard $q$-deformed log convention:

|Quantity|Value at $V=0.14$|
|:---|---:|
| $-\mathrm{Li}_2^q(-V)$ | $+0.1354$ |
| $\int_0^V \ln_q(1+t)/t \, dt$ | $-0.0096$ |
| diff | $0.145$ |

The two functions are not even sign-consistent. The integration
derivation in [`prop:mass-endomorphism-tower`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md)
either uses a different $\ln_q$ convention or is itself approximate.

### 2. $\alpha \cdot \ln|V|$ and $-\mathrm{Li}_2^q(-V)$ differ by ~50× in magnitude with opposite signs

At $V = 0.14$:

|Quantity|Value|
|:---|---:|
| $-\mathrm{Li}_2^q(-V)$ | $+0.1354$ |
| $\alpha \cdot \ln\lvert V \rvert$ ($\alpha = 3.74$ MeV) | $-7.35$ |
| ratio $\alpha \cdot \ln V / (-\mathrm{Li}_2^q(-V))$ | $\approx -54$ |

So $\alpha \sum \ln |\hat V_i^\text{full}|$ is **not** the Kashaev limit
of $T_2$ in any meaningful sense. The two formulas are
**structurally different functions** that happen to both produce
sub-percent atomic-mass accuracy via different mechanisms.

### 3. Implication for the pair-gen term

There is **no clean Kashaev limit identity** to derive
$\alpha z^2 \sum \ln|\hat V_i \hat V_j|$ from $T_3 = -z^2 \sum \mathrm{Li}_2^q(-|V_i V_j|)$.
The single-gen analog is itself an empirical match, not a derived limit.

The pair-gen extension to $\rho_K$ therefore needs **either**:

**(a) Empirical fit:** find the prefactor $c$ in
$c \sum \ln|\hat V_i \hat V_j|_\text{Wedd}$ that minimises the
mean atomic-mass error. From the empirical Wedderburn-pair probe
(`rho-k-pair-gen-v2-wedderburn.witness.json`, $Z = 1..20$):

| Pair coefficient | Mean \|err\| | Max \|err\| |
|:---|---:|---:|
| $0$ (single-gen alone) | $0.25\%$ | $0.35\%$ |
| $\alpha z^2 \approx 0.93$ MeV (current) | $4.68\%$ | $8.95\%$ |
| ? (smaller $\|c\|$) | could improve | open |

A simple least-squares fit on $c$ would set $c \approx 0$ (the single-gen
form already fits well; any non-zero pair correction degrades). This is
a **negative result for the pair-gen extension as stated**.

**(b) Direct $\mathrm{Li}_2^q$ form (not Kashaev-limited):** use $T_3$
directly in MeV via the $E_0$ scaling from the six-term theorem:

$$
  \rho_K^\text{pair-gen} \cdot m_e |\text{tr}_M|
  \;=\;
  -E_0 \cdot z^2 \!\!\sum_{i<j}\!\! \mathrm{Li}_2^q(-|\hat V_i \hat V_j|_\text{Wedd}).
$$

This is the un-Kashaev-limited form. It avoids the $\ln \to \mathrm{Li}_2^q$
substitution mismatch but introduces the $E_0$ proton-calibration
constant (which the atomic-braid-mass formula manages to avoid via
the $\alpha = m_e \cdot 8G$ closed form).

**(c) Path-B defect-binding form** (`path-b-defect-binding-probe.witness.json`):
$B(K) = \alpha \cdot (|\text{tr}_M^\text{free}| - |\text{tr}_M^\text{atomic}|)$
already achieves $0.34\%$ across $A = 1..6$ via a fundamentally
different binding model — no per-generator decomposition at all,
just a global free-vs-atomic Markov-trace difference.

## Open problem (revised)

The pair-gen functional form is genuinely open. The single-gen
empirical formula $\alpha \sum \ln|\hat V_i^\text{full}|$ does
**not** generalise to a pair term via the formal Kashaev-limit
substitution; the single-gen form is itself not a proven Kashaev
limit. Closing the pair-gen piece requires:

1. **Either** a deeper categorical derivation that produces the
   correct functional form for binding corrections at all orders
   (single-gen, pair-gen, triple-gen, …) from a unified principle —
   not the term-by-term substitution we currently have.
2. **Or** acceptance that the atomic-braid-mass formula is already
   close to optimal at the $\alpha \sum \ln|V_i|$ truncation; pair
   and higher corrections are below the detection threshold of
   CODATA atomic masses for $Z = 1..20$.

The empirical evidence supports (2): adding any pair term degrades
the fit. The "graded expansion" framework is therefore **a
structural identification with the six-term theorem**, not a
practical accuracy improvement for atomic masses.

## Status update for `prop:rho-k-graded-expansion`

The graded-expansion framework remains valid as a **structural
identification** with the six-term theorem (term-by-term
correspondence with $T_1, T_2, T_3, T_4, T_5, T_6$), but the
pair-gen and higher pieces are **not currently expressible** as
simple log-volume corrections analogous to the single-gen piece.
The open work is the underlying derivation of the Kashaev limit
itself — which the empirical evidence suggests does not produce
an exact $\ln$-form for any single channel, just a rough
single-gen approximation that happens to dominate at the
binding-energy scale relevant to atomic masses.

## Recommendation

Update [`prop:rho-k-graded-expansion`](../../content/quantum-observable-universe/braids-and-knots/rho-k-graded-expansion.md)
to:
1. Keep the structural identification with the six-term theorem (term-by-term correspondence).
2. Mark the pair-gen and higher pieces as **open functional-form questions** rather than "Wedderburn-coupling implementation tasks".
3. Reference this audit for the empirical evidence that the simple log-form fails.

The honest summary: ρ_K is fully captured to $0.18\%$ across $Z=1..20$
by the single-gen log-volume correction, and pushing accuracy further
requires a different categorical derivation (the path-B defect-binding
form is one alternative, achieving $0.34\%$ via a global Markov-trace
difference rather than per-generator decomposition).
