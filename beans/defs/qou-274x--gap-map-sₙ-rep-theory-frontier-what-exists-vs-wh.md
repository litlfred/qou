---
# qou-274x
title: 'GAP MAP: Sₙ rep-theory frontier — what exists vs what''s genuinely open'
status: todo
type: task
tags:
    - lean
    - sn-rep-theory
created_at: 2026-08-02T00:08:48Z
updated_at: 2026-08-02T00:08:48Z
parent: qou-0ap1
---

Corpus-grep survey 2026-08-02 (do NOT re-derive existing infra):

FOUNDATION ALREADY BUILT (sorry-free on main):
- QOU/Mathlib/StandardYoungTableau.lean: SYT type (SSYT refinement), row_strict, encode, instFinite, numStandardYoungTableaux. THE canonical SYT type.
- QOU/Mathlib/StandardYoungTableauBot.lean: numStandardYoungTableaux ⊥ = 1.
- QOU/Mathlib/PartitionListBridge.lean: Nat.Partition n ≃ sorted List ℕ (P5 index bridge).
- QOU/Mathlib/RSKBurnsideTarget.lean: RSKBurnsideHolds n as a fully-DEFINED Prop (∑#SYT²=n!) — not yet a theorem.
- IdentityBWedderburn.identityB_via_wedderburn_unconditional (#3193/#3220): the ABSTRACT (unlabelled) ∑dᵢ²=n! AND content-square trace identity ∑dᵢ²ωᵢ=n!·C(n,2) PROVED sorry-free via Artin-Wedderburn on ℂ[Sₙ] + Jucys centrality (IdentityBCentrality). axiom-clean.
- IdentityIPlancherelInstances.lean: PlancherelSnData instances n≤12 by decide → Identity I unconditional for n≤12.

GENUINELY OPEN (hard, multi-session; sorries concentrated here):
1. RSKBurnsideHolds PROOF — the RSK correspondence Sₙ ≃ Σ_λ SYT(λ)² (Schensted insertion+bijectivity). Mathlib has NO Combinatorics.RSK at v4.24.0. Discharges PlancherelSnData.sum_dim_sq LABELLED form.
2. Hook-length formula dimSYT=dimHLF (i.e. numSYT_mul_hookProduct). ~19 parallel WIP files in QOU/Mathlib/SYTHook*/SYTBranching* (SYTHookGNW 17 sorries, SYTHookFormulaGeneral 14, SYTBranchingRecursion 14). Greene-Nijenhuis-Wilf / hook-walk route. HARD.
3. Specht module completeness (P1: every Sₙ irrep is some S^λ) + JM seminormal eigenvalue LABELLING (JucysMurphy.seminormalVector_base_exists, SnWedderburnPartitionBridge.sn_isotypic_specht_split). Needs Mathlib.RepresentationTheory — only ~30 RT oleans in the qou lake-cache (partial), so LARGELY NOT lean-direct verifiable in this sandbox. This is the labelling that turns the proved abstract Wedderburn blocks into λ⊢n-indexed ones.

BOTTOM LINE: 'build the missing Sₙ infra' is mostly DONE. Residual = (a) RSK proof, (b) HLF proof, (c) Specht/JM partition-LABELLING of already-proved abstract blocks — each a genuine theorem, (c) needs a full-Mathlib env. See docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md (phases P1-P5, all updates through 2026-07-02).
