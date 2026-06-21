---
# yq59
title: He-4 alpha-cluster 4-body binding term — derive-or-refute (opt 1)
status: completed
type: task
priority: normal
created_at: 2026-06-20T16:39:31Z
updated_at: 2026-06-21T19:39:07Z
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

## Option 2 (operator-selection SDP active-set) ALSO blocked (2026-06-20)

Checked deuteron_real_sdp.py (the genuine per-atom SDP: P_λ projectors, t_λ=y_λχ^λ,
G=diag(tr_M P_λ), n_target=tr_M β_D). Recorded witness:
- frobenius_gram_indefinite=True, strong_duality_holds=False, well_posed=False —
  bare program UNBOUNDED at q₀ (negative-norm forbidden blocks).
- active_set = 7 blocks (positive-norm subspace), NOT ν=1. Bounded only after
  choosing 1 of 6 Phase-B encodings; canonical doesn't close binding (Δ_λ gate).
So "ν_SDP = SDP active-set" gives 7≠1 for D. BOTH operational definitions fail
(PSD-count→1,2,1; SDP-active→7). ν_SDP has NO computable definition reproducing
1,2,2 — values are manual. ρ_F=2 for ⁴He unconfirmable; task not well-posed without
a derivation of ν_SDP. No fit. FINAL landing for the ν_SDP line.

## "Derive ν_SDP" attempt — self-conjugate candidate, mechanism refuted (2026-06-20)

kashaev def: ν_SDP = dim of saturating projection (MacMahon partition count).
- Deuteron BAR-FOLD SDP (principled §7b, no-fit) supports a SINGLE block (3,2,1) =
  the unique self-conjugate partition of 6. Other encodings rail to ±1e6.
- CANDIDATE: ν_SDP = #{self-conjugate λ⊢3A} = #{distinct-odd-part partitions of 3A}.
  Matches D(n6)=1, T(n9)=2, ³He(n9)=2 (all confirmed). Predicts ⁴He(n12)=3.
- PROBLEMS: (1) mechanism REFUTED — conjugate pairs do NOT cancel in the H₆ Gram
  (sums nonzero); (2) ⁴He=3 CONFLICTS with magic-A ρ_F=2 (ρ_F=3→+59% vs AME).
- VERDICT: not a derivation. Decisive next test = T/³He bar-fold support vs their 2
  self-conj blocks (needs y_λ, χ^λ at H₉). No fit, no forced number.
Audit: docs/audits/2026-06-20-nu-sdp-selfconjugate-candidate-and-binding-tension.md.

(1+q)/2: REFUTED near-match (PR #1707, bean cbnf) — NOT re-attempted; live non-fit
direction is GAP-A-3 P_λ, separate from this ν_SDP line.

## DECISIVE H₉ test: self-conjugate ν_SDP candidate REFUTED (2026-06-21)

Ran the bar-fold SDP support at H₉ (y_λ Wenzl bridge + χ^λ hoefsmit_numpy + bar-fold LP;
validated by reproducing deuteron support {(3,2,1)} first):
- D: bounded support {(3,2,1)} → 1 ✓
- ³He: bounded support {(5,1⁴)} → 1 (4 others ±1e6 RAILS) ✗ (ν=2)
- T: bounded support ∅ → 0 (all railed) ✗ (ν=2)
|bar-fold support|=(1,1,0) ≠ ν=(1,2,2). Bar-fold regularises ONLY the deuteron; A≥3
rails (indefinite-Gram unboundedness, #2552 pathology). #self-conj match was COINCIDENCE.
Weaker survivor: bounded support ⊆ self-conjugate blocks. Self-conjugate avenue CLOSED;
ν_SDP derivation remains open. Probe: he_nu_sdp_barfold_h9_test.py. No fit.

## CAPSTONE: SDP-saturation derivation OBSTRUCTED + critical-distance flag (2026-06-21)

Tested the bare operator-selection SDP saturation in both principled regimes:
- q→1⁺ (well-posed): single min-cost block → ν=1 for D,T,³He (never 1,2,2).
- q₀ (indefinite): rail-degenerate (0/0/1). neg-norm blocks present at BOTH q→1 and q₀
  ⇒ indefiniteness is structural, not a q₀ artifact.
NO principled saturation yields 1,2,2. With per-block-PSD/active-set/bar-fold/self-conj
all refuted, ν_SDP has NO first-principles SDP-saturation derivation.
CRITICAL-DISTANCE FLAG: ρ_F=ν_SDP is a naming of a hand-assigned value; ρ_F=2 (⁴He)
looks fitted (lands +5.87%; ρ_F=3→+59%) — an acknowledged input, not a derivation.
Audit: docs/audits/2026-06-21-nu-sdp-saturation-obstruction-and-critical-distance.md.
Probe: he_nu_sdp_saturation_obstruction.py. No fit. ν_SDP line CLOSED as open+flagged.
