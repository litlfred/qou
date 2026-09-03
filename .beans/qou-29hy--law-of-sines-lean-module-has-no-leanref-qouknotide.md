---
# qou-29hy
title: 'law-of-sines Lean module has no lean.ref: QOU.Knot.IdealTetLawOfSines uncited corpus-wide'
status: completed
type: task
priority: normal
created_at: 2026-08-25T16:32:33Z
updated_at: 2026-08-25T18:29:53Z
---

## Measured 2026-08-25 (fresh container, corrects my own earlier claim)

I previously reported the law of sines as "genuinely uncovered — nothing on main
cites norm_eq_sin_div_sin". **That was wrong on the content half.** Measured:

- `mass-theory/ideal-tetrahedron-relabelling-invariance.md:32` carries a whole
  `## The law of sines` section, and its `.ts:11` `defines: ["law-of-sines"]`.
- `mass-theory/kummer-bloch-wigner-identity.md:18` states the identity
  `‖z‖ = sin θ₂ / sin θ₃` and explains its role in the radial argument.

So the law of sines HAS paper presence. Authoring a new block for it would
duplicate existing prose — do not.

**The real gap is narrower and is purely wiring.** `grep -rn IdealTetLawOfSines
content/ --include=*.ts --include=*.md` returns **zero**: the proved module
`content/quantum-observable-universe/lean/QOU/Knot/IdealTetLawOfSines.lean`
(9 theorems incl. `norm_eq_sin_div_sin` at :118) is cited by no `lean.ref`
anywhere in `content/`.

**Why it is not a one-liner.** `lean.ref` is singular. The two blocks that
discuss the law of sines already point their refs at their own claims
(`QOU.MathlibExt.IdealTetrahedron.volume_rotate` and
`QOU.Knot.KummerRadial.kummer`), and neither should be repointed — those are
the claims those blocks actually make. Wiring `norm_eq_sin_div_sin` therefore
needs an authoring decision: give it its own `lemma` block, or leave the module
as a support lemma reached through `KummerRadial`.

Being a standalone library `.lean` with no `.qa.json` sidecar, it is invisible
to every per-block checker — nothing but an agent will notice it drift.


## RESOLVED 2026-08-25 — support-lemma disposition (owner call)

Owner chose "support lemma": no new content block. Verified the premise
rather than assuming it — `KummerRadial.lean:41` imports the module and its
docstring names `log_sin_sub_log_sin` as the mechanism.

Enforcement added instead of a block: all 9 declarations pinned in
`scripts/lean-axiom-guard.py`, measured by `#print axioms` against a
lean-direct build of the 3-module cone. All return
`[propext, Classical.choice, Quot.sound]` — zero `sorryAx`.
`--filter IdealTet` green.

Full guard still rc=2 on missing/stale `QOU.Mathlib*` oleans — pre-existing
`qou-agrd`, stash-proved identical with and without these entries.

Note for the next agent: the lean-direct oleans built here (3 modules) were
NOT seeded to a `lake-cache/*` addon branch. Doing so would save the ~40s
rebuild; skipped as out of scope.
