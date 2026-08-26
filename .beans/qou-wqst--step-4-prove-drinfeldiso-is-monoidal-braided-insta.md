---
# qou-wqst
title: 'Step 4: prove drinfeldIso is monoidal (braided instance)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-26T18:00:28Z
updated_at: 2026-08-26T18:37:58Z
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
