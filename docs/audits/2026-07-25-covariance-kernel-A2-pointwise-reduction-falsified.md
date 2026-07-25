# Covariance-kernel epic (`qou-x631`) — CORRECTION: the A2 pointwise reduction is FALSE for n ≥ 29

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-a2-pointwise-correction-2026-07-25` ·
**Tier:** honest retraction of a small-`n` over-generalization (scope-(a) route-death with an exact
counterexample) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged (2/7).
**Epic:** `qou-x631`, attack `qou-ogrk` (A2).

## What was over-claimed

Two same-day audits reduced the A2 leg `Cov_Planch(ln f^λ, ω₃) ≤ 0` to a **pointwise** sign:

- `2026-07-25-covariance-kernel-A2-hook-reduction.md` — "A2 ⟸ `Cov_Planch(H_s, ω₃) ≤ 0 ∀s>0`",
  reported "verified strictly < 0 on the interior, all `n ≤ 13`".
- `2026-07-25-covariance-kernel-A2-polynomial-positivity.md` (PR #4242) — the same target as the
  polynomial positivity "`R(x) ≥ 0` on `(0,1)`" where `P(x)=Σ_v ν_v x^v = x(x−1)R(x)`, reported
  "`R > 0` on `[0,∞)` verified `n ≤ 15`", and (in the probe/PR NET line) framed it as an equivalence
  "A2 ⟺ `R ≥ 0` on `(0,1)`".

## The correction (exact)

Pushing the **exact** computation past the verified window falsifies the pointwise target:

| n | `max_{s>0} Cov_Planch(H_s, ω₃)` | pointwise target `≤ 0`? |
|---|---|---|
| 13 | `−5.1e−4` | ✓ |
| 26 | `−1.8e−3` | ✓ |
| 28 | `−2.0e−3` | ✓ |
| **29** | **`+0.056`** (at `s≈0.52`) | **✗ FIRST FAILURE** |
| 30 | `+0.150` | ✗ (`R` gains a root in `(0,1)`) |
| 35 | `+0.944` | ✗ (grows with `n`) |

So the pointwise sign is a **small-`n` artifact**, not a theorem. `R ≥ 0` on `(0,1)` is **false** for
`n ≥ 29`, and the "A2 ⟺ `R≥0`" equivalence was wrong (it is only the one-way implication `R≥0 ⟹ A2`,
now with a false premise). The polynomial-positivity target **cannot** prove A2.

## What survives (verified exactly, `k, n ≤ 40` — the important part)

- **The kernel conjecture itself:** `cov(k) = Σ_λ (f^λ)³ ω₃(λ) ≤ 0` — strongly negative, intact.
- **The A2 leg itself:** `Cov_Planch(ln f^λ, ω₃) = −Σ_v ln(v) ν_v ≤ 0` — negative, intact.

A2 survives by **cancellation**: the Frullani identity
`Cov(ln f, ω₃) = ∫_0^∞ (1/s) Cov(H_s, ω₃) ds` still holds and stays `≤ 0`, even though its integrand
`Cov(H_s, ω₃)` is now *positive* on part of the `s`-range (`n ≥ 29`). Hence
"A2 ⟸ `Cov(H_s,ω₃)≤0 ∀s`" is a valid implication with a **false premise** — sufficient but not
satisfied. Proving A2 requires the **full signed integral** (a global cancellation argument), not a
pointwise sign.

## Consequence for the plan

The A2 **polynomial-positivity / pointwise-`Cov(H_s)` route is eliminated** — and, unusually, with an
*exact counterexample* (`n ≥ 29`) rather than a mere "no certificate found". This is a scope-(a)
route-death: it constrains the *method* (no pointwise/`R`-positivity certificate exists), not the
kernel, which stands. The live routes are unchanged: the finite-`n` proof must be global (the full
Frullani integral or the dimension-functional / DPP expansion), and the DPP route still needs
depoissonization. The three "easy-proof" sub-certificate eliminations from #4242 (ν single-crossing,
cumulative `S_v≤0`, `R` nonneg-coefficients) remain correct and are now seen as early symptoms that no
pointwise certificate exists.

## Compute

- Probe: [`computations/deltalambda/wlambda_covariance_epic_A2_pointwise_reduction_falsified.py`](../../computations/deltalambda/wlambda_covariance_epic_A2_pointwise_reduction_falsified.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-covariance-epic-A2-pointwise-reduction-falsified.witness.json`

## Cross-references

- Retracts (in part): [`2026-07-25-covariance-kernel-A2-polynomial-positivity.md`](2026-07-25-covariance-kernel-A2-polynomial-positivity.md), [`2026-07-25-covariance-kernel-A2-hook-reduction.md`](2026-07-25-covariance-kernel-A2-hook-reduction.md)
- Epic map (updated): [`2026-07-25-covariance-kernel-epic-synthesis.md`](2026-07-25-covariance-kernel-epic-synthesis.md)
- Attack plan: bean `qou-v8t7`; A2 `qou-ogrk`.
