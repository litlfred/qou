---
# qou-e4eu
title: '19 Lean -- Ref: keys resolve to nothing — 7 of them are not citations at all'
status: todo
type: bug
priority: high
created_at: 2026-08-31T05:06:11Z
updated_at: 2026-08-31T05:18:33Z
---

`folio-assistant/content/pipeline/validate-references.ts` is the only checker
that cross-checks Lean `-- Ref: [key]` against `content/schema/references.ts`.
**It has never been runnable in this folio**, so its surface has never been
measured. Made runnable via `scripts/run-validate-references.ts`; first run
reports **19 errors, 173 warnings, 411 info** over 367 Lean / 189 LaTeX / 345
`.ts` citations.

## Why it never ran — TWO stacked blockers, not one

1. **No registry.** It imports `references` from the DI shim at module scope
   and touches it in the schema loop before anything else, so running it
   directly throws immediately: *"Reference registry not configured."* No
   partial run.
2. **`requirePaper`.** Past that, it throws again at line 133: *"5 papers found
   (bach2013-double-slit, fred2005-formal-groups, quantum-observable-universe,
   unital-groebner-bases, visualizer) — name one explicitly."* It accepts
   `--paper`, which nothing passed.

Nothing invokes it either — no workflow, no script, no `package.json` entry;
every other mention of the name in the tree is prose describing what it would
do. Same defect family as `qou-cite`/`qou-idxg`.

## The 19, and they are two different things

**Twelve are real works missing from the bibliography** — all standard,
identifiable, and attached to `sorry` justifications:

`frenkel2020`, `koroteev-zeitlin2022`, `stanley1999ec2`, `rockafellar1970`,
`schrijver1986`, `murakami1996`, `neumann1985`, `bjorner-brenti2005`,
`wielenberg1978`, `ratcliffe2006`, `murakami2013`, `ggmw2020`.

**Seven are not citation keys at all** — a different convention leaking into
the citation slot:

`audit`, `probe`, `probe-w`, `probe-j`, `probe-q`, `bean`, `metallichierarchy`

concentrated in `QOU/AlgebraicSubstrate/MetallicLPIdentities.lean` and
`QOU/KnotTheory/MetallicPiecewise.lean`. An author used `-- Ref:` to point at
an audit doc, a probe script, or a bean. Those are legitimate things to point
at; `-- Ref:` is not the slot for them, because the slot means "the published
work justifying this `sorry`".

## Why this matters more than `qou-cite`'s ten

`qou-cite`'s ten orphaned `cites[]` keys support no written claim. **These do.**
AGENTS.md §1 makes `-- Ref:` the mandatory justification for a `sorry` — *"A
`sorry` without `-- Ref:` is always a review failure"* — so a `-- Ref:` naming
nothing is a `sorry` whose stated warrant does not exist. Seven of them name a
kind of thing that could never be a warrant.

## Next

- Add the twelve to `references.ts` (ordinary bibliography work, each is a
  well-known text).
- Decide what the seven should be: either a real citation, or `[manuscript]`
  per §1, or a non-`Ref:` comment form pointing at the audit/probe/bean.
- Wire `scripts/run-validate-references.ts` into the preflight so this cannot
  silently regrow.


## PARTIAL 2026-08-31 — 19 -> 13, and four "missing works" were never missing

Re-run after the fix: **13 errors** (was 19), 173 warnings, 411 info.

### The correction that saved six wrong entries

My plan was "add the twelve to `references.ts` — ordinary bibliography work".
That would have been wrong for a third of them. **Four of the twelve are already
held under a different id** — checked by matching TITLES against the module, not
by trusting the key:

| cited key | actually held as | title / author / year |
|---|---|---|
| `schrijver1986` | `schrijver1986theory` | *Theory of Linear and Integer Programming*, Schrijver, 1986 |
| `stanley1999ec2` | `stanley1999` | *Enumerative Combinatorics, Volume 2*, Stanley, 1999 |
| `neumann1985` | `neumann-zagier1985` | *Volumes of hyperbolic three-manifolds*, Neumann + Zagier, 1985 |
| `ratcliffe2006` | `ratcliffe` | *Foundations of Hyperbolic Manifolds*, Ratcliffe |

These are **key drift, not missing works**, so the fix is to repoint the Lean
`-- Ref:` to the held id. That is the *safe* kind of repointing — same title,
same author, same year — and it is the opposite of the `qou-cite` hazard, where
the near-misses are genuinely different papers.

**One caveat, stated because it is a real imprecision:** the held `ratcliffe`
entry is the **3rd edition (2019)**; the citation said 2006 (2nd ed), and cites
"§8 (fundamental domains and the volume of a quotient)". Same book, same author,
but section numbering could differ between editions. Repointed anyway on the
judgement that a live citation to the wrong edition of the right book beats a
key resolving to nothing — but it wants an eye on the §8 reference.

`neumann-zagier1985` was confirmed from the **held PDF itself**
(`library/1-s20-0040938385900047-main/`, whose doc-id is the Elsevier PII
`0040-9383(85)90004-7`): "WALTER D. NEUMANN and DON ZAGIER", p. 329 visible.

### Two genuinely absent, now added

- **`rockafellar1970`** — *Convex Analysis*, Princeton UP, Princeton Math.
  Series 28. Named in the citing comment ("Convex Analysis, Cor. 17.1.2").
  **No DOI asserted**: the Princeton reissue has one, but it was not verifiable
  from this sandbox and a guessed DOI is worse than none.
- **`bjorner-brenti2005`** — *Combinatorics of Coxeter Groups*, GTM 231,
  Springer. **DOI `10.1007/3-540-27596-7` taken from the citing Lean comment,
  which carries it inline** — the citing author's own record, not my recall.

Bibliography: 810 -> 812 entries.

### The 13 that remain

**Seven are not citations** (unchanged): `audit`, `probe`, `probe-w`, `probe-j`,
`probe-q`, `bean`, `metallichierarchy`. Needs a convention call.

**Six need external lookup**: `frenkel2020` (arXiv:2007.11786),
`koroteev-zeitlin2022` (arXiv:2108.01557), `murakami1996`, `murakami2013`,
`wielenberg1978`, `ggmw2020`. The first two carry arXiv IDs in the Lean, so they
are one fetch from settled — **but arxiv.org is blocked by this sandbox's egress
proxy**, and neither is in `library/`. That is why they are open, not because
they are hard.

`ggmw2020`'s Lean comment expands it as "Gukov–Garoufalidis–Mariño–Wheeler
(2020), eq (161)". `library/` holds four candidate resurgence papers; note the
expansion may itself be wrong (GGMW is usually Garoufalidis–**Gu**–Mariño–
Wheeler), so do not resolve it from the initialism alone.

### Lean verification

Five files edited (comment-only). Four `lean`-direct **exit 0**. The fifth,
`FiveTwoVolumeChord.lean`, exits 1 — **and it is not this change**: the
unmodified file fails identically, on
`FiveTwoNinthPower.olean ... does not exist`. That module's **source exists** on
this branch and on `main`; only its olean is absent from the restored cache,
which was seeded before it landed. Environmental gap, nothing broken in the
corpus.
