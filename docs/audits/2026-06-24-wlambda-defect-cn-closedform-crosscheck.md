# The `W_λ` defect cubic is EXACT, not empirical — closed form `C(n) = −n(n−1)(2n−13)/144` cross-checked against the actual `1−Z(n)`

**Date:** 2026-06-24
**Branch:** `claude/keystone-defect-cn-closedform-crosscheck-2026-06-24`
**Probe:** [`computations/keystone_wlambda_defect_cn_closedform_crosscheck.py`](../../computations/keystone_wlambda_defect_cn_closedform_crosscheck.py)
**Witness:** [`computations/keystone-wlambda-defect-cn-closedform-crosscheck.witness.json`](../../computations/keystone-wlambda-defect-cn-closedform-crosscheck.witness.json)

## The loop that was open

Three corpus artifacts described the `W_λ` partition-function defect `1 − Z(n)`
(`Z(n) = Σ_{λ⊢n} d_q(λ)²/[n]_q!`, balanced `[m]_q`, the q-Plancherel total mass) but
**never closed the loop between them**:

| Artifact | What it does | Gap |
|---|---|---|
| [`docs/audits/scripts/keystone_wlambda_Z_defect_n_scaling.py`](scripts/keystone_wlambda_Z_defect_n_scaling.py) | Computes `1−Z(n)` and extracts its small-h coefficient `C(n)` **EMPIRICALLY** | Explicitly: *"C(n) is reported EMPIRICALLY — no closed form is claimed"* (line 24). A **hook-moment ansatz** `C(n)=(1/n!)Σ dim·hook²` was **tested and REFUTED** (lines 177–178). |
| [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean) | Proves `144·C(n) = −n(n−1)(2n−13)` ALGEBRAICALLY (from Identity I), sign-flip `n144C_pos` (2≤n≤6) / `n144C_neg` (7≤n) | Never cross-checked against the *actual* `Σ_λ d_q²/[n]_q!` defect — only derived symbolically from Identity I. |

So: one script said "no closed form" (having refuted a *different*, hook-moment guess), and a
Lean file proved a closed form from Identity I — but **nobody verified the Lean cubic against the
directly-computed defect.** A reader could not tell whether `−n(n−1)(2n−13)/144` was the real
small-h coefficient of `1−Z(n)` or an algebraic artifact of the Identity-I bookkeeping.

## What the cross-check does

For `n = 2..10` (spanning the n=7 sign flip), compute `Z(n,q) = Σ_{λ⊢n} d_q(λ)²/[n]_q!` directly
at 60 dps via q-hooks, set `h = q − 1/q`, and Richardson-extrapolate
`C_emp(n) = lim_{h→0}(1−Z(n))/h²` (two halvings, killing the `O(h²)` and `O(h⁴)` tails). Compare
to `C_cf(n) = −n(n−1)(2n−13)/144`.

## Result — EXACT to <2e-14, sign flip identical

| n | `C_empirical` | `C_closed_form` | rel err | sign |
|---:|---:|---:|---:|:--:|
| 2 | 0.125 | 0.125 | 2.4e-15 | + |
| 3 | 0.2916666… | 0.2916666… | 7.3e-15 | + |
| 4 | 0.4166666… | 0.4166666… | 1.6e-14 | + |
| 5 | 0.4166666… | 0.4166666… | 2.5e-14 | + |
| 6 | 0.2083333… | 0.2083333… | 3.7e-14 | + |
| **7** | **−0.2916666…** | **−0.2916666…** | 1.9e-15 | **−** |
| 8 | −1.1666666… | −1.1666666… | 2.5e-15 | − |
| 9 | −2.5 | −2.5 | 1.2e-14 | − |
| 10 | −4.375 | −4.375 | 8.3e-15 | − |

**Empirical sign flip at n=7 = closed-form sign flip at n=7.** All nine match below 1e-10
(actually below 4e-14). The closed form `C(n) = −n(n−1)(2n−13)/144` **IS** the exact small-h leading
coefficient of the real `W_λ` defect — not an empirical fit, and not the refuted hook-moment ansatz.

## Why the empirical script's "no closed form" was not wrong

The empirical script refuted **`C(n)=(1/n!)Σ dim·hook²`** — a hook-*moment* guess. That guess does
fail. The Identity-I cubic is a structurally different object (it comes from
`M(n)=n(3n−1)/2 = binom(n,2)+n²`, the per-partition content/hook decomposition Identity (A)
proved sorry-free in #2655, propagated to the Plancherel mean). The two are not in tension: one
ansatz is wrong, the *derived* cubic is right. This cross-check is the first artifact to state
that distinction with the numbers attached.

## Why this matters for the keystone

The full-Hecke geometric `W_λ` index program
([`docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`](../scope/2026-06-24-keystone-fullhecke-geometric-index-program.md))
lists **target (1)** as: *the index's 2nd heat-kernel coefficient must equal `144·C(n)` including the
n=7 sign flip.* Before this probe, target (1) rested on a Lean derivation whose contact with the
*actual* `W_λ` weights was unverified. Now the target is **pinned exactly** against the direct
computation: a geometric index that reproduces `W_λ` must produce the cubic
`−n(n−1)(2n−13)` and flip sign at n=7, and this is a **q₀-free** statement (it is the small-`h`
*leading* coefficient — the whole `h→0` limit, independent of the substrate anchor). It is the
sharpest single falsifiable gate the geometric construction (phase **G2**) has to clear.

## Discipline

- **No fit.** Every number is computed (q-hooks + mpmath, 60 dps); `q₀` never appears; the defect
  is read off by Richardson extrapolation, not tuned.
- **(a)/(b) framing.** This is a **positive** confirmation (the cubic matches), so the
  refuted/ruled-out scoping does not apply. The one *negative* in the neighbourhood — the
  hook-moment ansatz — was already correctly scoped by the empirical script (a specific ansatz
  fails; "no [hook-moment] closed form"), and this probe does **not** disturb it.
- **Formalize-first complement.** The cubic was Lean-proved first (`WLambdaDefectClosedForm`); this
  probe is the empirical confirmation that the proved object is the physical one — the forward
  direction of the formalize-first discipline (prove the invariant, *then* confirm it governs the
  compute).

## Cross-references

- [`computations/keystone_wlambda_defect_cn_closedform_crosscheck.py`](../../computations/keystone_wlambda_defect_cn_closedform_crosscheck.py) — this probe.
- [`docs/audits/scripts/keystone_wlambda_Z_defect_n_scaling.py`](scripts/keystone_wlambda_Z_defect_n_scaling.py) — the empirical defect script (the "no closed form" disclaimer this closes).
- [`WLambdaDefectClosedForm.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaDefectClosedForm.lean) — the Lean closed form (`n144C`, `n144C_pos`, `n144C_neg`).
- [`docs/scope/2026-06-24-keystone-fullhecke-geometric-index-program.md`](../scope/2026-06-24-keystone-fullhecke-geometric-index-program.md) — target (1) is this cubic; phase G2 gates against it.
- [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) — keystone ledger.
- #2655 — Identity (A) `Σ h² = Σ c² + n²` proved sorry-free (the cubic's algebraic origin).
