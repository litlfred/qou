---
# 1j39
title: 'Integration: I-infra-no-witnessbuilder-P30 batch port'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-21T21:41:08Z
updated_at: 2026-10-04T15:20:57Z
---

## DUPLICATE of `cmiy` — DEFERRED (dedup 2026-06-28)

This bean and `cmiy` ("canonical watcher - P30 WitnessBuilder rollup") are
the **same work** (the P30 WitnessBuilder port, ~133 scripts). **`cmiy` is
the canonical bean**; see its body for the deferral rationale (high collision
with the active compute-PR storm — `/coordinate` 2026-06-28). Owner-close
this duplicate when convenient (resolve is human-only).

> **Investigated 2026-07-05 (swarm 2, PR #3344) — DUPLICATE of cmiy; kept OPEN pending owner close.** Same P30 WitnessBuilder scope; compute-blocked.


## 2026-08-25 — MEASURED: this is the only unstamped class regeneration cannot fix

Found while retracting a wrong recommendation on `qou-1c4y` (see its
2026-08-25-later entry). Relevant to this bean's scope:

`WitnessBuilder.build()` has called `resolve_q0_anchor_payload_first` since
`9d52483f5` (on `main` 2026-08-25T10:20 UTC), and it always sets `q0Anchor`.
So every WitnessBuilder producer stamps itself on its next run — the ~157
unstamped-but-single-pin witnesses in the corpus are simply stale and will
resolve on regeneration.

**Hand-rolled `json.dump` producers never reach `build()`, so they never
stamp — and re-running them never will.** Measured instance: four witnesses
computed 16:52 UTC / committed 16:54 (`58db04f28`), 6.5 h after the fix was on
`main`, all four unstamped. I verified that commit's own tree carried the fix
rather than assuming it, so this is not a dating artifact:

    computations/qbeta/birkhoff_barodd_pythagoras_bridge_probe.py
    computations/deltalambda/deuteron_interface_handle_curvature_probe.py
    computations/deltalambda/yekutieli_trefoil_surface2form_discretization_probe.py
    computations/qbeta/a3_branching_asymmetry_vs_required_probe.py

Each carries a single muon pin under a key `_Q0_FIELDS` already knows, at depth
≤ 3 — i.e. everything the resolver needs is present in the payload, and nothing
consults it. Porting these four to `WitnessBuilder` stamps them with no change
to any number.

This gives the port a second, sharper justification beyond consistency: it is
the difference between a witness that becomes verifiable on its next run and
one that stays unverifiable permanently.

---

## 2026-08-28 — the 4 are ported; the CLASS is measured; `cmiy` still owns the full port

### What landed

The four named producers now stamp, via a new shared helper
[`computations/_witness_q0_stamp.py`](../computations/_witness_q0_stamp.py)
(`stamp_q0(payload, __file__)`, called immediately before `json.dump`). Each
witness gained **exactly two keys** and nothing else:

    + "q0Anchor": "muon"
    + "q0Value": "1.10997859555733471989976322048322502665620840878015368660798114614493"

All four resolve **muon** — a `qou-1c4y` datum in itself: these were invisible to
every anchor audit and belong to the population that migration has to move.
Measured after re-running all four: 16 insertions / 8 deletions across the four
witnesses, and **0** changed lines outside `computedAt` / `notes` / the two new
keys. Assertions still pass, exit 0 on all four.

### A stamp, deliberately, NOT the WitnessBuilder port

This bean proposes porting to `WitnessBuilder`; that is still the right end state
and is still `cmiy`. But a hand-rolled payload is an arbitrary dict, so the port
reshapes each witness file — a large per-file diff, 120 times. The stamp adds the
two provenance keys and touches nothing else, so it applies uniformly across the
class where the port does not. A stamped hand-rolled witness still lacks
`environment` / `scriptHash` / `commitSha` / `precisionMetadata`. **`cmiy` is not
discharged by this.**

### The class, measured on `main` (this is the number `cmiy` needs to size itself)

    witnesses carrying q0Anchor                          1103
    unstamped, no resolvable pin                         1897
    UNSTAMPED but carrying a resolvable pin at depth <=3  169
      -> attributed to a named producer                  124   (120 producers)
      -> UNATTRIBUTED, scriptFile null                     45   (cannot be ported)

Producers using `WitnessBuilder`: 1341. Hand-rolled `json.dump` with no builder:
251. Every one of the 169 is hand-rolled, confirming this bean's premise.

The **45 unattributed** are the harder half and are not addressable by either
route: with `scriptFile` null there is no producer to port or to re-run. They are
the "bare producers" class this bean's own earlier entry names.

### Two defects I introduced and caught before they shipped

1. **The helper stamped payloads with NO pin.** `resolve_q0_anchor_payload_first`
   consults the payload first but *falls back to the manifest/env* when there is
   no payload evidence — measured, `{"zzz": 1}` resolves to `("proton", <proton
   pin>)`. Right for `WitnessBuilder`, which knows what q₀ its producer was
   handed; **wrong** here, where it would assert a layer the numbers may not
   belong to, with a provenance field vouching for it — the exact straddle this
   work exists to expose, manufactured by the tool meant to reveal it. Fixed:
   `stamp_q0` now requires the payload to carry a recognisable pin at depth ≤ 3,
   and an unstampable witness stays visibly unstamped. Five-case self-check in
   the commit.
2. **A regex patch hit the wrong site.** My `out = … with open(out, "w")` anchor
   also matched a *local* `out` inside `surface2Form()` in the yekutieli probe,
   injecting `stamp_q0(witness, …)` where `witness` is undefined —
   `NameError`, caught by running it. Re-patched by hand against the witness
   *filename literal*. Confirmed against the pre-change file that the failure was
   mine, not pre-existing.

### Still true

This bean remains a DUPLICATE of `cmiy` and is still owner-close-when-convenient.


---

## 2026-08-28 (later) — CORRECTION to my own entry above; the 2026-08-25 entry was right (PR #5923)

### What was wrong

`computations/_witness_q0_stamp.py` shipped this morning asserting

> "Every one of the 169 is from a hand-rolled producer."
> "That is the one unstamped class regeneration cannot fix."

**Both are wrong about most of the class**, and the error is mine and recent.
The **2026-08-25 entry above states it correctly** — that the ~157
unstamped-but-single-pin witnesses "are simply stale and will resolve on
regeneration", with hand-rolled producers as the *exception*. My 2026-08-28
entry took the exception and applied it to the population.

Re-measured: of **120 named producers, 62 already use `WitnessBuilder`**
(re-running stamps them) and only **17 hand-roll**. So the practical
consequence is the opposite of what the docstring said — most of the class is
closed by a re-run, and `stamp_q0` is the right tool for a minority.

### Why the count came out wrong — two extraction traps

Worth recording, because each independently produces a plausible-looking number:

| trap | wrong reading | true |
|---|---|---|
| `scriptFile` is **top-level**, not under a `witness` block | 0 named | 124 |
| `scriptFile` holds a **bare basename**, not a path, so `Path(sf).exists()` reads as "producer deleted" | 121 of 124 gone | 41 |

I hit both in a single session, in opposite directions, and each looked like a
finding before it looked like a bug.

### The number is now computed, not written down

`computations/audits/unstamped_q0_portability_split.py` splits the class by
**what closes each bucket**:

    RESOLVABLE BUT UNSTAMPED   180   (of 3406 tracked witnesses)
      A-producer-gone     41   nothing to port — producer deleted/renamed
      B-builder-stale     65   RE-RUN the producer; build() stamps
      C-handrolled        18   apply stamp_q0() — re-running never will
      D-unnamed           56   no producer named; classify by the recorded pin

and names the **16 live hand-rolled producers**, which is the actual
`stamp_q0` worklist. Do not restate these figures from any prose — the last
docstring constant was stale within one day of being written.

### Also corrected: the "45 unattributed" figure

Quoted in this bean, in PR #5899, and in `qou-uilp`. It was **correct when
measured** (169 resolvable / 124 named / 45 unnamed); today the same query
gives 180 / 124 / 56, because `main` moved. The `124` is stable. A separate
figure of "40" that appeared mid-session came from a filter that also admitted
falsy-stem rows and should be ignored.

### Not done here

`cmiy` still owns the full port. The 16-producer `stamp_q0` worklist is
tractable but each application needs its producer re-run and diffed for
byte-stability, which is the next step rather than this one.


---

## 2026-08-28 (later still) — BUCKET C IS NOT UNIFORMLY STAMPABLE. Measured 14/14 (PR #5923)

The split script names 16 live hand-rolled producers as the `stamp_q0`
worklist. **That list is a candidate set, not a worklist.** I ran 14 of them
(skipping `regenerate_y_lambda_orphans_conventionD`, which rewrites the
load-bearing y_λ tables, and counting the already-landed trefoil separately)
and only **3 are actually stampable**:

| outcome | n | producers |
|---|---|---|
| **STABLE — stamped** | 3 | `trefoil_complex_volume_probe`, `zhabiro_physical_z_pin`, `brane_tower_full_channel_trace_audit` |
| **STRIPS provenance on re-run** | 4 | `beta_ew_delta_I_321_and_wedderburn`, `beta_ew_delta_I_numerical_spectrum`, `nv_pslq_tr_pure_basis`, `sublemma_2_1_alpha_shift_extract` (+ `nv_categorical_derivation_probe`) |
| **numbers move** | 4 | the three `option_e_*` + `he3_pairknot_composite_lp_probe` |
| **content moved** | 1 | `qbeta_habiro_p8_identification_probe` (`check_q` -> `u` in the polynomial strings) |
| **now FAILS its own assertions** | 1 | `qbeta_cal3_anchor_table_impact` |
| **writes nothing** | 1 | `binding_additive_linked_cluster_probe` |

### The one that changes the plan: re-running STRIPS provenance

Five producers emit a witness **missing** `scriptFile`, `engine` and
`auditOnly` — fields the committed copy has. Those fields were added
**downstream**, by hand or by a later pass; the producer never emitted them.
So for these, running `stamp_q0` would add `q0Anchor` **while deleting the
`scriptFile` that my own split script used to classify them into bucket C.**
Net provenance loss, in the name of a provenance fix.

This is AGENTS.md's documented "bare producers" hazard (*"re-running one
deletes the field this audit keys on"*), and it means the split script's
`C-handrolled` bucket silently mixes two populations. **Fix the producer to
emit its provenance first** — then stamp. Not a two-line change.

### The other non-stampables are real findings, filed where they belong

  * The four numeric movers are `qou-fl9i`'s: its `mp.dps = 50` ->
    `set_compute_dps()` fix landed in the producers and the witnesses were
    never regenerated. Recorded there with the ruled-out alternatives
    (nondeterminism: no, self-reproducible; environment: no, identical under
    mpmath 1.3.0 and 1.4.1; input drift: no, inputs predate the witnesses).
  * `qbeta_cal3_anchor_table_impact` now prints *"VERDICT: INCONCLUSIVE — a
    factorization/wiring assertion failed"* and exits 1, flipping two
    `passed: true` to `false` against its committed witness. **Not
    investigated** — flagged here so it is not mistaken for a stamp candidate.

### What the split script should say

Its `C-handrolled` count is an upper bound on stampable producers, and the
measured ratio on this sample is 3 of 14. A future pass should either add a
dry-run stability probe to the script or carry this table; I have added a
warning to the script rather than a second measurement that will also decay.


### Follow-up, same day: the strip-provenance blocker was FIXABLE (7 of 15 now stamped)

The table above recorded "5 STRIP provenance on re-run" as a blocker. It is a
**producer defect**, not a property of those witnesses, and fixing it converted
most of the blocked set. Each of the 5 now emits `scriptFile` / `engine` /
`auditOnly` itself; **4 then stamped cleanly** (two q0 keys, zero numbers
moved, all resolve `proton`).

Running total: **7 of 15 examined are stamped.** Bucket C 18 -> 11 witnesses;
corpus-wide `q0Anchor` 1259 -> 1266.

**Two DANGLING `auditOnly` pointers repaired as a side effect.** Both targets
had moved to `docs/audits/_deprecated/` and the witnesses still named the
pre-move path — `sublemma-2-1-alpha-shift-extract` and
`nv-categorical-derivation-probe`. **Nothing in the repo checks that
`auditOnly` resolves**, which is how they stayed broken. I verified all five
associations rather than copying the recorded values; a third
(`beta-ew-delta-I-numerical-spectrum`) points at a doc that exists but does
**not** mention the witness. Kept as recorded and noted — not invented, not
deleted.

**One deliberately left unstamped.** `sublemma_2_1_alpha_shift_extract` gets
the provenance fix but no stamp: a re-run moves **92 lines of numbers**,
`value_re` shifting in the **4th significant digit** (1.00544843… ->
1.00552033…) and `max_relative_residual` 25.3556 -> 25.5245, a ~7e-5 relative
change. That is **two orders above** the `qou-fl9i` dps class and has a
different, unidentified cause — `34b2a75d43` did not touch this file. Stamping
forces a regeneration, so it would have rewritten those values under a commit
message about provenance. Its witness is byte-identical; the producer carries
the reason. **Open: what moves it.**

**A rake I walked into, recorded because this bean's own text warns of it.** My
first import insertion landed inside a multi-line `from x import (...)` block
and broke two producers — exactly `qou-fl9i`'s *"import insertion is
AST-located; a regex lands inside multi-line blocks"*. Redone with
`ast.end_lineno`, which is the only thing that sees the block's true extent.

**Generalisation for whoever takes the rest:** "not stampable" was usually a
fixable producer defect rather than a fact about the witness. Five of the eight
blockers were the same downstream-provenance bug. Check that before writing a
candidate off.


### CORRECTION to the entry above: the `sublemma_2_1_alpha_shift_extract` drift IS identified

I wrote that its ~7e-5 move had a "different, unidentified cause". **It is
identified, and the corpus was one grep away.** It is the **float64 -> mpmath
port**, and the committed values are the OLD ones:

    witness computedAt   2026-08-24T08:06:59
    253e2ffaf5 landed    2026-08-24T08:10:43     <- 3 min 44 s later

`253e2ffaf5` (*"sublemma alpha-shift solves in mpmath, and the FIRST fix was
wrong"*) swapped `chi_lambda_fast` -> `chi_lambda_fast_mp` and `Q` (a Python
float) -> `Q_MP` (an mpf). The committed numbers came out of the float64
producer **minutes before it stopped existing**; a fresh run is the mpmath one.
So the drift is a **correction**, the fresh values are the better ones, and my
framing of it as a worrying unexplained move was wrong in sign.

This is the same *"stamped minutes before the commit that superseded it"*
signature as §0 of
[`2026-08-23-pr5517-downstream-witness-attribution.md`](../docs/audits/2026-08-23-pr5517-downstream-witness-attribution.md)
(there: seven minutes), and the same shape as its §1, where float64-floor
values dropped ~55 orders once the rep was fixed upstream.

**A near-miss worth recording.** §2 of that same audit attributes a **1.745e-7**
move in this exact witness to a **muon -> proton re-pin** on regeneration
(`qou-b3l8`). That is a real finding, it is about the right file, and it is
**not** what I measured — the re-pin has since happened (`parameters.q_0` now
reads the proton pin `1.10997858275138…`) and 7.19e-5 is ~400x that effect.
Two different causes, five days apart, in one witness. Reaching the audit and
stopping at §2 would have produced a confident wrong attribution.

**Still not regenerated here**, and the reason is unchanged even though the
values are now known to be better: stamping forces a regeneration, and rewriting
92 lines of values under a provenance commit is the substantive-change-smuggled-
past-a-reviewer that AGENTS.md forbids *regardless of the direction*. It is now
a justified deliberate refresh for whoever picks up `qou-b3l8`, on its own
commit, citing the 3m44s window.


### 8 of 16 stamped — and one bucket-C blocker was a DETECTOR bug, not a producer bug

`qbeta_cal3_anchor_table_impact` was on the blocked list as "now fails its own
assertions". It does not. **The producer was fine; its c_3 tripwire was
over-flagging.**

That script asserts *"no production table row uses c_3"* from a **live scan** of
`canonical_mass.py` + `derived_masses.py` — deliberately falsifiable, so that
wiring c_3 into production flips it red. It had gone red, with verdict
*"INCONCLUSIVE — a factorization/wiring assertion failed; re-derive before
citing"*, which points a reader straight at a c_3 wiring regression.

**There is no regression.** The scan was a line-regex over source TEXT, and its
only two hits in the entire production surface were `derived_masses.py:550` and
`:552` — both inside the coefficient-tier **docstring**, both saying c_3 is not
wired:

    • c_3 = −2 : EMPIRICAL — near-match, REFUTED as a real-q fibre element
                 (… no fixed real c_3 holds across anchors — SRigidityPrune).

So writing the correct thing down in the production file was enough to fail the
check that the thing has not been done. Same over-flagging class as the 141-hit
prose grep I declined to ship earlier in this tranche — third instance on this
branch of *a detector keying on text rather than on code*.

**Fixed AST-based** (comments never enter the AST; string constants skipped
explicitly), with a **`--selftest`** so the narrowing cannot quietly defang a
tripwire that is supposed to be able to fire:

    [PASS] wired: bare c_3 in code / order-3 truncation call / c[3] subscript
    [PASS] clean: c_3 in a docstring / in a comment / inside a string / c_2 rung

All five assertions pass, exit 0, and **the committed witness needed no
substantive change** — it already recorded them passing. The producer had
regressed away from a correct witness, not the reverse. Then stamped: two q0
keys, zero numbers moved, anchor self-consistent.

**Running total: 8 of 16 live bucket-C producers stamped.** Remaining 8 are
4 `qou-fl9i` numeric movers, 1 `qou-b3l8` (float64→mpmath, identified),
1 content drift (`qbeta_habiro_p8`, `check_q`→`u` rename), 1 that writes
nothing (`binding_additive_linked_cluster_probe`), and the y_λ regenerator I
will not run.

**Adjacent, NOT fixed here.** That same docstring carries `dc_3/dq ≈ 4.6×10⁶`,
which AGENTS.md corrects to **3.84e6**. Measured **~18 live sites**, including
**three `.lean` files** (`SRigidityPrune`, `ImQAnchorCarrier`,
`ThetaLipschitzObstruction`) and this production module — broader than
AGENTS.md's own list (*"audit docs and `local/compute-author` §precedent-table"*),
which names neither Lean nor `computations/`. A sibling already flagged the
discrepancy in `docs/audits/2026-08-25-cheat-sheet-paper-alignment.md`. Left
alone: corpus-wide doc-currency in a different domain.


### 9 of 16. `qbeta_habiro_p8_identification_probe` — NOT stamped, and the reason is a notation collision

Its re-run rewrites **14 recorded polynomial strings**, every one
**coefficient-identical**:

    committed  "check_q**8 + 2*check_q**7 + … - 2*check_q + 1"
    fresh      "u**8 + 2*u**7 + … - 2*u + 1"

So no mathematics moves. I still did **not** stamp it, for two reasons:

1. **The new symbol collides.** In this producer `u` means `q^{1/2}` (line 264,
   `h_q = u0 - 1/u0`; line 391, *"when u = q^{1/2}"*). Corpus-wide, `u` is the
   c_k ladder variable `u = b·ℏ_q² ≈ 0.00852` — AGENTS.md's own Q_β banner.
   Two different `u`, and stamping bakes the ambiguous one into a witness.
   AGENTS.md §7aa is strict about exactly this (*"never conflate"*, *"rename
   one"*). `check_q` (q̌) had no such collision.
2. **The committed strings' provenance is unclear.** `git log -S"check_q"` on
   this producer returns **no commit** — the string never appears in its
   history. So the committed witness's `check_q` came from something other
   than this file as it has ever stood. Overwriting it silently would destroy
   the only surviving trace of that.

Neither is a numeric problem, and neither is mine to settle: renaming the
symbol back (or to something that does not collide) is an authoring decision in
the q-β notation register.

**Bucket C is now 9 witnesses / 8 producers.** What is left, all with a named
owner:

| producer | why not stamped | owner |
|---|---|---|
| 3 × `option_e_*` + `he3_pairknot_composite_lp_probe` | dps 50 -> canonical; witnesses never regenerated | `qou-fl9i` |
| `sublemma_2_1_alpha_shift_extract` | float64 -> mpmath by 3m44s; provenance fixed, regeneration deferred | `qou-b3l8` |
| `qbeta_habiro_p8_identification_probe` | symbol collision above | notation register |
| `regenerate_y_lambda_orphans_conventionD` | rewrites the load-bearing y_λ tables | not run, deliberately |

None of the remaining eight is blocked on `1j39` infrastructure. The
`stamp_q0` mechanism is done for everything it can reach.


## 2026-09-03 — this bean's worked example is DONE; see `cmiy` for the fresh measurement

The four producers named above as the measured never-stamps instance are all
**ported and stamped** now (`scriptHash`, `commitSha`, `engine`, `q0Anchor`
present on each witness). Do not re-do them.

The canonical bean `cmiy` carries the 2026-09-03 re-measurement: **347** witnesses
with missing provenance, of which only **23 (7 %)** are hand-rolled and need the
port — **255 (73 %)** are ordinary staleness that self-heals on the next run. The
"~133 scripts" figure in this bean's header is superseded.

Still a duplicate; still awaiting owner close (resolve is human-only).



## Reasons for Scrapping

Duplicate of `beans/defs/*-watcher-queue.json` (watcher-queue state, not a bean`` (work-plan reorganisation 2026-10-04). Evidence: [M] mirrors a watcher-queue finding class; those queue items are all status wontfix/resolved/needs-author in beans/defs/*-queue.json
Content is untouched; only this work item is closed.
