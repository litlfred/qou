---
# qou-kcii
title: habiro-coefficients-extended.witness.json exists twice, with different q0Anchor
status: in-progress
type: task
priority: normal
created_at: 2026-08-21T15:05:02Z
updated_at: 2026-09-07T17:39:31Z
---

Found 2026-08-21 diagnosing qou-3zby (the red L1 tr_M gate).

  computations/habiro-coefficients-extended.witness.json        q0Anchor=ambiguous
  computations/habiro/habiro-coefficients-extended.witness.json q0Anchor=ABSENT

Identical payload (json-equal 'data') and identical scriptHash 6fdad0d63cff,
both computedAt 2026-07-18. They differ ONLY in the anchor field.

Why it matters beyond tidiness: which copy you get depends on how you
resolve the name. The gate uses _path_bridge.witness_path and gets the
top-level one. A probe I wrote used rglob and got the OTHER one, and
reported the wrong q0Anchor for its headline input until I caught it. Two
files with the same name, the same hash, and different provenance metadata
is a trap for exactly the kind of audit that reads witnesses by stem -- and
several do.

Not fixed in that PR: deciding which copy is canonical (and whether
'ambiguous' or absent is the right label for it) is the Habiro arc's call,
not a bystander's. Note the anchor question is live -- Habiro's values are
measured at the PROTON pin (qou-3zby), so 'ambiguous' may itself be wrong.

Cheap check for whoever takes it: are there OTHER duplicated witness stems?
The one-liner is a find | basename | sort | uniq -d over computations/.


## MEASURED: it is 25 stems, not one — and none is a harmless copy

  duplicated witness stems in computations/ (excl. _deprecated) : 25
    payload identical, same anchor  :  0
    payload identical, anchor differs: 0
    PAYLOAD DIFFERS                 : 25

Every single duplicated stem holds two DIFFERENT results under one name.
Contradictory anchors are common among them:

  alpha-k-jones-markov-h3        None      vs proton
  alpha-k-jones-markov-h4        None      vs proton
  geom-leading-alt-q-locality    None      vs proton
  pentagon-to-borromean-h4       ambiguous vs proton
  per-knot-density-borromean-h4  None      vs proton
  habiro-coefficients-extended   ambiguous vs None
  q0-consistency-audit           None      vs None
  e0-calibration-audit           None      vs None

Note e0-calibration-audit and q0-consistency-audit are in the list: two of
the AUDIT witnesses are themselves duplicated with differing payloads.

CORRECTION to my own first measurement. I initially reported habiro's two
copies as 'identical payload' -- that compared only the  block. A
whole-document comparison (excluding computedAt/commitSha/durationMs/
scriptHash/engineVersion/environment) shows they differ. My first classifier
then had a second bug: it left q0Anchor INSIDE the payload comparison, so
the 'anchor differs' bucket was unreachable and everything fell into
'payload differs' for the wrong reason. Both fixed; the 25 stands under the
corrected classifier.

Reproduce:
  find computations -name '*.witness.json' -not -path '*_deprecated*' \
    | xargs -n1 basename | sort | uniq -d

Which copy a consumer gets depends on how it resolves the name --
_path_bridge.witness_path vs rglob vs a hardcoded path. That is not a
theoretical risk: it already produced one wrong reading (qou-3zby probe,
caught pre-commit).


## Correction: the two copies are NOT payload-identical (2026-08-23)

Commit `667c9ab3f6`, which flagged this duplicate, describes the two files
as having *"identical payload and scriptHash but different q0Anchor"*. The
scriptHash half is right; **the payload half is wrong**, and it is wrong on
the field that matters.

Measured on both files:

    same scriptHash   : True   (6fdad0d63cff)
    payload identical : False
    file size         : 23857 B  (computations/)  vs  1892 B  (computations/habiro/)

    only in A         : q0Anchor
    only in B         : engineVersion
    shared keys DIFFERING: results, commitSha, computedAt, engine, scriptCommitSha

**`results` differs.** So this is not a benign copy that merely disagrees
about its anchor label — the two files disagree about the numbers, while
advertising the same producer hash. A consumer resolving the wrong path gets
different mathematics, not just a different label, and `scriptHash` gives no
warning because it matches.

That raises the priority of this bean: the duplicate is a correctness hazard,
not a tidiness issue. It also means whichever copy is regenerated to drain the
pin straddle (`qou-3zby` / `qou-dau6`), the OTHER copy stays stale and
silently wrong.

Note the 12x size difference suggests one is a truncated or partial write
rather than a full second run — worth establishing which is authoritative
before deleting either.


## The second copy is not data at all — it is a PRE-FIX FAILED RUN (2026-08-23)

Sharpens the correction above. `computations/habiro/habiro-coefficients-extended.witness.json`
does not hold different numbers; it holds **no numbers**. All four isotope
keys are error records:

    D (deuteron, A=2)  {'error': 'ValueError: LaurentQ.from_sympy: non-Laurent factor ...'}
    T (triton, A=3)    same
    3He (helion, A=3)  same
    4He (alpha, A=4)   same

That is why it is 1892 B against the top-level copy's 23857 B — it is a
**failed regeneration attempt that got committed**, not a second successful run.

**Dating it: this predates PR #5376.** Per `qou-iayk`, the LaurentQ parser
fix landed in #5376 and the producer then runs **4/4 clean**. So this file
captures the failure mode that fix removed. It is stale in the strongest
sense — not merely out of date, but a record of an error that no longer
occurs.

**Consequence for the disposition.** The earlier note asked which copy is
authoritative before deleting either. That question is now answered: the
top-level copy is the only one carrying data, and the `habiro/` copy has no
recoverable content to preserve. It still must not be deleted casually — a
consumer may resolve that path (the `667c9ab3f6` probe did exactly that,
via `rglob`) and would then read an error record as though it were a
witness. Fix the resolution, then remove the artifact.

**Not the regeneration blocker.** Do not read this as the reason Habiro
cannot be regenerated. Per `qou-iayk` the parser error is FIXED; the live
blocker is that the fresh values contradict a landed D(u) closed-form law
that the old witness satisfies exactly. Different problem, different bean.


## The MECHANISM is undetected: 6 sites bypass the resolver (2026-08-23)

`duplicate_witness_stem_audit` measures the duplication and, better, the
7 consumer-splitting stems. It does **not** detect the mechanism by which the
incident in its own docstring happened — *"a probe used `rglob` instead of
the resolver, read the other copy, and reported the wrong q0Anchor"*. Its
only `rglob` references are that narrative and its own sweeps.

So a recurrence would not be caught. Six sites resolve a witness or producer
**recursively by name and take one**, without calling
`_path_bridge.witness_path`:

    computations/q0_muon_reproduction_sweep.py    L105   return w      (first match)
    computations/witness_padding_provenance.py    L209   hits[0]
    computations/producer_repad_sweep.py          L159   hits[0]
    computations/witness_provenance_audit.py      L356   return cand   (first match)
    computations/q0_repin_sweep.py                L332   break         (first non-deprecated)
    scripts/convention-c-taint.py                 L108   return first

Spot-verified on three of them: none references `witness_path` at all.

**Why 'first match' is not a tie-break.** `Path.rglob` yields in
`os.scandir` order — filesystem-dependent, and **not** sorted. Several of
these sites do not wrap it in `sorted()`. So the copy chosen is not merely
*a* deterministic wrong one; it can differ between machines and between runs
after unrelated file churn. That is the worst failure shape for a witness
read: silent, and not reproducible from the source.

**Scope, honestly.** This is the *capability* to pick wrong. I have NOT
established that any of the six currently resolves one of the 25 ambiguous
stems — that needs per-call-site tracing of what names reach each. Read it as
'the guard rail is absent here', not as six live defects. Four of the six are
sweep/audit drivers, where a wrong pick corrupts a report rather than a
published number; `witness_provenance_audit` is itself an audit.

**Cheapest fix, if wanted:** route these through `witness_path`, which
already implements the prefer-dir search order. Failing that, `sorted()` at
minimum, and a hard error on `len(hits) > 1` rather than a silent `[0]`.

Not building a detector for this here — if it should be gated, the existing
`duplicate_witness_stem_audit` is its natural home rather than a second
script scanning the same tree.


## Six bypasses fixed; the resolver itself was one too (PR #5589, 2026-08-23)

Measured first: **25 duplicated stems, 6 consumer-splitting** — not 7. The
habiro fix removed one. Do not quote the 7.

### The root cause was in `witness_path`, not only in the bypasses

`_path_bridge._WITNESS_DIRS` was built from an **unsorted** `_HERE.iterdir()`,
so the canonical resolver the six sites were meant to be routed *to* carried
the same defect they did. Measured cluster tail before the fix:
`phase5, a_operator, markov, probes, substrate, alpha, audits, habiro, sweeps,
qbeta, hecke`. Sorted now. Verified over 500 (consumer dir, duplicated stem)
pairs: **0 resolutions moved** — it removes nondeterminism, it does not move a
number.

Note `duplicate_witness_stem_audit._cluster_dirs()` claims to mirror
`_WITNESS_DIRS` but always sorted, so the audit's predictions and actual
behaviour could disagree. They now genuinely agree.

### Two of the six were LIVE defects, not latent capability

The bean scoped these as "the capability to pick wrong". For two that was too
generous:

**`q0_muon_reproduction_sweep` was self-certifying.** `run_one` resolves the
path ONCE, reads its committed text, runs the producer, then reads `fresh`
back *from the same path*. `_witness_for` preferred the `computations/` ROOT,
but producers emit beside themselves — so for a cluster-resident producer with
a stale root copy, the producer rewrote the cluster file while the sweep
re-read the untouched root file. committed == fresh, empty diff, **PASS
printed for a producer never verified**. Measured over the 623-entry manifest:
**17** producers in that position (adjacent_vs_full_probe,
alpha_k_jones_markov_h3/h4, eleven probes/ entries). The rglob fallback also
had no `_deprecated` filter and sent `hecke_character_symbolic` into
`_deprecated/`. Fixed to `witness_path(name, producer.parent)`; 622 resolved,
605 unchanged, exactly those 17 moved, `_deprecated` 1 → 0.

**`convention-c-taint` read three producers' edges out of `_deprecated/`.**
`_read_source`'s fallback had no `_deprecated` filter, and `_deprecated/`
precedes `probes/`/`audits/` in this tree's scandir order:
`path_b_habiro_mass_probe`, `rho_k_markov_multiplicativity_probe`,
`term5_aK_audit` all had their read-edges extracted from retired source. Wrong
edges in a convention-C taint fixpoint are the thing the script exists to
compute. Graph moved 3617 → 3606 edges over 5 producers; ruled out my own
harness by running the committed `build_graph` twice (0 differences).

`witness_provenance_audit.py` there is **the first demonstrated consequence of
qou-2r42**: the old code read the ROOT correctness audit and attributed its
edges — including its own test fixtures `foo-bar`, `x`, `mine`, `anything`,
`orphan` — to `audits/witness-provenance-audit.witness.json`, which the
**audits/ I14 completeness audit** produces. Nineteen bogus edges out, eight
real ones (q-pinning-50-digit, methodology-deprecation, the
-audit/-scan/-compliance suffixes) in.

The other four sites: `witness_padding_provenance` and `producer_repad_sweep`
(sorted + refuse an ambiguous basename rather than blind-pick; the latter also
now resolves beside the witness that names it, which fixes it deterministically
picking the WRONG `witness_provenance_audit.py`), `witness_provenance_audit`
itself (its `{p.name: p}` producer index was **last-wins over an unsorted
rglob** — a 7th site, in the file the bean already named; verified
protective-only: 2437 witnesses, **0 verdicts changed**), and `q0_repin_sweep`
(before/after snapshots each ran their **own** rglob across the producer's run,
so `rel_moves` could compare the before-text of one file to the after-text of
another; resolved once now — 609 pairs, 16 moved, and those 16 are exactly the
pairs with >1 copy).

### The mechanism is now detected — `--bypasses`

Added to `duplicate_witness_stem_audit` (its natural home, as this bean said).
AST-based: flags `[index]`, `next()`, first-hit `break`, basename-keyed
comprehensions, and `hits = list(...)` → `hits[0]`; recognises `sorted()`
structurally.

**Back-testing it mattered more than writing it.** On the fixed tree it reports
a clean 0 LIVE, which proves nothing. Run against the `origin/main` sources it
flags all six files at 11 sites — 105, 209, 159, 356+364, 176+344+382, 108 —
matching every line this bean names (the L332 recorded here had drifted to
344). The **first** version missed two of the six: it walked only the
expression tree, so `hits = list(...)` … `hits[0]` was invisible while it
flagged an unrelated `sorted()` comprehension a few lines above. Adding
assignment-then-subscript tracking also took the tree-wide count from 8
unordered sites to **17** — nine that were there all along and unseen.

## The 25 duplicates: disposition, and why NOTHING was deleted

Compared both copies of every stem with the ephemeral set masked (computedAt /
commitSha / durationMs / scriptHash / engineVersion / environment /
invocation):

    copies identical after masking provenance : 0
    copies genuinely differ in content        : 25

**No pair is a harmless copy.** So consolidating any of them changes what some
consumer reads, and since `witness_path` searches the root before the clusters,
deleting a stale root copy silently flips every non-cluster consumer onto
different numbers. That is the outcome this bean exists to prevent, so no
witness was deleted.

Which copy is LIVE is nonetheless decidable for 23 of 25, and the shape is
uniform: the producer sits in a cluster dir and writes `Path(__file__).parent`,
so the **cluster copy is written and the root copy is a pre-refactor leftover
no producer touches**. This is the habiro failure mode generalised — and
inverted: habiro's producer wrote the cluster copy nobody read, and was
repointed to the root; here the producers write the cluster copy while
`witness_path` hands most consumers the root one.

Not decidable, left alone:

- **`qbeta-phib-2loop-bdictionary`** — two genuinely different producers share
  a basename AND their witnesses share a basename; both witnesses record the
  same `scriptFile`, and the top-level keys differ (`context` vs `data`). The
  answer is a rename by the qβ arc, not a deletion. It is also the one
  cluster-vs-cluster pair, i.e. the only stem where `_WITNESS_DIRS` ordering is
  load-bearing. **The convention-c-taint fix moved this producer's resolution
  probes/ → qbeta/ — that is arbitrary, follows from `docs` last-wins aliasing,
  and is NOT claimed as a fix.**
- **`e0-calibration-audit`** — neither copy records a `scriptFile`. The
  producer (`audits/e0_calibration_audit.py`) writes `HERE/` = `audits/`, so
  the root copy is the leftover; but it is **50902 B against 1868 B** with the
  same key set, i.e. the retired run reported far more findings. Worth an
  owner's eye before either is touched.
- **`q0-consistency-audit`** — `audits/` copy is 64284 B and producer-written;
  the root copy is 1023 B with a **different schema** (`new_proton_q0`,
  `old_muon_q0`, `timestamp`, none of which appear in the live one). Live
  consumer `witness_constant_staleness.py` currently resolves to that 1 KB
  stale-schema copy.
- **`option-e-deuteron-delta-lambda-probe`** — the only producer writes
  `probes/`, yet the **root** copy carries today's `computedAt` (2026-08-23)
  and the probes/ copy 2026-07-19. Something refreshed a copy its producer does
  not write. Most root copies in this set went stale while their cluster twin
  was refreshed today; this one is the other way round. Unexplained — recorded,
  not guessed at.

### Follow-ups (not done here, deliberately)

1. Consolidating the 23 decidable pairs is a **per-consumer** job, not a
   deletion sweep: each needs its readers re-pointed before the leftover goes,
   because no pair is content-identical.
2. The 17 latent unordered glob sites `--bypasses` now lists.
3. `qbeta-phib-2loop-bdictionary`: rename, qβ arc's call.


## 2026-09-06 — both open items answered: the duplicate is GONE and the cheap check is now a permanent audit

Found by `scripts/bean-staleness-triage.py` (16th of 291 artifact beans, 19
commits over its named paths since 2026-08-23).

### 1. The bean's own instance is resolved

`find computations -name 'habiro-coefficients-extended.witness.json'` returns
**one** file — `computations/habiro-coefficients-extended.witness.json`,
`q0Anchor: muon`, regenerated 2026-08-30. The `computations/habiro/` copy is
gone.

**And the producer now carries the fix with this bean's own diagnosis in its
source.** `habiro_coefficients_extended.py:205-217` writes to
`_COMPUTATIONS / "habiro-coefficients-extended.witness.json"` and explains why:

> This previously wrote `HERE / …`, i.e. `computations/habiro/`. Every consumer
> that matters reads the `computations/` root — `cross_check_trM_1ppb` (the L1
> gate), `d_u_closed_form_proof`, `mass_formula_6term_mpfr_50dps` — so the
> producer refreshed a copy nobody reads while the copy everybody reads went
> stale. … Bean `qou-kcii`.

It also **deliberately does not use `_path_bridge.witness_path` for output**,
naming the exact trap this bean reported: *"it searches `prefer_dir` first,
which is what handed a habiro/-local probe the dead error-record copy and made
it report the wrong `q0Anchor` (667c9ab3f6)."*

That is the same finding this bean made, reached independently and fixed at the
producer — the strongest possible disposition for it.

### 2. The "cheap check for whoever takes it" — done, and permanentised

The bean proposes *"a `find | basename | sort | uniq -d` over `computations/`"*.
That exists as
[`computations/audits/duplicate_witness_stem_audit.py`](computations/audits/duplicate_witness_stem_audit.py),
and it is better than the one-liner: it reports, per duplicated stem, **which
copy each consumer reads**.

    witness stems duplicated across paths : 27
    of those, CONSUMERS DIVERGE on        :  8

**Run the one-liner too, and reconcile — the numbers differ and both are
right.** My raw `find | uniq -d` gives **53**; the audit gives **27**. The
difference is exactly the `_deprecated/` tree: excluding it gives 27, so
`53 = 27 live + 26 involving a deprecated copy`. Quote 27 for live surface.

The eight where a "cleanup" would change what code reads:

    adjacent-vs-full-probe            alpha-k-jones-markov-h3
    alpha-k-jones-markov-h4           hecke-core-symbolic-migration
    option-e-deuteron-delta-lambda-probe   pentagon-rt-torus-knot-higgs-probe
    q0-consistency-audit              qbeta-phib-2loop-bdictionary

The audit is careful about its own limits (*"these are REFERENCES, not verified
reads: the scan is textual"*) and declines to gate, pointing at `qou-2r42` for a
pair where consolidating by name would swap one audit for a different one. So
this bean's follow-up question is answered and owned; it does not need to
re-ask it.

### 3. One thread I did NOT close, named rather than guessed

The bean's live worry was *"Habiro's values are measured at the PROTON pin
(`qou-3zby`), so 'ambiguous' may itself be wrong."* The label is now `muon`, and
the stamp is **internally consistent**: the recorded `q0Value` is
`1.109978595642739046681795…`, which is the live muon pin to **0.0 ppb** and
**11.6141 ppb** from the proton pin.

But that verifies the *stamp against itself*, not the payload's layer. Two facts
sit oddly together and I have not reconciled them:

* `habiro_coefficients_extended` is in **none** of the manifest's three lists
  (`ideal_muon` / `physical_proton` / `ambiguous`), and `q_parameter` selects by
  `if _stem in _man["ideal_muon"]`, so an untagged stem resolves to **proton**.
* Its arithmetic is **symbolic** — line 98 takes `q` as a free sympy symbol —
  so the producer chooses no numeric pin at all.

An untagged, symbolic producer whose witness nonetheless stamps `muon` is not
obviously wrong (a symbolic result is anchor-free, and the stamp may be recording
the evaluation point a consumer uses), but it is not obviously right either, and
I could not find where `stamp_staleness_metadata` sources the anchor. **Whether
this is correct or a straddle is unresolved**; it is the `qou-aj91` "67 untagged"
shape, one instance. Not asserted as a defect.


## The raw-float64 consequence: both copies are baselined, and only one drains

Found 2026-09-07 from the drain side (`qou-r47m`), and it is a concrete cost of
this duplication rather than another instance of it. The count is **27** stems
now, up from the 25 measured above.

`computations/raw-float64-baseline.json` keys witnesses by PATH, so a duplicated
stem gets **two entries** and the same quantity is counted twice in the backlog.
Worse, the producer writes only one of them, so re-running drains only that one
and the other sits at its baselined count forever.

Worked instance, measured:

| path | size | baselined dirty | touched by a re-run? |
|---|---|---|---|
| `computations/pentagon-rt-torus-knot-higgs-probe.witness.json` | 29,293 B | **346** | **no** |
| `computations/probes/pentagon-rt-torus-knot-higgs-probe.witness.json` | 49,364 B | 0 | yes |

The producer is `computations/probes/pentagon_rt_torus_knot_higgs_probe.py` and
writes beside itself. Running it changed the `probes/` copy and left the
top-level one untouched — confirmed by `git status`, not inferred. Its source
already carries the fix (its own comment: *"These were `float()` at
construction, which is where 389 raw float64 fields entered a witness"*), so the
top-level copy is a pre-fix artifact that no producer can reach.

Same shape, from the table of duplicated stems: `pentagon-to-borromean-h4-probe`
(216 dirty top-level, 0 in `probes/`). The other 25 pairs mostly carry EQUAL
dirty counts on both sides (`adjacent-vs-full-probe` 276/276,
`ew-couplings-substrate-derivation-probe` 178/176), which is the double-count
case rather than the orphan case.

**Not proposing a fix here** — which copy is canonical is this bean's open
question and, per the note above, the owning arc's call rather than a
bystander's. Recording only that the duplication has a measurable cost in a
second place, and that any backlog figure quoted from the baseline is inflated
by the duplicated stems.


---

## A SECOND, larger double-count in the same baseline — and it is not the one recorded above (2026-09-07)

This bean records that duplicated witness stems are **double-counted** in `raw-float64-baseline.json` because the baseline keys by path and both copies are listed. Measured today, that is **18 stems / 2,374 fields** — correct as stated.

There is a second effect it does not cover, and it is worse in kind. For **21 dirty entries / 1,550 fields**, the baseline lists **only one** path, and that path is the one **no producer writes to** — a pre-refactor copy left at the `computations/` root when the producer moved into `probes/` (or `substrate/`, or `alpha/`). Those entries are not merely counted twice; they are **undrainable**, because re-running the producer regenerates the sibling and never touches them.

**633 of the 1,550 are already fixed at the live path.** So the backlog charges the corpus for work that is finished.

Two of the orphans are **cited by path from the paper** while their live sibling is at 0 dirty — the mass-binding-algorithms appendix (`mba-step02-gs-reduction.ts:13`) points at the 31-dirty `hecke-core-symbolic-migration.witness.json` orphan, and two Lean files point at the 216-dirty `pentagon-to-borromean-h4-probe.witness.json` orphan.

Full table, method, and the disposition options: bean `qou-baye`.

**Consequence for anyone quoting a remaining-backlog figure off this baseline:** it is inflated by both effects, not one.
