---
# qou-fl9i
title: Raise 838 sub-canonical mp.dps sites to set_compute_dps() — producers serialize 10 digits past what they compute
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T08:04:50Z
updated_at: 2026-08-23T10:10:08Z
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
