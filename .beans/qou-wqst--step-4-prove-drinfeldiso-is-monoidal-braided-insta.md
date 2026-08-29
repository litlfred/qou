---
# qou-wqst
title: 'Step 4: prove drinfeldIso is monoidal (braided instance)'
status: completed
type: task
priority: normal
created_at: 2026-08-26T18:00:28Z
updated_at: 2026-08-26T20:06:55Z
---


## Open, statement pinned, route identified (2026-08-26)

The statement typechecks (see qou-ezas). No cheap tactic reaches it: simp with
the definitions unfolded, aesop_cat, monoidal, and a rightDualIso extensionality
guess all fail. Expected -- this is the substantive content of the tranche.

### The route to try (not yet attempted)

UNIQUENESS OF DUALS, the technique that has worked repeatedly in this arc.
Both sides are maps X tensor Y -> Xdd tensor Ydd. Pair both against the
evaluation and use

    whiskerRight_evaluation_injective   (already proved, PivotalCategory.lean)
    Function.Injective (fun g : A -> B => (g |> B') >> eps_ B' B)

with B := Xdd tensor Ydd and B' := Ydual tensor Xdual, whose exact pairing is

    tensorExactPairing (Ydual) (Ydd) (Xdual) (Xdd)
      : ExactPairing (Ydual tensor Xdual) (Xdd tensor Ydd)

i.e. supplied by the module qou-l8az just closed. So the ingredients all exist;
what remains is computing both sides against eps, which is string-diagram work
of the same genre as the snakes.

### Why this is the last hard step

Everything downstream is plumbing: with monoidality proved, the class field is
added, pivotalOfBraided supplies it, and Barrett-Westbury's "any braided pivotal
category satisfies the extra spherical condition" becomes applicable -- which is
what the whole tranche was for.



## Tooling built toward it (2026-08-26); the theorem itself is still open

Three lemmas added to PivotalCategory.lean, all sorry-free, all missing from
Mathlib (which carries rightDualIso and rightDualIso_id and nothing else):

  rightDualIso_hom_evaluation  the evaluation identity characterising the
                               comparison
  rightDualIso_hom_unique      ANY map commuting with the evaluations IS
                               rightDualIso -- turns "construct the map" into
                               "check one identity"
  rightDualIso_hom_trans       comparisons compose

The reduction of monoidality also works: applying
whiskerRight_evaluation_injective with Y' := Ydual tensor Xdual (whose pairing
tensorExactPairing supplies) typechecks and reduces the goal to an
evaluation-level identity.

### Still open, and why

After that reduction nothing automatic closes it -- 5 further routes tried
(simp with every relevant definition unfolded, simp with
rightAdjointMate_comp_evaluation, aesop_cat, monoidal, and an extensionality
guess). It needs the same hand-written regrouping the snakes did.

### The most promising route now

Use rightDualIso_hom_unique on BOTH sides: show each of
  drinfeldIso (X tensor Y) >> tensorDoubleDualIso X Y
  drinfeldIso X tensorHom drinfeldIso Y
commutes with the evaluations of the two pairings of Ydual tensor Xdual, hence
each equals the same rightDualIso, hence they are equal. This replaces one hard
computation with two checks of a single identity each, which is what uniqueness
buys.

Caution recorded: LHS is a composite of a rightDualIso with tensorDoubleDualIso,
and tensorDoubleDualIso is built from rightDualMapIso -- which is NOT itself a
rightDualIso. So rightDualIso_hom_trans does not apply to it directly; that was
my first thought and it does not work.


## 2026-08-26 — the target was FALSE; retracted and re-aimed

`drinfeldIso` is natural but **not monoidal**, so a braided right-rigid category is not
pivotal in the monoidal sense.  Two independent arguments, both in the
`QOU/MathlibExt/PivotalCategory.lean` module docstring:

1. Hopf-algebraic — the Drinfeld element satisfies `Δ(u) = (u⊗u)(R₂₁R)⁻¹` (Kassel XIV.6),
   so `u` is grouplike iff the monodromy is trivial.
2. Diagrammatic — expanding `β_{X⊗Y, Yᘁ⊗Xᘁ}` by the two hexagons leaves two crossings
   after the caps absorb the other two.  Counting **with the orientation reversal at each
   cap**, they have the same sign: the loops are Hopf-linked.  The discrepancy is the
   monodromy `(β_ X Y).hom ≫ (β_ Y X).hom`.

I nearly concluded the opposite: read naively, "X over Yᘁ" and "Y over Xᘁ" look like an
over/under pair that cancels by R2.  That reading ignores the cap orientation and is wrong.

Corrected target: **`pivotalOfRibbon`** — the twisted map `θ_X ≫ drinfeldIso X` is monoidal,
because the balancing axiom `θ_{X⊗Y} = β β (θ_X ⊗ θ_Y)` is exactly the monodromy, and
`θ_X ⊗ θ_Y` commutes with it by braiding naturality.

**Do NOT add the monoidality field to `PivotalCategory` while `pivotalOfBraided` is an
instance** — the field would be unprovable there, and it is unprovable because it is false.
This supersedes bean `qou-ezas` as scoped.

Landed this pass: `rightDualIso_tensorExactPairing` (the formal half — the dual comparison of
a tensor is the tensor of the comparisons, order reversed), sorry-free, lean-direct exit 0.

Remaining gap: in a braided rigid category, `β_{X, Yᘁ}` is the bent-round *inverse* braiding
`β_{Y,X}⁻¹`.  Mathlib lacks it; it is a snake-identity computation.  Everything else then
follows from it plus `rightDualIso_tensorExactPairing`.



## 2026-08-26 (later) — the diagrammatic argument is now PROVED, not argued

The retraction note's string-diagram argument has been replaced by Lean:

* `braiding_slide_cap_right/_left`, `braiding_slide_cup_right/_left` and
  `braiding_slide_cap_right_inv` (QOU/MathlibExt/BraidedSlide.lean) — a strand crossing a
  cap or cup can be pushed off, at the cost of braiding past EACH leg.
* `evaluation_swap_tensor_step`, `braiding_cap_monodromy`,
  `evaluation_swap_tensor_eq_monodromy`, `rightDualIso_swap_tensor`
  (QOU/MathlibExt/BraidedTensorDual.lean) — swap-then-tensor and tensor-then-swap differ by
  exactly `((β_ X Y).hom ≫ (β_ Y X).hom)⁻¹`.  **The comparison is the INVERSE monodromy.**
* `rightDualIso_tensorExactPairing` (RigidTensorDual.lean) — the formal half.

All sorry-free, `#print axioms` clean.

**What is still NOT Lean-proved, and cannot be schematically**: the negative headline
"drinfeldIso is not monoidal".  It is false in general but TRUE in symmetric categories, so
there is no schematic refutation.  It follows from `rightDualIso_swap_tensor` in any category
with `M ≠ 𝟙`; exhibiting one is not formalised here (FGModuleCat is symmetric).

Remaining for pivotalOfRibbon: assemble `rightDualIso_swap_tensor` +
`rightDualIso_tensorExactPairing` into the monoidality of `θ ≫ drinfeldIso`, using
`twist_tensor` to cancel the monodromy.  The sign is now known, so the direction is
determined: the balancing axiom supplies `β β`, the comparison supplies its inverse.



## LANDED 2026-08-26 — PR #5848 merged as bfdedc68e6

Target retracted, replaced, and both halves proved:

* `rightDualIso_swap_tensor` — the comparison is the INVERSE monodromy
* `twist_drinfeld_monoidal` — and `θ ≫ drinfeldIso` IS monoidal, so ribbon is the right hypothesis

Remaining, and NOT part of this bean: identify `pivotorTensor` with
`drinfeldIso (X ⊗ Y) ≫ tensorDoubleDualIso`.  Needs a pairing transported along
`tensorRightDualIso` (Mathlib's `exactPairingCongrLeft`) plus a `rightDualIso`
compatibility lemma nobody has written.  Until then a `PivotalCategory` monoidality
field cannot be phrased — see qou-ezas, which stays blocked for that reason.
