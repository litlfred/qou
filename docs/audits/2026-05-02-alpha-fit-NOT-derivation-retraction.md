# Retraction: α ≈ 82 · E_0 is FITTING, not categorical derivation

## What I claimed

In commit `4ee273805` and the closing summary I called the
relation $\alpha \approx 82 \cdot E_0$ a "structural binding
formula" linking the binding coefficient to the 6th nuclear
magic number.

## Why that was wrong

The chain of reasoning was:

1. **Fit** $\alpha$ from AME data via least-squares on $B/A$ vs
   $T_6/A^3$. Result: $\alpha = 342.5$ MeV with fit uncertainty
   ~5-10%.
2. **Compute** $\alpha / E_0 = 81.96$.
3. **Notice** that 82 is the 6th nuclear magic number.
4. **Claim** the formula $\alpha = 82 \cdot E_0$ is structural.

Step 1 is a fit to data. Step 2 is arithmetic. Step 3 is
post-hoc pattern recognition. Step 4 conflates these with
categorical derivation.

A **categorical derivation** would start from the framework's
structures (the GS spectral sequence's level-3 page, the
Markov-trace normalization on $H_9(q)$, the q-Plancherel weight
on triple-strata) and **compute** the coefficient $\alpha$
producing 82 (or whatever integer) directly — not extract it
from the fit and then look for matches.

The match $81.96 \approx 82$ is suggestive (and one of seven
magic numbers, so any of them could match by coincidence
within ~5% windows). It is **not** a categorical link until:

- the integer is derived from the spectral sequence, and
- the relation $\alpha = N_\text{magic} \cdot E_0$ is shown
  to follow from the framework's algebraic structure
  (without recourse to AME fitting).

## What's actually established

- The shape $B/A \approx \alpha \cdot T_6/A^3 + \beta + \delta_M$
  with $R^2 = 0.70$ over 7 light atoms is **empirically valid**.
  The Term 6 (level-3 GS-stratum) IS a legitimate binding-energy
  contribution, with two empirically-fit parameters $\alpha, \beta$.
- The magic-pair operator correction (Tier 2, $R = +0.74$ on the
  residual) IS also empirically valid.

These are the rigorous claims. The categorical INTERPRETATION
of $\alpha$ remains **open**.

## What an honest claim would look like

Two-tier formula:

$$
B/A \approx \alpha_\text{fit} \cdot T_6/A^3 + \beta_\text{fit} + \delta_M(Z, N)
$$

with $\alpha_\text{fit}, \beta_\text{fit}$ **calibrated** from
AME data on a 7-atom panel, $R^2 = 0.70$. The shape (cubic
normalization + magic correction) is structurally derived; the
coupling constants are still calibrations.

This is GOOD — it's a 2-parameter calibrated fit that beats
SEMF's 5-parameter fit at the per-atom level (even with magic-
shell residuals). But calling it a "structural binding-energy
derivation without SEMF fitting" was wrong.

## Lesson

Avoid claiming a derivation when:

- one or more coefficients come from a least-squares fit, AND
- the proposed "structural" expression is identified by
  searching among many candidates for the closest match.

Both apply here. The session's results stand on their own
empirical merits — there's no need to dress them up with
spurious categorical interpretations.

## Status

The Term 6 binding-derivation memo
([2026-05-02-Term6-binding-derivation.md](2026-05-02-Term6-binding-derivation.md))
is correct EXCEPT for the implicit suggestion in §"Comparison
with SEMF" that the formula is "structurally distinct" without
empirical fitting. It is structurally distinct in **shape**
(one Term 6 vs five SEMF terms) but the **coefficients** are
still empirical fits.

The α-categorical-probe witness
([2026-05-02-alpha-categorical-probe.witness.json](2026-05-02-alpha-categorical-probe.witness.json))
should be read as a candidate-search audit, not a derivation.
The candidate $82 \cdot E_0$ is the closest in the search; it
might or might not have categorical meaning. The framework
needs to **predict 82** from its own structure before the
match is significant.

## Update 2026-05-03 — superseded compute removed

The two probe scripts that produced this retraction
(`alpha_analytic_attempt.py` and `alpha_categorical_derivation.py`)
have been removed from `computations/`. They were
both **null-result candidate searches** (closest fit
$m_e \cdot [7]_q [8]_q [9]_q = 361.2$ MeV, off by +6.4%; α/E₀ ratio
falsified at 81.27 not 82). Their results stand recorded in the
witness JSONs under `docs/audits/`:

- `2026-05-02-alpha-analytic-attempt.witness.json`
- `2026-05-02-alpha-categorical-derivation.witness.json`
- `2026-05-02-alpha-categorical-probe.witness.json`

The downstream **canonical α/binding pipeline** is now the
magic-A formula (`computations/magic_A_formula.py`,
landed via PR #519) which exposes
$$
B \;=\; \rho_F \cdot m_e \cdot A \cdot 8G
$$
as the doubly-magic shell-closure formula at ⁴He (+5.87% vs AME).
Either of the deleted attempts was strictly coarser, and the
attempts contained no infrastructure that magic-A doesn't already
supply. The retraction memo and witnesses preserve the search
record; the compute scripts themselves no longer carry their
weight.
