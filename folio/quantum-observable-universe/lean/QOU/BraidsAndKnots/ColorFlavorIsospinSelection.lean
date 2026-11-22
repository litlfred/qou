import Mathlib.Tactic.NormNum

/-!
# QOU.BraidsAndKnots.ColorFlavorIsospinSelection — the flavor side of `W`

Bean `qou-63n2`, continuing `qou-ctkw` (`ColorPairIsotypicDecomposition`).

The color side is settled: ordered color-sheet pairs carry `T₁ ⊗ T₁ = A ⊕ T₁ ⊕ H`
with the forced grading `Sym² = A ⊕ H` (dim 6) / `Alt² = T₁` (dim 3). That left
`W_{c₁c₂}(F₁,F₂)` a 2-parameter convex family, with the **flavor dependence**
`(F₁,F₂)` unsupplied.

Flavor is a representation too: a nucleon pair carries
`I=½ ⊗ I=½ = I=1 ⊕ I=0` (dims `3 + 1 = 4`), with `I=1` exchange-**symmetric**
(`pp`, `(pn+np)/√2`, `nn`) and `I=0` exchange-**antisymmetric** (`(pn−np)/√2`).

## The hypothesis (named, not hidden)

`InterfaceExchangeAntisymmetry` is a **conjecture class**: the assertion that the
two-nucleon interface carries definite antisymmetry under *simultaneous* exchange
of color-sheet and flavor labels. This is a physical assumption about the
interface, **not** a theorem — nucleon-level Fermi statistics constrains the full
wavefunction (space ⊗ spin ⊗ isospin ⊗ color), not this sub-sector in isolation.
It is carried as a class field with **no instance**, so every consequence below
is genuinely conditional (§3b-cond).

Given it, only two couplings survive:

  `color-Sym (A ⊕ H) ⊗ flavor-Alt (I=0)`   and   `color-Alt (T₁) ⊗ flavor-Sym (I=1)`

## The falsifiable consequence

`pp` and `nn` both sit in `I=1`, so the rule forces the **same** color system on
them: `W` cannot distinguish `pp` from `nn` — charge symmetry is a *consequence*,
not an imposed constraint. It would fail if the rule let them draw on different
summands.

**Honest caveat (recorded in the audit too).** That consequence follows because
the construction is organised by isospin, and `pp`/`nn` are isospin conjugates —
so *any* isospin-covariant weighting is charge-symmetric. The content is that the
production `σ`-vs-`σ⁻¹` assignment is **not** isospin-covariant, which is exactly
the diagnosed CSB defect; it is not an independent coincidence.

-- Ref: [leitner2026] folio/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md
-/

namespace QOU.BraidsAndKnots.ColorFlavorIsospinSelection

/-! ## Flavor-pair data -/

/-- The four nucleon-pair channels. -/
inductive NucleonPair
  | pp | nn | pnSym | pnAlt
  deriving DecidableEq, Repr

/-- Total isospin of each channel: the triplet `I=1` is exchange-symmetric, the
singlet `I=0` exchange-antisymmetric. -/
def NucleonPair.isospin : NucleonPair → ℕ
  | .pp => 1 | .nn => 1 | .pnSym => 1 | .pnAlt => 0

/-- Dimensions of the isospin summands of `I=½ ⊗ I=½`. -/
def isospinSummandDims : List ℕ := [3, 1]

/-- **The flavor pair space decomposes as `3 + 1 = 2 × 2`.** -/
theorem isospin_pair_dims : isospinSummandDims.sum = 2 * 2 := by decide

/-! ## The color systems the rule can select -/

/-- The two admissible color systems: `Alt² = T₁` (for `I=1`) and
`Sym² = A ⊕ H` (for `I=0`). -/
inductive ColorSystem
  | altT1        -- `T₁`, dim 3 — forced, no residual freedom
  | symAH        -- `A ⊕ H`, dim 6 — a 1-parameter mix
  deriving DecidableEq, Repr

/-- **The selection rule.** Exchange-symmetric flavor (`I=1`) pairs with the
antisymmetric color summand and vice versa — the only two couplings with overall
exchange antisymmetry. -/
def select : NucleonPair → ColorSystem :=
  fun p => if p.isospin = 1 then ColorSystem.altT1 else ColorSystem.symAH

/-- **CONJECTURE (§3b-cond, no instance).** The two-nucleon interface carries
definite antisymmetry under simultaneous exchange of color-sheet and flavor
labels — the hypothesis the selection rule rests on.

**Corrected 2026-08-09.** This docstring used to end "so it is not vacuously
satisfiable". That is **false**, and `trivially_inhabited` below exhibits the
one-line witness `⟨select, rfl⟩`. The class fixes its own field to a definition
already in scope, so as a *mathematical* object it constrains nothing.

What is genuinely open is the physics, and the distinction matters: the class
does not assert "some coupling satisfies this"; it asserts "the coupling the
**physical** interface induces is `select`". No Lean instance can establish
that, and none is registered, so every consequence below remains conditional —
just not for the reason previously given. -/
class InterfaceExchangeAntisymmetry where
  /-- The interface's induced color system for each nucleon-pair channel. -/
  coupling : NucleonPair → ColorSystem
  /-- The exchange-antisymmetry constraint: the coupling is the selection rule. -/
  antisymmetry_forces_select : coupling = select

/-- **The conjecture class is trivially inhabited** — the retraction, machine-
verified rather than asserted.

`⟨select, rfl⟩` witnesses it. So the four theorems below are not "conditional on
an open mathematical hypothesis"; they are conditional on a *physical
identification*, and as mathematics they are `rfl` on a two-line table.

Deliberately a `theorem` about `Nonempty`, **not** an `instance`: registering an
instance would let typeclass resolution discharge `[InterfaceExchangeAntisymmetry]`
automatically and silently turn every conditional consequence below into an
unconditional theorem about `select` — true, worthless, and easily misread as the
physics having been proved. Stating inhabitation as a `Nonempty` fact records it
without changing what anything downstream depends on. -/
theorem trivially_inhabited : Nonempty InterfaceExchangeAntisymmetry :=
  ⟨⟨select, rfl⟩⟩

/-! ## Consequences (conditional on the class) -/

/-- **`W` is charge-symmetric between `pp` and `nn`** — the falsifiable
consequence. Both are `I=1`, so the interface coupling assigns them the *same*
color system; the weight tensor cannot distinguish them. -/
theorem charge_symmetric_pp_nn [h : InterfaceExchangeAntisymmetry] :
    h.coupling .pp = h.coupling .nn := by
  rw [h.antisymmetry_forces_select]; rfl

/-- The like-nucleon channels are forced onto `T₁`, which carries **no residual
freedom** (its normalised weights are `0` on same-color pairs and `1/6` on each
different-color pair). So the `I=1` sector of `W` is fully determined. -/
theorem like_nucleon_forced_to_altT1 [h : InterfaceExchangeAntisymmetry] :
    h.coupling .pp = ColorSystem.altT1 ∧ h.coupling .nn = ColorSystem.altT1 := by
  rw [h.antisymmetry_forces_select]; exact ⟨rfl, rfl⟩

/-- Only the `I=0` (deuteron) channel retains freedom — the `A`/`H` mix. So the
selection rule leaves exactly **one** open parameter. -/
theorem only_singlet_channel_free [h : InterfaceExchangeAntisymmetry] :
    h.coupling .pnAlt = ColorSystem.symAH ∧
    h.coupling .pp = ColorSystem.altT1 ∧
    h.coupling .nn = ColorSystem.altT1 ∧
    h.coupling .pnSym = ColorSystem.altT1 := by
  rw [h.antisymmetry_forces_select]
  exact ⟨rfl, rfl, rfl, rfl⟩

/-- **The symmetric `pn` channel sits with the like-nucleon pairs, not with the
deuteron.** A non-obvious consequence: `pn` splits, with its `I=1` component
weighted like `pp`/`nn` and only its `I=0` component free. -/
theorem pn_symmetric_groups_with_like_nucleons
    [h : InterfaceExchangeAntisymmetry] :
    h.coupling .pnSym = h.coupling .pp ∧ h.coupling .pnSym ≠ h.coupling .pnAlt := by
  rw [h.antisymmetry_forces_select]
  exact ⟨rfl, by decide⟩

end QOU.BraidsAndKnots.ColorFlavorIsospinSelection
