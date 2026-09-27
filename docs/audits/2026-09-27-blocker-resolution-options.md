# The seven open blockers: resolution options, costs, downstream impact

**Date:** 2026-09-27. **Corpus:** `18e1ba553e`. **Platform:** `836810b9a41`
(qou's pin is `37a36ce9296…`, unchanged).
**Requested by the owner:** *"Give options for resolutions, pros and cons.
Recommendations in Downstream impacts for all of the blockers"*.

Every figure below was **re-measured on the merged `main` for this document**,
not carried from the session that surfaced these items. Four of the recalled
figures were wrong; each correction is flagged 🛑 in place, because in this
corpus a stale number is the failure mode the whole document is about.

Recommendations are marked **judgement** and are mine, not findings.

---

## Summary table

| # | Blocker | Kind | Recommendation |
|---|---|---|---|
| 1 | `.beans/` → `beans/defs/` doc sweep | mechanical, scoped | **1c** — fix the 16 skills + 1 dead `-- Ref:`, leave dated records |
| 2 | Delete `folio.config.json` | mechanical, safe | **2a** — delete it now |
| 3 | Move `content/` → `folio/` | **authorised work, not a decision** | **3b** — do it, one commit, after #2 |
| 4 | Does the `gh-pages` branch go? | decision | **4a** — keep the branch, it is a file store |
| 5 | Does PDF output go? | decision | **5a** — keep it |
| 6 | Four stub QA checkers | upstream decision | **6c** — registry `implemented: false`; **NOT** the obvious precedent |
| 7 | TypeScript half of the M5 sweep | measurement | **7b** — fold into the next TS visit |

Only **#4, #5 and #6** are genuine decisions. **#3 is already authorised** and I
have been mis-reporting it as a decision — see its 🛑 below. #1, #2 and #7 need
scoping, not rulings.

---

## 1. The `.beans/` → `beans/defs/` documentation sweep (`qou-utbr`, in-progress)

`58a1f3231c` moved the bean store from `.beans/` to `beans/defs/`. `.beans/`
does not exist. `AGENTS.md` was drained of operative references in `18e1ba553e`
— including corpus-grep **path 6**, whose literal `grep -rl <topic> .beans/` had
been returning empty on every run. The rest of the tree was not swept.

### 🛑 Corrected measurement

I reported **241 files** and **"4 runtime paths, all in `fsh-guts/deprecated/`"**
during the session. Re-measured on `18e1ba553e`:

| class | files |
|---|---:|
| `docs/**` | 143 |
| bean bodies | 98 |
| code (`.py`/`.ts`/`.sh`) | 70 |
| `.claude/skills/**` | **16** |
| other | 27 |
| **total** | **354** |

So the population is **354, not 241** — I was low by 32 %. And of the 15 files
whose reference sits outside a `#`/`//` comment, **every one inspected is prose**
— a docstring, a witness `description` string, or a `-- Ref:` citation. So the
operative claim I made ("no live code is broken") **holds**; only the count was
wrong.

**One genuine defect inside the population**, which the file-class table hides:
`computations/probes/b3_sign_one_root_probe.py:41` carries

```
-- Ref: [manuscript] .beans/qou-q8vl; docs/audits/2026-09-12-ursell-…
```

A `-- Ref:` is the citation form AGENTS.md §1 requires beside every `sorry`. This
one resolves to nothing.

### Options

**1a — Sweep all 354.**
*Means:* one mechanical find-and-replace across docs, skills, code comments and
bean bodies.
*Costs:* a ~354-file diff; ~1 h; unreviewable by reading.
*Risks:* rewrites paths **inside dated findings**, falsifying the record — the
`4.66e6` drain deliberately refused exactly this, and `qou-3nva` records that
decision. Collides with any open PR touching those files (48 are open).
*Commits to:* nothing further.

**1b — Sweep nothing.**
*Means:* leave it; `AGENTS.md` is already correct, which is the file agents read.
*Costs:* zero.
*Risks:* the 16 `.claude/skills/**` files are **instructions agents follow**, and
they still name a path that cannot resolve. That is the same class of defect as
the dead path 6, one directory over.
*Commits to:* re-encountering it.

**1c — Sweep the 16 skills + the 1 dead `-- Ref:`; leave the 338 records.** ⭐
*Means:* fix only files whose `.beans/` reference is an **instruction or a
citation**, not a record of a past measurement.
*Costs:* ~17 files; well under an hour; reviewable line by line.
*Risks:* low. Small residual: a `docs/` reader may still meet `.beans/`, but in
prose describing what a dated pass measured, which is correct.
*Commits to:* nothing; 1a stays available.

### Downstream impact

The 16 skills are the live surface: `.claude/skills/local/todo-manager.md` and
`bean-coordination.md` are what an agent opens before touching the tracker, and
`integration-watcher.md` names four `*-queue.json` paths. An agent following a
stale path gets an empty result and, per path 6's own history note, reads it as a
clean bill. The 98 bean bodies and 143 docs are **records**; rewriting them costs
fidelity and buys nothing.

**Recommendation (judgement): 1c.** It fixes everything that can mislead a
future agent and touches nothing that would falsify a dated finding. The dead
`-- Ref:` rides along because it is a one-line citation fix in the same class.

**Default if nothing happens:** `AGENTS.md` stays correct, the 16 skills keep
pointing at a path that returns empty, and `qou-utbr` stays `in-progress`.

---

## 2. Delete `folio.config.json` (`qou-8321` line 84; gated by `qou-yf1y`, `qou-w5av`)

`qou-8321` obliged the pin-bump commit to also `git rm folio.config.json`. The
pin bump landed (`1ea9676d3f`, coupling check green); the deletion did not.

### Measured state — and it is safer than the gates imply

- **Three config files coexist** on `main`: `folio.config.json`,
  `qou.config.json`, `qou.json`.
- **No code reads `folio.config.json`.** Its only referrers are `AGENTS.md` and
  seven bean bodies.
- The **pinned platform's own source says so**:
  `cat-harness/schemas/harness-config.ts:495` at `37a36ce` is headed
  *"`folio.config.json` is not read"*.

### 🛑 `qou-sm2c` is stale — its "one LIVE defect" is already fixed

`qou-sm2c` (`todo`, priority **high**) states that `folio.config.json` carries a
live-broken `"feedbackDir": "folio-assistant/feedback"`, pointing qou's feedback
store inside the platform checkout. Measured on `main`: the file reads
`"feedbackDir": ".folio-feedback"`, and `qou.config.json` carries a
`_feedbackDir_comment` recording that exact fix. `.folio-feedback` does not
exist on disk, so no data is implicated either way.

So the one argument for urgency here is spent, and the one argument for caution
("something live might read it") is refuted by the platform's own source.

### Options

**2a — Delete it now.** ⭐
*Means:* `git rm folio.config.json`, plus the `AGENTS.md` mention.
*Costs:* two files; minutes.
*Risks:* near zero — nothing reads it at the pin. If a *future* pin re-introduces
a reader, that is caught by the bump's own before/after count, which
`.folio-assistant-pin` already requires.
*Commits to:* `qou.config.json` + `qou.json` as the declaration pair, which is
`qou-yf1y`'s stated end state anyway.

**2b — Keep it until `qou-yf1y` completes.**
*Means:* honour the recorded gate literally.
*Costs:* zero now.
*Risks:* three config files keep asserting overlapping things; a reader cannot
tell which is authoritative without reading the platform source. This is what
produced the stale `qou-sm2c` in the first place.
*Commits to:* carrying the ambiguity for `qou-yf1y`'s duration.

**2c — Delete it and close `qou-sm2c` as already-fixed.**
*Means:* 2a plus retiring the stale bug bean.
*Costs:* 2a + a bean update.
*Risks:* none beyond 2a. Note `qou-sm2c` is a **bug**, not a conjecture, so
§13a does not bar completing it.
*Commits to:* nothing.

### Downstream impact

Nothing at the pin — measured, not assumed. The real downstream is *legibility*:
`qou-8321`, `qou-yf1y`, `qou-29i6`, `qou-f50c`, `qou-qqia` and `qou-sm2c` all
reason about which config is authoritative, and three files coexisting is why
there are six beans. Deleting the unread one collapses that.

**Recommendation (judgement): 2a, extended to 2c.** The gate was written when it
was unknown whether anything read the file; the platform now says in its own
source that nothing does. Closing the stale `qou-sm2c` in the same change stops
a high-priority bug bean advertising a defect that no longer exists.

**Default if nothing happens:** three configs coexist, `qou-8321` stays `todo`
with an unmet obligation, and `qou-sm2c` keeps reporting a fixed defect as live.

---

## 3. Move `content/` → `folio/` (`qou-yqko`)

### 🛑 This is NOT a decision, and I have been reporting it as one

I told you repeatedly that *"`qou-n4r9` step 3 is a decision, not work"* and
listed it as waiting on you. Reading `qou-yqko` properly: **you already ruled.**

> **Owner direction, 2026-09-26:** *"Can move content/ for to folio/ to match.
> Align to f-asst unless specific reason not to"*.
>
> **🟧 OWNER RULING 2026-09-26 — the 2026-09-20 instruction was TEMPORARY. This
> bean is LIVE again.** … *"The retitle to `DO NOT ACTION` is withdrawn."*

The `🛑 STOP — DO NOT ACTION THIS BEAN` at line 81 is **superseded** by the
ruling at line 208, and the bean's own closing line reads: *"the move is
unblocked on the ground the note above holds it, and the remaining work is the
mechanical tree move plus the `qou.json` `path` change in the same commit."*

I was reading the `DO NOT ACTION` header and stopping — the same
first-claim-wins error this corpus documents in `AGENTS.md` §4d. What actually
gates it is its frontmatter `blocked_by: qou-8321`, i.e. **blocker 2 above**.

### Measured blast radius (from the bean, spot-checked)

| population | files |
|---|---:|
| tracked files under `content/` | **18,768** (18,816 by my count today) |
| outside `content/` mentioning the string | 36,653 |
| …of which `library/` JSON-LD **namespace URLs**, not paths | **31,241** |
| …of which bean bodies | 1,161 |
| **genuine path-shaped referrers** | **4,237** |

The bean flags the trap explicitly: the 31,241 `library/` hits are
`"@context": "https://…/ns/content/v1.jsonld"` — rewriting them "would look like
success" and would corrupt the knowledge graph.

### Options

**3a — Do nothing.**
*Risks:* leaves the instance misaligned with the platform it is being migrated
onto; `qou-n4r9` cannot close.

**3b — Move it, one commit, after blocker 2.** ⭐
*Means:* `git mv content folio` + `qou.json`'s `path` + the 4,237 referrers, in
a single commit (the bean states the same-commit constraint; the rewrite is
invalid at the old layout and vice versa).
*Costs:* the largest item here by an order of magnitude — ~23k files touched,
7 workflows, and a mandatory exclusion of `library/` and bean bodies.
*Risks:* high if the `library/` namespace URLs are swept (graph corruption,
looks like success); low if they are excluded. Not bisectable — it is one commit
by necessity.
*Commits to:* the platform-aligned layout; every external link into
`content/**` on GitHub breaks.

**3c — Move it behind the declaration instead.**
*Means:* keep the tree, let `qou.json` declare `content/` as the folio root —
which the platform supports (`folioDir()` honours the declaration).
*Costs:* near zero; already true today.
*Risks:* **contradicts your 2026-09-26 ruling**, which was specifically that the
2026-09-20 "declare a folio at content/" instruction was *temporary*.
*Commits to:* re-opening a question you have closed twice.

### Downstream impact

Everything that names a path: 7 `.github/workflows/*`, `qou.json`, the skills,
the `.qa.json` sidecar tree, every `uses[]` resolution, and ~2,655 files under
`content/quantum-observable-universe` alone. The `library/` JSON-LD `@id` values
are keyed on the *paper*, not on `content/`, so they are unaffected — that is the
one piece of good news in the radius.

**Recommendation (judgement): 3b, and not yet.** Do blocker 2 first (it is
`qou-yqko`'s recorded gate and is a ten-minute change), then schedule 3b as its
own session with nothing else in flight — a 23k-file single commit will conflict
with most of the 48 open PRs, so it wants a quiet window rather than a race.
I would **not** do it today.

**Default if nothing happens:** `qou-yqko` stays `todo`, correctly gated, and
the layout stays misaligned. Nothing breaks.

---

## 4. Does the `gh-pages` branch go? (decision, recorded in #7480 / `qou-w5av`)

#7480 merged (`2ba7567f2a6`) having deprecated the *rendered site* and
deliberately **not** touched the branch.

### Measured state

- `gh-pages` head: **`45cf621dd0`, 2026-07-08** — 81 days stale.
- README carries **11** `blob/gh-pages/…` links (I said "~12"; it is 11) and
  **zero** `litlfred.github.io` links.
- So the branch is in use **as a file store**, not as a website.

### Options

**4a — Keep the branch.** ⭐
*Costs:* zero.
*Risks:* an 81-day-old snapshot remains reachable; mitigated, since #7480 already
removed the "rendered" advertising from README.
*Commits to:* nothing. Rule 9 ("never delete branches") points the same way.

**4b — Delete the branch.**
*Costs:* must repoint 11 README links first.
*Risks:* breaks those 11 links and the whole chapter table for no functional
gain; irreversible in effect for anyone holding a link.
*Commits to:* hosting chapter PDFs somewhere else, or not at all — which is
blocker 5, so 4b cannot be decided independently of it.

**4c — Keep the branch, refresh the snapshot.**
*Means:* dispatch `build.yml` once so the 11 links serve current PDFs.
*Costs:* one manual dispatch; Actions minutes.
*Risks:* the four high-volume workflows last *failed* on 2026-06-30, so a
dispatch may fail and needs watching.
*Commits to:* nothing.

### Downstream impact

The 11 links are in README's chapter table — the most-read file in the repo.
Deleting the branch breaks the repo's own front page. Nothing else reads
`gh-pages`: the `lean/` subtree's producer (`doc-gen4.yml`) is now in
`fsh-guts/deprecated/`, and `docs-site.yml`'s publish step was removed by #7480.

**Recommendation (judgement): 4a — keep it.** The branch and the site are
separable, #7480 already separated them, and the only thing the branch still does
is serve 11 links the front page depends on. If you want them current rather
than merely working, 4c is the cheap follow-on.

**Default if nothing happens:** branch stays, 11 links keep serving an 81-day-old
PDF set, README no longer claims it is current.

---

## 5. Does PDF output go away at all? (decision, `qou-w5av`)

### Measured state

`build.yml` is `workflow_dispatch:` only and its `uses:` line is
`litlfred/folio-assistant/.github/workflows/publish.yml@37a36ce9296…` — pinned
to `.folio-assistant-pin`. So **the PDFs are producible today**, on demand. The
earlier reading that they were orphaned was retracted inside #7480 before merge.

### Options

**5a — Keep PDF output.** ⭐
*Costs:* zero.
*Risks:* none; it only runs when dispatched.
*Commits to:* keeping `build.yml` and `paper-builder-image.yml`, which #7480
deliberately left untouched.

**5b — Remove PDF output.**
*Means:* drop `build.yml` + `paper-builder-image.yml`.
*Costs:* small diff.
*Risks:* removes qou's **only** render entry point and orphans the 11 README
links for real. Reversible only by rebuilding the workflow pair.
*Commits to:* folio-assistant's `justthepages` as the sole rendering route —
which is `qou-w5av`'s premise but is not yet demonstrated for this paper.

**5c — Keep it, and prove it.**
*Means:* 5a plus one dispatch to confirm the pinned `publish.yml` still produces
a PDF for this corpus.
*Costs:* one dispatch; watching one run.
*Risks:* it may fail, which is information rather than damage.
*Commits to:* nothing.

### Downstream impact

This is the one blocker that can make a *reader-facing* thing disappear. The
chapter PDFs are what the README chapter table serves, so 5b turns blocker 4 from
"keep a file store" into "delete a broken file store", coupling two decisions
that are currently independent.

**Recommendation (judgement): 5a, and 5c if you want certainty.** Keeping it
costs nothing and preserves the only route that currently works. I would not
remove a working render path on the strength of a replacement that has not been
demonstrated for this paper.

**Default if nothing happens:** PDFs stay producible on dispatch; nobody
dispatches; the 11 links keep serving the 2026-07-08 set.

---

## 6. The four stub QA checkers (`folio-assistant-89wq`; upstream)

Confirmed still unconditional `n/a` on platform `836810b9a41`:

| criterion | checker | self-documenting? |
|---|---|---|
| `detangler-no-xchapter-fwd` | `checkDetanglerNoXChapterFwd` `:1847` | `// TODO … n/a until wired` |
| `detangler-archimedean-wall` | `checkDetanglerArchimedeanWall` `:1856` | same |
| `proof-no-axiom-growth` | `checkProofNoAxiomGrowth` `:2783` | **no comment** |
| `proof-build-green` | `checkProofBuildGreen` `:2789` | **no comment** |

All four `automated: true` with a full description of a test they do not perform.
**8949** qou sidecar entries, 100 % `n/a`, since 2026-07-13.

### 🛑 The platform already solved this once — and copying it here would be a defect

`qa-criteria-registry.ts:700-735` records the same finding for
`proof-no-placeholder-stub` (bean `fg6z`, 2026-09-18): declared `automated: true`
with **no checker anywhere**, so `qa-sweep` fell through to `needs-agent` and was
*"billing a model call for a check nobody had implemented, and arriving
downstream indistinguishable from a criterion legitimately marked
non-automated."* The fix was `automated: false` + an explanatory comment, and the
comment notes *"This edit changes NO runtime behaviour."*

**That precedent does not transfer.** `proof-no-placeholder-stub` had **no
dispatch entry**; these four **do**, returning `n/a`. Flipping them to
`automated: false` would remove the auto-`n/a` and route them to `needs-agent` —
i.e. it would **start** billing agent adjudications across 8949 entries. The
move that was behaviour-neutral there is actively harmful here.

### Options

**6a — Write the four checkers.**
*Costs:* real work; two carry a TODO spec, two carry nothing.
`proof-build-green` and `proof-no-axiom-growth` could follow
`proof-lean-compiles`, which reads a cached artefact and reports **131 pass**.
*Risks:* new checkers produce new findings across the corpus.
*Commits to:* maintaining them.

**6b — Retire all four from the registry.**
*Costs:* small.
*Risks:* loses the recorded intent — the descriptions are the only specification
of these tests that exists. `proof-no-axiom-growth` is the sidecar face of the
anti-laundering discipline; deleting it deletes the plan.
*Commits to:* re-deriving them if ever wanted.

**6c — Mark them: a registry `implemented: false` (or a distinct sentinel).** ⭐
*Means:* keep the stub and the description; add one machine-readable field so a
consumer or reader can tell "not implemented" from "ran and declined".
*Costs:* smallest of the three; no Lean, no artefact, no agent billing.
*Risks:* the criteria remain unimplemented — this makes the gap *legible*, it
does not close it.
*Commits to:* nothing; 6a and 6b stay available, and a follow-on test
("every `automated: true` criterion resolves to a non-trivial checker") would
then be landable.

### Downstream impact

`n/a` currently means *two different things* in every sidecar, and the tell is on
the record: of `detangler-archimedean-wall`'s 3579 entries, 2274 carry the
harness's honest note *"block has no .lean sibling"* and **1303 carry no note at
all** — blocks that do have a `.lean` and get `n/a` because nothing looked. In
qou this already misdirected two consumers: bean `3t8p` chased a CI `lake build`
for three months while the artefact it wanted sat in the repo unread, and M5
published a rate diluted 30–47 pp until `18e1ba553e`. Both were *qou* paying for
an *upstream* ambiguity, which is the argument for fixing it upstream.

**Recommendation (judgement): 6c first, then 6a for the two `proof-*`.** 6c is
cheap, needs nothing, and is the only option that protects the next consumer that
aggregates a criterion list. Do **not** apply the `fg6z` precedent literally —
it reads as the obvious move and would start billing 8949 adjudications.

**Default if nothing happens:** the four keep writing `n/a` into every new
sidecar, indistinguishable from a correct decline. qou is protected at M5; the
next aggregate is not.

---

## 7. The TypeScript half of the M5 sweep (`qou-306p`)

The Python surface is settled: of 17 files reading `.qa.json`, exactly **one**
aggregated a pass rate (M5, fixed), one counts failures only and is immune by
shape, and 15 act per-entry. `qa-evidence-provenance-gate.py:153` already
excludes `n/a` explicitly.

The TS surface is **not** settled: 18 `content/pipeline/*.ts` files carry
aggregate operations; 17 open a `.qa.json` and 9 index a `criteria[` array. Most
are verdict **producers** counting their own findings, so the op count is not
evidence either way.

### Options

**7a — Sweep it now.** *Costs:* per-file reading of 18 files, ~1-2 h.
*Risks:* likely finds nothing, given the Python result. *Commits to:* nothing.

**7b — Fold it into the next visit to that surface.** ⭐
*Costs:* zero now. *Risks:* a diluted TS metric goes unnoticed meanwhile; bounded,
since the platform's own `qa-sweep` does not publish rates. *Commits to:* nothing.

**7c — Close it as out of scope.** *Risks:* records a negative that was never
measured — the failure mode `AGENTS.md` names explicitly.

### Downstream impact

Bounded. These are audit scripts, not reader-facing numbers, and no content block
or witness consumes their aggregates. The M5 dilution mattered because it reached
a **witness**; nothing here does.

**Recommendation (judgement): 7b.** The Python result makes a second find
unlikely, and `qou-306p` already records the surface as *explicitly unmeasured*
rather than clean — which is the honest state and costs nothing to hold.

**Default if nothing happens:** `qou-306p` stays `todo` with the TS surface
marked unmeasured. Correct as it stands.

---

## What I would do, in order

1. **#2** — delete `folio.config.json`, close the stale `qou-sm2c`. Ten minutes,
   and it opens `qou-yqko`'s gate.
2. **#1c** — the 16 skills + the dead `-- Ref:`. Under an hour.
3. **#4a / #5a** — keep the branch and the PDFs. A ruling, no work.
4. **#6c** — upstream, one field.
5. **#3b** — the `content/` → `folio/` move, in its own quiet session.
6. **#7b** — nothing now.

Items 1-4 are ungated once you rule on 4a/5a. Item 5 is the only large one and
is the only one I would deliberately hold.
