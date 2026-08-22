---
# qou-1c4y
title: 'MIGRATION: move the ~840 muon-q0 computations/ witnesses to the experimental (proton) anchor'
status: in-progress
type: task
priority: normal
created_at: 2026-08-07T08:35:43Z
updated_at: 2026-08-22T19:11:35Z
---


## Why

Owner directive 2026-08-07: **all agents and all production code default to the
experimental (proton) q₀ anchor**. Recorded in `AGENTS.md` §"q₀ anchor convention".
That sets the target end state; this bean tracks getting the existing corpus there.

## Scope

`computations/` currently carries ~840 witnesses from ~72 producers built at the
**ideal / canonical 3-CAL muon** pin (`q-pinning-50-digit.witness.json`,
`q₀ = 1.10997859555733471…`). The experimental pin is
`q_parameter.Q = 1.1099785827513808`. Separation **11.54 ppb** — the μ–p substrate
tension itself.

Per the updated AGENTS.md rule 4 this is **not** an idle-drain. New/touched code
already uses proton with no sign-off; this bean is the tracked sweep for everything
untouched.

## The specific trap to fix corpus-wide

`wedderburn_jones_markov.y_lambda_at(n, q)` serves the cached **muon-built**
`y-lambda-at-q0.witness.json` whenever `|q − q_parameter.Q| < 1e-12` — a gate
satisfied **trivially** when the caller passes `q_parameter.Q` itself. So an
ideal-layer cache reaches an experimental-layer caller with **no signal** that a
layer boundary was crossed. This is how the μ₃ Fréchet probe ended up straddling
both layers.

**Audit every cached-witness accessor with the same "matches the package constant
⇒ serve the cache" shape** — `y_lambda_at` is unlikely to be the only one.

## Measured impact (so the sweep can be prioritised honestly)

On the μ₃ Δ²g, the mixed-vs-pure difference is **~1e-7 relative** — no conclusion
changed. See `computations/deltalambda/mu3_anchor_consistency_probe.py`. So this is
a **correctness/hygiene** migration, not a results-changing emergency: expect most
witnesses to move by ~10 ppb-scale amounts. Re-verify any witness whose assertions
have tolerances tighter than ~1e-7 before assuming it survives the move.

## Already done (do not redo)

- `computations/deltalambda/mu3_frechet_perblock_probe.py` — proton ✓
- `computations/deltalambda/mu3_abs_choice_robustness_probe.py` — proton ✓
- `computations/deltalambda/mu3_anchor_consistency_probe.py` — reports all three
  readings by construction ✓

## Definition of done

1. Every `computations/` producer reads the experimental pin, or explicitly
   documents why it must not.
2. Every witness records the q₀ it was built at (AGENTS.md rule 4, last bullet).
3. No producer mixes layers inside one quantity.
4. The cached-accessor trap above is closed — the cache gate must distinguish
   *which* q₀ the cache was built at, not just whether the caller passed the
   package constant.


## Surveyed scope (2026-08-07) — supersedes the "~840" estimate

`_deprecated/` **excluded per owner instruction**; it turned out to contain **0**
affected witnesses, so the exclusion costs nothing.

| | count |
|---|---|
| producers importing `y_lambda_at` | 145 |
| producers referencing the muon `q-pinning-50-digit` | 122 |
| witnesses carrying the **muon** q₀ | 481 |
| witnesses carrying the **proton** q₀ | 416 |
| total witnesses | 2383 |

## Step 1 — DONE (PR #4665): root cause closed

`y_lambda_at`'s cache gate now keys on the **witness's own recorded q₀** rather
than on `q_parameter.Q`. This corrects ~145 call sites **without editing any of
them**: a proton-anchored caller falls through to the live closed form at the
anchor it asked for, while a muon-anchored caller still hits the cache (fast path
re-gated, not lost). Regression test `computations/q0_anchor_gate_test.py`, exit 0.

## Step 2 — NEXT: regenerate the 481 muon witnesses

Deliberately **not** bundled with step 1 — mixing "fix the mechanism" with
"regenerate 481 files" makes both unreviewable, and several producers are 18-min
long-computes (AGENTS.md long-compute logging discipline applies: `-u` + `tee`).

Sequencing that keeps it reviewable:
1. Classify the 481 by producer; find the ~122 that read `q-pinning-50-digit`.
2. **Re-verify tolerances first.** Measured anchor impact is ~1e-7 relative, so any
   witness whose assertions are tighter than that may legitimately fail after the
   move. Those are findings, not breakage — triage before regenerating en masse.
3. Batch by producer, ≤ 49 files per PR (Gemini review limit).
4. Long-computes get their own PRs with logged wall times.

## Step 3 — audit the other cached accessors

`y_lambda_at` is unlikely to be the only accessor with the "matches the package
constant ⇒ serve the cache" shape. Grep for other witness caches gated on
`q_parameter.Q` and apply the same fix (gate on the artifact's own recorded q₀).

## 2026-08-15 — the inventory rests on a field that could flip (PR #5082)

**Re-scope this before running the sweep.** The premise is "move the ~840
muon-q0 witnesses to proton", which presumes you can tell which witnesses are
muon-anchored. That identification was not sound.

### 1. ~~The muon LABEL was about to flip~~ — RETRACTED 2026-08-15

**This section asserted a claim that is FALSE. Struck rather than deleted, so
the error is visible to anyone who read the earlier version.**

I claimed that re-running `q_pinning_50_digit.py` would make every
muon-anchored witness stamp a PROTON value, because that script sets
`Q = q_at(mp.dps)`. It does not. `q_pinning_50_digit` is listed in
`computations/q0_anchor_manifest.json` under `ideal_muon`, so `q_parameter`
resolves the anchor from the argv stem and rebinds `q_at` to return the
witness string. Verified under the producer's real argv:
`q_at(70)` -> `1.10997859555733471989…`. **The producer is a FIXED POINT;
re-running it changes nothing.**

The "fix" I built on that claim — deriving the muon label from `q_muon_at()`
— was a REGRESSION and is reverted: it made the stamped label disagree with
the value the producer actually computes with (1.1099785955541805 stamped vs
1.1099785955573347 computed), which is the exact misread the field exists to
prevent.

**The real defect, which that story obscured: the muon 50-dps constant is
CIRCULAR** — its producer reads, via `q_at`, the witness it writes. It has
never been derived from a closed form. Breaking that loop must move the LABEL
and the COMPUTED VALUE together, or it reintroduces the disagreement above.

Note also: `computations/substrate/q_parameter.py` asserts the witness starts
with `1.109978595557`, so substituting the canonical string there hard-fails
all 257 `ideal_muon` producers, and a second copy of that guard ships in the
published `qou_mass` package. Any proton migration has to deal with both.

### 2. The real inventory, measured (not "~840")

**Do not quote a count from this bean.** Run it:

    python3 computations/q0_provenance_audit.py --json

Three generations of this census were live at once — 406/709/1978 here,
470/799/2453 in `qou-xm91`, and different numbers again from the script. Each
was correct when written and none was marked superseded, so they read as
disagreement about the corpus when they were really successive fixes to the
audit's anchor-key pattern and its false-precision test. The frozen table that
stood here is deleted rather than refreshed, because refreshing it would just
mint a fourth generation.

**What survives, and does not depend on the exact counts:**

* The migration's headline "~840 muon witnesses" is wrong in both directions.
  The muon-labelled group is smaller than that.
* The far larger group **records no anchor at all** — roughly half the corpus.
  For those, "is this muon?" cannot be answered from the file; it needs the
  producer. A sweep scoped to "the muon ones" silently leaves them in an
  unknown state. See `qou-xm91`, and read its CORRECTION section: most of that
  gap is a deliberately-tolerated state, not a defect.

### 3. Scope calibration on the 243

They are a REPRODUCIBILITY defect, not accuracy: the gap is 2.842e-12, which
is **431x smaller** than the CODATA uncertainty on q_muon itself (m_mu/m_e is
known to ~7 sig figs, capping q_muon at ~8). No physical quantity moves.
Do not report it as a precision problem — an earlier version of my own note
did, and that was an overclaim.

### Suggested re-scope

1. Land the derived-label fix (#5082) first — otherwise the sweep's own
   identification step can flip mid-run.
2. Decide what to do about the **1978 unrecorded** witnesses; that is the
   actual bulk, and it is a producer-side question, not a witness-rewrite.
3. Only then consider the 709 labelled-muon files, and only where a producer
   re-run is genuinely wanted — not as a string substitution.

## 2026-08-19 — the gate is now satisfied, and the sweep is not a re-run

**Authorisation.** The owner's 2026-08-15 directive ("otherwise pin proton";
"fix all, even if not visible") is now recorded in AGENTS.md §q₀ anchor
convention rule 4, which is where the gate asked for it. PR #5049 held the
bulk reclassification back on exactly that ground and was right to — a chat
transcript does not satisfy a durable gate.

**What the first attempt cost, and what it bought.** It broke `main` for 208
producers (`qou-m9xp`). The four constraints now recorded with the
authorisation come out of that, and the second is the one an agent is most
likely to skip:

1. never re-pin an anchor-DEFINING witness (`q-pinning-50-digit`) — that
   redefines what "muon" *means* rather than migrating a consumer;
2. the muon anchor keeps a definition — "proton everywhere" governs what new
   compute pins to, not whether the ideal layer is statable;
3. a comparison producer needs BOTH pins, so the manifest cannot serve it —
   it reads `q_at()`/`q_muon_at()` by name and lives under `physical_proton`;
4. manifest and witnesses are ONE change — #5049 split them and the half that
   landed is the half that broke main.

**Sequencing that follows from those.** This is not "run the sweep". It is:

- confirm `q0_repin_sweep.py` still carries `ANCHOR_DEFINING` /
  `ANCHOR_DEFINITIONS` (added by the `qou-m9xp` fix — do not remove);
- flip the manifest and run the sweep in ONE branch, so the two never separate
  again;
- expect the sweep to resurrect long-broken producers: three did last time
  (missing scipy; `float(mpc)`; `'.6f'` on an mpf), and each crash was a real
  finding, not noise — the `float(mpc)` one was the probe correctly reporting
  that ²H and ³H have negative bar ratios;
- classify every float64-carrying producer it surfaces with
  `classify_production_reach.py`; production → mpmath, otherwise
  `precision_tier: "float64"` + `deprecated` per the owner's ruling.

**Measured, so the next agent does not re-measure.** Triaging the 257 down is
not available: by precision, 255/255 carry ≥9 sig figs somewhere; by reader
count, 44 have a reader and 211 are leaves — and skipping leaves is how the
μ–p tension audit understated its own subject 155× unnoticed.

---

## 2026-08-19 — the sweep RAN, the predicted failure fired, and the triage was never used

Reviewed against `origin/main` at `5b158ef06c`, 1163 commits after the triage
landed. Three things to record, in descending order of how much they should
change what happens next.

### 1. The circularity hazard this bean documented is no longer hypothetical

The §"1. RETRACTED" section above says, in its own words:

> **The real defect ... the muon 50-dps constant is CIRCULAR** — its producer
> reads, via `q_at`, the witness it writes. ... Breaking that loop must move
> the LABEL and the COMPUTED VALUE together, or it reintroduces the
> disagreement above.

The `tnjb` sweep (`9a9c6b31c`, "first 25 witnesses regenerated at the proton
pin") moved the VALUE without the accessor. `q-pinning-50-digit.witness.json`
is what `qou_substrate/witness.py::_q0_value_for_anchor` reads *as the
definition of the muon pin*, so regenerating it at proton left both anchors
resolving to the same value and **the muon pin with no definition in the tree
at the path its own accessor points to**. Measured consequence: 262 Q0_FLIPs
against `--strict`.

Fixed by `2e4745448d` ("restore the muon anchor — the repin sweep overwrote its
own definition"); bean `qou-cezp` is completed and `qou-m9xp` carries the full
trace. Verified in this tree: the file is back at `q0Anchor: muon`, `computedAt
2026-07-18`, and the two anchors now resolve 11.54 ppb apart as they should.

**The lesson is not "be careful".** It is that this file is a *definition*, not
a datum, and a sweep that treats it as a datum breaks the layer it is sweeping.
Any future batch must exclude `q_pinning_50_digit` explicitly, or move the
accessor off it first.

### 2. The tolerance triage merged and has never been run by anything

`computations/q0_migration_tolerance_triage.py` (`8b0dee25ea`) exists to order
exactly this sweep — step 2 item 2 of the sequencing above. Measured today:
the only file in the corpus that references it is **its own test**. The sweep
ran without it.

That is not a complaint about the sweep; it is a defect in how the tool was
delivered. A triage nothing calls is a triage that does not run. Wiring it into
the batch entry point is the actionable item, not writing more of it.

### 3. A dated DELTA — not a census, and not a number to quote

§2 above says "do not quote a count from this bean", and that rule stands: the
canonical census is whatever `--json` prints today. What follows is a different
object — a *dated before/after* whose only job is to answer "is the migration
moving?", which a single census cannot answer. Reproduce with:

    python3 computations/q0_migration_tolerance_triage.py
    python3 computations/q0_provenance_audit.py --json

If you need a count for anything else, run those and use that.

    q0_migration_tolerance_triage.py        q0_provenance_audit.py --json
      muon-anchored witnesses  576             scanned          3222
      PINNED-TO-ANCHOR           0  (was 1)    muon              940  (was 981)
      AT-RISK                   55  (was 61)   proton            637  (was 553)
      producers to order        25  (was 28)   neither          2487
                                               known-stale       380  (was 421)

The migration IS moving: proton +84, muon −41, known-stale −41, and the single
`PINNED-TO-ANCHOR` assertion (`lambda_plus_eq_q`, 1e-18 tolerance against a
quantity shifting 1.15e-8) is gone. Both audits still run clean across a corpus
that gained 84 witnesses, which is the useful robustness signal.

### Next step, concretely

1. **Wire the triage into the batch driver** so a sweep cannot start without an
   ordering. Until then it is decoration.
2. **Exclude `q_pinning_50_digit` from every batch**, per §1, or repoint
   `_q0_value_for_anchor` at a definition that is not itself a sweep target.
   The second is the real fix; the first is the safe stopgap.
3. Then the 25 producers, AT-RISK first, one at a time.

## 2026-08-19 (b) — ~~the migration is 357, the ideal layer is comparison~~ RETRACTED

> **The conclusion of this section is WRONG and is retracted 2026-08-21.**
> Struck rather than deleted, because the *measurement* stands and only the
> inference from it was bad — and because this is the second time in this bean
> that a correct measurement carried a wrong conclusion.
>
> **What was wrong.** I read "declared `ideal_muon` in the manifest" as
> "explicitly justified as a comparison, therefore keep". It is not. It is
> simply where `q_parameter`'s argv-stem auto-selector happens to route a
> producer. The owner's actual carve-out, recorded verbatim in AGENTS.md rule 4
> on 2026-08-19, is narrower:
>
> > *"we want proton unless for an explicit reason (like comparison on proton
> > vs muon results). otherwise pin proton"* / *"fix all, even if not visible."*
>
> A manifest entry is not an explicit reason. The 219 are the sweep's
> **target list**, not a keep-list, and `q0_repin_sweep.py` on main is built
> to flip exactly them.
>
> **What survives.** Only two things stay muon, and neither is the manifest:
> 1. `q-pinning-50-digit` — the anchor DEFINITION. "Proton everywhere" governs
>    what compute pins *to*, not whether the ideal layer is *statable*; delete
>    it and the μ–p tension cannot be expressed at all. Guarded on the live
>    driver as `ANCHOR_DEFINING`.
> 2. Genuine comparison producers, which read `q_at()` / `q_muon_at()` **by
>    name** and live under `physical_proton`. The manifest cannot serve them —
>    it selects one anchor, and a comparison needs both.
>
> That design is better than the one I proposed and it was already on main
> while I was proposing mine.
>
> **The measurement that stands:** 219 muon witnesses from a declared producer,
> 357 not. Both sets are in scope. "Fix all, even if not visible" explicitly
> rejects triaging either by visibility.

### Original section follows (measurement good, conclusion retracted)


Owner question, and the right one: *"why muon pinned? is it comparison? if so
ok, otherwise proton pin."* Measured rather than reasoned about.

`computations/q0_anchor_manifest.json` declares which producers run at the
ideal anchor. Cross-tabbing that against the muon-anchored witnesses:

    muon witnesses from a DECLARED ideal_muon producer : 219
    muon witnesses NOT declared (unmigrated)           : 357

So the answer splits cleanly, and it is exactly the owner's rule:

* **219 — comparison, leave them.** The declared ideal layer is the canonical
  3-CAL chain: CAL-2 is `𝔇_β` with proxy `m_μ/m_e`, so muon is correct there
  **by definition**, not by inertia. The μ–p tension (11.54 ppb; 9.5 σ on
  m_μ) is only *measurable because both pins exist*. Collapsing the ideal
  layer into the experimental one does not tidy the corpus — it deletes the
  comparison that the framework's own cross-check depends on.
* **357 — not comparison, migrate them.** No manifest entry, no declared
  reason, just unswept. These are the migration, and the target is proton per
  the 2026-08-07 directive.

**Caveat on the split.** "Declared" is intent *as recorded*, not proof. A
producer could be undeclared and legitimately need muon (nobody declared it),
or declared and wrongly so. The manifest is the repo's own statement of intent
and so the right first cut, but a producer moving between the two sets is a
judgement call, not a sweep step.

### The driver did not read the manifest at all

Measured before the fix: of the 23 producers in the driver's plan, **16 were
declared `ideal_muon`**. Sweeping them would have migrated canonical-chain
artifacts off their declared layer — the same class of error as the pin-file
overwrite in §1 above, distributed across sixteen files instead of
concentrated in one, and correspondingly harder to notice.

Fixed: the driver now loads the manifest and excludes declared ideal-layer
producers by default (`--include-declared-ideal` to override, which is an
owner call since it re-declares a layer). Effect on the live plan:

    before:  333 producers considered
    after :  132 candidates
             215 excluded — declared ideal_muon
               1 blocked  — NEVER_SWEEP (the pin definition)
               3 deferred — at-risk assertions
             110 actually sweepable

### Correction to my own previous "next" item

The 2026-08-19 (a) entry ended by pointing at `alpha_k_jones_markov_h12` as
the remaining live straddle. **It is not** — it was repinned to
`q_parameter.Q_50_DIGIT_STR` (proton) earlier in this arc; its `Q_PIN` line is
a `record_upstream` provenance call, not a value read. I carried that item
forward from `qou-m9xp`'s older "To close" list without reading its own later
correction four sections down. The corpus is the source of truth, not the
status note — including when the status note is in the same file as its
retraction.


## 2026-08-21 — two more corrections to my own work on this bean

**1. I patched the wrong driver.** `q0_repin_regen_batch.py` (216 lines, last
touched 2026-08-10) is superseded by `q0_repin_sweep.py` (397 lines, touched
2026-08-19), which already had the `ANCHOR_DEFINING` guard I "added", plus
topological ordering and a resume journal that mine lacks. I checked whether
the guard existed *on the file I was editing* and not whether a better driver
existed. The stale one now refuses to run and says why.

**2. Deferring at-risk producers is against the directive.** My gate deferred
them by default. "Fix all, even if not visible" rejects exactly that: the live
sweep's docstring records that bucketing by significant digits (255/255 carry
≥9 sig figs) and by reader count (44 readers, 211 leaves) were both tried and
both rejected, because they leave a stale number on the theory nobody is
looking. The tolerance triage is still useful — but as **ordering and
annotation**, never as a skip. Offering it to `q0_repin_sweep.py` in that form
is the remaining actionable item.


---

## 2026-08-22 — this bean's headline count is stale, and the shortfall is not what it looks like

Measured on `main` today, over all 3030 `computations/**/*.witness.json`:

| measure | count |
|---|---|
| muon **fingerprint** anywhere in the file (the method behind the "~840") | **624** |
| muon **stamp** — `q0Anchor: muon` or a muon `q0Value` | **65** |
| fingerprint present but no muon stamp | **559** |

The title says *"~840 muon-q0 witnesses"*; AGENTS.md §q₀ rule 4 has carried 870. By the comparable fingerprint method it is now **624**.

**The 559 are not a migration backlog, and counting them as one repeats a mistake this arc already made twice.** A fingerprint hit means the muon digit string appears *somewhere* in the file — which a deliberate two-pin comparison, a recorded pin-gap diagnostic, or a stale data field all produce without the witness claiming muon anywhere. Reading a raw grep count as a defect count is exactly what produced the retracted `qou-0hnz` claim (254/78 → measured 0) and the `qou-sccd` opening framing (11 candidates → measured 2). The stamp count, **65**, is the only figure tied to a claim the corpus actually makes.

**And 65 is not automatically a work-list either.** Three of them are now *legitimately* muon by design — `q_pinning_50_digit` (the anchor definer, which must never move), `atomic_tr_m_mpfr_50dps` and `cross_check_trM_1ppb` (two-pin comparison producers restored under `qou-ibbr` / `qou-wn6d` precisely because moving them to proton broke them). Any re-baseline has to separate that class before proposing a sweep.

### Suggested re-baseline, before any bulk work

1. Partition the **65** stamped-muon witnesses into: (a) anchor-defining, (b) deliberate comparison producers, (c) genuine migration remainder.
2. Sample the **559** fingerprint-only witnesses to establish what the fingerprint is actually hitting — comparison values, pin-gap diagnostics, or stale fields. Do not assume.
3. Only then size the sweep. The four constraints recorded in AGENTS.md rule 4 still bind, and the first attempt at this migration broke `main` for 208 producers (`qou-m9xp`).

Recording the numbers rather than acting on them: the sweep is the step that has gone wrong before, and it should start from a measured work-list, not from a count nobody has re-derived since the migration ran.
