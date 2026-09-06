# The κ_n derived symbolically (κ₁–κ₁₂ exact); Borel A honest correction; Φ_b real construction

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Date:** 2026-07-12 · **Axis:** z→c_k f-map keystone · **Tier:** symbolic-exact
(derivation) + extrapolated-A (2 digits, honest negative) + proved-lean (Φ_b laws) ·
**Discipline:** no fit, no Q_β c_k wired, no Q_β tier change. PR #3689; builds on
merged #3606/#3628.

## 1. Track 2 — the even-channel rungs are DERIVED, not identified

[`qbeta_ohtsuki_symbolic_saddle.py`](scripts/qbeta_ohtsuki_symbolic_saddle.py)
computes the 4₁ Ohtsuki rungs from first principles, in exact ℚ(√3,π) sympy
arithmetic with **no numerical input and no PSLQ**:

1. **Euler–Maclaurin** on the inner Kashaev partial sum (all singular endpoint
   data is k-independent and lands in the stripped `(3/2)logN + N·Vol/2π + A₀`,
   never in the κ_n);
2. **Poisson summation** on the outer sum (non-integral modes exponentially
   suppressed);
3. **Laplace expansion** at the interior maximum `x* = 5/6` (`G''(x*) = −√3π`),
   Gaussian moments in exact arithmetic.

**Kill criteria pass**: κ₁–κ₄ reproduce the independently PSLQ-identified values
(#3606/#3628) to **symbolic zero**, and κ₅/κ₆ match the numerical extractions to
their attained digits (13d/9d). Consequently κ₁–κ₄ upgrade
`numerical-exact → symbolic-exact` (even-channel internal; **no Q_β rung tier
changes**), and the derivation emits new exact rungs beyond any extraction reach:

| rung | exact value |
|---|---|
| κ₅ | (110011/688905)·√3π⁵ |
| κ₆ | (207892/295245)·π⁶ |
| κ₇ | (32729683/26572050)·√3π⁷ |
| κ₈ | (139418294/18600435)·π⁸ |
| κ₉–κ₁₂ | in the Borel witness (e.g. κ₁₂ = (8151561592180588/2237353323975)·π¹²) |

The √3-parity alternation and 3-power denominators are **consequences of the
derivation** (`cot(5π/6) = −√3` Taylor data + rational Bernoulli/moment
arithmetic) — they were never assumptions.

## 2. Track 1 — exact-rung Borel analysis: honest correction

[`qbeta_ohtsuki_borel_exact.py`](scripts/qbeta_ohtsuki_borel_exact.py) runs
Richardson on the exact Δr_n (r_n = κ_{n+1}/κ_n) from κ₁–κ₁₂:

- **A ≈ 0.758 with only ~2 stable digits** — the Richardson diagonal is still
  drifting (subleading Borel structure is not a pure 1/n correction).
- **`A = Vol(4₁)/π` is REFUTED as an exact identification** (17% deviation on
  exact input). #3628's "A ≈ Vol/π to 4.4% (suggestive)" was low-order-fit bias
  and is **superseded** (scope-(a): these candidates, this extrapolation).
- Clean structural byproduct: **β = 1.9983 ≈ 2**, i.e. `κ_n ~ C·Γ(n+2)/A^n`.
- The exact resurgence action awaits the **state-integral (Garoufalidis–Gu–
  Mariño-style) singularity identification**, not more Richardson — that is the
  designated next tranche.

## 3. Track 3 — Φ_b real-integral construction (delivered to #3544)

[`QOU/MathlibExt/FaddeevPhiBRealIntegral.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/FaddeevPhiBRealIntegral.lean)
(sorry-free, lean-direct EXIT 0, wired into `QOU.lean`): `phiB` as a **genuine
`noncomputable def`** — Bochner integral `J(b,z)` plus the phase
`−J/2 + πz²/2 + π(b²+b⁻²)/24` pinned to 8e-29 in #3544's P1–P4 battery — with
sorry-free `phiB_self_dual` (modular double, from the manifest kernel `b↔b⁻¹`
symmetry, total identities), `norm_phiB` (unitarity), `phiB_inversion` (via
`J_odd`), `phiB_zero`. Unlike the T3 scaffold (`FaddeevQuantumDilogarithm`,
axiom-class), nothing is axiomatized. Honest scope: kernel integrability and the
identification with the contour Φ_b remain analytic content (the numerical pin).
Delivered for cherry-pick (`f5dee6c210`); #3544's probe/audit items untouched.

## Honest scope (anti-laundering)

Tracks 1–2 are 4₁-Kashaev/Ohtsuki topology; track 3 is analytic infrastructure.
**No Q_β c_k value is produced or wired; no Q_β tier changes.** The 4₁↔Q_β bridge
remains open (Borel/Φ_b continuation, #3628 scope-(b)) — track 3 is precisely
the foundation of the object that owns it.

## Cross-references

- Exact rungs + bridge obstruction (merged): [`2026-07-12-ohtsuki-higher-rungs-exact.md`](2026-07-12-ohtsuki-higher-rungs-exact.md), [`2026-07-12-fmap-4one-qbeta-bridge-growth-obstruction.md`](2026-07-12-fmap-4one-qbeta-bridge-growth-obstruction.md)
- Φ_b program: PR #3544 (real-form pin); [`FaddeevQuantumDilogarithm.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/FaddeevQuantumDilogarithm.lean) (T3 scaffold)
- Witnesses: `qbeta-ohtsuki-symbolic-saddle.witness.json`, `qbeta-ohtsuki-borel-exact.witness.json`
