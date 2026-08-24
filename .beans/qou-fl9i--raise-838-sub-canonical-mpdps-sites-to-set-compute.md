---
# qou-fl9i
title: Raise 838 sub-canonical mp.dps sites to set_compute_dps() — producers serialize 10 digits past what they compute
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T08:04:50Z
updated_at: 2026-08-23T12:26:41Z
---

## The defect, with evidence

`qou_substrate.precision` sets the convention: **COMPUTE at `OUTPUT_DPS + GUARD`,
SERIALIZE at `OUTPUT_DPS`** — `OUTPUT_DPS=60`, `GUARD=10`, `COMPUTE_DPS=70`.
Bumped 2026-05-31 (PR #1595) from 50→60 output / 65→70 compute. Most call sites
never followed.

**838 sites across 828 files** set `mp.dps` below canonical: 564 at 50 (the old
output value), 205 at 40, 90 at 30, plus a tail. **732 of those files write
witnesses**, so they compute at 50 and serialize at 60 — emitting ten digits
nobody computed.

Confirmed on real witnesses:

    option-e-v8-hecke-involution-isospin-mirror.witness.json
      0.047894838938013599999999999999999999999999999999999   <- 51 decimals, float64 padded
    canonical-mass-table-extended.witness.json
      0.0242545979013089793867766275070607662200927734374981106160886   <- 61 decimals

The trailing run of 9s and the `...0927734374...` tail are binary64 values
expanded past the precision they were computed at.

## Not the never-raises-dps defect

`never_raises_dps_audit.py` is blocking and green — 10 runnable producers left of
a 46-file baseline, 0 new, 0 regressed. Those never raise dps at all. **These
sites DO raise it**, to a value that stopped being canonical. No ratchet covers
"raises dps, but below canonical", which is why 838 sites sit behind green gates.

## The fix

Replace `mp.dps = N` / `mp.mp.dps = N` (N < 60) with `set_compute_dps()`, adding
`from _precision import set_compute_dps` where missing. That is the canonical
pattern, already used by 869 files. Import insertion is AST-located — a regex
lands inside multi-line `from x import (...)` blocks.

33 sites sit next to a deliberate-looking marker (float64 / deliberate /
low-precision) and are **left alone** for a human read.

## Scope boundary — witnesses are NOT regenerated here

Changing a producer's precision changes every value it emits, so all 732 witness
producers become self-stale on scriptHash. Regenerating them means RUNNING each
one; several are hours long and the seminormal cache filled this container's disk
twice at n=12 alone. That is a separate, large piece of work and is deliberately
out of scope for this bean.


---

## Swarm verification — five agents, 828 files, and three bugs in my own transform

The mechanical sweep was verified by five subagents, one per directory shard,
each **running** every changed file rather than trusting the transform. That was
the right call: `ast.parse` passed on every file, and it caught none of what
follows.

### Bugs the swarm found in my tooling

| bug | effect | count |
|---|---|---|
| import inserted after the file's LAST import, but `set_compute_dps()` called earlier | `NameError` at module scope | **99** |
| rewrote a fallback wrapper's body into a self-call, `def set_compute_dps(): set_compute_dps()` | `RecursionError` | 2 |
| `_path_bridge` presence tested by substring — matched a COMMENT | `ModuleNotFoundError` | 1 |
| `_path_bridge` present but only as a FUNCTION-LOCAL import inside `main()` | `ModuleNotFoundError` | 4 |
| rewrote `except ImportError:` fallbacks to call the name the failed import never bound | dead branch, passing only by accident | 13 |
| pre-existing function-local `_precision` import made the name local | `UnboundLocalError` (not `NameError` — grep triage misses it) | 1 |

All fixed. Final AST validation over 823 changed files: 0 parse failures,
0 call-before-import, 0 self-call wrappers, 0 `__future__`-not-first.

### Reverted — files where the dps VALUE is the subject matter

- **`mpf_context_dps_audit.py`** — a BLOCKING gate script. The line I rewrote was
  example code inside its own docstring, illustrating the very defect it detects
  (`mp.dps` vs `mp.mp.dps`, a silent no-op). I broke the illustration in the gate
  that catches it.
- **`proton_error_anatomy_1ppb.py`** — a deliberate PSLQ window: drop to 20 dps
  "for convergence", restore to 50. Both ends became the same call, so the search
  ran at 70 rather than the 20 its comment justifies.
- **`qbeta_5two_legacy_provenance_narrowing_probe.py`** — `_lp()` deliberately
  tests dps 6..10 as hypothesis H5. Converting changes what the probe tests. I
  first "fixed" this file and made it worse, then reverted it wholesale.
- **`phi_b_evaluator.py` + `phi_b_substrate_regime.py` + `qbeta_c3_two_route_cross_pin_probe.py`**
  — a documented precision INTERLOCK my sweep voided from both ends. The source
  says the evaluator pins `mp.mp.dps = 35` at import time and the regime was
  validated at 40, with an explicit gotcha note. Decisive detail:
  `phi_b_evaluator.py:87` computes its quadrature truncation bound *from*
  `mp.mp.dps` — changing dps changes the integration itself.
- **`y_lambda_su_n.py`** — save/restore self-test, same shape, milder.

### Fixed properly rather than skipped

`deuteron_naive_z_physical_probe.py` and `alpha/alpha_em_shift_chain.py` each had
a module-scope raise their own comment demands happen BEFORE the constants are
built. My marker heuristic skipped them (their comments contain "default 15"),
leaving constants at 50 while `main()` ran at 70 — a partial fix worse than none.
Both now call `set_compute_dps()` at module scope.

### Cost, stated plainly

**Self-staleness grows from 744 to 1167** (+423). That is the direct, expected
consequence: 822 producers changed, so their witnesses no longer match their
producer's scriptHash. Witness regeneration remains out of scope for the reason
in the bean body — it means RUNNING each producer, and this container's disk
filled twice at n=12 alone.

Against that, the raw-float64 ratchet shows the change **drained 4,287 raw
float64 fields across 56 witnesses**.

### Gates

    precision-gates.sh    EXIT 0 — "All blocking precision gates green"
    never-raises-dps      10 producers left of a 46-file baseline; 0 NEW, 0 REGRESSED
    raw-float64 ratchet   green after removing 4 UNTRACKED witness files the
                          verification runs created (`git checkout --` cannot
                          revert untracked files — that was the hole in my sweep)
    staleness-gates.sh    EXIT 1, on the same three pre-existing reds as main
                          (vendor mirror: main's own 2 witnesses; scriptHash
                          drift: the 744 above)

### Process error of mine

All five agents were given the same scratch directory and clobbered each other's
working files; two caught it via dry-run guards and redid their work in private
subdirectories. Nothing bad landed, but that was their care, not my design. Fan
out shards with per-agent scratch paths.


---

## Witnesses regenerated — staleness drained BELOW its pre-sweep baseline

The bean body scoped witness regeneration out. Doing it anyway, under a disk
guard, turned out to be feasible: 664 changed producers, batched 40 at a time,
~8.4s each.

    664 producers: 530 ok, 54 timeout, 40 error
    563 witnesses regenerated and committed

    self-staleness   744  (before the dps sweep)
                  -> 1167 (after the sweep — 822 producers changed scriptHash)
                  ->  686 (after regeneration)

So the sweep's +423 is paid back and the corpus ends **58 witnesses cleaner than
before this branch started**.

### The regeneration proved the padding was FABRICATED, not truncated

    before: 0.0073087015600556568914203806394122356062676461516769
    after : 0.00730870156005565689142038063941223560626764615167775333384...
                                                              ^ diverges at ~digit 51

The values do not merely extend — they **disagree from about digit 51**. A
producer computing at dps=50 and serializing at 60 was not padding with harmless
zeros; it emitted digits that were wrong. Anything downstream reading past digit
50 of those witnesses was reading noise. This is the direct proof the earlier
trailing-9s evidence only suggested.

### My 45-second timeout corrupted 5 witnesses, and the shape guard caught it

Producers that write incrementally were killed mid-write:

    chi-numpy-dtype-fix-benchmark    durationMs 408,402 -> 32,812
    habiro-coefficients-helium-3     data_keys 1 -> 0
    habiro-coefficients-helium-4     data_keys 1 -> 0
    qbeta-ck-local-taylor-around-u0  63 -> 33 leaves (48% gone)
    rho-k-full-via-wenzl-lr          306 -> 58 leaves (81% gone)

All five reverted to HEAD. `witness_shape_guard.py` exists for exactly this and
its warning is worth repeating: *"The raw-float64 ratchet will NOT catch this: a
gutted witness scores zero raw floats, which reads as a perfect drain."* Had that
guard not been blocking, my run would have reported a larger drain than it earned.
Any future regeneration pass needs a per-producer timeout well above the slowest
producer, or none at all.

### Also removed

Four UNTRACKED witnesses from producers that had never run to completion before
the import fixes. Three carry raw float64 and would have entered the corpus as new
dirty witnesses. Their producers need a `_precision.fmt` fix before their output
is committed — not in scope here.

One witness, `audits/hardcoded-literal-audit.witness.json`, was reverted rather
than committed: its new content is a **self-referential false positive** — the
literal audit harvests the float64-padding audit's own test fixture, and the
padding audit then flags the report. Filed as **qou-tknj**; that witness is
knowingly stale until it is fixed at the producer.

### Gates

    precision-gates.sh   EXIT 0 — all blocking gates green
    witness shape guard  563 modified, 0 collapsed
    raw-float64          0 NEW, 0 REGRESSED


---

## Re-ran the Li_2^q consumers after the truncation fix

The 563 witnesses regenerated earlier used the **truncated** `li_2_q` — correct
to ~21 digits, not 70. Re-ran the producers that consume it, with a 300s cap
(vs the 45s that gutted five witnesses last time). 20 ok, 1 timeout, 2 error;
shape guard **0 collapsed**, so no repeat of the mid-write damage.

Only **2 of 23** produced real value changes. The rest differed by timestamp
alone and were reverted rather than committed as churn.

### 1. The truncation fix, visible

`pentagon-reduction-li2q.witness.json`:

    before 0.99691749365058832615339880074753972921545435821921249075196766
    after  0.99691749365058832615345387364575161283101167046312650339379126
                                 ^ diverges at digit ~22

Exactly the ~21-digit error the `max_k=2000` cap predicted, now corrected.

### 2. A stale payload that a metadata-only refresh had masked — 8% error

`canonical-ordering-dof.witness.json`, assertion `closed_form_matches_full_trace`,
flipped **False -> True**. That is NOT the precision fix — its tolerance is 1e-6,
far too loose for a 21-vs-70-digit difference to matter. The real magnitudes:

    ratio                 rel BEFORE      rel AFTER
    T_npn_over_pnn         0.0803424    4.92315e-17
    He3_pnp_over_ppn       0.0467039    4.92315e-17
    T_npn_over_pnn         0.0803863    4.92315e-17
    He3_pnp_over_ppn       0.0466652    4.92315e-17

The closed form was disagreeing with the full trace by **5-8%** and now matches to
machine precision. Cause, from the history: the producer's last substantive fix
was `7d7ad545c` ("Part 6 measures its own readings instead of quoting eight
decimals"), but the witness's last touch was `e049d2830` — *"metadata only,
payload identical"*. The payload was never regenerated after that source fix, so
it kept carrying the pre-fix numbers while its metadata looked current.

That is the strongest argument yet for draining stale witnesses: a **metadata-only
refresh actively hid an 8% error**, and nothing flagged it, because scriptHash and
provenance both looked fresh.

### Still not committed

`per-knot-density-borromean-q-locality-probe.witness.json` regenerated again
(its producer is a Li_2^q consumer) and again carries 23 raw float64 fields, so it
would enter the corpus as a NEW dirty witness. Removed a second time. Its producer
needs to carry mpf and serialize with `_precision.fmt` before its output belongs
in the tree — same for the two `casimir-*` producers noted earlier.

### Not re-run

The Li_2^q consumer set was built with a loose regex; a strict `\bli_2_q\b` scan
finds ~19 further witness producers not in the re-run set, including
`derive_m_p_hecke_full_tower_50dps.py` and `m_p_m_e_li2q.py` — proton-mass paths.
Their witnesses were computed with the truncated series too. Not run here.
