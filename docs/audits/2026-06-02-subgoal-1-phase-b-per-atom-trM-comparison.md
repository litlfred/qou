# Subgoal-1 Phase B — per-atom tr_M comparison vs Family A H₄

**Date:** 2026-06-02
**Branch:** `claude/m-avg-subgoal-1-operator-combiner-2026-06-02` (PR #1698)
**Scope:** Compare the categorically-correct per-atom `tr_M` (via `markov_peel.tr_M_atomic` ground truth) against the production-default Family A H₄ Wedderburn average (= 2.532780 at q₀). Characterize the structural gap as preparation for Phase C closure.

## Phase B run (markov_peel ground truth)

| atom | A | \|tr_M(β_K)\| at q₀ | m via Family A (MeV) | m via per-block (MeV) | CODATA (MeV) | err Family A | err per-block | ratio FA / PB |
|---|---|---|---|---|---|---|---|---|
| proton | 1 | 1.06530614 | 966.05 | 406.33 | 938.272 | +2.96 % | −56.69 % | **2.378** |
| neutron | 1 | 0.92323323 | 966.05 | 352.14 | 939.565 | +2.82 % | −62.52 % | 2.743 |
| D | 2 | 0.38828642 | 966.05 | 148.10 | 1875.61 | −48.5 % | −92.1 % | 6.523 |
| T | 3 | 0.10405211 | 966.05 | 39.69 | 2808.92 | −65.6 % | −98.6 % | 24.34 |
| ³He | 3 | 0.20654082 | 966.05 | 78.78 | 2808.39 | −65.6 % | −97.2 % | 12.26 |
| ⁴He | 4 | 0.05534833 | 966.05 | 21.11 | 3727.38 | −74.1 % | −99.4 % | 45.76 |

**Mass formula used (production):**
```
m(K) = m_e · Geom_leading(q₀) · linking_weight(K, q₀)
Geom_leading(q₀) = Vol(𝓑₃) / ℏ_q² = 8·G / (q₀ − 1)²·q₀² = 746.418
```

- **Family A**: `linking_weight = (3q² + 4 + 3q⁻²)/4 = 2.532780` at q₀ (uniform across atoms — this is the H₄ Wedderburn average, acknowledged CAL-4)
- **Per-block**: `linking_weight = |tr_M(β_K)|` at q₀ (categorically-correct H_{3A} Markov trace)

## Three structural findings

### (i) Production mass-table uses uniform Geom_leading

Per `mass_table_comprehensive.py:9`:
```
m(K) = m_e · [Vol(𝓑₃)/ℏ_q²] · λ_A · (1 ± Δm/(2·M_N))
```

The `Vol(𝓑₃)/ℏ_q²` is the proton's hyperbolic volume — used for ALL atoms. Per-atom variation in production comes from the binding-energy decomposition (Δ_λ etc.), NOT from atom-specific hyperbolic volume. This is the same scalar Family A applied uniformly.

### (ii) Per-block H_3 trace regresses m_p by −56.7 % (confirms canonical reference)

Switching from Family A → per-block tr_M reproduces the −56.7 % m_p regression documented in `linking_weight_canonical_object_lwfix.py` and ruled out as Subgoal-1's mechanism. **Not a viable closure.**

### (iii) The 2.378× gate at the proton anchor

The FA/PB ratio at the proton is **2.378** — the exact "2.38× gate" documented in PR #1623 §4. This ratio quantifies the SCALAR difference between the H₄ Wedderburn average (CAL-4 near-match to CODATA m_p) and the H₃ per-block trace (categorically-correct but off by −56.7 %).

For higher-A atoms the ratio increases sharply (D = 6.52, T = 24.3, ⁴He = 45.8). This indicates that any Subgoal-1 closure mechanism must:
1. Reproduce the ~2.38× factor at A=1 (proton anchor)
2. Scale with A to reproduce atom-specific masses
3. Do this categorically — not by introducing an empirical (Z, N)-dependent multiplier

## What Phase B rules out

- ❌ Replacing `VolDensity(K) = Vol(𝓑₃)/ℏ_q² · Family_A(q)` with `VolDensity(K) = Vol(𝓑₃)/ℏ_q² · |tr_M(β_K)|` for general atoms
  - Reproduces the canonical-reference's −56.7 % m_p regression
  - Fails CODATA for D, T, ³He, ⁴He by 48 % to 99 %
- ❌ Any (Z, N)-dependent scaling of Family A that reproduces atom-specific masses without categorical derivation (forbidden per AGENTS.md §"Δ_λ gate")

## What Phase B confirms

- ✓ Family A's CODATA-close behavior on m_p is structural (a 2.378× scaling of the per-block trace)
- ✓ The Subgoal-1 closure must come from atom-specific Vol(𝓑_{3A})/ℏ_q² (atomic hyperbolic volume), NOT uniform Vol(𝓑₃)/ℏ_q²
- ✓ The operator-valued Wenzl branching combiner (A=2 deuteron verified at 0.72 ppb in Phase A) is the canonical tool to compute χ^λ(β_atom); pairing it with atom-specific Vol is the Subgoal-1 path

## Phase B verdict

The production m_avg formula uses uniform Vol(𝓑₃). For Subgoal-1 m_avg closure at higher A, atom-specific hyperbolic volumes Vol(𝓑_{3A}) are needed. The infrastructure for atom-specific tr_M exists (markov_peel + branching combiner at A=2; markov_peel direct at A≥3). The volume side requires SnapPy / categorical Vol(𝓑_{3A}) — separate from the operator-valued combiner.

**Concrete Phase B follow-up** (out of scope for this session):

1. Locate / compute Vol(𝓑_{3A}) for A=2, 3, 4 hyperbolic atom braids
2. Re-run the per-atom prediction with atom-specific Vol
3. If m_avg lands in the right ballpark (within ~10 %), then operator-valued + atom-specific Vol IS the Subgoal-1 closure; refine for ppb-level accuracy
4. If still off, return to the +2.89 % m_p Family A near-match as the documented CAL-4 status, awaiting a different categorical insight

## Phase C — Lean scaffold

Created [`content/quantum-observable-universe/lean/QOU/BraidKnot/OperatorValuedCombiner.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/OperatorValuedCombiner.lean) per AGENTS.md §3b-cond conditional-class pattern:

- **`class WenzlAOperator (R : Type u) [CommRing R] (q : R) [CrystalGraphRealization R q]`** — the universal A^λ_{ξν}(I) operator-extract claim with `extract_universal` field (the H_9+ universality conjecture)
- **`theorem operator_valued_combiner_convergence`** — Nat.rec on A ≥ 2; base case A=2 verified at 0.72 ppb in Phase A; inductive step deferred to `sorry` carrying the manuscript citation to the audit doc

This is **NOT** instance-populated — `WenzlAOperator` carries the research-grade sorry per AGENTS.md §3b-cond. Production safe.

## Cross-references

- Phase A: [`docs/audits/2026-06-02-subgoal-1-phase-a-baseline.md`](2026-06-02-subgoal-1-phase-a-baseline.md)
- Subgoal-1 scope: [`docs/coordination/2026-06-02-m-avg-subgoal-1-operator-combiner-scope.md`](../coordination/2026-06-02-m-avg-subgoal-1-operator-combiner-scope.md)
- Lean §3b-cond class: [`content/quantum-observable-universe/lean/QOU/BraidKnot/OperatorValuedCombiner.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/OperatorValuedCombiner.lean)
- 2.38× gate: PR #1623 §4 (referenced via [`docs/audits/2026-06-01-linking-weight-residual-fix.md`](2026-06-01-linking-weight-residual-fix.md))
- L2-100× shared root: [`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md)
