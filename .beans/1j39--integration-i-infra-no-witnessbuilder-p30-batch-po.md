---
# 1j39
title: 'Integration: I-infra-no-witnessbuilder-P30 batch port'
status: todo
type: task
priority: normal
created_at: 2026-06-21T21:41:08Z
updated_at: 2026-08-28T20:47:45Z
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
