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

## Candidate ν_SDP definition VALIDATED on B₃ atoms (2026-06-20)

Took the formalize-first first step. Candidate operational definition:
  ν_SDP = #{ λ≠(n) : ρ_λ(T_w) PSD }  (exclude always-positive trivial rep).
Reproduces BOTH confirmed B₃ atoms: D→1 (only sign PSD; std (2,1) indefinite
[−0.89,+0.03]), ³He→2 (std+sign PSD). Naive total PSD count (2,3) does NOT match;
excluding trivial does. Discriminator block = std (2,1).
Probe: computations/probes/he_nu_sdp_definition_b3_validation.py (exit 0).
CAVEAT: 2 points, both B₃ — coincides with (#PSD−1) here. T (8_11, B₅) at H₅ is
the discriminator; ⁴He needs H₁₂. No fit, no forced ⁴He number.
Upgrades open item: no-definition → candidate validated 2/3, T@H₅ discriminates.

## Per-block-PSD ν_SDP candidate REFUTED by T (8_11) at H₅ (2026-06-20)

Out-of-sample test in the canonical orthogonal Hoefsmit form: the candidate
ν_SDP = #{non-trivial PSD Wedderburn blocks of ρ_λ(T_w)} gives D=1✓, ³He=2✓ but
T=1✗ (only the (1⁵) sign rep PSD; all 5 higher-dim non-triv blocks indefinite).
Canonical ν(T)=2. The 2-point B₃ agreement was coincidental. ("exclude trivial" ≡
"(#PSD)−1" identically — trivial = q^writhe>0 always PSD; no two readings.)
⇒ ν_SDP is NOT a per-block PSD sign test; needs the operator-selection SDP
(t, G, n_target), no per-atom spec reproducing 1,2,2 in corpus. #2552 finding
sharpened. Probe: computations/probes/he_nu_sdp_psd_count_test.py (REFUTED, exit 0).
No fit, no forced ⁴He number.
