---
# qou-wqst
title: 'Step 4: prove drinfeldIso is monoidal (braided instance)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T18:00:28Z
updated_at: 2026-08-26T18:44:09Z
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
