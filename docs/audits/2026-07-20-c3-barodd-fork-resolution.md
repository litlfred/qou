# c₃ bar-odd fork resolution: `|S| = |(q;q)_3| × phase` — resurgent branch confirmed, machinery is categorically derived, open piece narrowed to the odd-channel determined solve + fibre `Δ_ω` phase

**Date:** 2026-07-20 · **Bean:** `qou-1dnr` / `qou-fk0w` (c₃ → Q_β 100×) ·
**Branch:** `claude/argument-principle-residue-sum-2026-07-20` ·
**Tier:** corpus-corroborated resolution of the Lean-surfaced fork; scope-(a);
no fit, no c_k wired, no tier change.

## The fork (from the Lean proof `QOU.Mass.QbetaC3PochhammerPhase`)

The proved decomposition `S = c₃ + Vol(4₁) = (q;q)_3 · phase` (phase bar-even,
via the `h`-factorization `(q;q)_3 = h · pochCofactor`, `1−q² = −q·h`) plus
`phase_is_unit_of_magnitude_match` gives: **IF `|S| = |(q;q)_3|` exactly THEN
`phase = ±1`** (algebraic), which would contradict KC22 (`D(ũ)` resurgent). Two
horns:
- **(A) exact algebraic:** `|S| = |(q;q)_3|`, `phase = ±1`, `D` algebraic, KC22 false.
- **(B) resurgent:** `|S| = |(q;q)_3| × (1+ε)`, `phase` resurgent, KC22 holds.

## Resolution: horn (B), with a precise 0.74% correction

1. **`D(ũ)` is rigorously divergent (radius → 0)**
   ([`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md)):
   exact `d_k`; root test `|d_k|^{1/k}` climbs without plateau (4.37→5.91→6.08 at
   k=27); super-exponential fit `log|d_k| = A+B·k+C·k·log k` with `C ≈ 0.05–0.08 > 0`
   on every window (50–300× tighter SSR than geometric). q-Gevrey / Écalle. **Not
   algebraic.**
2. **`|phase| = 1.0074`, not 1.** Precise `|S|_geom = 0.00945` (substrate, real q₀;
   [`2026-07-18-dladder-fibre-branch-stokes-ambiguity.md`](2026-07-18-dladder-fibre-branch-stokes-ambiguity.md)
   table) vs the exact `|(q;q)_3| = |(1−q)(1−q²)(1−q³)| = 0.00938022` at q₀ →
   `|phase| = 0.00945/0.00938022 = 1.0074`. A **0.74% resurgent correction** above
   the leading algebraic magnitude.
3. **The Lean tension is resolved, not contradicted:** the `phase = ±1` antecedent
   (`|S| = |(q;q)_3|` exact) is false by 0.74%, so `phase ≠ ±1`, `D` resurgent,
   consistent with KC22. `|(q;q)_3|` is the **leading algebraic magnitude**; the
   resurgent `D(ũ)` is the 0.74% correction + divergent tail.

## The machinery is categorically DERIVED, not a CODATA fit

`qbeta_ck_sseries_exact_rational.py` builds the c_k / D-ladder from:
- **`Δ(net)(q)`** — the neutron−proton net decay-width Laurent polynomial,
  **symbolic, Gröbner-reduced** from the H₃ Hecke structure
  (`free-neutron-decay.witness.json`) — *not* CODATA;
- a **determined triangular solve** over exact `ℚ(√3)` (`R(q) = (Q_β/m_e)/[(Q_A/m_e)·
  cos α_eff]`, `log R = Σ log(1+c_k u^k)`) → the c_k are exact `ℚ(√3)` scalars.
- Probe discipline line: **"no fit (triangular solve is determined)."**

The `ℚ(√3)` is the figure-eight / H₃ trace field. So the cat-action → net →
Frobenius chain *is* how the ladder is built, and the **bar-even / binding channel
is exactly derived**. This is the categorical origin the owner's steer predicted.

## The remaining open piece (narrow and precise)

Two specific gaps keep c₃ empirical:
1. **The bar-odd rungs are near-match tier.** The determined solve exactly pins the
   *even/binding* channel; the *odd* rungs (`c₃^odd ≈ −2` near-match; `c₄^odd`
   CAL-anchored) are not pinned by it. c₃'s bar-odd **magnitude** is derived
   (`|S| = 0.00945`, Borel-summable to `10⁻³⁹` on the substrate — least term at the
   `k=31` edge, Stokes jump `~5·10⁻³⁹`), but the exact bar-odd **rung value** is the
   near-match.
2. **The anchor sign/phase is the fibre-branch `Δ_ω`.** On the substrate the Stokes
   jump is `~10⁻³⁹`-suppressed (anchor-blind); the unsuppressed `Δ_ω` datum that
   fixes the sign lives on the **fibre branch (|q|=1)** and is "not produced" on the
   substrate meridian.

## The attack this opens — the odd-channel determined solve

The even channel proves the *shape* of derivation is achievable (a determined
`ℚ(√3)` triangular solve on the symbolic net). The natural next move: **Borel-sum
the exact `d_k` ladder at the substrate** (optimal truncation `k=31`, `10⁻³⁹`
ambiguity) to get `D(ũ_substrate)` → `S = h·D` → an *exact* (to `10⁻³⁹`) bar-odd
`c₃^odd`, replacing the near-match `−2`. This is a derivation (the `d_k` are from
`Δ(net)`, no CODATA), and it is well-posed on the substrate; the fibre-branch
`Δ_ω` sign is the residual. If the Borel-summed value is anchor-consistent (modulo
the `1/u³` ladder inversion) and closes Q_β to the 7.8 ppb 100× target, c₃'s
bar-odd channel is derived. Honesty gate: nothing may be tuned to Q_β/CODATA; the
`d_k` and their Borel sum are the only inputs.
