# mmst — the ~5e-8 "dual tr_M" gap is a q₀ mismatch in `y-lambda-mpfr-witness.json` (2026-06-30)

**Bean:** `mmst` — *"~5e-8 Wenzl-Frobenius vs markov-peel dual-implementation tr_M gap."*
**Verdict:** ROOT-CAUSED. **Not** a two-implementation discrepancy — a **q₀
mismatch**. The shared default y_λ witness was evaluated at the **retired-proton**
q₀ while every other canonical compute uses the **muon** q₀.

## The finding

`computations/tr_m_wenzl_bridge_mpfr._load_y_lambda` defaults to
`y-lambda-mpfr-witness.json`. That file (generated 2026-05-29) carries

```
q_0_50dps = 1.1099785827513808075916690956107688798744991218736   ← RETIRED-PROTON pin
```

but markov-peel, the χ witnesses, and the rest of the `computations/` layer use

```
muon q₀   = 1.1099785955573347198997632204832250266562084087802   ← canonical
```

These diverge at digit 8 (relative **1.15e-8**). So every Wenzl Frobenius
`tr_M = Σ_λ y_λ χ_λ` computed through `_load_y_lambda` silently mixes
**muon-q₀ χ** with **retired-proton-q₀ y_λ**, producing the ~5e-8 gap against the
(correctly muon-q₀) markov-peel scalar.

## Decisive confirmation (deuteron)

Re-evaluating the symbolic y_λ (`y-lambda-wenzl-bridge-symbolic-witness.json`) at
the **muon** q₀ and re-summing collapses the gap by twelve orders of magnitude:

| y_λ evaluated at | Σ y_λ χ_λ (deuteron) | rel gap vs markov-peel |
|---|---|---|
| retired-proton q₀ (committed) | 0.38835720735922143664… | **4.8e-8** |
| **muon q₀ (corrected)** | 0.38835718872378100727… | **9.1e-20** |
| markov-peel (muon q₀) | 0.38835718872378100730… | — |

The two trace *implementations* (Wenzl Frobenius pairing vs markov-peel recursive
ascent) agree to **1e-19** once both use the same q₀. There is no algorithmic
discrepancy; `2026-05-17-dual-tr-m-discrepancy.md` (the 57–99 % q-Plancherel vs
Wenzl *weight-choice* gap) is unrelated.

Ruled out along the way: the atomic word (identical d-coefficients), the colour δ
(`flavor_split_leading` numeric vs markov-peel's symbolic mirror agree to 0.0), and
y_λ floating-point precision (f64 truncation is ~1e-14, six orders too small).

## Scope / impact

- Every `Σ y_λ χ_λ` tr_M via `_load_y_lambda` is ~1e-8–1e-7 off (mixed q₀). This is
  **below every tolerance in the framework** (the 1e-6 cross-validation check, the
  CAL-2 ~780 ppb floor, all L2 targets), so no assertion currently fails on it —
  which is why it survived as an accepted "dual-path" gap (bean `gnb1` recorded the
  same 4.8e-8 as within-tolerance).
- The He-4 χ witness completed in PR #3150 stores `tr_M_at_q0 = Σ y_λ χ_λ` with these
  retired-proton y_λ; its documented `tr_M_dual_path_rel_gap = 1.32e-7` **is exactly
  this q₀ mismatch**, not an intrinsic two-implementation gap. (The per-λ χ table
  itself is unaffected — it is pure muon-q₀ character data.)

## Fix APPLIED (2026-06-30, PR #3174)

`y-lambda-mpfr-witness.json` regenerated at the **muon** q₀ via
`regenerate_y_lambda_mpfr.py` (`q_parameter.Q_MP` is muon). Verified: the deuteron
**and** He-4 Wenzl `Σ y_λ χ_λ` now collapse onto markov-peel to **9.1e-20** (from
4.8e-8 / 1.3e-7). The He-4 χ witness (PR #3150) was re-run — its `tr_M_at_q0` now
equals the canonical markov-peel scalar and its dual-path annotation drops to
9.1e-20. This aligns the one stray retired-proton witness **to** the canonical muon
layer (it does not migrate the muon layer — not the AGENTS.md §"q₀ anchor convention"
gated direction).

**No regressions:** `cross_check_trM_1ppb.py --strict`, `compute_audit_scan.py`,
`derivation_chain_validator.py`, and `y_lambda_symbolic_validate.py` all exit 0 with
the corrected witness (0 divergent atoms; 5/6 still certified 1 ppQ).

### Bounded downstream follow-up (within tolerance, non-breaking)

~34 scripts consume `_load_y_lambda`; several committed witnesses store a
`Σ y_λ χ_λ` tr_M computed with the old proton-q₀ y_λ and are now ~5e-8 stale against
the corrected source. This is **below every framework tolerance** (1e-6
cross-validation, ~780 ppb CAL-2 floor) and **no validator flags it** (witness
staleness keys on `scriptHash`, not on upstream numeric drift), so it is not
urgent and is intentionally **not** swept here — a blind 34-producer re-run (several
slow / pyhecke-gated) would add churn without changing any verdict. The witnesses
refresh naturally on their next producer run; tracked under `mmst`.
