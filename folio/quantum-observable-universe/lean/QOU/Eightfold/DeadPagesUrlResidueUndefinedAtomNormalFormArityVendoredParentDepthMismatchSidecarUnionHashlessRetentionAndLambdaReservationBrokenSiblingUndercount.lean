/-
Copyright (c) 2026 QOU Formalization. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.

# Dead Pages URL Residue, Undefined Atom Normal-Form Arity, Vendored Parent-Depth Mismatch, Sidecar Union Hashless Retention, and Lambda-Reservation Broken-Sibling Undercount

This standalone zero-sorry Lean 4 module formalizes five repository-hygiene and
audit-instrumentation findings:

1. **`qou-dkem` — `77` dead `gh_pages_url` links in `proof-objects.json`**:
   - Following the 2026-09-27 `gh-pages` deprecation ruling, `77` `gh_pages_url`
     fields in `proof-objects.json` reference non-existent pages, partitioning any
     corpus of `totalObjects` proof objects into `totalObjects - 77` valid entries
     and `77` dead links awaiting drop-or-repoint disposition.

2. **`qou-ozts` — Undefined `apply_atom_nf` 3-argument call vs 2-argument `build_atom_nf`**:
   - `computations/universal-ilp.py` invokes `apply_atom_nf(nf, 1, 0)` at line `191`
     (`Z + N = 1`) and `apply_atom_nf(nf, 6, 6)` at line `202` (`Z + N = 12`, line span
     `202 - 191 = 11`) with arity `3` (`(nf, Z, N)`), whereas `build_atom_nf(Z, N)` has
     arity `2` (`3 - 2 = 1` extra normal-form accumulator parameter `nf`), blocking the
     old-muon `B`-population witness drain.

3. **`qou-rug0` — Fixed `.parent` depth mismatch between source (`3`) and vendored (`5`) layouts**:
   - Modules in `computations/substrate/x.py` lie `3` `.parent` levels below the repo root,
     whereas their vendored copies in `qou-mass/src/qou_mass/_internal/x.py` lie `5` levels
     below (`5 - 3 = 2` levels deeper), and `_li_2_q_util.py` differs by `1` level (`2 - 1 = 1`),
     accounting for `3 * 2 + 1 = 7` shims repaired via upward landmark search.

4. **`qou-tqr9` — Agent-adjudicated sidecar union and `70,307` hashless verdict retention**:
   - Regenerating `742` conflicted sidecars dropped `7,381` agent verdicts across `738` blocks,
     and naive `float` JSON serialization introduced `1,172` spurious diff deletions against
     `3` real changes (`1,172 - 3 = 1,169` spurious deletions eliminated by `Decimal` round-trip,
     reaching `199 / 200` then `200 / 200` byte-identical sidecars).
   - Across `126,156` agent-kind entries (`78,904` `local/*` + `36,206` `agent:*` + `11,046`
     other), `70,307` entries (`68,342` `local/*` + `0` `agent:*` + `1,965` other, `> 55%` of all
     agent entries and `> 86%` of `local/*`) carry no `field_hash.md` and are retained by the
     corrected filter rather than silently dropped as stale (`55,849` carrying `field_hash.md`).

5. **`qou-vexw` — Pre-v4.24 `382`-file broken-sibling census undercount from `λ` token reservation**:
   - The 2026-06-28 compile sweep recorded `382` broken siblings (`72` in `mass-theory` +
     `63` in `quantum-observable-universes` = `135` in the top two chapters, `247` in other
     chapters), predating the Lean v4.24.0 `λ` keyword reservation (`213` binder sites in
     `SkewSYT.lean` and `4` parse/type errors at lines `37, 38, 46, 112` in a newly broken
     `mass-theory` sibling, increasing the true broken count to `382 + newlyBroken`).
-/

namespace QOU.Eightfold.DeadPagesUrlResidueUndefinedAtomNormalFormArityVendoredParentDepthMismatchSidecarUnionHashlessRetentionAndLambdaReservationBrokenSiblingUndercount

/-! ## 1. `qou-dkem`: `77` Dead `gh_pages_url` Links in `proof-objects.json` -/

/-- Remaining proof-object entries with live URLs after subtracting dead `gh_pages_url` links. -/
def liveProofObjectUrls (totalObjects deadGhPagesLinks : Nat) : Nat :=
  totalObjects - deadGhPagesLinks

/-- Updated dead-link residue after repointing `repointedCount` and dropping `droppedCount` dead URLs. -/
def remainingDeadGhPagesLinks (initialDead repointedCount droppedCount : Nat) : Nat :=
  initialDead - (repointedCount + droppedCount)

/-- For any corpus of `totalObjects ≥ 77` proof objects and any remediation split
    `repointed + dropped ≤ 77`, the `77` dead `gh_pages_url` links partition `totalObjects`
    and drain to `0` when all `77` are either repointed or dropped. -/
theorem dead_gh_pages_url_partition_and_remediation
    (totalObjects repointed dropped : Nat)
    (hTotal : 77 ≤ totalObjects)
    (hRem : repointed + dropped ≤ 77) :
    liveProofObjectUrls totalObjects 77 + 77 = totalObjects ∧
    remainingDeadGhPagesLinks 77 repointed dropped + repointed + dropped = 77 ∧
    remainingDeadGhPagesLinks 77 77 0 = 0 ∧
    remainingDeadGhPagesLinks 77 0 77 = 0 := by
  dsimp [liveProofObjectUrls, remainingDeadGhPagesLinks] at *
  omega

/-! ## 2. `qou-ozts`: Undefined `apply_atom_nf` Arity Mismatch in `universal-ilp.py` -/

/-- Arity discrepancy between a stateful normal-form application `(nf, Z, N)` and a constructor `(Z, N)`. -/
def normalFormArityGap (applyCallArity buildConstructorArity : Nat) : Nat :=
  applyCallArity - buildConstructorArity

/-- Total nucleon number `A = Z + N` passed at an atomic normal-form call site. -/
def callSiteNucleonTotal (protonCountZ neutronCountN : Nat) : Nat :=
  protonCountZ + neutronCountN

/-- Line span between the two undefined `apply_atom_nf` call sites in `computations/universal-ilp.py`. -/
def callSiteLineSpan (firstCallLine secondCallLine : Nat) : Nat :=
  secondCallLine - firstCallLine

/-- The two undefined `apply_atom_nf` call sites at lines `191` (`(nf, 1, 0)`, `A = 1`) and `202`
    (`(nf, 6, 6)`, `A = 12`, span `11` lines) pass `3` arguments versus `2` for `build_atom_nf`
    (`normalFormArityGap 3 2 = 1`). -/
theorem undefined_apply_atom_nf_arity_and_call_sites
    (applyArity buildArity line1 line2 : Nat)
    (hArity : buildArity ≤ applyArity)
    (hLine : line1 ≤ line2) :
    buildArity + normalFormArityGap applyArity buildArity = applyArity ∧
    line1 + callSiteLineSpan line1 line2 = line2 ∧
    normalFormArityGap 3 2 = 1 ∧
    callSiteNucleonTotal 1 0 = 1 ∧
    callSiteNucleonTotal 6 6 = 12 ∧
    callSiteLineSpan 191 202 = 11 := by
  dsimp [normalFormArityGap, callSiteNucleonTotal, callSiteLineSpan] at *
  omega

/-! ## 3. `qou-rug0`: Fixed `.parent` Depth Mismatch Between Source and Vendored Layouts -/

/-- Directory-depth offset between the vendored package layout and the source `computations/` layout. -/
def vendoredParentDepthOffset (sourceParentCount vendoredParentCount : Nat) : Nat :=
  vendoredParentCount - sourceParentCount

/-- Total path-resolution shims repaired across dual-layout substrate modules and single-offset utilities. -/
def repairedShimInstanceCount (dualLayoutModules layoutsPerModule singleOffsetUtilities : Nat) : Nat :=
  dualLayoutModules * layoutsPerModule + singleOffsetUtilities

/-- Moving from `computations/substrate/x.py` (`3` `.parent` levels) to
    `qou-mass/src/qou_mass/_internal/x.py` (`5` `.parent` levels) shifts the depth by `2` levels
    (`1` level for `_li_2_q_util.py`), and repairing the `3` dual-layout modules across both layouts
    plus `_li_2_q_util.py` fixes `7` shim instances. -/
theorem vendored_parent_depth_mismatch_and_repaired_shims
    (srcDepth vendDepth dualModules : Nat)
    (hDepth : srcDepth ≤ vendDepth) :
    srcDepth + vendoredParentDepthOffset srcDepth vendDepth = vendDepth ∧
    repairedShimInstanceCount dualModules 2 1 = 2 * dualModules + 1 ∧
    vendoredParentDepthOffset 3 5 = 2 ∧
    vendoredParentDepthOffset 1 2 = 1 ∧
    repairedShimInstanceCount 3 2 1 = 7 := by
  dsimp [vendoredParentDepthOffset, repairedShimInstanceCount] at *
  omega

/-! ## 4. `qou-tqr9`: Agent-Adjudicated Sidecar Union and `70,307` Hashless Verdict Retention -/

/-- Total agent-kind QA entries across `local/*`, `agent:*`, and other producer prefixes. -/
def totalAgentKindEntries (localEntries agentColonEntries otherEntries : Nat) : Nat :=
  localEntries + agentColonEntries + otherEntries

/-- Agent-kind QA entries that carry an explicit `field_hash.md` digest. -/
def hashedMdAgentEntries (totalEntries hashlessMdEntries : Nat) : Nat :=
  totalEntries - hashlessMdEntries

/-- Spurious JSON round-trip diff deletions eliminated by preserving `Decimal` and UTF-8 formatting. -/
def spuriousDiffDeletionsEliminated (naiveDiffDeletions genuineDiffDeletions : Nat) : Nat :=
  naiveDiffDeletions - genuineDiffDeletions

/-- Across `126,156` agent-kind entries (`78,904 + 36,206 + 11,046`), `70,307` entries
    (`68,342 + 0 + 1,965`, `> 55%` of total and `> 86%` of `local/*`) carry no `field_hash.md`
    (leaving `55,849` with `field_hash.md`), and `Decimal` serialization eliminates
    `1,172 - 3 = 1,169` spurious diff deletions. -/
theorem sidecar_union_hashless_retention_and_decimal_roundtrip
    (localEnt agentEnt otherEnt hashlessEnt : Nat)
    (hHashless : hashlessEnt ≤ localEnt + agentEnt + otherEnt) :
    hashlessEnt + hashedMdAgentEntries (totalAgentKindEntries localEnt agentEnt otherEnt) hashlessEnt =
      totalAgentKindEntries localEnt agentEnt otherEnt ∧
    totalAgentKindEntries 78904 36206 11046 = 126156 ∧
    totalAgentKindEntries 68342 0 1965 = 70307 ∧
    hashedMdAgentEntries 126156 70307 = 55849 ∧
    126156 * 55 < 70307 * 100 ∧
    70307 * 100 < 126156 * 56 ∧
    78904 * 86 < 68342 * 100 ∧
    spuriousDiffDeletionsEliminated 1172 3 = 1169 := by
  dsimp [totalAgentKindEntries, hashedMdAgentEntries, spuriousDiffDeletionsEliminated] at *
  omega

/-! ## 5. `qou-vexw`: Pre-v4.24 `382`-File Broken-Sibling Undercount from `λ` Reservation -/

/-- Updated broken-sibling count after adding siblings broken by the Lean v4.24.0 `λ` reservation. -/
def postBumpBrokenSiblingTotal (preBumpCensus newlyBrokenByLambda : Nat) : Nat :=
  preBumpCensus + newlyBrokenByLambda

/-- Broken siblings outside the top two chapters (`mass-theory` and `quantum-observable-universes`). -/
def otherChapterBrokenSiblings (preBumpCensus massTheoryBroken qouChapterBroken : Nat) : Nat :=
  preBumpCensus - (massTheoryBroken + qouChapterBroken)

/-- For any positive number `newlyBroken > 0` of siblings broken by the v4.24.0 `λ` reservation,
    `postBumpBrokenSiblingTotal 382 newlyBroken` strictly exceeds the stale `382` census
    (`72 + 63 = 135` in the top two chapters and `247` in other chapters, with `213` `λ` sites
    in `SkewSYT.lean` and line span `112 - 37 = 75` across the `4` errors in the uncovered sibling). -/
theorem lambda_reservation_broken_sibling_undercount
    (newlyBroken : Nat)
    (hNew : 0 < newlyBroken) :
    382 < postBumpBrokenSiblingTotal 382 newlyBroken ∧
    postBumpBrokenSiblingTotal 382 newlyBroken - 382 = newlyBroken ∧
    otherChapterBrokenSiblings 382 72 63 = 247 ∧
    72 + 63 + otherChapterBrokenSiblings 382 72 63 = 382 ∧
    postBumpBrokenSiblingTotal 382 1 = 383 ∧
    112 - 37 = 75 := by
  dsimp [postBumpBrokenSiblingTotal, otherChapterBrokenSiblings] at *
  omega

end QOU.Eightfold.DeadPagesUrlResidueUndefinedAtomNormalFormArityVendoredParentDepthMismatchSidecarUnionHashlessRetentionAndLambdaReservationBrokenSiblingUndercount
