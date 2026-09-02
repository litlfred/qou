import Mathlib.Tactic

/-!
# `QOU.Braiding.r_matrix_braiding_structure` — intentionally empty; the formalisation lives in the content-block sibling

This module used to hold `RMatrixBraidingContext` together with a projection that
discharged the Yang–Baxter equation from that class's own fields.  Both are
removed (2026-08-31).

**Why the declaration was empty.**  The class carried `V3`, `comp`, `R12`, `R13`,
`R23` and the Yang–Baxter equation itself as *fields*, and
`r_matrix_braiding_structure` returned `ctx.claim_yang_baxter` — so a
`[RMatrixBraidingContext]` binder assumed nothing and the declaration asserted
nothing.  The old docstring was candid about the projection (*"Assumed, not
derived here"*) and even named the risk (*"`comp`, `R12`, `R13`, `R23` are
arbitrary context data and YBE fails for a general assignment"*), but drew the
wrong conclusion from it: because the data are the *instance's* to choose, the
statement is not conditional on anything.  Measured — `V3 := ℕ`,
`comp := (· * ·)`, `R12 := 2`, `R13 := 3`, `R23 := 5` discharges
`claim_yang_baxter` by `ring`.  It is the `proof-no-self-assuming-projection`
shape of AGENTS.md §3b-cond item 5 (bean `qou-z9ws`).

**Why removal costs nothing readable.**  Three facts, all measured:

1. The content block's `lean.ref` is `qou:QOU.Braiding.r_matrix_braiding_structure`,
   and per AGENTS.md §0a resolution checks the **sibling first** — so the block
   already resolves to
   [`braids-and-knots/r-matrix-braiding-structure.lean`](../../braids-and-knots/r-matrix-braiding-structure.lean),
   never to this file.
2. That sibling carries what there is to carry: `RMatrixEigenData` and
   `su2_fundamental_r_matrix` (the Hecke eigenvalue data, real content), plus
   `YangBaxterHolds` / `BraidRelationHolds` / `r_matrix_braiding_structure`,
   which **name** the manuscript's two claims over caller-supplied data rather
   than asserting them.  That is the honest disposition here: the `.md` itself
   says *"The underlying `R`-matrix theory is standard"*, for the universal
   `R`-matrix of `U_q(𝔰𝔲(2))` — an object this development never constructs.
3. **Nothing imports this module** and nothing else in `content/` names the
   class (measured 2026-08-31 across every `.lean` in the tree).

So the declaration was unreachable from its own block, unreachable by import,
and vacuous where it stood.

The file is kept rather than deleted so that the `lean.ref`'s second resolution
candidate — `<lakeRoot>/QOU/Braiding/r_matrix_braiding_structure.lean` — still
exists as a real path.

Bean `qou-z9ws`; `docs/audits/2026-08-30-the-remainder-is-vacuous-not-open.md`.
-/
