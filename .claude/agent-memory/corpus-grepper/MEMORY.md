# corpus-grepper — memory

Entry types: **STABLE** · **TRAP** · **BASELINE** (re-measure, never quote).
Seeded 2026-08-29 from `AGENTS.md`. Confirm entries as you use them.

---

## STABLE — step 0: `corpus_search` (MCP), before any grep

All six paths below are greps, and they share one blind spot: a grep finds
prior work only if it used **your** words. Work written in different words is
the case that actually costs a session — the grep comes back empty and reads
as a clean bill.

`corpus_search` seeds lexically and then expands along the knowledge graph,
across the authored corpus and the ingested library at once. A block that
never says "Temperley-Lieb" but `uses` one that does is one hop from the query.

Read three fields. **`why`** — MATCHED vs REACHED, and by which edge; a `~`
prefix means the edge ran backwards, so that node depends on the seed rather
than the reverse. **`seedsByProvenance`** — many ingested hits with no authored
ones means *cite it*, not *derive it*. **`emptyRoots`** — a directory present
but holding no graph nodes; an ungenerated `.jsonld` corpus answers every query
with a silence indistinguishable from "nobody has done this".

It does not replace the six: it seeds on labels, titles, kinds and tags
(`searchText: true` for companion prose), so a topic named only inside a proof
body is still a grep's job.

## TRAP — an empty `corpus_search` is not evidence until you have read `emptyRoots`

Added 2026-09-03, from the run that generated the graph. Before that day the
qou graph was **empty**: 3595 authored blocks, 576 library documents, **zero**
`.jsonld`. Every graph-backed query returned nothing and returned it in the
shape of "no results" rather than "nothing was indexed". The distinction is the
entire value of the field, so check it before treating an empty answer as an
absence — this is the same failure the tool exists to prevent, one level up.

## STABLE — the six paths, in order

All six must return empty (modulo the originating file) before anything is
declared open. A source file's own `## Status` / `Open math` note is **not
authoritative** — the corpus is.

1. `grep -rln <topic> docs/audits/` — owner-authorised resolutions land here
   first; the originating file's status note can lag by months.
2. `grep -rln <topic> content/` — **whole tree**, not just the chapter you
   started in. Conjectures cross-cut chapters.
3. `grep -rln <topic> computations/` — implemented Python may already
   realise what a source file calls open.
4. `docs/coordination/<theme>.md` — the ledgers. A prior agent may have
   closed it.
5. **`library/`, three tiers, cheapest first** — see below.
6. **`.beans/`** — `grep -rl <topic> .beans/`. See the TRAP below; this is
   the path most often skipped and the one that most often holds the answer.

## STABLE — the library: read [`library-and-staleness-traps.md`](library-and-staleness-traps.md)
Three tiers (`INDEX.md` -> `summary.json` -> `sections/`) plus the fourth (`ocr/`),
with counts and commands. The traps below stay here — they are what gets skipped.

## TRAP — for some docs `sections/` is BOILERPLATE; the text is in `ocr/`

25 of 542 library dirs keep their real text in `ocr/`, and the documented
`sections/` grep cannot see it. Worked cases and the measured share:
`library-and-staleness-traps.md`.

## TRAP — `uploads/` is invisible to path 5

`uploads/` and `library/` are **two stages of one pipeline, not a rename**.
A PDF sits in `uploads/` until it is processed into `library/<doc-id>/`, and
`uploads/` stays live for the next drop. Path 5 searches `library/` only, so
an un-ingested paper will not be found by any "has the corpus got this?"
check — which is exactly how a held source gets re-derived.
`scripts/migrate-uploads-to-library.py` moves one across.

(`AGENTS.md` said "renamed from uploads/ 2026-08-15" until corrected
2026-08-25; reading it that way makes a live queue look like a dead alias.)

## TRAP — the library holds 19 works more than once

Extra copies keep their text on disk, so a full-text grep lands in them.
Each carries `duplicate_of` in its section front-matter naming the copy to
prefer. **Two hits on one work are not two sources.** Neumann–Zagier is
present three times. Adjudicated in
`docs/audits/library-duplicate-ledger.json`.
`scripts/library-find-duplicates.py` *proposes*; its same-work and
different-work score ranges overlap, so a proposal is not a verdict — a
sequel sharing its setup sections outscores four true duplicates.

## TRAP — the beans path is not reachable from paths 1–5

`.beans/` is not under `docs/`, `content/`, `computations/` or `library/`,
and a coordination ledger is a different file. It is a corpus in its own
right (tens of thousands of files) and it is where a prior agent's
*conclusion* usually sits before it reaches an audit doc or a block.

Read `status` and the **whole body**, not the title:

- a **`completed`** bean is the one that bites — the answer may be a single
  sentence in the body with no artifact anywhere else;
- a **`scrapped`** bean usually names the bean that superseded it, which is
  how you find the live carrier;
- and when you are **appending** to a bean, read the whole file before you
  write — the destination is the source you are skipping. 2026-09-03
  (`qou-zrx2`): I wrote "no closed form was identified" two sections below
  "the floor has a CLOSED FORM" and "the floor is DERIVED", having read the
  bean with `tail -60`.

Worked case (added 2026-08-26 after a PR re-derived two held results): the
trail ran `qou-8pl3` → `qou-8p1i` (scrapped) → `qou-dwsh` (completed,
2026-08-03), whose body states the conclusion the PR spent a tranche
proving. Paths 1–5 cannot reach that sentence.

## TRAP — a sibling's bean is not a primary source either

The "not authoritative, the corpus is" rule applies to beans verbatim,
including beans by other agents that look authoritative because they are
specific and recent. Worked case: bean `qou-q7lf` reports a scipy-sparse
boundary in `hecke_core_legacy.unified_iterative_correction`; commits
`da645cf0f32` and `46dcfc62a57` fixed exactly that site the next day. The
bean was stale and was believed over the code.

**And the sharper version, 2026-09-04: I cited a bean for the OPPOSITE of what
it says.** I wrote "anything carrying SPIN … (the same wall bean `qou-7zob`
reaches from the flavour side)" into five merged artifacts. `qou-7zob` does not
reach that wall — it *refutes* the spin route, in its own body, via the Pauli
lock (`S=1 ⟺ T=0`), and `InterfaceScalar.separable_interface_degenerate` proves
it sorry-free. I had matched the bean on **topic** and cited it on **agreement**
without reading it. A bean cited in support is a bean you must have read to the
end; its title tells you the subject, never the verdict.

## TRAP — two ways a `content/` grep lies about coverage (2026-09-04)

**1. Vendored Mathlib sits UNDER `content/`.** `content/quantum-observable-universe/lean/.lake/packages/mathlib/`.
A `find content` list is 20,472 files; excluding `/.lake/` it is **12,427** — every
naive `content/` count inflated ~65 %, and `hyperbolic metric` / `uniformizer` /
`Poincare` return Mathlib docstrings as corpus hits. **Filter `/\.lake/` first.**

**2. `Fuchsian` here is an ODE homonym.** All six `content/` hits are the Fuchsian
**singular point** of the C1 difference equation (`C1FuchsianExponents.lean`,
indicial `c₀² + (q−1)c₀ + (q−1) = 0`). **None is a discrete subgroup of `PSL₂(ℝ)`** —
so the count measures irregular-singularity work, not uniformisation. Same family
as `sasaki`-the-surname: check what hits ARE before reading a count as coverage.

## TRAP — "held" is not "held in full", and `references.ts` records the page count

2026-09-04. `[thurston1978]` is registered with `library: { docId: "thurston",
pages: 33, sections: 22 }`. **That is Chapters 1-2 of a ~370-page book.** Measured
inside the held copy: `gluing equation` **0**, `hyperbolization` **0**,
`figure-eight` **0**. Against **113 citers**, several with explicit Ch. 4 locators
(`shared-denominator-cusp-holonomy.lean:91` "§4.5 (gluing equations)";
`ManifoldVolumeBridge.lean:112` "Ch. 4"). The attribution is right; the holding is
partial, so **path 5 for the cited topic never lands in the cited directory** —
the exact failure path 5 exists to prevent, wearing a green light.

**Check `library.pages` against the locator before treating a hit as coverage**,
and grep the held copy for the cited phrase rather than for the author.

Three cheap discriminators (held-vs-registered; held-but-UNregistered;
a `-- Ref:` key resolving to nothing) — `library-and-staleness-traps.md`.

## TRAP — grep the claim SHAPE, not only the topic

Four conflations reached durable artifacts in one session (2026-08-15), each
having survived a topic-grep. Read the declaration's **type**, and check:

1. **One proposition, or a family?** (`kappa_vanishes : ℕ → Prop` is indexed.)
2. **Pointwise, or the universal closure?** (`v ↔ ∀P, Pred P` is trivial.)
3. **Shared type, or shared instance?** (two legs at different values.)
4. **Set-level premise, truth-value conclusion?** (independent claims.)

Also check the **binder generality** — it decides scope. Worked 2026-08-30:
`b3_eq_zero_ofBondFunctional (f : R → R) (μ : Fin 4 → Fin 4 → R)` quantifies
over *every* bond functional and allows *bond-dependent* weights, so it excludes
a whole assembly class, not one ansatz — but `Fin 4` fixes `A = 4`, so "for all
`A`" is not what was proved.

Criterion `da-arity-conflation` in
`.claude/skills/local/devils-advocate-watcher.md` carries the worked
examples and why a machine checker cannot do this.

## TRAP — `beans create` is not idempotent
Exact-title check before every create; an unguarded re-run made 14,688
duplicates and corrupted a later corpus-grep. Detail: `library-and-staleness-traps.md`.

## TRAP — an inherited "X is unavailable" is HALF a measurement

2026-09-03: the corpus said *"the ptolemy DB is firewalled; only `4_1`/`5_2`/
`3_1` ship Magma fixtures"*. I carried both halves into a PR body, a bean and a
report. **Firewall: real** (403 on CONNECT, re-verified two ways). **Fixture
list: wrong** — the wheel ships **seven** manifolds; nobody had run `ls`.

**The shape: a claim bundling an ENVIRONMENT fact (a host is blocked) with a
CORPUS fact (what we hold locally).** The environment half ages slowly and is
usually right; the local half is cheap to check and is the one that is wrong.
Enumerate the local surface yourself before repeating either half.

## STABLE — refutation scoping

- **(a) scope-limited negative** — "this construction, *alone*, does not
  reproduce the numbers as-is." This is what a failed numerical probe
  actually shows. **Default to this phrasing.**
- **(b) structural exclusion** — "this ingredient cannot appear in any
  closure." Permitted only with a **proved invariant**: parity/sign, a
  dimension/orbit-count/degree bound, a Lean-proved impossibility, an
  entropy or precision bound. **Cite it.**

Two permanence principles that make most (b) claims wrong: a Lean-proved or
structurally-exact piece stays a correct contribution even while the total
is inaccurate; and a compositional/trace object is already many-body, so
"pairwise can't do it" against `1 − ∏ᵢ fᵢ` is a category error — the probe
measures the size of the missing higher term, it does not exclude the
factor.

Found an over-claimed (b)? Re-scope to (a). Do not delete the finding — the
numerical result stands, only the scope was wrong.

## TRAP — your own two halves disagreeing is a BUG, not a refutation

Testing `tr_M|_(q=1) = 2^(c-n)` for the classical binding floor I got
`c_free = 6` from a cycle count and `tr_M(W_free) = 1/4` from Richardson —
and `1/4 = 2^(c-6)` forces `c = 4`. I published that disagreement as a
refutation of the formula rather than a bug in the count (it was the count:
the permutation is `(0 1)(3 4)`, 4 cycles). The mechanism was the corpus's
own **derived** one, in a probe, a sorry-free Lean file, and the bean I was
appending to. Check a refutation against every other number **in your own
probe** before you write it down. `qou-zrx2`.

**Second instance, three days apart, a different session** (`qou-brng`,
`0be7d66fad`): a Lean exclusion re-proved that `qou-edt7` had landed four
days earlier and proved more generally, plus a "surviving escape" ratio that
was the corpus's own `w(2)/w(1)` with the obvious mechanism already refuted
there. Their generalisation is the one to carry: **a "next direction" line in
a bean or PR body is a novelty claim and needs the checklist exactly as much
as an "open" declaration does** — and run it BEFORE merging, not after.

## Resolved topics — where the answer actually lives

A lookup table, consulted when a specific topic
comes up. In `resolved-topics.md` — read it before declaring any of
these open, and add a row whenever a sweep settles one.

- **Exchange-sensitive NON-trace invariant of the six-strand two-nucleon link
  for the T=0/T=1 ratio 33.7055?** → `resolved-topics.md` (2026-09-03). Open as
  a *class*; the **linking-data subclass is closed** scope-(b) (`lk` IS `I₃`,
  both channels at `I₃ = 0`); the exchange OPERATOR is closed three times over.

## BASELINE — re-measure, do not quote

| what | command | last seen | when |
|---|---|---|---|
| library size | `git ls-tree -r --name-only origin/main -- library/ \| cut -d/ -f2 \| sort -u \| wc -l` | **536 dirs** (was recorded 332 — that figure was low, not merely old) | 2026-08-30 |
| docs with `ocr/` | same, filtered to `/ocr/` | 25 dirs; 11 single-section; 10 of those <15 % sections/ocr bytes | 2026-08-30 |
| INDEX.md briefs | `wc -l library/INDEX.md` | 320 briefs, ~14k tokens | 2026-08 |
| duplicate works | ledger = `docs/audits/library-duplicate-ledger.json`; machine marks = `grep -rl duplicate_of library/*/sections/ \| cut -d/ -f2 \| sort -u \| wc -l` | **ledger 4** (hand-adjudicated DETECTOR MISSES only) vs **23 dirs** front-matter-marked. The old "19 works" conflated the two. | 2026-09-04 |

---

## Session log — one line per sweep. Prune this, never the TRAPs.
- 2026-09-03 · `qou-brng` six-strand non-trace invariant · open as a class, linking-data subclass closed scope-(b) · `resolved-topics.md`.
- 2026-09-04 · `qou-xlw1` contact-distribution rank / dim 7 / `J` on `ker Θ` · **both `ker Θ` ranks are DERIVED (scope-(b) contradiction); no 7-manifold; `J` on `ker Θ` is present in 7 prose sites and in NO Lean** · detail in `resolved-topics.md`. TRAP: the site count (2 vs 9) answers the rank question backwards — count CONSUMERS, not assertions.
- 2026-09-04 · `qou-xlw1` hyperbolic volume as a QOU structure · **I claimed it was 'imported, not QOU' and that Mathlib+library held nothing — WRONG on all three.** ~180 QOU .lean files; VC numerically CONFIRMED for 4₁. Weakest link is a TYPE (`BlochWignerD : ℝ → ℝ` vs the corpus's own proof that D vanishes on ℝ). Bring's ℍ²↔H³ link genuinely open, 0 beans. Detail in `resolved-topics.md`.
- 2026-09-04 · `qou-8lxd` CITATION-gap inventory for the hyperbolic-volume/eightfold arc · 15 beans, `docs/audits/2026-09-04-citation-gap-inventory.md`; **held-but-partial and held-but-unregistered are two new classes** — detail in `resolved-topics.md`.
