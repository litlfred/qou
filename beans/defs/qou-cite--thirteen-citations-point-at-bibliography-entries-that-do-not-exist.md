---
# qou-cite
title: 13 citations point at bibliography entries that do not exist — the check had never run
status: todo
type: bug
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:55:00Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-mub3
---

`cites-resolve` — the check that validates every content block's `cites[]`
against `content/schema/references.ts` — **has never run in this folio**, and its
first run finds **13 unresolved keys across 10 blocks**.

## Why it never ran

Two layers, and the second was invisible behind the first:

1. Until `folio-assistant#150` (merged 2026-08-30), `validate-references` and
   eight sibling scripts threw on `requirePaper()` in a multi-paper folio —
   `qou-idxg`.
2. **Independently**, `scripts/run-validate.ts` never called
   `configureReferenceRegistry`. It *imports* `references.ts` (to check it
   parses — bean `qou-3vgs`) and then does not hand it to the platform. So
   `cites-resolve` no-ops and says so, in an `ℹ` line that has been in every
   run's output for months:

   > `ℹ [(bibliography)]: no reference registry configured — cites-resolve did
   > not run, so cites[] entries were NOT validated against references`

   The gate announced its own absence on every run and nobody read it.

## The 13 keys

| key | cited by | held near-miss |
|---|---|---|
| `faddeev1996` | `inter-nucleon-channel-color-tube`, `pachner-pentagon-borromean` | `faddeev1994`, `faddeev1995` |
| `manuscript` | `categorical-proton`, `categorical-proton-properties` | — (see below) |
| `champanerkar-kofman-mullen2008` | `q-zero-stokes-region-identification` | `champanerkar2003` |
| `bokut1978` | `phi-q-tower-algebraic-stratification` | `bokut2001`, `bokut2005` |
| `feigin-hashizume2009` | `dim-master-pentagon` | — |
| `dimofte-gaiotto-gukov2014` | `mirror-3d-3d-correspondence` | `dimofte-gaiotto-gukov2013` |
| `terashima-yamazaki2011` | `mirror-3d-3d-correspondence` | `terashima-yamazaki2013` |
| `kashaev-tirkkonen2014` | `modular-s-transform-q-q-tilde` | `kashaev1995`, `kashaev1997` |
| `macdonald1971` | `quantum-langlands-dual` | `macdonald1995` |
| `lusztig1989` | `quantum-langlands-dual` | `lusztig1990`, `lusztig1993` |
| `frenkel-reshetikhin2002` | `quantum-langlands-dual` | `frenkel2004`, `frenkel2007` |

## `manuscript` is a different defect and should be fixed separately

`[manuscript]` is the placeholder AGENTS.md §1 prescribes for a Lean `-- Ref:`
when no published reference exists. It is **not** a bibliography entry, so using
it in a content block's `cites[]` can never resolve. Two blocks do. That is a
category error rather than a missing paper, and it is the one item on this list
that needs no research.

## DO NOT sweep the near-misses

The right-hand column is suggestive and is **not** a fix list. Some are probably
wrong-year typos of a held entry; others are plainly distinct works —
`macdonald1971` is *Spherical Functions on a Group of p-adic Type*, the held
`macdonald1995` is *Symmetric Functions and Hall Polynomials*; Lusztig 1989
(*Modular representations and quantum groups*) is not Lusztig 1990. **Repointing
a citation at a different paper is worse than a broken link** — it puts a claim
behind a source that does not support it, silently.

Each of the 13 needs checking against what the citing block actually claims.
That is per-citation research, not a rename sweep, and it is why this bean is
filed rather than fixed.

## What was done instead

`scripts/run-validate.ts` now configures the registry **under `--strict` only**.

- Default run: unchanged, `✓ Valid — 14`.
- `--strict`: `cites-resolve` runs and reports the 13, `✗ Invalid — 23`.

Configuring it unconditionally would take the default gate red for everyone on
an untriaged backlog. Gating it makes the check *runnable* — which it has never
been — without inflicting that. Once the 13 are resolved, move the call out of
the `if (strict)` and the check becomes permanent.

## Suggested order

1. `manuscript` ×2 — category error, no research needed.
2. The four with a same-author near-miss differing only in year
   (`dimofte-gaiotto-gukov`, `terashima-yamazaki`, `faddeev`, `champanerkar`) —
   check the citing claim, then either fix the year or add the work.
3. The rest — genuinely absent works needing real metadata.
4. Then un-gate.


--------

## VERIFIED 2026-08-31 — the gate fires; and the arithmetic that looked wrong is right

The commit that landed this (`f5ecea6e36`) said in its own message that one
thing was NOT confirmed: *that `--strict` under the GATED code actually fires
the check*. It does. Measured, three runs, platform `21498cc`:

| run | registry | verdict |
|---|---|---|
| default | not configured | `✓ Valid — 14` |
| strict, registry forced OFF (`if (false)`) | not configured | `✓ Valid — 288` |
| strict, as committed | configured | `✗ Invalid — 297` |

The committed strict run prints the line the gate was written to print —
`bibliography: 805 entries, parses; registry configured (cites-resolve ON)` —
and carries all 10 `Unresolved citations` lines with the same 13 keys.

### The 9-vs-10 discrepancy, resolved rather than waved past

297 − 288 = **9**, but there are **10** citation lines. That is one short, and
a one-off in a count is exactly the shape of a miscount, so it was chased
rather than rounded.

It is not a miscount. Configuring the registry *removes* an issue: the
`ℹ [(bibliography)]: no reference registry configured — cites-resolve did not
run` line, which is itself counted. Verified directly — the with-registry run
contains **zero** `ℹ` lines. So 288 − 1 + 10 = 297 exactly.

That self-announcement is the whole story of this bean in one line: the gate
reported its own absence on every run for months, was counted as an issue
every time, and nobody read it. It only stops being emitted at the moment it
stops being true.

### What the 288 is NOT

`--strict` also turns on `term-mention-coverage` (AGENTS.md §4c), a separate
pre-existing backlog of unwrapped glossary mentions. **288 of the 297 have
nothing to do with citations.** Do not quote 297 as the citation debt, and do
not read `Valid — 288` as an all-clear either: it is `Valid` only because
those are warnings.

**The citation debt is 13 keys across 10 blocks, unchanged.** Still not fixed
here, for the reason in the body above: repointing a citation at a
different paper is worse than a broken link.


## CORRECTED 2026-08-31 — "13 dead citations" is ONE number over TWO unrelated defects

I filed this bean, and the framing was wrong. Measured against the
bibliography module itself (`bun -e` importing `content/schema/references.ts`,
**810 entries**) rather than by grepping for a spelling:

### Class A — 10 orphaned `cites[]` keys, cited in NO prose

`faddeev1996`, `champanerkar-kofman-mullen2008`, `bokut1978`,
`feigin-hashizume2009`, `dimofte-gaiotto-gukov2014`,
`terashima-yamazaki2011`, `kashaev-tirkkonen2014`, `macdonald1971`,
`lusztig1989`, `frenkel-reshetikhin2002`.

**Every one appears ONLY in a `.ts` `cites[]` array. Zero appear in any `.md`
prose, and zero in any Lean `-- Ref:`.** Measured both ways: a bare grep for
the key across `--include=*.md`, and a grep for `\cite{...}` containing it,
both corpus-wide. So none of the ten supports a written claim — they are
`cites[]` metadata that no sentence draws on.

That materially changes the fix. It is **not** "the paper cites a work that
does not exist"; it is "a block's metadata lists further reading whose key was
never added". Nothing a reader sees is broken today.

### Class B — `manuscript`, a DOCUMENTED CONVENTION with no backing

Different defect entirely, and much larger. `AGENTS.md` §1 says: *"The `[key]`
must match an entry in `content/schema/references.ts` exactly. **If no
published reference exists, use `[manuscript]`**"*. Those two sentences are in
tension, and the corpus resolves it the wrong way:

- **`manuscript` is NOT an entry.** Absent from all 810.
- **4436 Lean `-- Ref: [manuscript]` sites use it**, exactly as §1 instructs.
- The work it means **is** held — `leitner2026`, `type: "manuscript"`,
  `note: "This manuscript"`.

So the two `cites[]` hits this bean counted are the visible tip of a
convention that instructs 4436 sites to use a key the same paragraph requires
to resolve.

### Why the count was one number

Class A is 10 keys across 8 blocks; class B is `manuscript` in 2 blocks, and
`faddeev1996` is cited by two blocks — giving 13 **citations** across 10
blocks. The arithmetic was right. The **framing** was wrong: one of those
"citations" is a corpus-wide convention failure and the other twelve are
dormant metadata.

### What I did NOT do

Research the ten. Still the right call, and the reason is now confirmed
against the held set rather than asserted: the near-misses are mostly
**distinct works**. `macdonald1971` *Spherical Functions on a Group of p-adic
Type* vs held `macdonald1995` *Symmetric Functions*; `dimofte-gaiotto-gukov2013`
(held) and a 2014 companion are separate papers, as are
`terashima-yamazaki2013` (held) and a 2011 one. Repointing any of these at its
near-miss would silently attribute a claim to the wrong paper.

Class B is a **decision, not research**, and is framed for the owner rather
than actioned unilaterally: an alias entry would make the documented
convention work at all 4436 sites with a one-entry change, but would put the
same work in the bibliography twice.


## CORRECTED AGAIN 2026-08-31 — Class B was overstated; the Lean layer is FINE

The Class B analysis above says `manuscript` is *"a convention that instructs
4436 sites to use a key the same paragraph requires to resolve"*, and I put a
decision to the owner on that basis, recommending an alias entry. **Both were
wrong, and the evidence was one grep away.**

`validate-references.ts`, the Lean cross-checker, lines 171-172:

    // Skip cross-paper refs (paper-dir:label format) and manuscript self-refs
    if (!referenceMap.has(key) && key !== "manuscript" && !key.includes(":")) {

**`manuscript` is explicitly exempted, deliberately, with a comment saying so.**
Confirmed by running the checker: `manuscript` errors = **0** of 19. The 4436
Lean sites are working exactly as designed. AGENTS.md §1 is not in tension with
itself in practice — the checker implements the carve-out §1 implies.

### What the real defect is — much smaller, and obviously fixable

`cites-resolve` (`folio-assistant/schemas/constraints.ts:986-990`) does the
same job for `.ts` `cites[]` and has **neither** carve-out:

    const missing = (block.cites as string[]).filter((c) => !ctx.allRefIds!.has(c));

No `manuscript`, no `key.includes(":")`. So two checkers over the same key
conventions disagree, and only the newer one flags the sanctioned key.

**The fix is one condition in `cites-resolve`, matching the precedent already
in the sibling checker** — not an alias entry (which would duplicate the work
in the bibliography), and certainly not a 4436-site sweep. It also picks up the
cross-paper `:` carve-out, which `cites-resolve` is likewise missing; nothing
exercises that today, but a qualified `paper-dir:label` in a `cites[]` would
false-positive the same way.

That change is in **folio-assistant**, not this repo.

### The residue

With Class B correctly scoped, `qou-cite` is: **10 orphaned `cites[]` keys
supporting no prose** (Class A, unchanged) plus **2 false positives from a
missing carve-out**. Neither is a broken citation in the paper.

The genuinely load-bearing citation defect found while checking this is a
different bean: `qou-e4eu`, 19 dead Lean `-- Ref:` keys, 7 of which are not
citations at all.


## Recovered 2026-09-06 from a duplicate-ID file (`qou-cite--13-citations-point-at-bibliography-entries-that.md`, no front matter; merged here and deleted)

## Re-measured 2026-09-04 — 13 keys is now 4, and the gate's status is different

**Do not act on the table above; it is stale in both directions.** Re-measured by
**importing** `content/schema/references.ts` (827 entries) rather than grepping
for a spelling, which is the method this bean's own successor comment in
`scripts/run-validate.ts` recommends:

| key | status now | citing blocks left |
|---|---|---|
| `feigin-hashizume2009` | **PRESENT** | — |
| `dimofte-gaiotto-gukov2014` | **PRESENT** | — |
| `terashima-yamazaki2011` | **PRESENT** | — |
| `kashaev-tirkkonen2014` | **PRESENT** | — |
| `macdonald1971` | **PRESENT** | — |
| `lusztig1989` | **PRESENT** | — |
| `frenkel-reshetikhin2002` | absent, **and no longer cited** | 0 |
| `champanerkar-kofman-mullen2008` | absent — **fixed in this branch** | 0 |
| `faddeev1996` | absent | 2 |
| `bokut1978` | absent | 1 |
| `manuscript` | absent — but see below | 2 |

**The six were resolved CORRECTLY, and that is worth recording**, because this
bean's central warning was that they must not be collapsed into their
near-misses. They were not: `macdonald1971` is *Spherical Functions on a Group
of p-adic Type* and `lusztig1989` is *Modular representations and quantum
groups* — the two distinct works this bean names, added as themselves rather
than repointed at `macdonald1995` / `lusztig1990`.

### `champanerkar-kofman-mullen2008` needed no research either — it was already adjudicated

`references.ts:5251` carries a note on `champanerkar2003`: it was added
2026-06-28 to correct *"the phantom key 'champanerkar-kofman-mullen2008' … no
such Champanerkar–Kofman–Mullen 2008 A-polynomial paper exists (the 2008
Champanerkar–Kofman paper is on Khovanov homology)"*. That drain fixed one of
the two citing blocks; `q-zero-stokes-region-identification`, which `uses` the
block that was fixed, kept the dead key. Repointed here.

### The gate: it is wired, and it is deliberately `--strict`-only

This bean says the check "has never run". It now runs — **under `--strict`**.
`scripts/run-validate.ts` (`9f1322dd81f`, 2026-08-30) imports and calls
`configureReferenceRegistry`, inside `if (strict)`. A default run still prints
the `ℹ no reference registry configured` line and reports `✓ Valid — 14
issue(s)`; that is the documented choice, not a regression — enabling it
unconditionally would move the default from `Valid — 14` to `Invalid — 23` on an
untriaged backlog.

**So a clean default `run-validate` is NOT evidence the citations are clean.**
Use `--strict` when you want the citation gate.

### 🟡 `manuscript` — a DECISION, and AGENTS.md §1 contradicts itself

Not a typo and not research. AGENTS.md §1 says two things that cannot both hold:

> The `[key]` must match an entry in `content/schema/references.ts` exactly.
> If no published reference exists, use `[manuscript]` …

`manuscript` is **not** an entry — it is a CSL *type* name. So every site
following the second sentence violates the first. Measured: **4436 Lean
`-- Ref:` sites** use `[manuscript]`, plus the 2 content blocks here
(`categorical-proton`, `categorical-proton-properties`; neither `.md` contains
any `\cite{}`, so the key is hand-set metadata, not extracted from prose).

**The work it means IS held**, as `leitner2026` — *"Quantum Observable
Universe", Leitner, Fred, 2026, `type: "manuscript"`*, i.e. this paper.

Two ways to close it, and they differ in blast radius:

- **(a) Add an alias entry `manuscript` → the same work.** One bibliography
  entry. Makes §1 self-consistent and makes all 4438 sites resolve at once.
  Risk: a duplicate CSL entry for one work, which the duplicate-detection and
  BibTeX export would then see twice.
- **(b) Re-key the 2 content blocks to `leitner2026`, leave the Lean convention
  alone.** Two lines. `cites-resolve` does not validate Lean `-- Ref:`, so the
  4436 are untouched either way — but §1 stays self-contradictory and the next
  author to put `manuscript` in a `cites[]` reintroduces the defect.

**Default if nobody decides: nothing changes** — the two blocks keep a key that
cannot resolve, and the gate reports them under `--strict` only. That is safe;
no reader-visible claim is broken, because neither block's prose cites anything.

**My judgement, not a finding: (a).** It is smaller, it fixes the rule rather
than two instances of it, and the "duplicate entry" objection is weak for a
self-citation. But it edits the bibliography, so it is the owner's call and is
deliberately not done here.

### Still needing real research (2 keys, 3 blocks)

- **`faddeev1996`** — `inter-nucleon-channel-color-tube`,
  `pachner-pentagon-borromean`. Held Faddeev entries are `faddeev1994`,
  `faddeev1995`, `faddeev_kashaev1994`, `faddeev-kashaev-volkov2000`. The
  library holds no Faddeev 1996 either (INDEX scan: the Faddeev hits are
  Skyrme–Faddeev soliton papers and quantum-dilogarithm work by others).
- **`bokut1978`** — `phi-q-tower-algebraic-stratification`. Held Bokut entries
  are `bokut2001`, `bokut2005`, `bokutchen2011/2014/2015pbw`. Library holds
  `arxiv-0910.0096v1` (*Gröbner–Shirshov bases for Coxeter groups*), which
  *cites* Bokut–Shiao but is not the 1978 work.

Both still need checking against what the citing block claims. The bean's
standing warning holds for these two: repointing a citation at a different paper
is worse than a broken link.

### Audited the six — they hold, and one of them made the hard call correctly

The claim "the six were resolved correctly" above was checked rather than
assumed: each entry's `issued` year was compared against the year its own key
asserts. Five match. **One does not, and it is the interesting one.**

`kashaev-tirkkonen2014` carries **`issued: 2003`**, and its own note says why:

> Cited in q-geometric-langlands/modular-s-transform-q-q-tilde for the Volume
> Conjecture. The citing key says 2014, but the sole Kashaev–Tirkkonen paper is
> the torus-knot VC proof: Zap. Nauchn. Sem. POMI 269 (2000) 262–268, English
> transl. J. Math. Sci. 115 (2003) 2033–2036. **Key year is wrong; entry carries
> the true year.**

That is precisely the judgement this bean exists to demand. The lazy resolution
was available and cheap — mint an entry dated 2014 so the key stops failing — and
it would have put a fabricated year behind a real citation. Instead the agent
found the actual work, entered its true year, and recorded the mismatch. Do not
"correct" the entry's year to match the key.

**Latent, and deliberately not fixed here: the KEY is now a misnomer.**
`kashaev-tirkkonen2014` names a work published 2000 (Russian) / 2003 (English
translation). Anyone reading the citation without opening the entry will date it
thirteen years late. Renaming the key would touch the citing block and any
`\cite{}`; the note prevents the misreading for anyone who looks, so this is
recorded rather than swept — consistent with this bean's own standing rule that a
citation's *identity* is not something to change casually.

The other five (`feigin-hashizume2009`, `dimofte-gaiotto-gukov2014`,
`terashima-yamazaki2011`, `macdonald1971`, `lusztig1989`) match their key years
and carry distinct titles from their near-misses.


--------

## 🟧 OWNER RULING 2026-09-26 — the `manuscript` decision is closed, and the answer is NEITHER (a) NOR (b)

This bean twice put the self-citation to the owner as a two-way choice:

> **(a) Add an alias entry `manuscript` → the same work.** … **(b) Re-key the 2
> content blocks to `leitner2026`, leave the Lean convention alone.**
>
> **My judgement, not a finding: (a).**

**The owner chose a third option**, verbatim:

> *"leitner2026 should be in folio/. its the new paper/book thing"*

`leitner2026` is not to be a bibliography entry at all. It is **the work** — the
paper/book — and works live in `folio/`. That rejects (a) on its own terms: (a)
would have added a *second* bibliography entry for the self-citation, when the
ruling says the *first* one is already in the wrong place. My recommendation was
pointing the wrong way, not merely at the smaller of two options.

### Why the corpus supports the ruling, checked rather than assumed

- `content/schema/references.ts:2339` holds `leitner2026` with title
  **"Quantum Observable Universe"**, `type: "manuscript"`,
  `note: "This manuscript"`.
- `content/folio.ts:14` lists the folio's first paper with title
  **"Quantum Observable Universe"**, `dir: "quantum-observable-universe"`.

**Same work, same title, held twice** — once as a folio node, once as a
reference to itself. That duplication is the defect the ruling removes, and it is
a stronger objection than the "duplicate CSL entry" risk I raised against (a):
the duplication already exists.

- `scripts/cited-source-availability-audit.py:86` already carries
  `SELF_KEYS = {"manuscript", "leitner2026"}`. The corpus had already concluded
  these are one thing; it just had no place to put it.

### What this does and does not change

- **The Lean layer stays fine.** The 2026-08-31 correction in this bean stands
  and is not affected: `validate-references.ts:171-172` exempts `manuscript`
  explicitly, with a comment saying so, and the checker reports **0**
  `manuscript` errors of 19. There is **no** 4,436-site sweep, and re-measured
  today the Lean `-- Ref: [manuscript]` population is **3,998**, not 4,436 —
  quote a fresh measurement, not either figure.
- **`cites-resolve` still lacks both carve-outs** (`manuscript`, and the
  cross-paper `key.includes(":")`) that its sibling checker has. That is still a
  one-condition fix **in folio-assistant, not here**, and it is still the real
  residue for the 2 content blocks. The ruling does not remove it: whatever
  `folio/` ends up holding, a `cites[]` entry naming the folio's own work needs
  the checker to know that is legal.
- **Class A is untouched.** The remaining genuinely-absent keys are
  `faddeev1996` (2 blocks) and `bokut1978` (1 block), and this bean's standing
  warning still binds on both: repointing a citation at a near-miss is worse
  than a broken link.

### Sequencing — this cannot land yet, and that is not a stall

`folio/` **does not exist**. The rehoming is part of `qou-yqko`
(`content/` → `folio/`), where this ruling is also recorded. Doing it before
`folio/` exists would mean deleting the only held record of the work's
metadata with nowhere to put it.

Measured consumers that will need to resolve the key afterwards: **32 Lean
`-- Ref:` sites, 4 `.ts` `cites[]`, 3 `.jsonld`** (the knowledge graph — so this
touches the KG the owner has made authoritative), plus the generated
`references.bib`.

**Status stays `todo`.** Per AGENTS.md §13a the ruling settles *what* to do, not
that it is done.


## 2026-11-21 — expo-chapter drain (session https://claude.ai/code/session_01Qmmkt5JeUvGF2FboRQJbLN, issue #8826)

Re-measured on main 2ae54ab40 by importing `folio/schema/references.ts` (973 entries) and checking every `cites:[...]` key in `folio/quantum-observable-universe/**/*.ts` (keys with `:` skipped as cross-paper): **0 unresolved**. `faddeev1996` and `bokut1978` are no longer cited anywhere; the two `manuscript` blocks now cite `leitner2026`. The citation debt this bean was filed for is gone. What remains is not citation work: (1) the owner's 2026-09-26 ruling to move `leitner2026` into `folio/` (with `qou-yqko`); (2) the missing `manuscript` / `:` carve-outs in folio-assistant's `cites-resolve`; (3) moving `configureReferenceRegistry` out of `if (strict)` in `scripts/run-validate.ts`, which this session could not verify because the light platform lacks `unist-util-visit` for the validator. Recommend closing this bean once (3) is done by someone with the full platform.
