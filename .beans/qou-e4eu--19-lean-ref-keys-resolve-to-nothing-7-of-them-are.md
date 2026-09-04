---
# qou-e4eu
title: '19 Lean -- Ref: keys resolve to nothing — 7 of them are not citations at all'
status: completed
type: bug
priority: high
created_at: 2026-08-31T05:06:11Z
updated_at: 2026-09-04T02:12:59Z
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


## 2026-08-31 (cont.) — the seven were NOT a decision. 13 -> 6.

I flagged the seven non-citations as needing an owner convention call. **That
was premature** — the measurement that collapses the question was one grep, and
AGENTS.md §1 already answers it.

**What the seven actually point at**, read verbatim rather than inferred:

| key | target |
|---|---|
| `audit` | `docs/audits/2026-06-09-metallic-q-csc-phase-synthesis.md`, `docs/audits/2026-06-08-metallic-q-hierarchy-proof.md` |
| `probe` | `computations/metallic_q_symbolic_galois_proofs.py`, `computations/two_quark_active_set_mahler_sweep.py` |
| `probe-w` / `probe-j` / `probe-q` | `computations/metallic_q_{wenzl_sign_sweep,jones_sign_sweep,quark_bifurcation}.py` |
| `bean` | `qou-k5r5, qou-t6hc` |
| `metallichierarchy` | `QOU.AlgebraicSubstrate.MetallicHierarchy` — a Lean decl in this repo |

**Every one is an in-repo artifact. None is a published work.** §1: *"If no
published reference exists, use `[manuscript]` and cite chapter/section."*

And the corpus is not ambiguous about the form either — **391 sites already
write `-- Ref: [manuscript] <repo artifact>`**, e.g.
`chi-std-pernucleon-closed-form.lean:243` → `docs/chi-std-pernucleon-theorem.md
§Proof`, and `HabiroClassicalLimit.lean:18` →
`docs/coordination/ck-dk-canonical-registry.md §3`. So the seven were outliers
from an overwhelmingly established convention, not a fork in it.

Rekeyed all **11 sites** across 3 files, **pointer text preserved verbatim** —
only the key changed. `-- Ref: [probe-w] computations/…py` became
`-- Ref: [manuscript] computations/…py`; nothing about what is being pointed at
was altered, so no information is lost and the target stays greppable.

**Result: 13 -> 6 errors.** All three files `lean`-direct **exit 0**.

## The 6 that remain, and none is a judgement call

`frenkel2020`, `koroteev-zeitlin2022`, `murakami1996`, `murakami2013`,
`wielenberg1978`, `ggmw2020` — all real published works needing external
lookup. `frenkel2020` (arXiv:2007.11786) and `koroteev-zeitlin2022`
(arXiv:2108.01557) carry their identifiers inline and are **one fetch from
settled**; **arxiv.org is blocked by this sandbox's egress proxy** and neither
is in `library/`. That is the only thing keeping them open.

Do not resolve `ggmw2020` from its initialism: the Lean comment expands it as
"Gukov–Garoufalidis–Mariño–Wheeler (2020)", but GGMW is usually
Garoufalidis–**Gu**–Mariño–Wheeler, so the comment's own expansion may be wrong.
`library/` holds four candidate resurgence papers.

## 2026-09-03 — 6 -> 4. Two added, four are NOT clean adds (session cool-johnson-t1wveh)

Added to `references.ts` (verified via web search; arxiv.org still egress-blocked
but WebSearch resolves it):

- **`murakami2013`** — H. Murakami, "The colored Jones polynomial, the
  Chern-Simons invariant, and the Reidemeister torsion of the figure-eight
  knot", *J. Topology* (2013). Matches the Lean's "deformed 4₁ asymptotic".
  Volume/DOI unverified, so omitted.
- **`wielenberg1978`** — N. J. Wielenberg, "The structure of certain subgroups
  of the Picard group", *Math. Proc. Cambridge Philos. Soc.* 84 (1978). Matches
  WhiteheadVolumeCatalan.lean. Page/DOI unverified, so omitted.

**The remaining four are ambiguous — NOT one-fetch adds — and each needs the
PDF or the author, so they are recorded here rather than guessed:**

- **`frenkel2020`** — the Lean URL `arXiv:2007.11786` is **"Toroidal q-Opers"
  by Koroteev & Zeitlin (2020)**, *not a Frenkel paper*. Given `QOper.lean`'s
  context the intended work is most likely **Frenkel–Koroteev–Sage–Zeitlin,
  "q-Opers, QQ-Systems, and Bethe Ansatz", arXiv:2002.07344 (2020), JEMS
  (2024)** — but the key and the URL disagree, so this is a repoint/author call,
  not an add. Do not resolve from the URL.
- **`koroteev-zeitlin2022`** — the Lean URL `arXiv:2108.01557` **does not
  resolve** (no such Koroteev–Zeitlin paper). Closest is **arXiv:2108.04184,
  "q-Opers, QQ-systems, and Bethe Ansatz II: Generalized Minors" (Crelle
  2022)** — a plausible digit-typo, unconfirmed. Needs author confirmation of
  the arXiv id before adding.
- **`ggmw2020`** — the bean's own warning is confirmed: **GGMW = Garoufalidis–
  Gu–Mariño–Wheeler**, and their paper is **"Resurgence of Chern-Simons theory
  at the trivial flat connection", arXiv:2111.04763, CMP 406 (2025)** — a
  2021/2025 work, *not 2020*, and the initialism the Lean expands
  ("Gukov–Garoufalidis–Mariño–Wheeler") is wrong. The Lean anchors "eq (161)",
  which cannot be verified without the PDF. Cross-check against the four
  resurgence PDFs in `library/` before adding; do not resolve from the
  initialism.
- **`murakami1996`** — "Kauffman bracket = Hecke Markov trace" could not be
  disambiguated confidently: the canonical "Jones = Hecke Markov trace" is
  Jones 1987; J. Murakami's Kauffman-polynomial / BMW work is 1987/1990, not
  1996. Needs the author's intended paper.

**Status: 4 errors remain** (was 6), all needing PDF/author input. The four
key-drift repoints (`schrijver1986theory`, `stanley1999`, `neumann-zagier1985`,
`ratcliffe`) and `rockafellar1970` / `bjorner-brenti2005` are confirmed landed
on `main`.

## 2026-09-03 (cont.) — 4 -> 3: ggmw2020 CONFIRMED from library/, added

The library HOLDS the paper: `library/arxiv-2111.04763v2` =
"Resurgence of Chern-Simons theory at the trivial flat connection",
**Garoufalidis, Gu, Mariño, Wheeler** — exact GGMW match (the bean's warning
against the initialism was right; the Lean's "Gukov-…-2020" was wrong on both
the lead author and the year). Added to `references.ts` with the true authors,
arXiv:2111.04763 (2021), CMP 406 (2025); the "eq (161)" anchor is preserved in
the note but was not re-checked against the PDF (equations are not numbered in
the extracted `sections/`).

**Status: 3 errors remain** — `frenkel2020` (URL points to a Koroteev–Zeitlin
paper), `koroteev-zeitlin2022` (Lean arXiv id does not resolve), `murakami1996`
(Kauffman/Hecke, undisambiguated). All three need author input or a
key/URL repoint, not a lookup.

## 2026-09-03 (cont.) — 3 -> 2: the 2 QOper.lean keys resolved (both had wrong URLs)

Bib-triage sub-agent + web search confirmed both QOper.lean keys point at the
WRONG arXiv id, and identified the true papers:

- **`frenkel2020`** -> Frenkel-Koroteev-Sage-Zeitlin, "q-Opers, QQ-Systems, and
  Bethe Ansatz", arXiv:**2002.07344** (2020). The Lean URL was 2007.11786 =
  "Toroidal q-Opers" (Koroteev-Zeitlin) -- a real but DIFFERENT paper. Entry
  added; URL repointed 2007.11786 -> 2002.07344.
- **`koroteev-zeitlin2022`** -> Koroteev-Zeitlin, "q-Opers II: Generalized
  Minors", arXiv:**2108.04184** (Crelle 2022). The Lean URL 2108.01557 does not
  resolve (digit transposition). Entry added; URL repointed.

No DOIs (JEMS/Crelle not verifiable this session). PR #6496 f2d49f15ba.

**Status: 2 errors remain**, both genuine owner-decisions, NOT lookups:
- **`murakami1996`** (JonesPolynomial.lean, "Kauffman bracket = Hecke Markov
  trace"): no clean 1996 Murakami match. Content is already covered by existing
  `jones1987` + `kauffman1987`. Recommend either DROP the redundant `-- Ref:`
  line, or (if a distinct BMW source is wanted) rekey to J. Murakami, Publ.
  RIMS 24 (**1990**) -- the Kauffman *polynomial* / BMW Markov trace, not the
  bracket, and 1990 not 1996. Do not fabricate a 1996 entry.
- **`frenkel-reshetikhin2002`** (quantum-langlands-dual.ts cites[]): no clean FR
  2002 paper. Likely the q-characters / deformed-W-algebra Langlands piece --
  either FR "q-characters ... deformations of W-algebras" (math/9810055, 1999)
  or FR "Deformations of W-algebras" (q-alg/9708006, CMP 197, 1998). Recommend
  rekey to the true year (`...1998`/`...1999`) after owner confirms which.

## 2026-09-04 — FULLY DRAINED (2 -> 0), owner decisions applied

- **murakami1996**: DROPPED. It was one of three `-- Ref:` lines in the
  JonesPolynomial.lean module docstring (not a sorry citation), and its
  "Kauffman bracket = Hecke Markov trace" claim is carried by the two lines
  beside it (`jones1985` + `kauffman1987`). Replaced with an explanatory
  comment; nothing orphaned.
- **frenkel-reshetikhin2002**: REKEYED -> `frenkel-reshetikhin1998`
  ("Deformations of W-algebras associated to simple Lie algebras", CMP 197
  (1998), arXiv:q-alg/9708006) -- the W-algebra duality that IS the
  quantum-Langlands-dual content the block cites. Entry added; the one cites[]
  site updated.

All 19 originally-flagged keys are now resolved: 12 works added/repointed
across this arc, 7 non-citation `[audit]/[probe]/[bean]` keys rekeyed to
`[manuscript]` earlier. PR #6496 cf5ecaf51d. Closing.
