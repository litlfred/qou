---
# yq59
title: He-4 alpha-cluster 4-body binding term — derive-or-refute (opt 1)
status: in-progress
type: task
priority: normal
created_at: 2026-06-20T16:39:31Z
updated_at: 2026-06-20T17:24:27Z
---


## Triage verdict (2026-06-20, background Explore) — NO non-fit probe to add

Corpus already settles the question:
- **Beyond pairwise — proven.** B_sym linear-chain = exact 3A-strand Markov trace
  to 50 dps ⇒ bare trace adds ZERO cooperative binding (sibling formalized the
  additivity in Lean, bean 6z40, `fc30c04179`). The α-residual must come from a
  *different* categorical object.
- **Residual pinned, not fitted:** 20.9 MeV (signed-trace standard / `derive-binding-chain-cooperative.witness.json`), 16.3 (log), 12.7 (Pauli exploratory).
- **Four ansätze REFUTED — do not re-walk:** q-factorial ratio (PR #1386 retracted),
  `[2]_{q^½}`, per-nucleon `δ_int` fit, naive LR-fusion scalar extraction
  (`2026-06-01-he4-multi-nucleon-interface-research-state.md`). `ρ_F=2` in the
  magic-A formula is owner-gated §3b-cond.
- **Open piece = n=4 body-order jet / SW-period residue** (`docs/coordination/2026-06-05-step9-binding-closure.md`) — owner-gated research frontier, fit-trap-prone.

**DECISION: hold.** No honest non-fit deliverable without explicit owner direction.

## n=4 ρ_F finding (2026-06-20) — open item RECLASSIFIED: definition, not compute

Scoped attempt at ν_SDP(⁴He) found the audit chain's "only numerical verification
remains" framing is STALE (corpus-grep discipline):
- **No solver computes ν_SDP for any atom.** D/T/³He = 1,2,2 are HARDCODED
  ("manual-historical-volume-match" in joint_tower_sdp_solver_v2.py); the H₃
  sdp_feasibility check is a per-block boolean, not a multiplicity producer.
  The Rust witness rho_factor = 0,1,1 ≠ canonical 1,2,2 (different, unvalidated).
- **Extrapolated ⁴He=2 not uniquely forced:** max(Z,N)→2, A−1→3 both fit the
  confirmed 1,2,2 (T,³He both A=3); they diverge exactly at ⁴He.
- **Real gate:** pin an operational ν_SDP definition (saturating SDP active-set
  count) that REPRODUCES D/³He=1,2 at H₃, THEN extend to ⁴He (H₁₂ Hoefsmit, the
  1-2-session Rust extension). Do NOT run H₁₂ on a guessed definition (rainbow).

Audit: docs/audits/2026-06-20-he4-nu-sdp-not-computed-definition-gate.md.
No fit, no forced number. ρ_F less settled than the magic-A wireup states.
