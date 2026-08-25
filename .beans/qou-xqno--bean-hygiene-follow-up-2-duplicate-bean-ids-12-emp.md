---
# qou-xqno
title: 'Bean hygiene follow-up: 2 duplicate bean IDs + 12 empty-title beans'
status: completed
type: task
priority: low
created_at: 2026-08-10T12:59:09Z
updated_at: 2026-08-23T00:00:00Z
---

<!-- recovered 2026-08-23 from orphaned file `qou-xqno--bean-hygiene-follow-up-2-duplicate-bean-ids-12-em.md` (no front-matter; invisible to the tracker) -->

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

---

## RESOLVED 2026-08-23 — and two of this bean's own claims were wrong

Both were wrong in the same direction: they under-stated the defect and, in the
`sp06` case, the recommended action would have destroyed data.

### "Twelve beans have an empty `title:`" — no; twelve have NO FRONT-MATTER

Measured over 3833 files: empty `title:` = **0**. Files whose front-matter a
parser cannot read = **12**. "Empty title" is what a lenient parser *reports*
for such a file; it is not what is wrong with it. Those 12 carried no id, no
status and no title, so they were invisible to `beans list` and therefore to the
§4 idle-backlog policy that walks it — while looking, to `git`, like healthy
tracked beans.

That makes this bean's closing judgement — *"cosmetic unless something parses on
title"* — the wrong call. Between them the 12 held ~700 lines of real work:
`qou-mpq5` (`status: todo`, a Mathlib Schur–Weyl gap assessment), `qou-pvem` (a
measured, still-actionable `DEAD_TOL` precision fix), the 152-line s5-so3
keystone probe record with a REFUTED finding, and the `sp06` record below.

Four distinct shapes, each needing a different repair:

| shape | count | cause |
|---|---|---|
| no front-matter at all | 9 | `cat >>` to a GUESSED slug |
| front-matter present but body PREPENDED above it | 1 (`qou-mpq5`) | append landed at the top |
| opening `---` missing, fields + closing `---` present | 1 (`s8ho`) | delimiter dropped |
| never had front-matter | 2 (`xbz1`, `xbz2`) | notes dropped into `.beans/` |

**Root cause of the 9.** `beans create` slugs a title by dropping punctuation:
`placeholders/TODOs` → `placeholderstodos`, `n=2` → `n2`, `s5-so3` → `s5so3`. An
agent reconstructing the path by hyphenating misses by one character, and
`cat >>` silently creates a new file beside the real bean. Nothing errors.

### "`sp06`: same bean re-slugged; one file is stale" — no, and deleting one would have lost 327 lines

The two `sp06` files are not one bean re-slugged. One is the real bean (proper
title, `status: todo`, `parent: sp00`, 14 lines). The other has an **empty**
title and carries a 327-line session record of the whole
`specht_exhausts_irreducibles` route — three `MathlibExt` modules, two dead ends
documented as not-to-repeat, and a CLOSED verdict.

Verified before merging rather than taken on faith: `SpechtClassification.lean`
has **0 code-level `sorry`** — its 13 grep hits are all the word inside
docstrings, which a naive `grep -c '\bsorry\b'` reports as 13 — and all three
claimed `MathlibExt` modules exist. So the record is accurate and the *other*
file's `status: todo` was the wrong half. Merged into the real bean and its
status corrected to `completed`.

The lesson is the one this bean already states about counts, applied to
dispositions: **do not resolve a duplicate by picking the file that looks
canonical.** Read both. Here the canonical-looking one was the stale one.

### `qou-x4qm` — resolved as this bean recommended

Two unrelated beans that collided on a random id. The older three-generation
bean keeps `qou-x4qm`; the newer citation task re-issued as `qou-5isd`.

### Durable fix

[`scripts/check-beans.sh`](../scripts/check-beans.sh) validates all four shapes
plus duplicate ids, and exits 1 so it can gate a commit. It found three real
problems beyond the 12 and, in writing, two bugs of its own — both recorded in
its comments: a `[a-z0-9-]` id pattern that rejected the seven legitimate
mixed-case ids (`qou-vdvE`, `qou-dodK`, …), and a `printf | grep -q` under
`set -o pipefail` that reports FAILURE on a successful match, because `grep -q`
exits at the first hit and `printf` takes SIGPIPE (141). The second is
intermittent by construction and hit exactly 2 of 3825 files.

Note for anyone re-running the earlier duplicate-id scan in this bean: it also
used `[a-z0-9-]`, so it could not see a mixed-case duplicate id. The validator
now can, and reports none.
