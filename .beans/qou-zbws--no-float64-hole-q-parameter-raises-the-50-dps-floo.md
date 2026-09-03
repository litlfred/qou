---
# qou-zbws
title: 'NO-FLOAT64 hole: q_parameter raises the 50-dps floor ONLY on the muon anchor — every proton/default-anchor producer computes at mpmath''s 15'
status: todo
type: bug
created_at: 2026-09-02T21:53:12Z
updated_at: 2026-09-03T00:00:00Z
---

Found while fixing `qou-uiut` (the YSN braid defect). **Owner-facing**: the
fix is one line, but it changes the working precision of every producer on the
default anchor, so it is a numbers-move, not a refactor.

## Measured

    $ QOU_Q0_ANCHOR=<unset>  python3 -c "import hecke_core_legacy; ..."
        mp.dps after import : 15
        1/q                 : 0.900918283955741472368572431151   <- float64 tail
    $ QOU_Q0_ANCHOR=proton
        mp.dps after import : 15
        1/q                 : 0.900918283955741472368572431151
    $ QOU_Q0_ANCHOR=muon
        mp.dps after import : 50
        1/q                 : 0.900918273492422300050994867878   <- real 50 digits

`QOU_Q0_ANCHOR` is UNSET in this container, so 15 is the live default.

## Why

`computations/substrate/q_parameter.py:205`

    _mp.mp.dps = max(_mp.mp.dps, 50)

sits at 8-space indent — inside `if _anchor in ("ideal", "muon", "canonical"):`
(line 113). Its own comment states the directive as a GLOBAL one:

    > Owner directive 2026-07-06: "global dps 50 for compute accuracy". The
    > muon-anchored compute runs at a standing global precision of 50 dps —
    > this is the intended compute floor, NOT a temporary bump, so it is set
    > globally

but it is only set on that branch. On any other anchor the precision comes
from `qou_substrate/constants.py:316`:

    with _mp.workdps(_DPS_DEFAULT):
        Q_MP = q_at(_DPS_DEFAULT)
        ...

`workdps` RESTORES the ambient precision on exit — deliberately, and its
comment says so ("this module does NOT mutate the caller's mp.mp.dps"). So the
cached `_MP` VALUES are 50-digit mpf objects, but the ambient precision drops
back to mpmath's default 15 and every subsequent operation on them rounds to
~17 digits.

The two mechanisms are individually correct and jointly leave the floor unset.

## Why it matters

`hecke_core_legacy` was excised to mpf end to end under NO-FLOAT64 (bean
`qou-9ay6`) — `math` removed from the module entirely, `scipy.sparse` replaced
with a `_CooMPF` class written specifically because scipy refuses dtype object.
On the default anchor all of that arithmetic runs at 15 dps. The types say mpf;
the digits are float64. Nothing in the code shows it, and `repr()` displays at
the ambient dps, so a spot-check LOOKS right.

This is the same failure mode NO-FLOAT64 exists to prevent, one level up: not a
float64 value in an mpf pipeline, but an mpf pipeline evaluated at float64
precision.

Concretely measured on the `_M22_*` (2,2) constants (now fixed in `qou-uiut`
by deriving them lazily): frozen at import-time dps 15, they disagreed with
`_build_ysn_matrices` called later at 50 dps by **1.98e-17** — float64 epsilon,
inside the module the directive was applied to.

## The fix, and why it is not mine to land

Hoist the floor out of the anchor branch so it applies on every anchor. One
line. But:

- it raises the working precision of EVERY producer that imports
  `q_parameter` without setting its own dps, on the default anchor;
- so every witness those producers emit changes in its trailing digits;
- and the corpus's witness-equality ratchets will all go red at once.

That is the correct direction under NO-FLOAT64 and it is a corpus-wide
renumbering. Needs an owner call on sequencing, not a quiet commit.

## Scope to measure before landing

- [x] Enumerate producers that import `q_parameter` and never set `mp.dps`
      (those are the ones whose numbers move).  **229 of 1526** — see
      2026-09-03 below.
- [x] Producers that DO call `set_compute_dps()` are already at 50 and unaffected
      — count them, they are the safe majority or they are not.  **1276 of
      1526 = 83.6 %. They are the safe majority.**  (Correction to the wording
      of this item: `set_compute_dps()` with no argument sets **70**, not 50 —
      `COMPUTE_DPS = OUTPUT_DPS 60 + GUARD 10`, `qou_substrate/precision.py:82-84`,
      bumped from 50 by PR #1595. 324 of the 533 pre-import setters use the
      no-arg form, so the largest protected group sits at 70. Nothing about the
      conclusion changes — 70 ≥ 50 either way — but "already at 50" understates
      where the corpus actually computes and is the same conflation the third
      placement option below turns on.)
- [x] Decide whether the floor belongs in `q_parameter` or in
      `qou_substrate.constants` next to `_DPS_DEFAULT`.  **Recommendation:
      `constants.py`, as a monotone `max()`. Reasons + the one measurement
      that decides it below. Still an owner call — nothing landed.**

---

## 2026-09-03 — measured blast radius + placement recommendation

Analysis only. **No fix landed**, by design: the hoist renumbers proton-anchor
witnesses corpus-wide and that is an owner sequencing call.

Resolver: [`computations/audits/q_parameter_dps_floor_scope.py`](../computations/audits/q_parameter_dps_floor_scope.py)
(AST import graph + transitive cone; `--self-test` covers 18 cases; excludes
`qou-mass/` and `_deprecated/`). Its docstring lists what it can miss.

### The three symptom measurements reproduce exactly

    QOU_Q0_ANCHOR unset   -> mp.dps == 15 after `import q_parameter`
    QOU_Q0_ANCHOR=proton  -> mp.dps == 15
    QOU_Q0_ANCHOR=muon    -> mp.dps == 50

and the effect is isolated from the anchor change — **same** (default/proton)
anchor, two ambient precisions:

    1/Q_MP @ ambient 15 : 0.9009182839557414723685724311508238315582
    1/Q_MP @ ambient 50 : 0.9009182839557414921608228824810939360147
                     |d| = 1.97923e-17

The dps-15 result satisfies `a == mpf(float(a))` — it carries 53 bits and
nothing more. `Q_MP` itself does **not**: it is a genuine 50-digit mpf, so the
pin is intact and only consumer arithmetic is degraded. 1.97923e-17 is the
same float64 epsilon the `_M22_*` measurement in this bean reported (1.98e-17).

### Blast radius (AST, whole repo, 4049 files scanned, 4049 parsed, 0 unparseable)

Cone = transitive import closure. `q_parameter` is a **strict subset** of the
`qou_substrate.constants` cone (the shim star-imports it), which is why the two
placements are nested rather than alternative:

| | imports `q_parameter` | `constants` but NOT `q_parameter` |
|---|---|---|
| files in cone | 1891 | 1519 |
| runnable witness producers | 1526 | 1282 |
| **A** raise dps themselves — UNAFFECTED | **1276 (83.6 %)** | 831 |
| **B** muon-manifest, already at 50 | 7 | 1 |
| **C** no raise, own mpmath values — **MOVE** | **52** | 10 |
| **D** no raise, mpmath only via a helper — probably move | **177** | 25 |
| **E** no raise, no mpmath anywhere — unaffected | 14 | 415 |

So: **1276 of 1526 producers (83.6 %) are already protected — the safe
majority is real.** The moving population is **229** (C + D) for the shim
placement, **264** for the `constants.py` placement.

Committed witnesses attributable to a moving producer (attribution widened past
`gen_q0_anchor_manifest._producer_stem` with a unique-stem pass and a
literal-filename pass; 813 of 3104 still unattributed, so these are **lower
bounds**):

    floor inside q_parameter.py       164 witnesses
    floor in qou_substrate/constants  183 witnesses   (+19)

Manifest cross-tab of the 229: 70 `physical_proton`, 1 `ambiguous`, 158 not in
`q0_anchor_manifest.json` at all (no committed witness carries a readable q₀
signature). None are `ideal_muon` — by construction, those already run at 50.

### The corroborating measurement nobody has to take on trust

`WitnessBuilder` stamps `precisionMetadata.compute_dps` from the module
constant `qou_substrate.precision.COMPUTE_DPS` (= 70), **never** from the live
`mp.mp.dps` — `tools/qou-substrate/python/qou_substrate/witness.py:1958-1966`.
So of the 183 committed witnesses whose producer never raises dps,

    116 DECLARE compute_dps >= 50 while the run was at mpmath's default 15
    112 carry at least one numeric string of >= 18 decimals
      1 has a long string that is exactly float64-representable

— i.e. the float64-**padding** ratchet would flag **1 of 183**. That is the
bean's "nothing in the code shows it" claim, measured: the witnesses assert a
precision the run never established, and the existing detector cannot see it.

Worked example, chosen because its name states the anchor:
`computations/markov/markov_trace_atomic_proton_full.py:141` does
`from q_parameter import Q_MP` and never raises dps; its witness declares
`compute_dps: 70` and reports `tr_M_proton_at_q0: 1.6331533774490543`.
`computations/mass_endomorphism.py:40-41` imports `Q_MP`/`Q_INV_MP` the same
way and cross-checks itself against `atomic-tr-m-mpfr-50dps.witness.json`.

### Recommendation — `qou_substrate/constants.py`, as `max(mp.dps, 50)`

My judgement, not a finding. Two reasons, one of which is decisive:

1. **The shim placement fixes the past and not the future.** `q_parameter.py`'s
   own docstring calls itself "a back-compat shim … New code should import from
   `qou_substrate` directly". Putting the floor there leaves 1520 files —
   1282 producers, 35 of which never raise dps — outside it, and that hole
   grows every time a producer follows the shim's own advice.

2. **The documented objection to a global assignment in `constants.py` does
   not apply to a `max()`.** `constants.py:311-315` explains the `workdps`
   wrapper: *"Many downstream scripts set `mp.mp.dps` BEFORE importing
   q_parameter; the previous global assignment silently OVERRODE their
   precision setting."* That is an argument against **lowering**, and a
   monotone floor cannot lower. Measured over both cones, **533 files** set
   precision at module scope before their first substrate import — the exact
   population that comment protects — and they break down:

       324  set_compute_dps()  with no argument  -> COMPUTE_DPS = 70
       185  literal >= 50
        23  set from a non-literal expression    -> undetermined
         1  literal < 50

   So **509 of 533 demonstrably sit at 50 or above** and a `max()` floor
   preserves every one of them; 23 are undetermined; and exactly **one** sets
   below — `computations/probes/em_selfenergy_coupling_target_probe.py` at
   40 dps, which the floor would raise to 50. The concern that comment records
   costs one file under `max()`, not 533.

**Cost of B over A:** +35 producers, +19 committed witnesses. Against a base of
229 producers / 164 witnesses that move either way, the incremental cost of
doing it in the right place is ~15 %.

**Third option, named because it exists and I am not recommending it:** put the
floor in `qou_substrate/precision.py` as `max(mp.dps, COMPUTE_DPS)`. Same cone
as `constants.py` (both are pulled by `qou_substrate/__init__.py`; measured
identical at 3411 files), same producer set moves, but they land at **70**
instead of 50 — which would make the `precisionMetadata.compute_dps: 70` stamp
true and collapse the corpus's two standing-precision numbers (the owner's
2026-07-06 "global dps 50" vs `COMPUTE_DPS_DEFAULT = 70` from PR #1595) into
one. I am not recommending it because it silently re-decides the owner
directive's number as a side effect of fixing a scope bug; if the two numbers
should be unified that deserves its own ruling.

**Default if nothing is decided:** nothing changes. Every proton-anchor
producer keeps computing at 15, the 116 witnesses keep declaring 70, and the
padding ratchet keeps not seeing it. That is safe in the sense that nothing
breaks, and wrong in the sense the bean already argues.

### Side findings

- **`computations/never-raises-dps-baseline.json` is stale by 35 files.** It
  records 46 files / 206 constructions; re-running that audit's own `scan()`
  today gives **11 files / 63 constructions**. 39 of the 46 have since been
  fixed (verified with the audit's own `raises_precision` predicate, not mine).
  A `--rebaseline` is owed. 9 of the 11 still-flagged files are in bucket C.
- **572 producers raise dps only inside a function/class body**, never at module
  scope. That is fine when `main()` raises before computing, but 14 of them
  build `mpf` values at module scope first, so their import-time constants are
  at 15 today. The hoist would fix those, in the right direction.
- **`grep -rl` gets the direct-importer count wrong in both directions.**
  `grep -rlE '^\s*(from|import)\s+q_parameter(\.|\s|$)'` → 1382; AST → 1403.
  Three grep hits are `from q_parameter import Q` inside **docstrings**
  (`_path_bridge.py`, `q_mpmath.py`, `qou_mass_canonical_wiring_example.py`);
  24 real importers spell it `from substrate.q_parameter import …` (e.g.
  `computations/deltalambda/branching_tower.py:49`) and the anchored pattern
  cannot match them. Net −21.
- Basename collision is **not** a problem at this scope: 10 colliding stems
  over 33 files in the scanned universe, and only 2 module names ever resolve
  to more than one file.
