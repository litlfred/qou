---
# qou-0pe3
title: 'GAP: SpechtDimension assumes a dimension that Partition.dimIrrep already proves -- blocked by a Partition type collision'
status: todo
type: task
created_at: 2026-08-21T15:17:07Z
updated_at: 2026-08-21T15:17:07Z
---

Found by the TL-arc Lean infrastructure survey, PR #5352, branch claude/tl-arc-lean-infra-2026-08-21. Ledger: docs/audits/2026-08-21-tl-arc-lean-infra-ledger.md, gap F2-b.

An assumption stands where a proof is two files away, and a type collision is the
only thing in between.

THE ASSUMPTION.
content/quantum-observable-universe/lean/QOU/Hecke/Wedderburn.lean:54

  class SpechtDimension {n : ℕ} (lam : Partition n) where
    dim : ℕ
    positive : 0 < dim

It has NO INSTANCE anywhere in the tree. It assumes a Specht dimension exists and
is positive, and computes nothing.

THE PROOF THAT ALREADY EXISTS.
content/quantum-observable-universe/lean/QOU/BraidKnot/DeltaLambdaSignRule.lean:130

  def Partition.dimIrrep {n : ℕ} (Λ : Partition n) : ℕ :=
    Nat.factorial n / Λ.hookProduct

bridged sorry-free to the standard-tableau count at
BraidKnot/PartitionHookProductBridge.lean:163

  theorem dimIrrep_eq_numSYT {n : ℕ} (Λ : Partition n) :
      Λ.dimIrrep = numSYT (toYoungDiagram Λ)

(the ℕ-division is exact, witnessed by numSYT_mul_hookProduct_partition).

WHY IT IS NOT ALREADY WIRED -- a Partition TYPE COLLISION, at least threefold:

  QOU.Hecke.Wedderburn.Partition            Hecke/Wedderburn.lean:45
  QOU.BraidKnot.DeltaLambdaSignRule.Partition   DeltaLambdaSignRule.lean:46
  QOU.BraidKnot.Partition                   (DeltaLambdaSignRule's own docstring
                                             warns of this one, vs
                                             GramSeminormalBlock / PerPartitionKLambda)

dimIrrep lives on the second; SpechtDimension quantifies over the FIRST. They are
different structures that happen to share a glyph, so nothing connects them today.
This is the AGENTS.md 'grep the claim SHAPE, not only the topic' hazard in its
plainest form: a topic-grep for 'Specht dimension' finds both and suggests the work
is done.

THE WORK. Build the type bridge (an equiv or a coercion between the two Partition
structures, both of which are list-of-parts + sum + positivity + sortedness), then
supply

  instance : SpechtDimension lam := ⟨(bridge lam).dimIrrep, positivity⟩

with positivity from hookProduct_ne_zero + the exact-division bridge. Sized
small-to-medium; it is plumbing, not mathematics.

WHY IT IS WORTH DOING. Front 2 of the TL arc (all-n corank,
dim radical = n! - Σ_{ℓ(λ)≤2}(dim V_λ)²) needs dim V_λ as a COMPUTED quantity, not
an assumed one. Discharging SpechtDimension converts one of the front's four
ingredients from ASSUMED to PROVED. This is legitimate -- supplying a genuine
instance from a proved definition -- and is the opposite of the anti-laundering
concern, which forbids manufacturing a class to close a gap.

RELATED, and check before starting: qou-9ojy ('WIRE: burnside bridge (1)
dimIrrep=numSYT') may be stale -- dimIrrep_eq_numSYT is proved on main as of
9c6e9834cb. qou-r0jg / qou-oh6k carry the OTHER burnside half, Σ dimIrrep² = n!,
which front 2 also needs and which is still open.
