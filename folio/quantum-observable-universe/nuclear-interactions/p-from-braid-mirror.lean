import Mathlib.Data.Int.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidsAndKnots.PFromBraidMirror — the parity (P) conjecture carrier

**Sibling-resolution carrier** for content block
[`conj:p-from-braid-mirror`](p-from-braid-mirror.md): *parity as braid-diagram mirror*.

**No instance is provided** — the honest open state for a conjecture (AGENTS.md §3b).

## 2026-09-05 — this carrier used to assert nothing

It read, in full:

```lean
class PFromBraidMirror where
  holds : Prop
```

A field typed `: Prop` has the *universe* of propositions as its type, so an instance
supplies a proposition rather than a proof of one: `⟨True⟩` discharges it, and every
`[PFromBraidMirror]`-conditional theorem was conditional on nothing.

**Prior work, credited.** The defect class is bean `qou-tsnp`'s — *"GAP: 12 conjecture
carriers axiomatised as `holds : Prop` assert nothing"* — which lists this carrier among
its twelve, with the corpus-wide census at
[`docs/audits/2026-08-23-free-prop-field-census.md`](../../../docs/audits/2026-08-23-free-prop-field-census.md)
(PR #5562) and a detector at
[`scripts/free-prop-field-audit.py`](../../../scripts/free-prop-field-audit.py). What is
new here is the **repair**, in that bean's prescribed shape. D9
(`IsospinFromCanonicalBowtie`, #6671) and D10 (`SpinFromSo3Fiber`, #6683) were closed the
same way; a fresh library-twin check was run first, per the D11 lesson (#6711), and came
back empty — so the content repair is the right move here, unlike for D11.

## What is encoded

The block is unusually well-specified, and all three of its structural claims are stated:

* **`P` is an involution** — `P² = id`, which the block asserts outright.
* **`P` negates the signed writhe** — `w(Pβ) = −w(β)`, the block's own restatement of
  `σᵢ^ε ↦ σᵢ^(−ε)`.
* **`P` holds `q` fixed** — this is the field that does the *disentangling* work. The
  block's whole point is that `P` is **not** the bar-involution: bar sends
  `σᵢ ↦ σᵢ⁻¹` **and** `q ↦ q⁻¹`, and is `P·C·T` composed, whereas `P` alone fixes `q`,
  fixes colour-sheet flavours, and fixes trace cyclicity. Without this field the carrier
  would not distinguish `P` from bar, which is the one thing the block is for.

The braid-word type `B`, the map `P`, the writhe `w`, and the `q`-datum are **caller
parameters**, per the rule recorded in
`QOU/AlgebraicSubstrate/ConditionalClasses.lean` after its own retraction — an `∃` over
a quantity the class itself chooses cannot be false, whereas a `∀` about a quantity the
caller supplies can be. So the class is refutable, and that is discharged below rather
than asserted.

## What is DERIVED rather than axiomatised

`p_fixed_point_writhe_zero`: a `P`-symmetric braid has zero writhe. If `P b = b` then
`w b = w (P b) = −w b`, so `2 · w b = 0` in `ℤ`, so `w b = 0`. This is a real consequence
of the two structural fields and is proved, not assumed — the block's structure paying
off rather than being restated.

## What is NOT encoded

**The `bar = P · C · T` decomposition.** The block gives it as a three-row table (P on
Hecke-generator chirality, C on colour-sheet flavour, T on Markov-trace cyclicity). Stating
it needs carriers for `C` and `T` as maps on the same type — `conj:c-from-color-flavor-swap`
and `conj:t-from-trace-cyclicity` — and a bar-involution acting on the same `B`. Composing
three conjectural maps whose own carriers are separate blocks would encode a claim about
all three, not about `P`. What is stated here is `P`'s own action; the composition is named
and left.

Per `qou-tsnp`'s guard — *"if a conjecture's claim cannot yet be stated against existing
types … say so and note what type must grow first"* — **what must grow first is a common
braid-word type carrying all three of `P`, `C`, `T` simultaneously**, so the composite
identity can be stated at all.

**Also not claimed:** that any particular `P` exists on the corpus's braid types. No
instance is provided; the carrier says what `P` must satisfy, not that something does.

## Base ring

Deliberately generic. The writhe is `ℤ`-valued and the `q`-datum is an arbitrary type
`Q` — no ordering, no `Real`, nothing archimedean is needed to say what `P` does, so per
§7c this stays over type variables rather than specialising.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/p-from-braid-mirror.ts
-/

namespace QOU.BraidsAndKnots

/-- **CONJECTURE (parity closure).** Parity `P` acts as the mirror reflection of the braid
diagram — `σᵢ^ε ↦ σᵢ^(−ε)` with `q` held fixed — negating the signed writhe.

`B` is a braid-word type, `P` the parity map, `w` the signed writhe, and `qOf` the
`q`-datum that `P` must leave alone. All are supplied by the **caller**, so the class is
false for maps that do not behave this way (see `pFromBraidMirror_refutable`).

The `fixes_q` field is what separates this from the bar-involution: bar sends
`σᵢ ↦ σᵢ⁻¹` *and* `q ↦ q⁻¹` and is `P·C·T` composed, while `P` alone fixes `q`.

**No instance is provided.** Downstream results consume this as
`[PFromBraidMirror P w qOf]` and are genuinely conditional on it.

-- Ref: [leitner2026] conj:p-from-braid-mirror -/
class PFromBraidMirror {B : Type*} {Q : Type*}
    (P : B → B) (w : B → ℤ) (qOf : B → Q) : Prop where
  /-- `P` is an involution: `P² = id`. -/
  involutive : ∀ b, P (P b) = b
  /-- `P` negates the signed writhe — the block's restatement of `σᵢ^ε ↦ σᵢ^(−ε)`. -/
  writhe_neg : ∀ b, w (P b) = - w b
  /-- `P` holds `q` fixed. This is what distinguishes `P` from the bar-involution, which
  also sends `q ↦ q⁻¹`; without it the carrier would not say what the block is for. -/
  fixes_q : ∀ b, qOf (P b) = qOf b

/-- **A `P`-symmetric braid has zero writhe** — derived from the two structural fields,
not assumed. If `P b = b` then `w b = w (P b) = - w b`, so `2 * w b = 0` in `ℤ`.

This is the block's structure paying off: it is a falsifiable consequence that follows
from `P` mirroring the diagram, and it is discharged here rather than restated as a
field. -/
theorem p_fixed_point_writhe_zero {B Q : Type*}
    (P : B → B) (w : B → ℤ) (qOf : B → Q) [h : PFromBraidMirror P w qOf]
    (b : B) (hb : P b = b) : w b = 0 := by
  have hneg := h.writhe_neg b
  rw [hb] at hneg
  linarith

/-- The class is **refutable**, which the previous `holds : Prop` carrier was not: the
identity map on `ℤ` fixes every writhe rather than negating it, so it satisfies
`involutive` and `fixes_q` and fails `writhe_neg` at `b = 1`.

Stated as a theorem because "the carrier asserts something" is exactly the property that
was missing, and it should be visible as discharged rather than claimed in prose. -/
theorem pFromBraidMirror_refutable :
    ¬ PFromBraidMirror (B := ℤ) (Q := Unit) id (fun n => n) (fun _ => ()) := by
  intro hc
  have h := hc.writhe_neg 1
  simp at h

end QOU.BraidsAndKnots
