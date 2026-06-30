---
# mmst
title: 'Data-integrity: ~5e-8 Wenzl-Frobenius vs markov-peel dual-implementation tr_M gap (deuteron 4.8e-8, He-4 1.3e-7)'
status: todo
type: task
created_at: 2026-06-30T16:06:58Z
updated_at: 2026-06-30T16:06:58Z
---


## Finding (surfaced via b0vf / PR #3150, 2026-06-30)

Two production implementations of the **canonical Markov trace** disagree at
the 8th significant figure on atoms where **both** are complete:

| atom | Wenzl Frobenius `Σ_λ y_λ χ_λ` | markov-peel (recursive ascent) | rel gap |
|---|---|---|---|
| deuteron (H₆, 11/11) | 0.38835720735922… | 0.38835718872378… | 4.8e-8 |
| ⁴He (H₁₂, 77/77) | 0.05535843359500… | 0.05535842626678… | 1.3e-7 |

- The χ side is validated to **5e-50** (branch-decomp vs the deuteron
  χ-witness; `Σ y_λ·(witness χ)` == witness `tr_M_at_q0` to 6e-51), so the
  gap is **not** in χ.
- **Not** a δ artifact: branch-decomp at *subleading* δ moves the deuteron
  *further* from markov-peel (1.8e-7), not closer.
- **Distinct** from `2026-05-17-dual-tr-m-discrepancy.md` (that is the 57–99 %
  q-Plancherel `dim_q²/[n]_q!` vs Wenzl `y_λ` *weight-choice* gap). Here both
  sides already use the canonical Wenzl/Markov trace.
- **Distinct** from bean `gnb1` (`tr_M_cross_validation_within_1e-6` failing at
  1.8e-4 — a different, larger check / the iterative-lp-dual producer).

Both witnesses are on `main` (computed 2026-06-29). Likely a normalisation or
finite-precision artifact in one path. Sources: `markov/markov_peel.py`
(`tr_M_atomic`) vs `tr_m_wenzl_bridge_mpfr._load_y_lambda` + Wenzl `y_λ`.
Refs: `docs/audits/2026-06-30-b0vf-he4-chi-completion-dual-path-gate.md`,
`markov/markov-peel-atomic-tr-m.witness.json`.

Priority: low (8th digit, pre-existing, not blocking any L1/L2 leg). Worth
pinning the root cause so the two trace paths agree to machine precision.
