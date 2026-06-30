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

## ROOT-CAUSED 2026-06-30 — it's a q₀ mismatch, NOT a two-implementation gap

`y-lambda-mpfr-witness.json` (the `_load_y_lambda` default) was evaluated at the
**retired-proton** q₀ `1.1099785827513808…` (…827513808), while markov-peel + the
χ witnesses use the canonical **muon** q₀ `1.1099785955573347…` — diverging at digit
8 (rel 1.15e-8). Every `Σ y_λ χ_λ` mixes muon-q₀ χ with retired-proton-q₀ y_λ.

**Confirmation:** re-evaluating the symbolic y_λ at the muon q₀ collapses the
deuteron gap from 4.8e-8 → **9.1e-20** vs markov-peel. The two trace implementations
agree to 1e-19 at a consistent q₀.

**Fix (owner-gated coordinated sweep):** regenerate `y-lambda-mpfr-witness.json` at
the muon q₀ (`regenerate_y_lambda_mpfr.py`; `q_parameter.Q` is already muon), then
re-run downstream producers that store a `Σ y_λ χ_λ` tr_M (incl. the PR #3150 He-4
witness, whose `tr_M_dual_path_rel_gap = 1.32e-7` IS this mismatch). Below all
tolerances, so non-urgent. Full audit:
`docs/audits/2026-06-30-mmst-ylambda-retired-proton-q0-root-cause.md`.
