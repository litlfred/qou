---
# qou-1c4y
title: 'MIGRATION: move the ~840 muon-q0 computations/ witnesses to the experimental (proton) anchor'
status: in-progress
type: task
priority: normal
created_at: 2026-08-07T08:35:43Z
updated_at: 2026-08-07T09:01:57Z
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
