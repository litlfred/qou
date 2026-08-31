import Mathlib.Tactic

/-!
# `QOU.FluidDynamics.helicity_conservation` — intentionally empty; the formalisation lives in the content-block sibling

This module used to hold `HelicityConservationContext` together with a
projection that discharged all four manuscript claims from that class's own
fields.  Both are removed (2026-08-31).

**Why the declaration was empty**, and this one is a stronger case than most.
`HelicityConservationContext` carried `helicity_conserved : Prop` as a *field*
and `conservation_active : helicity_conserved` as a second field proving it —
so the instance chose the hypothesis **and** its proof.  Taking
`helicity_conserved := True`, `conservation_active := trivial`,
`knot_equiv := True`, `H_q := fun _ => 0` and every scalar `0` satisfies every
field, and `helicity_conservation` returned the four implications applied to
that self-supplied proof.  A `[HelicityConservationContext]` binder therefore
assumed nothing.  The file's own docstring said as much: *"the substantive
mathematical content is carried by the context-class axioms"*.  AGENTS.md
§3b-cond item 5 (bean `qou-z9ws`).

**Why removal costs nothing readable.**  Three facts, all measured:

1. The content block's `lean.ref` is
   `qou:QOU.FluidDynamics.helicity_conservation`, and per AGENTS.md §0a
   resolution checks the **sibling first** — so the block already resolves to
   [`fluid-dynamics/helicity-conservation.lean`](../../fluid-dynamics/helicity-conservation.lean),
   never to this file.
2. That sibling now carries a real derivation.  `helicity_conservation` there
   takes the md's *definition* of `ℋ_q`, the Călugăreanu–White–Fuller relation
   and the Moffatt–Ricca self-helicity identity as hypotheses on
   caller-supplied filaments, and **derives** both the writhe/twist/linking
   decomposition (md part 2) and time-independence (md part 1) — neither is a
   field of anything.  What it does not establish, it says: `hdef` is where
   the quantum Euler equation would enter, and md parts (3) and (4) are not
   encoded.
3. **Nothing imports this module** and nothing else in `content/` names the
   class (measured 2026-08-31 across every `.lean` in the tree).

So the declaration was unreachable from its own block, unreachable by import,
and vacuous where it stood.

The file is kept rather than deleted so that the `lean.ref`'s second
resolution candidate —
`<lakeRoot>/QOU/FluidDynamics/helicity_conservation.lean` — still exists as a
real path.

Bean `qou-z9ws`; `docs/audits/2026-08-30-the-remainder-is-vacuous-not-open.md`.
-/
