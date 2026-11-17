---
# qou-sym2
title: Sym2Gate.lean is vacuous — demote or encode the real decomposition claim
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-06T00:00:00Z
updated_at: 2026-10-04T15:24:41Z
parent: qou-6qbv
---

## The defect

`folio/quantum-observable-universe/lean/QOU/Eightfold/Sym2Gate.lean` carries
three declarations whose conclusions are arithmetic tautologies:

    theorem sym2_dim_3 : 3 * (3 + 1) / 2 = 6 := by norm_num
    theorem corpus_T1_fails_sym2_gate : (1 : ℕ) + 5 = 6 ∧ (1 : ℕ) > 0 := by …
    theorem octonion_3_passes_sym2_gate : (6 : ℕ) = 6 ∧ (0 : ℕ) = 0 := by …

`octonion_3_passes_sym2_gate` says `6 = 6 ∧ 0 = 0`. It mentions no octonion, no
Sym², no gate, and no representation. All representation-theoretic content lives
in the **statement names**, not the proofs — the exact pattern AGENTS.md
§"Strict Lean Discipline" item 5 bans ("any proposition that is provable without
using any hypothesis about the mathematical objects in question"), and a close
cousin of the `placeholder-true` / docstring-asserts-a-claim class in
§3b-tax.

This matters because the file was being cited as machine-checked backing for a
physics claim. `schur-weyl-eightfold.md` said "The second route has passed the
Sym² gate" and `dictionary-flavor-layer.md` listed colour as "Sym² gate passed".
Both have been rescoped to "not excluded by the Sym² gate" (see the
`content(eightfold)` honesty-pass commit), but the Lean file is unchanged.

## Honest dispositions (pick one)

1. **Encode the real claim.** The content is: for the icosahedral colour triple
   `T_1`, `Sym²(T_1) ≅ 1 ⊕ 5` contains a singlet; for the octonionic `3`,
   `Sym²(3) ≅ 6` does not. That is a statement about characters/decompositions
   of specific representations, and it is what the gate actually tests. Encode
   the decomposition (or at minimum the character inner product
   `⟨χ_{Sym²V}, 1⟩ = 0` vs `= 1`) so the proof depends on the representation.
2. **Demote to a `def`/`abbrev` of the arithmetic**, with a docstring making
   clear the representation-theoretic input is *cited from the literature*, not
   proved — and stop calling the declarations theorems.
3. **Demote the block to a conjecture carrier** per §3b-tax, with content-bearing
   fields.

Do **not** leave it as three "theorems" whose proofs are `norm_num` on integers.

## Cross-refs

Consumers rescoped: `eightfold-way/schur-weyl-eightfold.md`,
`eightfold-way/dictionary-flavor-layer.md`, `eightfold-way/color-su3-from-g2.ts`
(`lean: "qou:QOU.Eightfold.Sym2Gate"`).
Parent coverage bean: `qou-8fl1`.

## Round 56 Update (PR #8271)
- Opened PR https://github.com/litlfred/qou/pull/8271 (`b2cbd4734e5f10beb2130e3555212a3d78a87989`, C1 `22c4bf632182163314cbb930ffed44b139fa5265`).
- Compiled under Lean 4.24.0 (`0` `sorry`, `0` `axiom`, `0` warnings) and verified `0` advisories across all 6 static vacuity & borrowed-name audits, with 80-dps `mpmath` witness `computations/probes/round56-devacuify-6qbv-b9cj.witness.json` (`scriptHash = c44bdf430d4f`).
