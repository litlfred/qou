# Δ_λ covariance kernel — A3 leg-2 transfer-bound extension probe (n → 40)

**Date:** 2026-08-08
**Epic:** `qou-x631` (prove the Δ_λ covariance kernel `Cov_Planch(f^λ, Σc²) ≤ 0`)
**Leg probed:** `qou-4wl1` (A3 = leg 2 of attack plan `qou-v8t7`): the remainder-domination bound
`|R| = |g(1) − g'(0)| < |g'(0)|`.
**Scope:** scope-(a) numerical probe — confirms a *magnitude/robustness* claim; **not** a proof.
No fit; no `c_k`; nothing wired to production; L2 unchanged (2/7).

## Which leg, and why this one

The epic reduces the kernel sign `cov(k) = Σ_{λ⊢k} (f^λ)³ (Σ_□c² − C(k,2)) ≤ 0` to **two
sufficient legs** (attack plan `qou-v8t7`), stated via the dimension-tilted mean
`g(θ) := E_{β=2+θ}[ω₃] = Σ_λ f^{2+θ} ω₃ / Σ_λ f^{2+θ}`, with `ω₃ = Σ_□ c(□)² − C(n,2)`:

- **A2 (leg 1, `qou-ogrk`):** `g'(0) = Cov_Planch(ln f, ω₃) ≤ 0` (the linear / Gaussian main term).
- **A3 (leg 2, `qou-4wl1`):** `|R| = |g(1) − g'(0)| < |g'(0)|`, i.e. the transfer ratio
  `r := g(1)/g'(0) ∈ (0, 2)` (the non-Gaussian Taylor remainder cannot flip the sign).

Since `g(0) = E_2[ω₃] = 0` and `g(1) = E_3[ω₃] = cov(n)/Σ_λ f³` (the kernel up to a positive
factor), `A2 ∧ A3 ⇒ kernel ≤ 0`.

**Why re-run a "verified" bound at larger n.** The A3 bound was verified only to **n ≤ 14**
(Phase-7 script `wlambda_covariance_epic_phase7_transfer_bound.py`, bean `qou-jy04`). The
*sibling* A2 **pointwise** reduction (`Cov(H_s, ω₃) ≤ 0 ∀s ⇔ R(x) ≥ 0 on (0,1)`) was likewise
verified only to n ≤ 13/15 — and was then **falsified exactly at n = 29** as a small-n artifact
(bean `qou-ogrk`, audit `2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md`).
That precedent makes the A3 window (n ≤ 14) a genuine small-n-artifact risk: if `r` drifts toward
0 or 2 as n grows, the whole A2×A3 *decomposition* — not just the pointwise shortcut — collapses.
So extending A3 past n = 29 is a decisive confirm/falsify, and it is cheap: `g(1)` and `g'(0)`
have **exact closed forms** requiring only ordinary partitions and hook-length dimensions (no Jack
machinery).

## What was probed

Script: [`computations/deltalambda/wlambda_covariance_epic_A3_transfer_bound_extension.py`](../../computations/deltalambda/wlambda_covariance_epic_A3_transfer_bound_extension.py)
(50 dps mpmath; exact `Fraction`/`int` for the integer sums). For every n, 3 ≤ n ≤ 40:

- **g(1)** exact = `(Σ_λ f³ ω₃) / (Σ_λ f³)` — both sums are exact Python integers.
- **g'(0)** = `Cov_Planch(ln f, ω₃) = (1/n!) Σ_λ f² (ln f) ω₃` — the second Plancherel term
  `E_2[ln f]·E_2[ω₃]` vanishes because `E_2[ω₃] = 0` exactly. This is sharper than the original
  Phase-7 finite differences (`h = 1e-6`).

Three decisive checks per n: **(K)** kernel `Σ_λ f³ ω₃ ≤ 0`; **(M)** main `g'(0) < 0`;
**(R)** `r = g(1)/g'(0) ∈ (0,2)` ⇔ `|R|/|g'(0)| = |r−1| < 1`.

**Reproduction check:** for n ≤ 14 the probe reproduces the Phase-7 window exactly —
`r ∈ (0.5410, 0.8743)`, matching the beans-recorded `r ∈ (0.54, 0.87)`.

## Numerical result

| range | kernel ≤ 0 | g'(0) < 0 | r = g(1)/g'(0) | max \|r−1\| |
|---|---|---|---|---|
| 3 ≤ n ≤ 40 | **True (all)** | **True (all)** | **[0.5410, 0.8743]** | **0.459** |

The transfer ratio `r` oscillates in a **tight band [0.54, 0.87]** with **no drift toward the
(0,2) boundary**; near the top of the range (n = 40) it is `≈ 0.70`, comfortably interior. The
non-Gaussian Taylor remainder is at most `≈ 46 %` of the linear term throughout — never enough to
flip the sign. Full run (7.3 s): witness
[`computations/deltalambda/wlambda-covariance-epic-A3-transfer-bound-extension.witness.json`](../../computations/deltalambda/wlambda-covariance-epic-A3-transfer-bound-extension.witness.json).

**Contrast with the falsified sibling.** The A2 *pointwise* route developed a positive
integrand at n = 29 and the property grew with n; the A3 *ratio* shows no such degradation
through n = 40. So the A3 leg (and hence the A2×A3 decomposition) is **not** the same kind of
small-n artifact.

## Honest verdict

- **The leg ADVANCES (robustness confirmed, not proved).** The A3 remainder-domination bound
  `|R| < |g'(0)|` holds with uniform margin to n = 40 — a `>2.8×` extension of its prior n ≤ 14
  window, past the n = 29 point where the analogous pointwise route died. This retires the
  small-n-artifact risk for the A3 leg over the tested range and independently re-confirms
  **both** the epic's headline `cov(k) ≤ 0` (k ≤ 40) and A2's leg-1 sign `Cov(ln f, ω₃) < 0`
  from a single self-contained computation.
- **It is NOT a proof, and does not close A3.** The bound remains *verified, not derived*.
  A rigorous A3 still requires Plancherel-cumulant control of the mixed cumulants
  `g^{(m)}(0) = κ_{m+1}(ln f; …; ln f; ω₃)` (Kerov CLT / Ivanov–Olshanski second-order asymptotics
  / Śniady genus grading, per the resource set in `qou-v8t7`). The complete-monotonicity /
  Bernstein shortcut for that control was already **eliminated** (bean `qou-4wl1`,
  audit `2026-07-25-covariance-kernel-complete-monotonicity-target.md`): `−g'` is not completely
  monotone (Hankel matrices of `m_k = (k+1)!|a_{k+1}|` are not PSD). So the honest status of A3 is:
  the target **magnitude holds robustly**, but the **rigorous argument is still an open wall** —
  the genus-graded (effective, not exact) cumulant bound is the surviving route.

**Per AGENTS.md (a)/(b) scoping:** this is a *positive* magnitude confirmation, not a refutation,
so no "(b) structural exclusion" language is used. Nothing here is over-claimed as proved.

**LP/SDP dual note:** no LP or SDP solve is involved in this probe (it is a direct exact/
high-precision evaluation over partitions), so the AGENTS.md LP/SDP dual-emission rule does not
apply.

## Reproduce

```bash
python3 -u computations/deltalambda/wlambda_covariance_epic_A3_transfer_bound_extension.py 40 \
  2>&1 | tee /tmp/dl.log
```
