# corpus-grepper — memory

Entry types: **STABLE** · **TRAP** · **BASELINE** (re-measure, never quote).
Seeded 2026-08-29 from `AGENTS.md`. Confirm entries as you use them.

---

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

## STABLE — the library, three tiers

```sh
grep -in <topic> library/INDEX.md              # 320 one-line briefs, ~14k tokens total
cat library/<doc-id>/summary.json              # ~300 tokens: worth opening?
grep -rln <topic> library/<doc-id>/sections/   # the text itself
```

Full-text fallback: `grep -rln <topic> library/*/sections/`. Do not grep
straight into that when a line of `INDEX.md` will do. **But see the `ocr/`
TRAP below — `sections/` is not always the text.**

A section file's YAML front-matter names document, section and page range,
so a hit is immediately citable. `library/<doc-id>/candidates.json` holds
that document's extracted theorems and definitions.

Briefs and summaries are **extractive** — assembled from each document's own
abstract and section titles, nothing model-written — so a brief is only as
good as the abstract behind it.

## TRAP — for some docs `sections/` is BOILERPLATE; the text is in `ocr/`

Path 5 as written reads a file that, for scanned / JSTOR-style docs, holds only
the download banner. Measured 2026-08-30: **25 of 536 library dirs carry an
`ocr/` dir; 10 of the 11 single-section ones hold under 15 % of their OCR bytes
in `sections/`, six under 3 %.** Worked case: `procrsoclondona92` = Moffatt &
Ricca, *Helicity and the Calugareanu invariant* — 4.1 % visible; `Lk = Wr + Tw`
and `H = nΦ²` are in `ocr/page-002.txt` only.

**Add a fourth tier when the topic could sit in an older / scanned paper:**
`grep -rln <topic> library/*/ocr/`. Table + discriminator:
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
  how you find the live carrier.

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

Fresh ID every call, dedupes on nothing. Run the exact-title existence check in
`.claude/skills/local/todo-manager.md` first. An unguarded re-run on 2026-08-04
made **14,688** duplicate beans — 92 % of every open bean — and corrupted a
later agent's corpus-grep. Your searches read `.beans/`; that is why it matters.
Detail: `library-and-staleness-traps.md`.

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

## Resolved topics — where the answer actually lives

Append here whenever a sweep lands. Format: *question → where → verdict →
date*. This is the entry type that saves the most work.

- Groupoid with inequivalent fibre objects carrying a 3-dim `W` whose
  fundamental is not self-dual → bean `qou-dwsh` body (completed
  2026-08-03) → answered; reachable by path 6 only.

- **Why is the integer coordination count `M` the binding multiplier while
  mass carries the q-dim linking weight `lw`?** (bean `qou-brng`, "the
  linking-vs-self-energy route") → **PARTIALLY COVERED, and the target has
  moved.** 2026-08-30.
  - *Still open, and the corpus says so in as many words:*
    `docs/audits/2026-08-30-coordination-saturation-formalized.md`
    §"What stays open" — *"the amplitude assignment … is **not** proved."*
  - *But a `B = Σ_bonds f(bond)` law is scope-(b) EXCLUDED as a TOTAL* by
    `QOU.Mass.PairwiseCumulantVanishing.b3_eq_zero_ofBondFunctional`
    (sorry-free, `f` arbitrary, `μ` bond-dependent) against AME
    `b₃ = +1.426222 MeV`. So "why is `M` the multiplier" cannot be answered
    by any per-bond assembly alone.
  - *The nearest existing derivation* is the Gram-quadratic split
    `B ~ ⟨Σᵢgᵢ⟩²_G = Σᵢ⟨gᵢ⟩²_G + 2Σ_{i<j}⟨gᵢ,gⱼ⟩_G` —
    `docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md`
    Parts 10–13, beans `qou-v0yw` / `qou-vibo`. **Its numbers are stale**
    (convention-C + float64, see the TRAP below); its algebra survives.
  - *Citable rather than re-derivable:* Moffatt–Ricca `procrsoclondona92`
    (`ocr/` only — see the `ocr/` TRAP).

## BASELINE — re-measure, do not quote

| what | command | last seen | when |
|---|---|---|---|
| library size | `git ls-tree -r --name-only origin/main -- library/ \| cut -d/ -f2 \| sort -u \| wc -l` | **536 dirs** (was recorded 332 — that figure was low, not merely old) | 2026-08-30 |
| docs with `ocr/` | same, filtered to `/ocr/` | 25 dirs; 11 single-section; 10 of those <15 % sections/ocr bytes | 2026-08-30 |
| INDEX.md briefs | `wc -l library/INDEX.md` | 320 briefs, ~14k tokens | 2026-08 |
| duplicate works | `docs/audits/library-duplicate-ledger.json` | 19 works held more than once | 2026-08 |

---

## Session log — one line per sweep. Prune this, never the TRAPs.
- 2026-08-30 · `qou-brng` linking-vs-self-energy · **partially covered / target moved** · found on paths 1, 3, 4, 6; the citable source on path 5 was reachable only via `ocr/`.

- **Does the corpus hold "the Markov/Ocneanu trace family over all SU(N)
  specialisations `z_N = q^N/[N]_q` spans exactly `n` of the `p(n)` trace
  functionals, so no combination isolates a >1-dim block character"?**
  → **CLOSED, but on a BRANCH, not `main`.** 2026-09-02.
  - Carrier: `computations/probes/markov_trace_family_rank_probe.py`, commit
    `9f97474c46` (PR #6415), branch `claude/tower-row-cap-sm-binding-2026-09-01`
    — **not on `origin/main`** — plus the `2026-09-02` section of bean
    `qou-brng`. Verbatim same numbers (rank = n at n=2..7, only the two
    1-dim blocks recoverable, `(4,2)` visible-but-not-isolable).
  - **On `main` the result is genuinely absent** — all six paths empty for the
    span-dimension SHAPE.
  - **THREE different things are called "rank" here — resolve before citing:**
    (i) `markov_z_fibre_rank_bar_covariance_probe.py` "fibre rank" = the SU(N)
    index `N`; (ii) `pyhecke_n_generic.gram_inverse_n` "rank" = Gram rank at a
    FIXED z = #{≤2-row λ} (2 at n=3, 3 at n=4); (iii) the span dimension = n.
    A topic-grep for "rank" + "Markov" returns (i) and (ii) and misses (iii).
  - The H₃ coefficients `6.22044128, −33.41778449, 28.19734321` are in **no
    commit reachable from main** (`git log --all -S` empty); only the branch
    probe docstring + the branch bean carry them. The probe's phrase *"the
    corpus carries a three-trace combination at H₃"* is **unsourced**.
  - Adjacent-but-different result that IS on `main`: the >2-row blocks are the
    **TL kernel / Schur–Weyl row cap** (not "hidden information") —
    `QOU/QBeta/TraceBlindSector.lean` header, `qbeta_blind_sector_is_the_tl_kernel_probe.py`,
    bean `qou-i9gk` (completed). That is about `ω_λ = 0`, NOT about span rank.
  - Row cap / hook-content, citable on `main`: `schurPrincipal_eq_zero_iff`
    (`s_λ=0 ⟺ ℓ(λ)>r`, all n/λ/r, sorry-free), `wenzlLevel_conventionD`,
    `ocneanu_param_eq_of_fibre_qdim` (`z·[N]_q=q^N`),
    `computations/schurweyl/ocneanu_weight_general_n.py`,
    `docs/audits/2026-08-16-wenzl-level-family.md`. **Caveat:**
    `IsOcneanuWeightSystem` is class-carried with **no instance**.
  - Over-generalising an n=3 coincidence is a **named recurring defect** here:
    `qbeta_rank_one_identity_is_n3_only_probe.py` + PR #5337 (*"do not
    generalise the n=3 coincidence"*).
  - **Not classical from held sources.** Library has the p(n) side
    (`arxiv-2409.09372v4`: Irr is a basis of trace functions) and a BMW
    trace-space dimension (`arxiv-1403.4021v2`, ≤3), but **no rank = n**.
    **Wenzl 1988 (Invent. Math. 92) is cited in `references.ts` and NOT
    ingested** — the obvious place the classical statement would live.
