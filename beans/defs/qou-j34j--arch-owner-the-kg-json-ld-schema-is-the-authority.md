---
# qou-j34j
title: 'ARCH (owner): the KG (JSON-LD + schema) is the AUTHORITY; .ts becomes a rendered artifact'
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-26T14:20:26Z
updated_at: 2026-10-04T15:15:13Z
parent: qou-n4r9
---

## The ruling (owner, 2026-09-26, verbatim)

> "the KG is the json(ld)+scheme as authotity of public/rendered content. may be
> Skills+Tools to create the rendered content (e.g. typescript). existing KG needs
> to be put in the KG and adapt to new framework"

Read together with the same session's two companions:

> "i dont want the qou heavy rendering, the one with lots of client side rendering
> etc. i want the existing folio-asst just the docs rendering pipeline and what qou
> had been using. put heavy client side stuff (pre Skills/Tools) it in fsh-guts/
> under derprecated or so…"  /  "we can pull out later if we need."

> "also dont want to have strong depndency/assume MCP server running. keep it
> lightweight Tools for Skills to manage / use KG"

## 🛑 THIS INVERTS THE ARCHITECTURE AGENTS.md CURRENTLY STATES

Not a refinement — a reversal of the direction of generation, and AGENTS.md
asserts the old direction as fact in its opening lines (220-221):

> - **Content objects** (`.ts` + `.md` + `.lean` file triples) as authoritative source
> - **LaTeX** as a rendering target (generated from content objects)

And the generator says the same thing in its own words
(`folio-assistant/content/pipeline/gen-block-jsonld.ts`, line 5):

> "A block is authored as `<block>.ts` and rendered from `<block>.md`. This adds a
> **third companion**, `<block>.jsonld`, carrying the same manifest…"

So today JSON-LD is a **derived third companion** of an authored `.ts`. The ruling
makes it the **authority**, with `.ts` becoming one of the rendered outputs that
Skills+Tools produce. Direction reverses:

| | today | under the ruling |
|---|---|---|
| authority | `.ts` (+ `.md`, `.lean`) | **`.jsonld` + schema** |
| `.jsonld` | generated sibling | **the source** |
| `.ts` | authored by hand | **rendered artifact** (Skills+Tools) |
| LaTeX / HTML | rendered | rendered (unchanged) |

## What is measured, on this branch

    content/*.ts       3763
    content/*.md       3723
    content/*.lean    11917
    content/*.jsonld   3583      <- 180 FEWER THAN .ts
    content/*.qa.json  3653
    library/*.jsonld  31236
    tracked .jsonld   34819 total

**The 180-file gap is the sharp end of "existing KG needs to be put in the KG".**
Those blocks have a `.ts` and no `.jsonld`, so under the new framework they would
have **no authority record at all** — not a stale one, none. Identify them before
anything reads `.jsonld` as authoritative; a missing authority file is exactly the
existence-filtered silence the platform's own `dh4f` shape warns about (a declared
thing that is absent is dropped before any consumer sees it, and every consumer
then reports a clean run over nothing).

Note the gap is NOT simply "180 un-generated blocks" until checked: `.qa.json` is
3653 and `.md` is 3723, so the four companion counts disagree four ways. Whether
the 180 are missing JSON-LD, or 180 `.ts` files that are not blocks (builders,
index files, `references.ts`), is **unmeasured**. Measure per-file, not by
subtraction — a difference of counts is not a list of files.

## Why the MCP half of the ruling is the same problem

`corpus_search` — AGENTS.md's corpus-grep **path 0**, the one it says to run
FIRST — is implemented in `cat-harness/adapters/mcp-server/tools/graph.ts`. It is
an **MCP-server tool**. So the instruction an agent is given first requires a
server to be running, and in this very session all three non-Lean MCP servers
FAILED to connect (`paper-assistant`: `ENOENT … /home/litlfred/folio-assistant/
scripts/start-folio-assistant.sh` — a hardcoded home path absent in the container).

The platform has a Skills-facing Tools layer — `cat-harness/tools/{discover,index,
mcp,sessions,viewers}.ts` — and **the KG is not in it.** So the lightweight Tool
the owner is asking for does not exist in either repo yet; this is not a wiring
job.

**The good news, and it is decisive for feasibility:** the KG is fully materialised
on disk (34,819 tracked `.jsonld`). A CLI Tool that reads them needs no MCP server,
no network, and not even bun.

## Ordered plan

1. **Inventory** — per-file, which `.ts` blocks have no `.jsonld`, and classify the
   180 (missing vs not-a-block). Cheap, and everything else depends on it.
2. **A lightweight KG Tool** — read `.jsonld` from disk, seed lexically, expand
   structurally; the `corpus_search` contract without the server. Decide whether it
   lands in qou (`scripts/`) or upstream in `cat-harness/tools/` — upstream is the
   better home under "align to f-asst", and slower.
3. **AGENTS.md lines 220-221** must be rewritten, because they state the old
   direction as fact and are the first thing every agent reads. Also corpus-grep
   path 0, which tells agents to call an MCP tool.
4. **Reverse the generator** — `.jsonld` → `.ts`, rather than `.ts` → `.jsonld`.
   The large, last piece. A round-trip check (`.ts` → `.jsonld` → `.ts` is
   byte-identical) is the honest gate before any `.ts` is treated as disposable.

## Explicitly NOT started

Nothing in the list above is begun. This bean records the ruling and its measured
blast radius; step 1 is the next action and is pure measurement.

## Done in the same session, and adjacent rather than part of this

Parked under `fsh-guts/deprecated/`: the 11 interactive HTML simulators and
`ruby-3d-viewer.html`, with the 11 referring content blocks repointed and
`folio.config.json` updated. Kept, not deleted, per the owner's "pull out later".
Validate is **2 issues before and after**, so no constraint depends on the old
path. `.mcp.json` is **untouched** — its `lean-lsp` entry is load-bearing for Lean
verification, so removing the broken `paper-assistant` entry is surgery to do
deliberately (step 2's business), not a side effect of a move.


---

## Step 1 DONE — the inventory. The real gap is **94 blocks**, not 180.

Measured per-file (not by subtraction), 2026-09-26:

    content .ts stems      3763
    content .jsonld stems  3583
    .ts WITHOUT .jsonld     180
    .jsonld WITHOUT .ts       0     <- clean in that direction

The 180 classified by whether the `.ts` is actually a content block:

| count | class | verdict |
|---|---|---|
| **94** | **BLOCK — has an `.md` sibling, has NO `.jsonld`** | **the real gap** |
| 47 | chapter / paper manifest (`<dir>/<dir>.ts`) | container, not a block |
| 33 | other `.ts` with no `.md` (`content/pipeline/*.ts`, `content/folio.ts`) | not a block |
| 6 | schema / infra (`content/schema/builders.ts`, `constraints.ts`, …) | not a block |

So **quote 94, not 180.** The subtraction figure is inflated ~1.9× by three
classes of non-block `.ts`, and the paragraph above this one predicted exactly
that ("a difference of counts is not a list of files") — recorded because the
prediction was cheap and the check confirmed it.

**One of the six is not even qou's file:**
`folio/quantum-observable-universe/lean/.lake/packages/proofwidgets/widget/src/index.ts`
— a VENDORED Lean dependency inside `.lake/`, which any `content/**/*.ts` walk
picks up. Worth knowing before a future count is read as a corpus fact: `.lake/`
must be excluded, and this walk did not exclude it.

**Zero `.jsonld` with no `.ts`** is the useful negative: nothing has been
orphaned by a deleted block, so the gap is purely un-generated, never stale.

Next action is step 2 (the lightweight KG Tool). The 94 are generable by the
existing `gen-block-jsonld` — that is not this bean's hard part; the hard part is
still reversing the direction so `.jsonld` is the source rather than the sibling.

--------

## MEASURED 2026-09-26 — the gap is **94 blocks**, not 180, and this bean predicted why

This bean's own instruction was followed rather than its number quoted:

> Note the gap is NOT simply "180 un-generated blocks" until checked … Whether the
> 180 are missing JSON-LD, or 180 `.ts` files that are not blocks (builders, index
> files, `references.ts`), is **unmeasured**. Measure per-file, not by subtraction —
> a difference of counts is not a list of files.

Measured per file, walking `content/` with `.lake` and `node_modules` excluded, and
defining a **block** as a `.ts` carrying a same-named `.md` sibling (the
file-triple convention this repo documents):

| | count |
|---|---|
| `content/**/*.ts` | 3761 |
| `content/**/*.md` | 3692 |
| `content/**/*.jsonld` | 3583 |
| **blocks** (`.ts` **with** a same-named `.md`) | **3677** |
| **blocks missing `.jsonld`** | **94** |
| `.ts` with **no** `.md` sibling (not blocks) | 84 |
| `.jsonld` with **no** `.ts` sibling | **0** |

**So 180 decomposes almost exactly as this bean guessed it might: ~94 real gaps
plus ~84 non-blocks.** The 84 are what the bean named — `references.ts`,
`types.ts`, `introduction.ts`/`overview.ts` chapter manifests,
`appendix-surreals.ts`, and audit/test scripts such as
`witness-substitution-audit.ts` and `qa-evidence-audit.test.ts`. None of them is a
content block, so none of them wants a `.jsonld`, and counting them as missing
authority records overstated the real gap by **91 %**.

**`.jsonld` orphans are 0**, which is worth stating because it is the reassuring
half: every existing authority file has an authored `.ts` behind it. The
migration's risk is one-directional — blocks with no authority record, not
authority records with no block.

### My own counts differ slightly from the ones above this line — say why

`.ts` 3761 vs the bean's 3763, `.md` 3692 vs 3723. The difference is the walk, not
the tree: this pass excludes `content/**/.lake/` (Lean build output) and
`node_modules`. Quote a method with any of these figures.

### The 94 are a SCATTER, not one excluded directory — and that is the diagnosis

| blocks missing `.jsonld` | directory |
|---|---|
| 21 | `mass-theory/` |
| 9 | `lifting-and-descent/` |
| 7 | `brings-surface/` |
| 7 | `predicted-spectra/` |
| 5 | `quantum-universes/` |
| 5 | `stochastic-mechanics/` |
| 4 | `glossary/`, `knots-particles-confinement/`, `quantum-observable-universes/` each |
| 3 | `braids-and-knots/` |

Spread across **10+ chapters with no directory dominating**, which rules out the
tempting systematic explanation (a directory excluded from the generator's glob).
A scatter is the signature of **blocks authored after the last generation run** —
several are `outro-*` and `intro-*` blocks, i.e. recently-added connective
material. That points the fix at *"re-run the generator"*, not at *"debug the
generator's scope"*.

**Not established:** whether all 94 generate cleanly. A scatter is consistent with
"never generated" AND with "generation fails on these"; distinguishing them means
running the generator on one and reading the result, which has not been done here.

### Why this matters for sequencing, unchanged

Under the ruling these 94 blocks would have **no authority record at all** — not a
stale one, none. That is the existence-filtered silence the platform's `dh4f` shape
warns about: an absent declared thing is dropped before any consumer sees it, and
every consumer then reports a clean run over nothing. **Close the 94 before
anything reads `.jsonld` as authoritative**, and keep the count draining rather
than re-measuring it by subtraction.

Status stays `todo` — this is the measurement the bean asked for, not the migration.
