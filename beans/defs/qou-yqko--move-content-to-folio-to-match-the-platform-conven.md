---
# qou-yqko
title: Move content/ to folio/ (owner-confirmed 2026-09-26) — pin bump DONE, still blocked; recorded blast radius is an undercount
status: todo
type: feature
priority: normal
tags:
    - platform
    - migration
created_at: 2026-09-26T11:19:21Z
updated_at: 2026-09-27T05:30:00Z
parent: qou-n4r9
blocked_by:
    - qou-8321
---

**Owner direction, 2026-09-26:** *"Can move content/ for to folio/ to match.
Align to f-asst unless specific reason not to"*.

This **reverses the premise of `harness.json`**, which exists (its own words)
because *"qou keeps `content/` — five folios, a bun workspace, CI paths and every
cross-reference in the corpus point at it — so rather than move the tree, it SAYS
where the tree is."* The owner has now said the tree may move.

## Measured blast radius

| population | files |
|---|---|
| tracked files under `content/` | **18,768** |
| files outside `content/` mentioning the string `content/` | 36,653 |
| …of which are in `library/` | **31,241** |
| …of which are in `.beans/` | 1,161 |
| **genuine path-shaped referrers** (excl. `library/`, `.beans/`) | **4,237** |

Largest referrer groups: `content/quantum-observable-universe` 2,655 files,
`content/pipeline` 1,988, `content/schema` 1,155. Seven `.github/workflows/*`
reference it.

## 🛑 THE TRAP, and it would look like success

The 31,241 `library/` hits are **not paths**. They are JSON-LD namespace URLs:

```json
"@context": "https://litlfred.github.io/folio-assistant/ns/content/v1.jsonld"
```

That is the platform's own `ns/content/v1` vocabulary, nothing to do with qou's
directory. A naive `sed -i 's|content/|folio/|g'` across the tree would rewrite
all 31,241 to `ns/folio/v1.jsonld`, **break every block's JSON-LD context**, and
report a clean rename. The knowledge graph would go quiet rather than error —
`corpus_search`'s `emptyRoots` case, which AGENTS.md already warns reads as
"nobody has done this".

**So the rename must be path-anchored, never string-anchored.** Match
`content/<known-folio-dir>` and `content/{schema,pipeline}` explicitly; never bare
`content/`.

## `content/pipeline` may be largely STALE already

1,988 files reference it, but the pipeline moved to the platform in the miga
migration — `folio-assistant/content/pipeline/`. So a large share of those
referrers may already be dead and should be audited as part of this, not blindly
rewritten. Measure before rewriting; a dead reference rewritten is still dead.

## Sequencing

Do this when nothing else is in flight. It touches ~23k files and will conflict
with every open branch. It should land **after** `qou-yf1y` (so the declaration
can point at `folio/` in the same change) and ideally after `qou-utbr` (so the
`.beans/` referrer count is not being rewritten twice).

`harness.json`/`qou.json`'s `directories[0].path` changes `content/` → `folio/`
in the same commit, or the declaration points at a directory that no longer
exists.

## Not started. No files moved.


---

# 🛑 STOP — DO NOT ACTION THIS BEAN. The platform was changed to make it unnecessary.

Measured 2026-09-26 against platform **main `e3264b4`** (fetched into a throwaway
clone; the local `folio-assistant/` checkout is at the pin and cannot answer this).

## The decision, first

**Should qou's authored content move from `content/` to `folio/`?** It needs the owner
because **two of the owner's own instructions, six days apart, point opposite ways** —
and the later one carries an explicit escape hatch that the earlier one triggers.

- **2026-09-20** — quoted inside the platform's own test file: *"qou can declare a new
  folio at content/."* The platform was then **modified to honour it**.
- **2026-09-26** (to this session) — *"Can move content/ for to folio/ to match. Align
  to f-asst **unless specific reason not to**."*

The platform change of 2026-09-20 **is** a specific reason not to. I am not choosing
between two owner instructions; that is the owner's to do.

## The evidence

`cat-harness/schemas/cat-harness.ts:4557`:

```ts
export function folioDir(root: string): string {
  try {
    return directoryForGraph(root, "folio") ?? join(root, "folio");
```

**The declaration wins; `folio/` is only the fallback.** And
`cat-harness/schemas/folio-dir.test.ts` opens with:

> `test("a folio DECLARING content/ resolves to content/ — the qou case")`
> `// Owner, 2026-09-20: "qou can declare a new folio at content/". This is that`
> `// sentence as a test. Before folioDir, 162 sites spelled join(root, "folio")`
> `// as a literal and this declaration was ignored.`

So **162 hardcoded sites were rewritten** to make qou's `content/` work. Its end-to-end
test is titled *"a consumer finds a folio that declares content/"* and exercises the
real `findPapers`, recording that with the root hardcoded *"a folio keeping `content/`
was invisible however correctly it declared itself."*

`qou.json` already declares exactly the shape that test fixtures:
`{id: "folio", path: "content/", graphKinds: ["folio"], dependents: "reproduce"}`.

## The four options

### A — Leave `content/`, keep declaring it *(recommended)*
- **What it means.** Nothing moves. `qou.json` says where the tree is; the platform asks.
- **What it costs.** Zero. Already true as of this branch.
- **What it risks.** qou's layout differs from the platform's default `folio/`, so a
  reader may think it un-migrated. Mitigated: `qou.json`'s `_path_comment` now explains
  it and cites the test.
- **What it commits to.** Keeping the declaration readable **forever**. `folioDir`'s
  fallback is `folio/` and the platform *tests that the fallback is never `content/`*
  (*"that root is excised"*), so a declaration that stops parsing makes qou's content
  **invisible** rather than defaulting sensibly.

### B — Move `content/` → `folio/`
- **What it means.** 4,237 real referrers rewritten, tree relocated, `path` updated.
- **What it costs.** The largest change in this arc, and it **discards** upstream work
  done on the owner's own instruction. Also blocked at the pin regardless: **62 call
  sites across 54 files** in the *pinned* platform resolve `"content"` against a repo
  root (`CONTENT_DIR = resolve(REPO_ROOT, "content")`), with no configurable root — so
  B cannot land before `qou-8321`.
- **What it risks.** **31,241 of the 36,653** `content/` hits are JSON-LD `@context`
  namespace URLs in `library/`, not paths. A bare `sed` breaks every block's JSON-LD
  context *and reports a clean rename*. Five bun-workspace globs, CI paths and every
  cross-reference move at once.
- **What it commits to.** Convention over declaration, permanently.

### C — Move, but only after the pin bump
- **What it means.** B, sequenced: `qou-8321` → then this.
- **What it costs.** B's cost plus the coupling.
- **What it risks.** Same as B. It fixes only the *timing* objection, not the
  *substantive* one — the upstream work still gets discarded.
- **What it commits to.** Same as B.

### D — Ask upstream whether `folioDir` is transitional
- **What it means.** Treat the 2026-09-20 change as possibly a bridge, and confirm it is
  a supported end state before relying on it.
- **What it costs.** One question, no code.
- **What it risks.** Option A quietly depends on `folioDir` surviving; if upstream later
  re-hardcodes `folio/`, A breaks silently (invisible content, not an error).
- **What it commits to.** Nothing — it is information.

## Default if the owner says nothing

**Nothing happens, and that is safe.** `content/` stays, `qou.json` declares it, the pin
does not read the file at all. No follow-up is owed. This bean stays `todo` and is not
actionable.

## Blast radius in real terms

Not "4,237 referrers" abstractly. Option B rewrites: every `content/<paper>/**` path in
the five paper manifests; `folio.config.json`'s `adapterModule`; the bun workspace globs;
`scripts/check-sidecars.sh`, `run-validate.ts` invocations and the two Lean sweep scripts
(`lean-content-sweep.sh` walks 938 content-block `.lean` files by path); every
`lean.ref` resolution candidate-2 path under `content/<paper>/lean/`; and the 31,241
JSON-LD contexts that must **not** change. A partial application leaves the corpus
half-addressed with **checkers reporting clean**, because an existence-filtered declared
directory that is absent is dropped silently before any consumer sees it — the platform's
own `dh4f` shape.

## Recommendation — agent judgement, not a finding

**Option A, with D as a cheap follow-up.** Upstream spent 162 site rewrites and a
five-case test file making qou's `content/` a first-class declared path, on the owner's
instruction; moving now would discard that to gain a convention the platform
deliberately made optional. D costs one question and closes A's only real exposure.

## Done in this branch regardless of the choice

`qou.json`'s `graphs` → **`graphKinds`**. Independent of the path question: the platform
renamed the field 2026-09-21, and `graphs` survives only through
`acceptLegacyGraphsKey`, whose docstring says it exists for unmigrated *downstream*
folios like this one. Alignment, not a break fix — and inert at the pin, where nothing
reads this file.


---

## 🟧 OWNER RULING 2026-09-26 — the 2026-09-20 instruction was TEMPORARY. This bean is LIVE again.

Verbatim: *"Owner, 2026-09-20: 'qou can declare a new folio at content/'. --> temporary"*.

So **the move to `folio/` is intended**, and the four-option frame above is resolved
to **option B/C**. The retitle to `DO NOT ACTION` is withdrawn.

### What I got wrong, and it was a reasoning error not a measurement error

The platform measurement in the block above is **correct and stands**:
`cat-harness.ts:4557` `folioDir()` really does return
`directoryForGraph(root,"folio") ?? join(root,"folio")`, the declaration really
does win, and a folio really can keep `content/`. None of that is retracted.

What was wrong was the **inference**: I read a *test comment quoting an instruction*
as a *standing decision*. A test records what was asked for on the day it was
written. It is evidence about the platform's capability, never about what the owner
currently wants — and I used it to overrule a live instruction given to me directly.

### What does NOT change — the sequencing blocker is independent of the ruling

At the **pinned** platform `df28d02`, **62 call sites across 54 files** resolve
`"content"` against a repo root (`CONTENT_DIR = resolve(REPO_ROOT, "content")`)
with no configurable root. So the move **cannot land before `qou-8321`** (the pin
bump), on purely technical grounds. Order is: `qou-8321` → this.

Also unchanged, and it is the execution hazard: **31,241 of the 36,653 `content/`
hits are JSON-LD `@context` namespace URLs in `library/`, not paths.** A bare
`sed` breaks every block's JSON-LD context *and reports a clean rename*. Real
referrers: **4,237**. And `qou.json`'s `path` must flip in the SAME commit as the
tree move — an existence-filtered declared directory that is absent is dropped
silently, so a split change leaves every consumer reporting a clean run over nothing.

### Interaction with qou-j34j, which is new and larger

The KG-authority inversion (`.jsonld` becomes the authority, `.ts` a rendered
artifact) will rewrite what lives under this directory and how it is generated.
Moving the tree and inverting the authority are **separable**, but doing the move
first means doing it once rather than twice. Recommend: pin bump → move → inversion.


--------

## 🟧 OWNER RULING 2026-09-26 — `leitner2026` goes in `folio/` too

Verbatim: *"leitner2026 should be in folio/. its the new paper/book thing"*.

`leitner2026` is the folio's **self-citation**, held today as an ordinary
bibliography entry at `content/schema/references.ts:2339` —
`type: "manuscript"`, title *"Quantum Observable Universe"*, author Leitner,
`note: "This manuscript"`. That title is **verbatim the title of the folio's own
first paper** in `content/folio.ts:14`, so the work's identity is held twice: once
as a folio node and once as a reference to itself.

The ruling puts it in `folio/`, i.e. with the works rather than with the cited
sources. So this bean's move now carries a second item: **the self-citation
rehomes to the folio, it does not merely travel along inside
`schema/references.ts`.**

Current consumers of the key, measured (not the raw grep — `.olean` binaries
excluded): **32 Lean `-- Ref:` sites**, **4 `.ts` `cites[]`**, **3 `.jsonld`**
(the knowledge graph), plus `references.bib` (generated) and
`scripts/cited-source-availability-audit.py:86`, which already groups it with
`manuscript` as `SELF_KEYS = {"manuscript", "leitner2026"}`. **The corpus
already treats the two as one thing**; the ruling says what that thing is.

Cross-ref: `qou-cite`, where the `manuscript` key was parked as an owner
decision between (a) an alias entry and (b) re-keying two blocks. **The ruling is
neither** — see that bean.

## 🛑 THE RECORDED BLAST RADIUS IS AN UNDERCOUNT — do NOT plan the move off it

`qou.json`'s `_path_comment` states, as the binding sequencing fact:

> at the PINNED platform df28d02, **62 call sites across 54 files** resolve
> "content" against a repo root with no configurable root, so the move CANNOT
> land before the pin bump (qou-8321).

**The pin bump has landed** (`.folio-assistant-pin` = `37a36ce9296`, this
session). Two things follow, and the second is the important one.

**1. The bump did not unblock it.** Re-measured at the new pin with the same
method: **59**, against 62 at the old one. Essentially unchanged.

**2. Both figures are from a blind detector, and I reproduced the blindness
before catching it.** `grep '"content"'` matches `content` only as a *complete
quoted token*. The platform overwhelmingly writes the path as ONE string:

    grep -c '"content/'   -> 402      # e.g. "content/pipeline/build.ts"
    grep -c '`content`'   -> 126
    grep -c "'content/"   ->  28
    grep -c '"\.\./content' ->  49
    grep -c 'contentDir'  ->  17

A `"content"` grep cannot see any of the 402. So **59 and 62 are both
undercounts of unknown size**, and the sequencing note's authority rests on a
number that does not measure what it claims.

Of the 59, the majority are not directory resolution at all: **21 are
`holds: "content"`**, a graph-LAYER declaration, joined by `GraphLayer`,
`Bucket`, `bucket: "content"`, `CONTENT_EXT`, `SCAN_ROOTS`, `SCANNED` and two
`tags:` arrays. So the recorded figure is simultaneously **too high** for
directory resolution and **too low** for the path surface. It is not a usable
planning number in either direction.

**I am deliberately NOT supplying a replacement count.** A classifier written
here to do it returned visibly incoherent buckets (`content/content`,
`content/...`), i.e. the regex was wrong, and reporting a figure from an
unvalidated detector is row 45 of the detector-blindness taxonomy — an audit
that certifies its own calibration. Producing a defensible count is scoped work
for whoever runs this move.

## What IS established, and it is not retracted

- **The platform supports a folio keeping `content/`.**
  `folioDir()` (`cat-harness/schemas/cat-harness.ts:4557`) is still
  `directoryForGraph(root, "folio") ?? join(root, "folio")` — the declaration
  wins, the `folio/` literal is only the fallback. Unchanged across the bump.
- **`content/` is explicitly folio-owned**, alongside `folio/`:
  `FOLIO_OWNED = new Set(["folio", "content", "uploads", "library", "lean", ".lake"])`
  (`cat-harness/scripts/check-usage-paths.ts`), and the platform's own test
  asserts `FOLIO_OWNED.has("content") === true` while
  `FOLIO_OWNED.has("scripts") === false`.

So the move remains a **choice the owner has made**, not a correctness fix — and
the reason to sequence it carefully is unchanged. Only the *number* justifying
the sequencing is wrong.

## Unchanged and still binding

When it lands, `qou.json`'s `path` changes to `folio/` in the **same commit** as
the tree move, never before: an existence-filtered declared directory that is
absent is dropped silently, and every consumer then reports a clean run over
nothing.

--------

## MEASURED 2026-09-27 — ZERO sites block the move, and TWO are REPAIRED by it

The note above says the recorded 62 is an undercount from a blind detector and
**declines to supply a replacement**, because a classifier written that day
returned incoherent buckets. Here is the replacement, with a calibration that
can fail.

### Method, and it is calibrated rather than self-certified

Match every string literal that is `content` or begins `content/` (all quote
styles, `../` prefixes allowed) in non-test `cat-harness/**/*.ts`, then keep only
those on a line that actually **joins or resolves** it — `join(`, `resolve(`, or
`listDirBranch`. A literal that is a graph-LAYER name (`holds: "content"`), a
`Bucket`, a `tags:` entry or a type union is not a directory and is excluded by
construction rather than by a hand list.

**The calibration asserts ten hand-found sites are detected and FAILS loudly if
any is missing** — the row-45 lesson from the detector-blindness taxonomy, that
an audit which hardcodes its own calibration pass cannot discover its own blind
spot. Result: **10/10 detected.**

    string literals `content` / `content/...` (non-test)   495
      of those, JOINED or RESOLVED against a root            21

So 495 is the grep surface and **21** is the resolution surface. Neither 62 nor
my own 59 measured either quantity.

### What the 21 are

| group | n | what it is |
|---|---:|---|
| platform's own tree / a namespace path | 11 | `REPO_ROOT/content/docs`, `INSTANCE_ROOT/content/docs`, `content/assets/css`, `ns/content/v1.jsonld`, `__dirname/../../content` |
| `content/pipeline/<script>` | 8 | `build.ts`, `generate-block-tex.ts`, `glossary-candidates.ts` — instance-side pipeline scripts that **miga moved upstream**, so a separate question from the rename |
| **resolve a folio's content DIRECTORY** | **2** | `adapters/mcp-server/server.ts:513`, `adapters/document/resolver.ts:72` |

qou has no `content/docs`, so the 11 cannot touch it. The 8 are about where a
pipeline script lives, not where the folio lives.

### The 2 are ALREADY BROKEN for qou, and the move FIXES them

Both are the same fallback, and both are internally inconsistent:

```ts
const folioRel = "folio/folio.ts";
if (fileExistsBranch(br, folioRel)) { ... }          // primary
else {
  const dirs = listDirBranch(br, "content").filter(d =>   // lists content/
    fileExistsBranch(br, `folio/${d}/${d}.ts`));          // checks folio/
}
```

It **lists `content/`** and **tests for the manifest under `folio/`**. Traced
against qou's actual tree:

1. `folioRel` is `folio/folio.ts`. qou has `content/folio.ts` and no `folio/`,
   so `fileExistsBranch` is **false** — qou takes the `else` branch.
2. The listing finds qou's five paper directories under `content/`.
3. The filter tests `folio/<d>/<d>.ts` for each — **false for every one**.
4. **Zero papers discovered.**

So auto-discovery yields nothing for qou *today*. After the move, `folio/folio.ts`
exists, the **primary** path is taken, and this fallback never runs at all.

**The platform already knows.** Both sites carry the identical comment: *"declared-path-literal:
the folio content root. Resolving it through `directoryForGraph` is bean `hs08`;
the harness-side callers hit `ot9a`'s layering boundary, so the literal is COUNTED
here rather than hidden."* So the literal is deliberately visible and tracked
upstream as `hs08`.

### What this does and does not settle

**Settles:** the sequencing objection. The `qou.json` `_path_comment` says the
move "CANNOT land before the pin bump" on the strength of the 62. The bump has
landed, and the resolution surface is 21 of which **0 block** and **2 improve**.
There is no longer a measured code-resolution reason to hold the move.

**Does NOT settle, and I am not claiming it:**

- **Runtime consequence is untraced.** Both sites are in the MCP-server /
  document-adapter layer, which the owner de-prioritised (*"dont want to have
  strong depndency/assume MCP server running"*). Whether anything user-visible
  depends on paper auto-discovery is **not measured** — qou may not run that
  server at all, in which case the 2 are dead code in both layouts and the
  "repair" is theoretical.
- **The 8 `content/pipeline/` sites** need their own pass. They look for
  `build.ts` and friends in the INSTANCE's `content/pipeline/`, which miga moved
  to `cat-harness/content/pipeline/`. That looks broken independent of any
  rename, but I have not traced whether a live path reaches them.
- **Non-code consumers are out of scope here.** This measures `.ts` resolution
  only. Documentation, workflow `paths:` filters, `.gitignore`, skill files and
  the 3613 `.jsonld` `@id` values (`papers/<paper>/blocks/<label>` — note these
  are keyed on the PAPER, not on `content/`, so they are unaffected) were not
  part of this count.

**So the move is unblocked on the ground the note above holds it, and the
remaining work is the mechanical tree move plus the `qou.json` `path` change in
the same commit** — the constraint the note states and which is unchanged.

`leitner2026` rides this, per the owner ruling recorded above.
