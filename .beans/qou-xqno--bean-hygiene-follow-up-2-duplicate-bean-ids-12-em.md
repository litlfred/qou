
## Measured state (origin/main @ 0763606e4f, 3,125 beans)

Two IDs are used by more than one file:

- `qou-x4qm` — `gap-three-generation-structure-why-three-copies-of`
  and `cite-9504020v1pdf-at-qouqouqbetacyclicdilogpentago`.
  Two genuinely different beans that collided on a random ID.
- `sp06` — `c-specht-exhausts-irreducibles-spechtclassification`
  and `...spechtclassificatio` (slug truncated one char shorter).
  Same bean re-slugged; one file is stale.

Twelve beans have an empty `title:`.

Five titles are carried by more than one bean (2 copies each): the
`Verify proof using scripts/lean-verify.sh` / `Run QA script against
proposed changes` / `Vacuity fix: lean/QOU-root (8 defects)` /
`PROVE(lean): instance:archimedean_agreement` / `KSEL2-ID follow-up`
pairs. These predate the 2026-08-04 flood and are unrelated to it.

## Correction to the number previously reported

PR #4922's body and the session chat said "64 further bean ID
collisions". That was **inferred, not measured** — 79 colliding IDs
counted before the dedupe, minus the 15 known to involve a real bean.
The inference was wrong: most of the 79 were collisions *between two
duplicate-cluster beans*, so deleting the duplicates cleared 77 of 79,
not 15. The real remaining count is **2**.

Lesson worth keeping: a count carried forward by arithmetic across a
mutation is not a measurement. Re-run the query against the new state.

## Why this is low priority

`sp06` is a stale-slug artifact with one file to delete. `qou-x4qm` needs
one of the two beans re-issued under a fresh ID. The empty-title beans
are cosmetic unless something parses on title. None of it starves the
idle-backlog policy the way the 14,688 duplicates did.
