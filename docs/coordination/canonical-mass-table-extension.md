# Coordination ledger — canonical-mass-table-extension

**Branch:** `claude/canonical-mass-table-extension` (no PR yet; local-only)
**Goal:** All-atoms / all-isotopes atlas via the canonical Σ y_λ · χ^λ
pipeline + operator-valued Wenzl branching combiner.

## Scope map (2026-05-18, post-#689 merge)

| PR | Title | Classification | My relationship |
|---|---|---|---|
| #679 | Wire ρ_K consumer to LR witness + extend ⁶Li/⁷Li | OVERLAP (atom registry, y_λ at H_18/H_21) | Dependent; my y_λ cache extends theirs |
| #690 | Substrate m_p/m_n no-tautology + sub-leading + isobar Δm | OVERLAP (substrate anchors as my calibration baseline) | Dependent; will inherit substrate defaults |
| #696 | Flavor-dressing functor + wiring substrate split (Phase 3) | OVERLAP (re-points atomic_mass_via_rho_k.py) | Dependent on land order |
| #700 | Substrate Δm × χ-cache \|tr_M\| cross-check | OVERLAP (precision-side cross-check) | Will consume their cross-check output |
| #693 | Compute-integration audit + watcher skill | ADVISORY | Will consume their integration taxonomy |
| #701 | λ_scale conjecture Step 5 (Skein anchor) | PARALLEL | No direct overlap |

## Coordination comments posted (2026-05-18)

| Sibling | Link | Asks |
|---|---|---|
| #679 | https://github.com/litlfred/qou/pull/679#issuecomment-4474434572 | (a) cherry-pick `_hash_upstream` when #663 lands? (b) what should my Layer-1 records expose for ρ_K consumer? |
| #690 | https://github.com/litlfred/qou/pull/690#issuecomment-4474435071 | (a) Phase 3 conflict with `LEGACY_*` opt-out? (b) can I import `_precision.py` for per-tier dps tracking? |
| #696 | https://github.com/litlfred/qou/pull/696#issuecomment-4474435464 | (a) Phase 3 land order vs my isotopes-table wiring (b) functor_link field in KnotOperatorCatalogue? |

## Local commits (cherry-pickable for siblings if useful)

- `08016ee65 plan: all-atoms / all-isotopes atlas extension + y_λ to n=21`
  - Layered plan covering Layer 1..5
  - y_λ cache extended to n=2..21 (was n=2..15 on main)
  - Wenzl bridge + extend_y_lambda_at_q0_from_wenzl already on main

## Next concrete task (non-overlapping)

Per the agent's recommendation: build the **per-isotope record schema + knot-operator catalogue indexing** in isolation, independent of sibling witness wiring:

1. Schema definition (`.ts` content block or Python dataclass):
   - `IsotopeRecord { Z, N, A, spinJ, mass_pred_mev, calibration_source, knot_ops: [...] }`
   - `KnotOperatorCatalogue { type, q_level, witness_commit, canonical_form }`
2. Knot-operator catalogue skeleton — enumerate intra-nucleon / inter-nucleon / closure / fusion operators at each q-level (n=2..21)
3. Cross-reference table — per atom, list which existing probes feed the entry (can rebase onto sibling witness URLs later)

This locks in the schema before sibling witness wiring lands, avoiding merge friction. Then implement the **operator-valued Wenzl branching combiner** (`canonical_tr_m_via_branching.py`) which reuses A^λ_{μν}(I) extracts and should cut ⁴He from 15 min → seconds.

## Anti-patterns observed / avoided

- Did NOT add #701 (Skein anchor) to scope — parallel, no overlap.
- Did NOT silently rewrite my plan to incorporate #696's flavor-dressing functor — surfaced as a question instead.
- Did NOT request "ack" on coordination comments — they're FYI / coordination, not blocking asks.
