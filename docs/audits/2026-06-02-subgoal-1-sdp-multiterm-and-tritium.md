# Subgoal-1 — full R5 SDP, multi-term refutation, tritium PSD (options 1+3+2)

**Date:** 2026-06-02
**Branch:** `claude/m-avg-subgoal-1-operator-combiner-2026-06-02` (PR #1698)
**Trigger:** Owner directive "1 3 2 4" — build native engines, run full SDP, test multi-term, do tritium, then prepare-merge.

This session built the native compute layers and ran the canonical-knot SDP to completion across all three light nuclei.

## Builds completed this session

| component | how | status |
|---|---|---|
| `pyhecke_native` (PyO3 wrapper of hecke-engine) | `maturin build --release` + pip install wheel | ✅ installed |
| `hecke-engine` (Rust, H_5 Hoefsmit seminormal) | `cargo build --release` | ✅ built |
| `cvxpy` (SDP solver) | pip install | ✅ installed (prior commit) |
| `snappy` (hyperbolic volume) | pip install | ✅ installed (prior commit) |

## Option 1 — full R5 canonical-knot SDP (with native engine)

`r5_full_canonical_knot_solver.py` now runs end-to-end (needs `pyhecke_native`). Over 13088 B_3 braid words → 2556 KLR-canonical-basis classes:

| atom | historical knot | α_gap | \|tr_M\| | rank (full / PSD-feasible / top-8) | winner recovers historical? |
|---|---|---|---|---|---|
| ²H | 6_2 | 0.890510 (NOT PSD) | 0.288326 | 1075 / — / — | NO |
| ³He | L6a4 | 0.000000 (PSD ✓) | 0.998367 | 383 / 383 / — | NO |

Strong duality holds for all per-atom LPs. The single-term cost winner is a "PSD-trivial near-pure-power braid" whose \|tr_M\| coincidentally matches `B_AME/(m_e·ρ)`. The solver's own verdict: historical recovery "requires wiring the multi-term tower (T2-T6)".

## Option 3 — multi-term cost: STRUCTURALLY REFUTED for the deuteron

The audit hypothesis ("wire T2-T6 into the cost → 6_2 becomes the winner") is **structurally impossible** under the R5 cost design. Proof (`multiterm_cost_deuteron_psd_gate_probe.py`):

```
cost = w_alpha · α_gap + w_resid · rel_resid     (w_alpha=1.0, w_resid=0.25)
```

- The multi-term mass formula (T2 brane-tower + T4 Frobenius co-Casimir) enters only `B_pred`, hence only `rel_resid` (SECONDARY).
- It cannot change `α_gap` — the PRIMARY PSD-feasibility gate, intrinsic to the candidate braid's Hoefsmit Wedderburn-block eigenvalues.
- 6_2 has `α_gap = 0.890510`. So even with **perfect** binding residual (`rel_resid = 0`):
  ```
  cost(6_2) ≥ 1.0 · 0.890510 = 0.890510
  cost(winner, α_gap=0) ≤ 0.25
  ```
- **6_2 can never be the joint-cost winner while α_gap=0.89, for ANY binding formula.**

What multi-term *does* change: the effective \|tr_M\| target shifts from `B_AME/(m_e·ρ)` to `(B_AME − m_e·Σ)/(m_e·ρ)`. For the deuteron the ρ=4 multi-term target (0.28781) coincidentally ≈ 6_2's \|tr_M\| (0.288326) — but ρ=4 is the wrong multiplicity (deuteron is ρ=1) and 6_2 is PSD-infeasible regardless. A coincidence, not a closure.

**The deuteron SDP blocker is 6_2's intrinsic PSD-infeasibility, not the cost.**

### Formula-ambiguity finding

The repo carries **at least three** competing deuteron binding formulas:
- `B = E_0 · |Δtr_M|` with E_0 = 4.186 MeV (`binding_canonical.py`)
- `B = E_0 · |Δtr_M|` with E_0 = 0.782 MeV (`deuteron-first-principles.md` → 0.9953 MeV, −55%)
- six-term figure-eight-BW + chirality (`thm:six-term-mass-formula-complete` → 0.5-0.9%)

The "wire T2-T6" instruction does not specify which; the Frobenius co-Casimir term (the one unambiguously validated this session, `subgoal-1-frobenius-co-casimir-validation.witness.json`) is a per-atom CONSTANT and so only rescales targets — it does not, and cannot, change PSD-feasibility. Wiring a specific multi-term formula into production would require owner selection among the three; deferred.

## Option 2 — tritium ³H = 8_11 PSD-feasibility (via Rust H_5)

The check "DEFERRED to Rust" in `joint_tower_sdp_solver_v2.py` is now computable — `dump-block-matrices` (hecke-engine, built this session) emits the H_5 Wedderburn PSD report for the B_5 8_11 braid:

| λ | d_λ | min eig (sym) | PSD? |
|---|---|---|---|
| [5] | 1 | +0.658782 | ✓ |
| [4,1] | 4 | −1.032134 | ✗ |
| [3,2] | 5 | −0.832220 | ✗ |
| [3,1,1] | 6 | −1.185992 | ✗ |
| [2,2,1] | 5 | −1.359547 | ✗ |
| [2,1,1,1] | 4 | −1.324388 | ✗ |
| [1,1,1,1,1] | 1 | +1.517953 | ✓ |

**Tritium 8_11 is NOT PSD-feasible** — 5 of 7 blocks fail.

## Unified verdict across the three light nuclei

| atom | knot | H_n | PSD-feasible @ q_0? | blocks failing |
|---|---|---|---|---|
| ²H | 6_2 | H_3 | **NO** | standard (2,1): eig −0.89 |
| ³H | 8_11 | H_5 | **NO** | 5 of 7 |
| ³He | L6a4 | H_3 | **YES** ✓ | none |

**Only ³He's historical knot is PSD-canonical at q_0.** The ²H/³H assignments are reverse-engineered AME volume-matches (atlas tags `manual-historical-volume-match`) that fail the single-block Wedderburn PSD-feasibility certificate. This is consistent with — and now rigorously confirms — the atlas's own acknowledgment that those assignments are not principled derivations.

## What closes conj:canonical-knot-id-sdp

- **³He**: PSD-feasible; uniqueness conditional on the strict-complementarity hypothesis (Lean §3b-cond `helium3_canonical_uniqueness_via_strict_complementarity`, carries one `sorry`). **Effectively closed** modulo that categorical hypothesis.
- **²H, ³H**: the historical knots are PSD-infeasible. Closure requires EITHER
  (a) identifying the correct canonical objects — the structural decomposition (`conj-canonical-knot-id-sdp.md §"Structural decomposition"`) factors `T_w = K(binding) ⊗ ⊗ T_w(nucleon)`, with the deuteron binding `K = L_H` (Hopf), tritium `K = 8_11-class link` — i.e. the canonical object is the BINDING link, not the whole-atom knot; OR
  (b) revisiting the PSD certificate to use the joint multi-block constraint of `prop:joint-tower-sdp-confinement` rather than per-block checks.

Multi-term cost wiring (the audit's prior next-step) is **NOT** the closure path — refuted above.

## Deliverables (PR #1698)

| file | role |
|---|---|
| `r5-full-canonical-knot-solver.witness.json` | full SDP run (regenerated with native engine) |
| `multiterm_cost_deuteron_psd_gate_probe.py` + witness | option-3 refutation |
| `tritium_h5_psd_feasibility_witness.py` + witness | option-2 tritium PSD |
| `subgoal-1-frobenius-co-casimir-validation.*` | T4 term validation (prior commit) |
| this audit | unified verdict |

## Cross-references

- Prior SDP run: [`docs/audits/2026-06-02-subgoal-1-sdp-canonical-knot-run.md`](2026-06-02-subgoal-1-sdp-canonical-knot-run.md)
- Conjecture: [`content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md`](../../content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md)
- Unified mass formula: [`content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.md`](../../content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.md)
- Final verdict (the +2.89% is a proton problem): [`docs/audits/2026-06-02-subgoal-1-final-verdict.md`](2026-06-02-subgoal-1-final-verdict.md)
