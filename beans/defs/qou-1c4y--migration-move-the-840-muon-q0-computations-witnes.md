---
# qou-1c4y
title: 'MIGRATION: move the ~840 muon-q0 computations/ witnesses to the experimental (proton) anchor'
status: in-progress
pr: 8188
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-07T08:35:43Z
updated_at: 2026-11-16T20:23:00Z
parent: qou-2002
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


## Re-baseline #2 (2026-08-22) — my first re-baseline was wrong the same way the original was

Both the original `~840` and my `624 fingerprint / 65 stamped` came from
grepping a **12-digit prefix** of the muon pin. That prefix does not
identify the muon pin. The corpus carries **two** muon values agreeing to
11 digits:

    current     1.10997859555733471...   live ideal / CAL-2 pin
    superseded  1.10997859555418057...   the "old muon value"

Prefix sensitivity: `642 / 624 / 236 / 206` as the prefix lengthens. The
624 -> 236 drop is 388 witnesses carrying a **different number**.

Measured over 3030 tracked witnesses:

| population | count |
|---|---:|
| current muon | 212 |
| **superseded muon** | **375** |
| both (comparison) | 24 |
| rounded / low-precision | 31 |

The superseded class is the **largest** and is a **different defect**:
wrong under either convention, stale on its own terms, not "awaiting the
proton migration". Already documented as a pin-currency defect in
`local/language-trap-agent-audit`; what is new is its size.

### The confirmed, actionable class — 5

`q-pinning-50-digit.witness.json` is muon-anchored. Of live producers:
136 reference it, 69 read the JSON directly without importing
`q_parameter`, and **56 bind q0 from `derived_50_digit["q"]`** — so they
inherit its anchor rather than choosing one.

- **51 UNDECLARED** in `q0_anchor_manifest.json`
- **5 declared `physical_proton`** — flat contradiction, confirmed in
  both directions (manifest says proton, code pins muon, emitted witness
  is stamped `proton` while recording the muon value):
  `aK_via_lp_dual_hecke_basis`, `b_over_m_order_probe`,
  `path4_rho_K_at_h3A`, `q1_mass_gap_probe`, `q_beta_form_a_n1_extension`.
  `q1_mass_gap_probe.py:170` comments "(proton anchor)" directly above
  the muon read.

This is the **direct-read sibling** of the `y_lambda_at` cached-accessor
trap this bean already names — same failure one layer down, bypassing
every guard on the accessor path.

### Scope

Does **not** authorise the bulk sweep (constraints 1-4 stand; qou-m9xp
broke main for 208 producers). Does **not** make the 51 undeclared
producers defects — a genuine ideal-layer producer *should* read the muon
pin. The finding is 56 pinning muon against 3 declared `ideal_muon`.
Classifying the 51 is the next step; the 5 are actionable now.

Re-runnable: `python3 computations/audits/q0_muon_population_partition.py`
(`--list-contradictions` exits 1 while any remain). Audit:
`docs/audits/2026-08-22-q0-migration-worklist-partition.md`.


## Coordination with qou-o922 (measured 2026-08-22) — opposite failure modes

Sibling bean `qou-o922` measures a closely-related population
(`undeclared_muon_pin_flip_risk_audit.py`, ratcheted 49 -> 40). Intersection
against my 56 direct muon-pinners: **4 overlap, 45 sibling-only, 52 mine-only.**

Nearly disjoint, because the two behave **oppositely on re-run**:

- **qou-o922**: muon-stamped witness + producer undeclared. On re-run
  `q_parameter` falls through to the **proton default** and `WitnessBuilder`
  drops the label in the same step -> **the pin flips and the evidence
  disappears together.**
- **mine**: the producer reads `q-pinning-50-digit.witness.json` **directly**,
  never importing `q_parameter`. Manifest state is irrelevant -> **re-running
  flips nothing**; it stays muon indefinitely.

**Consequence for qou-o922's stated fix.** Its next step is *"add a manifest
entry ... THEN re-run"*. Correct for its own 45; **a no-op for my 52** — a
producer that never consults `q_parameter` cannot observe its manifest entry.
Declaring it and re-running leaves it on muon while the declaration says
proton, which is exactly how the 5 contradictions arose.

The 4 in both need the **read** fixed before the manifest entry, or the entry
will not take effect: `qbeta_dladder_ecalle_acceleration_probe`,
`qbeta_fsc_g_pattern_comparison`, `qbeta_symbolic_sdp_strict_complementarity`,
`qbeta_trm_crosscheck_convention_pin_split_probe`.

Together: 101 producers covered (49 + 56 - 4); neither audit sees the other's set.
## The relabel is not the migration (recorded 2026-08-19, PR #5332)

The section above covers never re-pinning the anchor-DEFINING witness. This is
the other half, and it is not covered above: the tempting one-line version of
this migration is to move every `ideal_muon` stem to `physical_proton` in
`computations/q0_anchor_manifest.json` and call the end state reached.

That is a *disabling*, not a migration. `q_parameter.py:100` selects the anchor
by membership in that list, so an empty `ideal_muon` means no producer ever
*requests* the muon anchor again — and the anti-corruption guard at
`q_parameter.py:224` ("Refusing to fall back to proton silently") fires only on
a *requested* muon anchor. Empty the list and the guard becomes unreachable for
exactly the producers it exists to protect, while their already-emitted
witnesses stay muon-computed under a proton label. Proposed in #5049, held back
in #5315.

Corollary measured on 2026-08-24: `ideal_muon` does NOT end at zero. Three
producers refuse a proton run by design (`atomic_tr_m_mpfr_50dps`,
`cross_check_trM_1ppb`, `he4_stage2_ranking_seminormal_xcheck`), several more
hold the muon value as a deliberate reference, and `q_pinning_50_digit` defines
the anchor. A run that drove the list to zero would be a bug, not a completed
migration.

## STOPPING POINT 2026-08-24 — bulk migration done, PR #5664

    ideal_muon      120 -> 36
    physical_proton 514 -> 598

~130 producers migrated, each verified by the muon value actually LEAVING its
witness rather than by the witness merely changing. Manifest moved LAST, after
the data, and re-verified: both anchors still resolve distinctly, a
keep-on-muon stem still resolves to muon (so the guard stays reachable), a
migrated stem resolves to proton, the lists do not overlap.

**Five mechanisms by which a producer holds a muon value**, each found only
after the detector built for the previous one came back clean:

  1. manifest tag                      -> the manifest move
  2. local source literal              -> resolve through q_parameter (23)
  3. shared-module literal             -> one constant, 22 importers
  4. provenance stamp moving alone     -> detect and revert
  5. direct read of the anchor witness -> architectural, bean qou-aj91

Mechanism 3 is the sharpest: `_gap_a4_qsafe.py` held the MUON value under a
comment reading "proton-mass-anchored q_0", imported by 22 modules — which is
how the T5-T12 series came to be tagged physical_proton over muon witnesses.

**Two self-corrections, recorded because the numbers were reported wrong
first.** I claimed 89 migrated; 36 were stamp-only flips and were reverted. The
revert then OVER-reached, because its file list came from the journal's
per-producer `files` and producers write SIBLING witnesses — genuine
migrations were rolled back with the bad ones and had to be re-run. Nothing
false entered the corpus either time; the failure was over-claiming, then
over-correcting.

## What is left, and why it is not "unfinished"

The 36 remaining are the correct end state: `q_pinning_50_digit` DEFINES the
anchor; five producers refuse a proton run by design;
`q0_anchor_consistency_audit` needs BOTH pins (moving it would disable the
audit that detects anchor corruption). A run that drove ideal_muon to zero
would be a bug.

Corrected on the rebase before merge: 36/598, not the 37/597 first reported.
`main` had independently migrated `rho_w_crystal_vertex_trace` with a better
fix than this branch's — it reads q FROM the deuteron chi cache header rather
than from any literal, so it can never again be read at a second anchor.
`main`'s side was kept.

Genuinely open, tracked elsewhere:
  * qou-aj91 — 85 producers read the anchor witness directly (67 untagged);
    needs an architectural decision, not a sweep.
  * qou-y82a — single_anchor_near_matches 25 -> 4 between anchors.
  * qou-2zjp — alpha_high_precision, now diagnosed as convention C->D drift,
    unrelated to the anchor.
  * ~6 slow producers needing a deliberate long compute (20-40 min per leg).

Keeping this bean IN-PROGRESS rather than closing on the manifest number: the
mechanism-5 question and the slow producers are real remaining work, and
closing on "120 -> 36" would read as done when it is not.


## CORRECTION 2026-08-24 — "five refuse a proton run" was wrong. Three refuse; two fail SILENTLY.

Caught in review of the #5664 merge: AGENTS.md (via #5332) says THREE producers
refuse a proton run by design, while #5664's own material says FIVE. AGENTS.md
is right, and the discrepancy is not cosmetic — it collapses two opposite
behaviours into one word.

Verified at source:

    atomic_tr_m_mpfr_50dps                REFUSES  "Refusing rather than writing
                                                    a straddled witness"
    cross_check_trM_1ppb                  REFUSES  "must run under the MUON q0 pin"
    he4_stage2_ranking_seminormal_xcheck  REFUSES  assert q.startswith("1.109978595557")
    ---
    chi_lambda_he4_full_partition_table   RUNS, and emits a STRADDLE
    bwhk_st_matrix_corroboration          RUNS, and emits a STRADDLE

The last two do not refuse anything. They complete with rc=0, flip `.q0Value`
to proton, and leave the muon value sitting in the payload
(`.parameters.q_0_f64`, `.data.q0`) — because they read the anchor-defining
witness directly (mechanism 5) rather than consulting q_parameter at all.

**Why the distinction matters more than the count.** A producer that refuses is
the SAFE case: it tells you, loudly, at the moment you get it wrong. A producer
that silently straddles is the DANGEROUS one — nothing surfaces, and the only
way to find out is to check whether the muon value actually left the witness.
Calling both "refuses by design" hides the dangerous class behind the safe one,
which is the opposite of what the label should do.

Both are still correctly held on `ideal_muon`; only the reason differs. The
keep-on-muon set is therefore:

    3  refuse loudly            (safe: they self-identify)
    2  straddle silently        (unsafe: found only by checking the payload)
    1  defines the anchor       (q_pinning_50_digit)
    1  needs BOTH pins          (q0_anchor_consistency_audit)

The two silent ones are the strongest argument for the WitnessBuilder fix
proposed in qou-aj91: make `.q0Value` report the anchor the PAYLOAD used, and
the silent class stops being silent.


## 2026-08-25 — re-measured end to end. Not done; the blocker moved.

Asked directly: "has all pinning moved from muon to proton, except where
explicitly indicated as muon?" Answer: **no**, and the residue is not where the
earlier entries in this bean expected.

### Declaration side — essentially migrated

    manifest physical_proton   651
    manifest ideal_muon         35
    manifest ambiguous          17
    Q0_FLIP                      0   (no witness contradicts its own stamp)

An unlisted producer resolves proton by default, so the default is now right.

### Payload side — 424 witnesses still carry a muon-family q0

`computations/audits/q0_muon_population_partition.py`, live:

    current muon  1.109978595557334...   144
    OLD muon      1.109978595554180...   261   <- superseded pin, stale on its own terms
    both (comparison)                      5
    rounded / low-precision               14
    TOTAL                                424

**The 261 dominate and are a different defect from the 144.** A grep for the
13-digit prefix `1.109978595557` matches only the current value and reports
~150 — I did exactly that before running the partition script, and it hid
almost two thirds of the population. Do not prefix-grep this.

### The real blocker is not the 424 — it is the ~1645 unstamped

`computations/audits/q0_anchor_consistency_audit.py`, live:

    Q0_OK                970
    Q0_ANCHOR_MISSING   1645
    Q0_AUDIT_EXEMPT       80
    Q0_INDEPENDENT        49
    Q0_FLIP                0

For a **majority** of the corpus nothing records which pin was used, so nothing
can verify it. `Q0_FLIP = 0` is therefore much weaker than it reads: it says no
*stamped* witness contradicts itself, over a set that is 35 % of the whole.

This inverts the sequencing in Step 2 above. Regenerating witnesses before they
are stamped produces files that are migrated and still unverifiable — and per
`undeclared_muon_pin_flip_risk_audit.py` the regeneration itself *drops* the
stamp for an unlisted producer, so a re-run can move the pin and delete the
evidence in one step. **Stamping (definition-of-done item 2) should come before
regeneration (item 1), not after it.** That is a judgement, not a finding.

### At-risk set, draining

`undeclared_muon_pin_flip_risk_audit.py`: **35** witnesses assert
`q0Anchor: muon` from a producer that would now resolve proton, against a
baseline of 40. Assertion 2 still holds — zero witnesses carry the muon
`q0Value` with no `q0Anchor`, so `q0Value` remains the correct discriminator.

### Code side still straddles

`q0_producer_pin_classifier.py`, of 146 undeclared producers carrying pinned
witnesses: 68 proton, 27 muon, 41 none, **9 BOTH** (straddle candidates, never
auto-proposed), 1 missing-producer. Three disagree with their own witness:
`alpha_em_channel_swap_involution_probe` and `gram_matrix_seminormal_h6`
(code muon, witness proton), `rho_k_h3a_residual_decomposition` (code proton,
witness muon).

### The keep-on-muon carve-out is mostly undocumented

Of the 35 `ideal_muon` stems this bean justifies 7 (3 refuse / 2 straddle /
1 anchor / 1 both-pins). **13 of the rest carry no anchor rationale in their own
source at all** — split into those the manifest actually re-pins (5, via
`q_parameter`) and those where it is decorative because they read the
anchor-defining witness directly (7, `qou-aj91` mechanism 5), plus 1 behind
`qou-dkm2`. Broken out with the two measured false positives in **`qou-bypn`**.

Method note: all four audits write witnesses as a side effect;
`computations/` was restored after each run, so this entry changed no numbers.

### Re-verified 2026-08-25 on a 31-commit-newer `main` (pre-merge rebase)

Every figure above reproduced **except one, and the exception is the point**:

    ideal_muon / physical_proton / ambiguous   35 / 651 / 17   unchanged
    muon-family partition  144 / 261 / 5 / 14 = 424            unchanged
    at-risk (asserts muon, resolves proton)    35 vs baseline 40  unchanged
    Q0_OK                                      970             unchanged
    Q0_ANCHOR_MISSING                          1641 -> 1645    +4

**Four more unstamped witnesses landed in 31 commits, in one afternoon.** The
unstamped population is not a fixed backlog being worked down — it grows with
ordinary merges, because nothing gates a new witness on carrying its pin. That
is a stronger argument for stamping-before-regeneration than the static count
was: regeneration drains a set that is being refilled upstream of it.

The figures above are stamped to a commit for exactly this reason. Re-run the
three audits rather than quoting them; on this corpus the shelf life is hours.

Sibling interaction: PR #5755 migrates `aoperator_a5_crosscheck` off
`ideal_muon`. It is still listed on `main`, so 35 is right today and becomes 34
when that lands. It is **not** one of `qou-bypn`'s 13 — that list is unaffected.


## 2026-08-25 (later) — RETRACTED: "stamp before regenerate". They are the same operation.

Earlier today I wrote, in this bean and in PR #5792, that the ~1645 unstamped
witnesses argue for **stamping before regeneration**, and I recommended that
ordering to the owner. **That recommendation was wrong.** I went looking for the
stamping mechanism that would need building, and found it already built and
already merged.

### What the measurement actually shows

    live witnesses                                 2765
      already stamped (q0Anchor present)           1058
      unstamped, record NO q0 anywhere             1458
      unstamped, record a q0 under a KNOWN key      160
        of those: single pin (should stamp)         157
                  both pins (walker returns None
                  BY DESIGN — these want
                  q0Anchor: "comparison")             3

`build()` already calls `resolve_q0_anchor_payload_first(payload, spath)`
(witness.py:1569), **without** `require_declared`, so it always sets
`q0Anchor` — falling through to the manifest answer when the payload shows
nothing. Reproduced against the live API: a payload carrying `parameters.q0`
= the muon 50-digit string resolves `-> muon` correctly, as an `mpf` too.

So for every producer that routes through `WitnessBuilder`, **the stamp arrives
when the producer is re-run.** Stamping is not a prerequisite to regeneration;
it IS regeneration. Sequencing them is a distinction without a difference, and
my Step-2 inversion above should not be acted on.

### Three hypotheses I tested and killed, in order

Recorded because each is the obvious next guess and each is wrong:

1. **"`_Q0_FIELDS` is too narrow."** It is only four names (`q_0_50dps`, `q0`,
   `q_0`, `q0_50dps`), so a q₀ under `q`, `substrate_q`, `q_proton`, … is
   invisible. True, but it reaches **89 files, ~5 % of 1645** — not leverage.
   The blind-key census is in the session log if anyone wants to widen it.
2. **"The walker's `depth > 4` cap hides them."** No: of the 160, the shallowest
   known-key hit is at depth 0–3, **zero beyond the cap**.
3. **"Producers bypass `WitnessBuilder`."** Partly — but 27 of the 38
   post-2026-08-24 cases *do* call `builder.save()`, so that is not the
   explanation for them either.

The actual explanation is dating. Payload-first reached `main` at
**2026-08-25T10:20 UTC** (`9d52483f5`), not on 08-24 as the surrounding text
implies. Every one of the 157 predates it. They are stale, not blocked.

### The one genuinely live residue

Four witnesses were computed at 16:52 UTC and committed at 16:54 (`58db04f28`)
— 6.5 h after the fix — and went out unstamped. I checked that commit's own
tree rather than assuming, and it **did** carry payload-first wired into
`build()`. So this is not staleness. All four come from **hand-rolled
`json.dump` producers that never reach `build()`**:

    computations/qbeta/birkhoff_barodd_pythagoras_bridge_probe.py
    computations/deltalambda/deuteron_interface_handle_curvature_probe.py
    computations/deltalambda/yekutieli_trefoil_surface2form_discretization_probe.py
    computations/qbeta/a3_branching_asymmetry_vs_required_probe.py

(The fifth 08-25 case, `canonical_lepton_braid_words.py`, does use
`WitnessBuilder` — and ran at 06:25 UTC, before the merge. Consistent.)

That is bean `1j39`'s territory (the no-WitnessBuilder batch port), and it is
the part that regeneration will **never** fix: re-running a hand-rolled
producer re-emits an unstamped witness forever.

### What this leaves open, unmeasured

**1458 witnesses record no q₀ at all** — the actual bulk, and I have not
established why. Two very different cases: the producer never reads q₀ (wants
`q0Anchor: "independent"`, a legitimate declared state), or it reads q₀ and
discards it (a real gap). Nothing here distinguishes them, and the split
decides how much of the 1458 is work versus bookkeeping. That is the next
measurement, and it is not this bean's Step 2.


## 2026-08-25 (later still) — the 1458 split, MEASURED

The previous entry left this open and said the split "decides how much of the
1458 is work versus bookkeeping". Measured now, with
[`computations/audits/no_q0_recorded_producer_split.py`](computations/audits/no_q0_recorded_producer_split.py)
(pure static inspection; no arithmetic, so NO-FLOAT64 is vacuous):

    population (unstamped AND recording no q0)   1458
      READS q0, file-local                        478
      READS q0, via one-hop import cone           105   -> 583 read but do not record
      NO q0 read anywhere                         742   -> candidates for "independent"
      producer unresolved                         133

**The actionable number is 583.** Those producers read a q₀ and do not record
it, so `_q0_anchor_from_payload` has nothing to match and `build()` falls
through to the manifest answer. Have them record the q₀ they used and
payload-first stamps them correctly on the next run — no new mechanism, and no
number moves.

The 742 are *candidates* for `q0Anchor: "independent"`, not confirmed ones.
Two reasons to treat the figure as an **upper bound**: the cone walk is
**one hop**, so a producer reading q₀ two modules deep is still counted as not
reading; and `independent` is a producer-declared claim about intent, which a
static scan cannot make on the producer's behalf.

### The harness error, recorded because it was large and nearly shipped

The first run reported **536** "reads q0 via import cone" and **302** "no read".
Almost every cone hit was attributed to `_path_bridge`. It is a path resolver
(`witness_path`) and reads no q₀ — the regex had matched
`from q_parameter import Q` inside its **usage docstring** and a `#` comment.

Normalising each module through `ast.unparse` with docstrings stripped moved
**431 files** from "reads via cone" to "no read". Two lines of prose in one
helper, inverting the majority verdict of the whole population. Any future
scan of this kind must measure **code**, not file text — the same lesson
`witness_staleness_triage.py` already encodes for a different question.

Three hand-verifications of the corrected classifier, one per bucket:

    aj_figure_eight_certificate.py   claimed no-read   -> ZERO q0 tokens present  OK
    a5_so3_branching_probe.py        claimed no-read   -> no q0 read tokens       OK
                                     (this was the _path_bridge false positive)
    binding_canonical.py             claimed reads     -> `from q_parameter import
                                       Q_MP as q0`, `Q_50_DIGIT_STR` in live code OK


### Directional correction (same day) — it churns BOTH ways, not one-way growth

The entry above says the unstamped population "grows with ordinary merges" and
"is being refilled upstream". Measured across three points in one evening:

    committed 19:04 UTC   Q0_ANCHOR_MISSING 1641   Q0_OK 969
    my run    ~20:05 UTC                    1645        970
    regen     21:24 UTC                     1644        971

So it grew by 4, then **drained by 1** as sibling PRs landed correctly-stamped
witnesses. "Refills on ordinary merges" is right; "not a backlog being worked
down" is too strong — it is being worked down *and* refilled at the same time,
and over this window the two were within a few files of each other.

What survives unchanged is the operational point: the number has a shelf life
of **hours**, so quote it with a timestamp or re-run the audit. What does not
survive is any claim about the trend from a two-point sample — including mine.


## 2026-08-25 — CORRECTION: the independence checker said 19; it is 10

I reported "19 witnesses falsely declare `q0Anchor: independent`" in PR #5797's
title, body and my summary to the owner. **The real number is 10.** Three
false-positive classes, each found by hand-checking flagged files rather than
by trusting the count:

1. **The declaration's own prose was evidence against itself.** `q0AnchorReason`
   is the field where an author explains *why* a compute is q₀-independent, so
   it naturally contains "q-pinning-50-digit" or quotes a pin. `ast.unparse`
   preserves string constants, so the reason matched the read pattern.
   Measured: **3 of the first 4** violations inspected were nothing but their
   own reason string. Several of these producers argue for `independent` in a
   comment right beside the declaration — that argument is what indicted them.

2. **`from q_parameter import <non-q₀ symbol>`.** That module also exports
   CODATA ratios. `knot-volumes.py` imports `MASS_RATIO_MU_E` and reads no q₀.
   Fixed by matching the SYMBOL, not the module name.

3. **Cone traversal into the q₀ provider.** Fixing (2) at the import site was
   not enough: the walk still followed the import into `q_parameter.py`, whose
   own source obviously reads q₀, and indicted the importer on it.
   `q_parameter` / `constants` are now TERMINAL — q₀-ness is decided at the
   import site by which symbol is bound, never by recursing into the provider.

A fourth defect was self-inflicted while fixing (1): blanking `Q0_ROLE` along
with the declaration strings silently disabled the auditor carve-out
(exempt 3 → 0). The marker is read back out of the same normalised source.

Progression: **19 → 14 → 11 → 10**, and 41 upheld (was 32).

### The 10, five of them hand-verified

    chi_content_eigenbasis_probe      -> canonical_braid_crossings does
                                         `from q_parameter import Q_50_DIGIT_STR`   VERIFIED
    lambda_scale_substrate_probe      loads q-pinning-50-digit.witness.json directly;
                                         also manifest `ideal_muon`                 VERIFIED
    markov_identity_symbolic_probe    evaluates at BOTH pins -> wants `comparison`,
                                         not a corrected single pin                 VERIFIED
    qbeta_c3_rung_structure_analysis  `Q0_MP_PIN = Q_50_DIGIT_STR`                  VERIFIED
    probe_he4_magic_baryeven_prune    `Q0 = mp.mpf(Q_50_DIGIT_STR)`                 VERIFIED
    chirality_topology_binding_probe          (not yet hand-checked)
    eigenbasis_structural_lemmas_probe        (not yet hand-checked)
    habiro_witness_convention_adjudication    (not yet hand-checked)
    qbeta_habiro_f_from_shape_collapse        (not yet hand-checked)
    qbeta_rung1_div25_framing_squared_test    (not yet hand-checked)

`markov_identity_symbolic_probe` is worth separating: it is not a mislabelled
pin but a mislabelled KIND. It evaluates at both anchors deliberately, which the
vocabulary already covers as `comparison`. Fixing it to `proton` would be as
wrong as leaving it `independent`.

### The lesson, which is the same one three times

Every one of these classes is "the checker matched text that describes the
thing rather than text that does the thing" — the `_path_bridge` docstring
earlier today, then the reason string, then the provider module. A q₀ checker
that reads prose about q₀ will always over-flag, and the corpus is full of
careful prose about q₀ precisely where the code is careful not to use it.


## 2026-08-26 — the 10 hand-checked: 7 genuine, 3 FALSE POSITIVES, and a fifth defect class

All ten violations read individually, at source. **7 are real. 3 are my checker
over-flagging again** — and one of the three was in the "✓ hand-verified" list
I published in PR #5806. That verification used the wrong standard and is
retracted below.

### The split is FILE-LOCAL vs CONE, and it is not incidental

    FILE-LOCAL (6)   the producer binds q₀ in its OWN file    -> all GENUINE
    CONE       (4)   q₀ reached through an imported module    -> 1 genuine, 3 false

**The six file-local are solid.** Each carries `Q0 = mp.mpf(Q_50_DIGIT_STR)` or
`Q0_MP_PIN = Q_50_DIGIT_STR` in its own source, so `independent` is false on the
face of it, no inference required:

    markov_identity_symbolic_probe          (wants `comparison` — evaluates BOTH pins)
    probe_he4_magic_baryeven_prune
    lambda_scale_substrate_probe            (also manifest `ideal_muon`)
    qbeta_c3_rung_structure_analysis
    qbeta_habiro_f_from_shape_collapse
    qbeta_rung1_div25_framing_squared_test

**One cone case is genuine, and flagrantly so.**
`chirality_topology_binding_probe` does `from hecke_channel_binding_probe import
channels, BONDS, E0, Q0` — it imports **`Q0` itself**, prints it, and writes
`"q0": str(Q0)` into its own witness payload while declaring `independent`. A
witness that records q₀ and denies reading it is self-contradictory.

### The three false positives

| producer | what it imports | why `independent` is CORRECT |
|---|---|---|
| `eigenbasis_structural_lemmas_probe` | `partitions_of(n)` from `hecke_characters` | signature `(n)`, zero q-references. Pure combinatorics. The probe proves a Laurent-character bar-symmetry identity **for all q**. |
| `habiro_witness_convention_adjudication_probe` | `tr_M_atomic_fast` | used **symbolically**: `U = sp.Symbol("u")`, `expr.subs(q, U**2)`, evaluated only at small exact rationals |
| `chi_content_eigenbasis_probe` | `atom_canonical_crossings(Z, N)` | zero q-references; it calls `classify_crossing(c, d, h_val, …)` where the substrate **h is a PARAMETER**, supplied by the caller |

`habiro_witness_convention_adjudication_probe` anticipated the flag in its own
`q0AnchorReason`: *"No substrate anchor is read and none is recorded --
deliberately no q0Value, which the q0-anchor audit correctly reads as
contradicting `independent`."* The author was right and the checker was wrong.

### RETRACTION of my own verification

PR #5806 listed `chi_content_eigenbasis_probe` as **✓ hand-verified genuine**,
on the evidence that `canonical_braid_crossings` contains
`from q_parameter import Q_50_DIGIT_STR`. **That is a fact about the MODULE, not
about the imported SYMBOL**, and it is exactly the standard this whole arc has
been correcting. The module's q₀ sits at lines 89–91, in a guarded block
computing `_AVG_COLOR_DELTA` — a different symbol entirely.

### Class 5: parameterised-on-q is not reads-q₀

Four classes were closed in #5806 (docstring text, the declaration's own reason
string, module-name-vs-symbol, cone-into-provider). This is a fifth, and it is
the hardest:

> A function that takes `q` — or `h = q − q⁻¹` — as an **argument** is
> q-PARAMETERISED, not q₀-READING. Whether its caller is q₀-dependent depends on
> what the caller passes, which is dataflow. No import-cone walk can decide it.

`classify_crossing(c, d, h_val)` is the worked case. This is why the corpus's
symbolic/q-generic probes keep landing in the violation list: **being about q is
the opposite of being pinned at q₀**, and a reachability analysis reads them the
same.

### A symbol-level cone was attempted and NOT shipped

I implemented one (`symbol_reads_q0`: traverse only if the imported symbol's own
definition reads q₀). It moved the broad numbers — `cone clean` 768 → 817,
`cone reads` 1748 → 1699 — and **did not fix any of the three false positives**,
because they fail on class 5, which symbol resolution does not reach. Reverted
rather than merged: an analyser change I cannot validate is how the last three
wrong numbers got published. The idea is sound and worth finishing with dataflow;
it is not worth shipping half-done.

**Verdict: 7 of 10 are real.** Fixing them means correcting each declaration —
five to their actual pin, `markov_identity_symbolic_probe` to `comparison`, and
`chirality_topology_binding_probe` to whatever `Q0` resolves to in its source
module.

## PROSE-VS-CODE, TWO MORE CLASSES FIXED 2026-08-26

Working this bean's closing lesson -- "a q0 checker that reads prose about q0
will always over-flag, and the corpus is full of careful prose about q0
precisely where the code is careful not to use it." Three classes were already
fixed (reason strings, module-vs-symbol imports, cone traversal). Two more, both
in q0_producer_pin_classifier.py, both the same shape one level down: the prose
is INSIDE the code, as message strings.

CLASS 4 -- is_prose covered only DOCSTRINGS. A guard that refuses to straddle,

    raise SystemExit(f"ANCHOR STRADDLE in q-pinning-50-digit.witness.json: ...")

names a muon artifact in its own warning, and the classifier counted that as
evidence the producer READS the muon pin. qbeta_habiro_residual_probe is
declared PROTON, carries exactly that guard, and was indicted on it. The prose
it matched exists precisely to prevent the thing it was taken to prove.
Fixed by _message_string_ids(): str constants inside an f-string, a raise, or a
print/warn/log call are prose -- EXCEPT when the string is an argument to an
operative call (open, Path, read_text, mpf, Decimal, json.load), because those
strings do the thing rather than describe it.

CLASS 5 -- the env-like gate read RAW SOURCE. `if s.lower() in MUON_ENV and
"ANCHOR" in src` tested the whole file text, comments and strings included, so
a file that merely DISCUSSES anchors satisfied it. That is what produced
su4_1111_markov_trace_probe's `env-like "muon"`. Fixed by _code_only_text(),
which tokenizes and drops COMMENT and STRING tokens.

MEASURED HONESTLY: the headline counts DO NOT MOVE. proton 71, muon 27, none
41, BOTH 9, before and after; the BOTH list is identical. What changed is the
EVIDENCE:

  qbeta_habiro_residual_probe  muon: ['"ANCHOR STRADDLE in q-pinning..."',
                                      '"q-pinning-50-digit.witness.json"']
                            -> muon: ['"q-pinning-50-digit.witness.json"',
                                      '(prose only) "...docstring..."']
  su4_1111_markov_trace_probe  muon: ['hardcoded muon 50-digit',
                                      'env-like "muon"']
                            -> muon: ['hardcoded muon 50-digit']

Both files stay BOTH, and correctly so -- each has independent real evidence.
qbeta_habiro_residual_probe genuinely does
`record_upstream(COMP / "q-pinning-50-digit.witness.json", ...)`, and its own
comment explains why that is right: the pin witness still supplies the CODATA
uncertainty budget, an m_p/m_e quantity belonging to the proton layer, while q0
itself comes from Q_50_DIGIT_STR. So the fix removes FALSE EVIDENCE, not false
verdicts. Claiming it reduced the over-flag count would be wrong.

REGRESSION TEST, and it can actually fail. --selftest asserts both demotions.
Verified by reverting each fix in turn: the reverted classifier FAILS with 2
regressions, the fixed one passes. That matters here more than usual, because
the counts do not move when this regresses -- the selftest is the only thing
that would notice.

STILL OPEN from the earlier pass: the 5 of 10 flagged producers not yet
hand-checked (chirality_topology_binding_probe, eigenbasis_structural_lemmas_probe,
habiro_witness_convention_adjudication, qbeta_habiro_f_from_shape_collapse,
qbeta_rung1_div25_framing_squared_test).


## RETRACTION 2026-08-26 — the 870 figure is CORRECT; I measured a different thing

Earlier this session I measured the muon-pinned witness count at 149, reported
AGENTS.md's 870 as "stale by ~5.8x", and named correcting it as next work.
THAT WAS WRONG and the number should not be changed.

WHY. "Carries the muon fingerprint" is ambiguous in this corpus, and the
ambiguity is already documented one directory over:
computations/audits/muon_pin_three_values_probe.py establishes that THREE
different values are all called "the muon q0" --

    A  1.1099785955573347...   frozen canonical pin
    B  1.10997859555418057...  lepton-tower derivation, CODATA 2018
    C  1.10997859564273904...  lepton-tower derivation, CODATA 2022

diverging at the 13TH SIGNIFICANT DIGIT. So the prefix length silently selects
which of the three you count:

    match on                    counts             2026-08-16   2026-08-26
    1.109978595   (10 digits)   all three             871          477
    1.1099785955573347 (full)   canonical pin only    468          149

870 is the ten-digit reading and is right. I matched the full canonical literal,
so I was counting A alone and missing B and C entirely.

WHAT IS ACTUALLY TRUE: the migration HAS run -- 871 -> 477 under the recorded
definition, a 45% drop, measured with one script at both ends (git ls-tree per
revision, so the denominator moves with the tree, 2947 -> 3102). It has NOT
fallen to ~149.

THE REAL DEFECT, and it is the one this bean is about: the number was recorded
WITHOUT ITS METHOD, in a domain where the method is genuinely ambiguous and the
ambiguity is documented elsewhere in the same corpus. That is prose about q0
that cannot be checked against code -- so the next reader measures it, gets a
different answer, and is one edit from replacing a correct figure with one
answering a different question. I was that reader.

FIXED: AGENTS.md now carries the method beside the number, both readings, both
dates, and a pointer to muon_pin_three_values_probe.py for why the definition
matters. Added computations/audits/muon_pin_witness_census.py so the count is
re-derivable at any revision rather than remembered -- it prints every prefix
length side by side and marks the two that are ambiguous with the proton pin,
which is the shape of mistake one notch further down.


## THE 5 UNVERIFIED PRODUCERS — HAND-CHECKED 2026-08-26, one is a real defect

Cleared the "not yet hand-checked" residue from the earlier pass. None of the
five is flagged `muon` any more (three `none`, two `proton`), but "the checker
says none" is not a hand-check, so each was read against its source.

  eigenbasis_structural_lemmas_probe        CORRECT. q0Anchor "independent"
                                            with an explicit reason: evaluated
                                            at any q0, and the declaration
                                            exists to stop the builder stamping
                                            a default pin plus a q0Value it
                                            never used. No q0 read anywhere.
  habiro_witness_convention_adjudication    CORRECT. q0Anchor "independent",
    _probe                                  deliberately no q0Value. (The bean
                                            recorded this without its `_probe`
                                            suffix, which is why it read as
                                            missing.)
  qbeta_habiro_f_from_shape_collapse        CORRECT. proton, via
                                            `from q_parameter import
                                            Q_50_DIGIT_STR`. No muon path.
  qbeta_rung1_div25_framing_squared_test    CORRECT. same, proton.
  chirality_topology_binding_probe          *** DEFECT, see below ***

### chirality_topology_binding_probe declared `independent` on a FALSE experiment

It imports Q0 from a PEER PRODUCER -- `from hecke_channel_binding_probe import
... Q0`, where `Q0 = Q_MP`, the proton pin -- uses it numerically, records
`"q0": str(Q0)` in its witness, and declared:

    q0Anchor: "independent"
    reason:   'PROVED by running this producer under QOU_Q0_ANCHOR=muon and
               =proton and diffing the emitted witness: the only non-ephemeral
               leaves that differ are q0Anchor and q0Value THEMSELVES -- every
               substantive field is byte-identical'

RE-RAN THAT EXPERIMENT. It refutes the claim. **43 non-ephemeral leaves
differ**, among them /E0_MeV and EVERY entry of /channel_values_at_q0 for pp,
nn and pn. Those are physics fields, not labels. Q_MP does track
QOU_Q0_ANCHOR (verified directly: muon 1.1099785955573347..., proton
1.10997858275138...), so the toggle really did move the value and the outputs
really did move with it.

And the committed witness held the MUON value for q0, under an `independent`
label, contrary to the proton default.

CONCLUSION UNAFFECTED, which is why this is hygiene and not an emergency:
Pauli-complete is the best model under both anchors, RMS values move by ~1e-8
relative -- consistent with the 11.5 ppb separation, and exactly the magnitude
this bean predicts for the class. Fixed: q0Anchor -> "proton", witness
regenerated at proton, reason string rewritten to record the measurement rather
than assert the refuted one.

### THE AUDIT GAP THIS EXPOSES

inherited_q0_pin_audit.py audits inheritance through WITNESS FILES
(upstream=...witness.json, reading src['constants']['q_0']). It does not audit
inheritance through a PYTHON IMPORT FROM A PEER PRODUCER, which is how this one
got its pin. q0_producer_pin_classifier scored it `none` for the same reason --
Q0 arrives from a sibling probe, not from q_parameter/constants, and the
provider-terminal rule (class 3) stops the walk before it reaches the real
source.

So there is an unaudited inheritance path: producer A imports a q0-bearing
symbol from producer B. Worth its own pass; not attempted here.

### AND IT IS THE SAME LESSON AGAIN

The declaration was prose about q0 that the code contradicts -- a reason string
asserting an experiment, where running the experiment refutes it. That is the
fourth variant this session, after the checker reading its own guard's warning,
the raw-source "ANCHOR" match, and the 870 figure recorded without its method.
The pattern is not that the prose is careless; it is that prose about q0 is
never re-run, so it decays silently while the code moves.


## CORRECTION 2026-08-26 — I got 2 of my 5 hand-checks WRONG; the sibling is right

My hand-check above recorded qbeta_habiro_f_from_shape_collapse and
qbeta_rung1_div25_framing_squared_test as "CORRECT. proton, via
`from q_parameter import Q_50_DIGIT_STR`. No muon path."

THAT IS WRONG. Both bind Q0_MP_PIN = Q_50_DIGIT_STR in their OWN source (lines
108 and 65) and declare q0Anchor: "independent" (lines 391 and 245). The
sibling's file-local list has them right and my entry is retracted.

HOW I GOT IT WRONG, because it is this arc's own error class and I walked into
it mid-arc: I confirmed what the CLASSIFIER said the pin was (proton) and that
there was no muon path, and reported on the CODE. The defect is a mismatch
between the code and the DECLARATION, and I never read the declaration. I
answered "which pin does it use" when the question was "does what it says match
what it does" -- the same substitution the whole bean is about.

CORRECTED TALLY for my five:

    eigenbasis_structural_lemmas_probe        CORRECT   (sibling agrees)
    habiro_witness_convention_adjudication..  CORRECT   (sibling agrees)
    chirality_topology_binding_probe          DEFECT, fixed by me
    qbeta_habiro_f_from_shape_collapse        DEFECT    (I said correct)
    qbeta_rung1_div25_framing_squared_test    DEFECT    (I said correct)

3 of 5 are defects, not 1 of 5.

CONVERGENCE ON chirality_topology_binding_probe, from two directions: the
sibling read the import (`it imports Q0 itself, prints it, and writes
"q0": str(Q0) into its own witness while declaring independent -- a witness that
records q0 and denies reading it is self-contradictory`); I re-ran the anchor
experiment its q0AnchorReason cites and measured 43 differing non-ephemeral
leaves. Same defect, independent routes, and the two findings are complementary
-- theirs shows the declaration is self-contradictory on its face, mine shows
the specific experiment the reason string invokes REFUTES it. Fixed on my side
(q0Anchor -> proton, witness regenerated, reason rewritten).

THE TWO I MIS-CLEARED ARE NOT FIXED. They are on the sibling's file-local list
and are theirs to drain; I am not duplicating the fix. Flagged here so the
mis-clearing does not sit in this bean as a clean verdict.


## COORDINATION 2026-08-26 — a sibling owns the shared normaliser; I am standing off it

PR #5818 (branch claude/muon-proton-pinning-migration-0u9qoc) landed
computations/audits/_source_normalise.py: code_only() (tokenize, blank COMMENT +
triple-quoted STRING, PRESERVE line and column), blank_declaration_prose(),
code_only_ast(), with its own --selftest. Its docstring records that the corpus
already carried FOUR independent correct implementations of that blanking pass,
shared by none.

I ADDED A FIFTH, AND MINE IS WORSE. My _code_only_text() in
q0_producer_pin_classifier.py joins tokens with " ", which DESTROYS LINE
NUMBERS -- the exact 476-vs-647 defect their module exists to fix. It currently
only gates a boolean ("ANCHOR" in code_only) so no reported position depends on
it, but it should become `from _source_normalise import code_only` once #5818
lands. Recorded so it does not quietly persist as implementation #5.

WHAT I HAVE THAT THEIRS DOES NOT, offered to them for folding in:
_message_string_ids() demotes str constants inside an f-string, a raise, or a
print/warn/log call -- EXCEPT when the string is an argument to an operative
call (open, Path, read_text, mpf, Decimal, json.load). code_only deliberately
leaves single-quoted strings intact (they carry declared values), which is right
but leaves MESSAGE strings matchable; the operative-call carve-out is the
load-bearing half, since without it real reads get blanked. Orthogonal to
blank_declaration_prose, which keys on dict keys rather than call context.

Posted all of this on #5818 as a coordination comment, including the retraction
of my two wrong hand-checks (their file-local list has them right).

STANDING OFF: the q0 reroute and the shared-normaliser wiring are
dependency-ordered mechanical work with one owner, and that owner is the #5818
branch. Their own scoping is the reason to stay off it -- they found the 44 are
not one batch (12 with no committed witness, 9 using record_upstream, and of the
remainder 5 BLOCKED because rerouting a producer whose upstream is muon-built
MANUFACTURES a straddle). That is exactly the kind of finding a second agent
batching by count would have destroyed.

My side of this bean is done: the two prose-vs-code classifier classes, the
selftest that can fail, the 870-method retraction plus the census script, and
the chirality fix.

---

## 2026-08-28 status re-measure — the standing-off note above is STALE; the block is now elsewhere

The last entry says *"STANDING OFF: … one owner, and that owner is the #5818
branch."* **#5818 merged 2026-08-26**, so no one owns it. That is not, however,
an invitation to execute: the work re-partitioned while the branch was away.

Measured on `main` today:

| tranche | state |
|---|---|
| batch C — 12 with a witness, no `record_upstream` | **executed** (`a2923609c3`) |
| no-witness batch (11) | **0 ready / 11 blocked** (`11db7f2856`) |
| 12 blocked on muon-built upstreams | **unchanged — the critical path** |

So the remaining work is blocked on two things, neither of which is effort:

1. **Dependency order.** A producer's q₀ can only move *after* its upstream
   witnesses move. #5818 established this by stopping at its first file:
   `hydrogen_qshuffle_compound` consumes `proton-mass-full-tower-50dps`
   (`q0Anchor: "muon"`), so rerouting it would **manufacture** the straddle this
   epic exists to remove. Any by-count batching cuts across the graph.

2. **An owner decision this bean already declined to make.** Its own words:
   *"Nothing in this batch is executable until either `1j39` gives the 7 a
   witness mechanism, or the owner accepts a reroute with no before/after
   record. The latter is not mine to decide."* That is still true and I am not
   overriding it — a reroute with no before/after record is exactly the kind of
   unverifiable change the four constraints in AGENTS.md exist to prevent.

**What would unblock it, in order of cheapness:** `1j39` (give the 7 a witness
mechanism, making the no-witness batch measurable); then walk the *roots* of the
upstream graph — the muon-built witnesses that themselves consume nothing muon —
since those are the only nodes movable without creating a straddle.

I did not attempt (2) and did not batch by count. Recorded so the next reader
does not repeat #5818's stop, or mistake the merged PR for an idle claim.


## 2026-08-28 — the `independent` label hides producers from THIS migration (PR #5895)

Slice taken: bean `qou-324i`, which was `todo` and unclaimed since 2026-08-23.
No overlap with the batch sweep; no manifest edit, no anchor-defining witness
touched, and the two producers a sibling claimed on 2026-08-26 were MEASURED but
NOT edited.

**Why it belongs to this bean.** `q0Anchor: "independent"` asserts the compute
never reads q0, so such a witness is invisible to every pin audit -- including
this migration's inventory. `probes/lambda_scale_substrate_probe` is the case:
it reads `q-pinning-50-digit.witness.json` directly, is listed `ideal_muon` in
the manifest, and declared `independent`. It is a MUON producer the migration
could not see. Relabelled `muon`, which puts it in scope; whether it should MOVE
is a separate question and is not answered here.

**Three labels corrected, zero numbers moved.** Each regeneration moved exactly
three non-ephemeral leaves -- `q0Anchor`, `q0AnchorReason`, and `q0Value`, the
last appearing where the witness previously recorded NO pin at all (rule 4's
last bullet). No substantive field moved in any of the three, so the committed
values were already at the anchor the manifest declares; only the label was
wrong.

  probe_he4_magic_baryeven_prune        independent -> proton   (manifest: physical_proton)
  qbeta/qbeta_c3_rung_structure_analysis independent -> proton   (manifest: physical_proton)
  probes/lambda_scale_substrate_probe    independent -> muon     (manifest: ideal_muon)

All three CONTRADICTED their own manifest entry, so no judgement call was needed.

**Provenance checked, not assumed** (PR #5883 / bean `qou-4un2` reports the
migration deleting provenance through bare producers). Before/after per file:
all of `scriptFile`, `commitSha`, `engine`, `engineVersion`, `scriptHash`, and
`auditOnly` where present, survived all three re-runs. Nothing lost.

## The unaudited peer-import inheritance path is now audited

This bean records: "there is an unaudited inheritance path: producer A imports a
q0-bearing symbol from producer B. Worth its own pass; not attempted here."
Attempted. `q0_independence_checker --flip-validity` now detects it, with the
known positive (`chirality_topology_binding_probe`'s `Q0 = Q_MP` via
`hecke_channel_binding_probe`) pinned in `--selftest`.

The guard that makes it usable: `hoefsmit_symbolic.Q` is `sp.symbols('q')`, not
a q0. Without a symbolic-RHS check the scan indicts two producers whose
disposition is CORRECT -- a detector keyed on the shape of a name rather than
its role, which is this bean family's recurring failure. Both directions are in
the selftest so a narrowing cannot lose either silently.

## CORROBORATION of a sibling's claimed pair — measured, not duplicated

The 2026-08-26 note here retracts two hand-clears and leaves
`qbeta_habiro_f_from_shape_collapse` and `qbeta_rung1_div25_framing_squared_test`
to their claiming sibling. I did not edit them. I did RUN the flip:

  qbeta_habiro_f_from_shape_collapse       MOVES, 5 fields, e.g. /data/numerical_sanity_at_q0/S_N0_at_q0
  qbeta_rung1_div25_framing_squared_test   MOVES, 7 fields, e.g. /data/numerical_at_q0/[5]_q

Both move SUBSTANTIVE numerical fields, so the sibling's DEFECT verdict is
independently confirmed by a different method (they read the declaration; I ran
the experiment it cites). Still theirs to fix.

## Two harness defects found by using the harness — reported, not fixed

1. `anchor_flip_straddle_audit._run` sets no PYTHONPATH and runs only with
   `cwd=<producer dir>`, so a producer importing a sibling under `computations/`
   is reported `RUN-FAIL ... UNTESTED`. Measured on `chi_content_eigenbasis_probe`
   and `eigenbasis_structural_lemmas_probe`: exit 1 plain, exit 0 with
   `PYTHONPATH=computations:.`, ZERO tracebacks either way. That audit is a
   BLOCKING gate in `scripts/staleness-gates.sh`, so it currently under-reports.
   Not fixed here: it moves a live gate's output and wants its own before/after.
2. Its EPHEMERAL mask has `elapsed_seconds` but not `elapsed_sec`, so
   `markov_identity_symbolic_probe`'s first "moved" field is
   `/results/0/bridge/elapsed_sec` -- the harness measuring itself.

Also: `habiro_witness_convention_adjudication_probe` is RUN-FAIL even WITH
PYTHONPATH, so it is UNTESTED rather than clean, and stays pending.

---

---

## The superseded-muon class TRIAGED 2026-08-28 — 19 actionable, not 260

The 2026-08-22 partition recorded the superseded-muon population as the largest
untouched class and I recommended it as the next work item on that basis. **That
recommendation was inflated by the same error class this arc kept correcting: a
population count is not a work count.**

    witnesses carrying the superseded value          265
      under _deprecated/                             214   <- 81%, not live work
      live                                            51
        no scriptFile at all (orphan)                 13
        scriptFile names a missing producer            2
        scriptFile names a LIVE producer              36
          self-declaring (deliberate)                 17
          GENUINE candidates                          19

**265 -> 19. A 14x over-count of actionable work.**

The 17 deliberate ones declare themselves in a field or producer name —
`stale_muon_pin_q0` (x4), `q0_muon_pin` / `q_muon` / `q0_muon` (x6),
`muon_pin_three_values_probe` whose subject IS the pin history,
`probe_trace_convention_production_impact`, and two audits whose subject is
literals. Re-pinning any of them would destroy what they measure.

The 19 genuine candidates carry it under a **bare** pin key (`q_0`, `q0`, `q`,
`q_0_50dps`, `q_0_mpf50`) with nothing declaring it deliberate. **Still an upper
bound**: each needs an individual read. Two to flag before anyone starts —
`q_beta_predicted` carries `CAL-2_q_0`, and naming CAL-2 identifies *which
calibration*, not *which pin* (the conflation the partition audit retracts); and
`confinement-operator-selection` is an LP/SDP witness, so the dual fields matter
to any re-run.

**Separate problem, worth its own bean:** the **13 orphans** are live, on the
superseded value, and carry **no `scriptFile` at all` — nothing can regenerate
them and nothing records what did. Re-pinning is not even an available action;
it is a provenance gap, not migration work.

Full detail: `docs/audits/2026-08-28-superseded-muon-population-triage.md`.


### 🛑 Correction to the entry above: the "13 orphans" were my detector, not a gap

I wrote that the 13 were a provenance gap needing their own bean — *"nothing can
regenerate them and nothing records what did"*. **Wrong.** The scan keyed on
`scriptFile`/`script` only. Opened by hand:

- **8** record provenance under `computation` — all 8 producers **exist**, 6 of
  them under `docs/audits/scripts/`, which a `computations/`-scoped search
  cannot see.
- **5** record no provenance field but resolve by the witness-name ↔
  producer-name convention — including `q0-value-drift-audit`, which this arc
  has been regenerating all along.
- **0** genuinely unregenerable.

Real finding: 13 live witnesses **omit `scriptFile`** — a field-completeness gap
in schema usage, not lost provenance. **No orphans bean is warranted.**

**Fourth detector correction in this arc**, all mine, two high and two low:
dual-purpose 21→3 (substring), contradictions 2→11 (file-local), superseded-muon
work 265→19 (population≠work), orphans 13→0 (`scriptFile`-only). Treat any count
here as a hypothesis with a several-fold error bar until a member is read.


## 2026-08-29 — the WITNESS count is not the migration's size; the SOURCE count is

Found while merging #5892 with main, and it corrects a framing this bean's
own title carries.

This bean is scoped as *"move the ~840 muon-q0 **witnesses**"*. But a witness
is an output — re-running its producer moves it only if the producer
**consults** `q_parameter`. Measured with the corpus's own
`computations/audits/q0_hardcoded_pin_audit.py` (which already existed; I
nearly rebuilt it before grepping):

    files mentioning a pin literal : 362
    PROSE_ONLY (not a finding)     :  66
    UNDECLARED (migration scope)   : 248
    consistent / not reached       :  46
    CONTRADICTS (defect)           :   2
    OFF_PIN (neither pin, in code) :  10

**248 sources hardcode a pin the manifest cannot reach.** For those, the
manifest is inert and a re-run is a no-op — so the sweep is a *source* edit,
not a *witness* regeneration, and any plan sized off the witness count
understates it.

Worked counterexample, and the reason this was found:
`deltalambda/deuteron_trefoil_qinvariant_closed_form_probe.py` line 38 is a
hardcoded frozen-muon literal. Its stem is in **neither** manifest list, so
the standard inference ("not `ideal_muon` ⇒ resolves to proton") says proton
— and the file never asks. Measured: its committed `z_markov` matches the
frozen muon anchor to **1.7e-19**, i.e. 21.9 ppb from proton (11.5 ppb in q₀
amplified by `d ln z/d ln q = 3 − 2q²/(q²+1) = 1.896`). A live pin, not a
stale output.

This invalidated a headline inference in #5892 ("all 19 GENUINE candidates
resolve to proton on a run today"); that PR's body now carries the
correction. The 265 → 19 population reduction is unaffected — it is a count,
not an inference.

**Not swept here.** Annotated only: the probe now records that its `LOCKED`
means the anti-fit target and not the anchor, that nothing in it consults
`q_parameter`, and that its verdict is robust to the eventual re-pin
(11.5 ppb against a 0.6904 % miss). Constraints 1–4 above still gate the
actual sweep.

**Suggested re-scope for whoever runs this:** partition by *whether the
producer resolves or hardcodes* before sizing. The resolving set is a
re-run; the 248 hardcodes are edits, each one changing every number that
producer prints — so each needs its own verdict-robustness check of the kind
done above, not a blanket regeneration.
## 2026-08-29 — second drain pass (PR #5950): 47 -> 5 flips

Ran the proton migration under the recorded owner authorisation. Gates:
q0-anchor flip 47 -> 5, q0-value drift 318/101 -> 240/26, refill ratchet green
(NEW 0), raw-float64 NEW 0 / REGRESSED 0. No baseline widened.

THE PARTITION THIS BEAN ASKED FOR, MEASURED. Of the 45 producers behind the 47
flips, **25 hardcode a q0 literal in EXECUTABLE code** (AST-checked). For those
a bare re-run does not migrate — it writes `q0Anchor: proton` onto a payload
computed with frozen muon A, i.e. replaces a truthful contradiction with a
silent one. All 25 were run, inspected and reverted; 17 were then migrated at
the source with a per-producer verdict-robustness check.

THE MANIFEST GATES THE STALENESS CHECK. A producer that declares no anchor
inherits the previous run's pin unless judged stale, and staleness needs either
payload evidence or `q0_anchor_is_declared`. 40 of 48 had an UNLISTED stem, so
their stale pair was immune to any number of re-runs. That is why constraint 4
is load-bearing rather than procedural.

Also: 11 producers falsely declared `q0_anchor=False` (deleting the stamp every
run); `main`'s `a-K-via-lp-dual-full` active_set disagreed with its own y_star
in all six atoms; `low_isotope_sign_flip_diagnostic` fixed (its TypeError was a
string/float boundary, and the naive fix would have added float64 aggregation).

NOT LANDED: the c3even/c4even ladder re-run. It moves `c2_even` -8.00641 ->
-7.45876, and that is NOT the pin — origin/main's producer with its frozen
muon-A literal produces the identical value. It is qou-cds1's C->D
re-derivation surfacing through a witness that predates its own producer.

Remaining 5 flips, all with stated reasons, in
docs/audits/2026-08-29-q0-muon-anchor-repin-drain.md.

## 2026-09-08: this bean is the canonical ledger for the q₀-gate family (audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 3 / §7.3 C3)

Chosen because AGENTS.md names it as the migration tracker. Family members and statuses as of 2026-09-08 (each now carries a one-line pointer back here; no status changed). Note `qou-3f7a`'s own finding: the two red q₀ gates are one unfinished migration — this one.

| bean | status | subject |
|---|---|---|
| qou-1c4y | in-progress | MIGRATION: move the ~840 muon-q₀ computations/ witnesses to the proton anchor (this ledger) |
| qou-3f7a | in-progress | fix the two RED q₀ gates: anchor flip + value-drift ratchet |
| qou-324i | in-progress | the `independent` q₀ disposition tests override-sensitivity — 7 false positives |
| qou-po7i | in-progress | q₀ anchor selected by sys.argv[0]; 2384/2785 producers undeclared, 1887 witnesses no anchor |
| qou-kx04 | in-progress (parent qou-pq8k) | 4 more witnesses landed with no q0Anchor (1885 → 1889) |
| qou-aj91 | in-progress | ARCHITECTURE: 85 producers read the anchor-defining witness directly, bypassing q_parameter |
| qou-zk51 | in-progress | q₀ gates are blind to witnesses that consume the anchor but record only derived numbers |
| qou-q0rf | in-progress | q₀-anchor refill ratchet RED on main (NEW 147) — fix the arrival rate |
| qou-eggf | in-progress | 17 witnesses put free text in q0Anchor instead of the token |
| qou-y98b | in-progress | gate the q0Anchor refill: ~50 % of new witnesses land unstamped |
| qou-i229 | todo | AUDIT: 35 published figures have no computational provenance |
| qou-9ugp | todo | retired muon pin literal 1.10997859555733471 hardcoded in ~180 producers, invisible to the 3f7a drain |
| qou-a1lw | in-progress (empty body) | Session: drain the OLD-MUON (CODATA 2018) B-population witnesses |
| qou-silm | completed | AGENTS.md's frozen muon pin is stale — anchor moved to CODATA 2022 on 2026-08-28 |
| qou-m4au | completed | drain the qou-silm stale-figure sites |
| qou-tekx | todo | muon pin migration to CODATA 2022 — staging, not a sweep |

Previously measured cross-citation (16 beans, 17 directed links, ~10 %): 3f7a→{q0rf,y98b}, 324i→{zk51,1c4y}, aj91→{3f7a,1c4y}, zk51→3f7a, q0rf→{3f7a,1c4y}, eggf→{q0rf,tekx}, y98b→kx04, 1c4y→{324i,aj91}, i229→po7i, 9ugp→{3f7a,y98b,1c4y}, silm→3f7a, m4au→silm.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.



## 2026-10-10 (M6, qou-2cof): six content blocks owe a proton re-pin
physics-names-knot-operations:17, mass-tower-coefficient-stratification-proof:26, exterior-square-borromean-proof:47, derived-mass-formula-light-isotopes-proof:21 and its -context:1, schrodinger-color-falsifiability:33. They are now labelled with the muon pin their producers actually used. None is an E1/E2 exception. Two need a producer re-run (wedderburn-strata, deprecated derived-only-formula); one cites a missing cache; two have no producer.

## Progress Update (2026-11-16, PR #8188)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/CodataTruncationAndQ0AnchorRecentering.lean` (wired into `QOU.lean`, `0` `sorry`, `0` vacuity advisories across all 7 static audits).
- [x] Paired with 50-dps `mpmath` + `sympy` verification probe `computations/probes/codata_truncation_and_q0_anchor_recentering_probe.py` and stamped witness `computations/probes/codata-truncation-and-q0-anchor-recentering.witness.json` (`allPassed: true`, `0` raw `float64` fields, `scriptCommitSha: 4f0055fd85b9bb82232f9b87ef757139e895bd6d`).
- [ ] Awaiting merge of PR [`litlfred/qou#8188`](https://github.com/litlfred/qou/pull/8188) (`548ed6acbe88e5772065a0fdb4d623f3472d3430`).

