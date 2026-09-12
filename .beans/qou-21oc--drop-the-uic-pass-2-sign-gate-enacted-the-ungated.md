---
# qou-21oc
title: 'Drop the UIC Pass-2 sign gate: enacted; the ungated total is ALSO wrong-signed'
status: todo
type: task
created_at: 2026-09-12T22:56:10Z
updated_at: 2026-09-12T22:56:10Z
---


## What was done

Owner ruled 2026-09-12, of four options for the Pass-2 sign gate in
`hecke_core_legacy.unified_iterative_correction`, to take two: **drop the gate**
and **hunt the primal LP**. The hunt is PR #7251 and does not reverse the drop.
This is the drop — PR #7253, on `claude/stalled-agents-em-linking-jilmbv`.

Removed:

```python
if s.get('final_tr_sign', 1) <= 0:
    gated_total += s['cumul_partition']
```

The function now returns `float(cumul_total)`, the sum over every enumerated
partition.

## 🛑 It makes the numbers WORSE, and that is the finding

**Q1 = the producer's return, `unified_iterative_correction(Z, N, k_exact=.)`.
It is STRONGLY `k_exact`-dependent -- 43x across the tiers -- so never quote a
bare figure.** Q2 is the gated companion of the same run, now reported as
`per_step[-1]['gated_total_DISPROVED_SELECTION_MeV']`.

| tier | atom | Q2 gated (before) | Q1 ungated (after) | factor | admitted | wall |
|---|---|---|---|---|---|---|
| `k_exact = 4` | ²H | `-0.0895596830589507` | `-0.412212192245027` | 4.603x | 4/10 | 10 s |
| `k_exact = 4` | ⁴He | `-0.0805867484776914` | `-0.2742397716174` | 3.403x | 2/10 | - |
| `k_exact = 5` | ²H | `-0.7335499391634978` | `-1.2268740026260945` | 1.672x | - | - |
| `k_exact = 6` | ²H | `-1.3656848170878801` | `-2.251131977321312` | 1.648x | 15/28 | 10 s |
| `k_exact = 6` | ⁴He | `-0.8387490758934286` | `-1.448199112790757` | 1.727x | 10/28 | - |
| **default** `k = 11` | ²H | `-9.14773623102088` | `-17.6908290020795` | 1.934x | 94/193 | **425.5 s** |
| **default** `k = 11` | ⁴He | `-8.20155846836239` | `-15.9926510049258` | 1.950x | 90/193 | **1165.1 s** |

**A bare "the ungated total is -0.4122 MeV" is the `k_exact = 4` figure**, not
the production number, which is `-17.69`. Every prior statement of the gate's
size (the old code comment, #7251's table, #7237's content-block rewrite) quotes
`k_exact = 4` without saying so -- corrected at all of them here.

**Q3 -- a THIRD quantity, reconciled here for the first time.**
`uic_sign_forced_by_gate_probe` sums over partitions with `k <= 6` from the
partition table, no per-step accumulation, ordering `["p"]*Z + ["n"]*N` where the
producer uses the alternating ground state. At ²H (orderings coincide) its
`-2.251132` matches Q1 at `k_exact = 6` to **8 s.f.**; at ⁴He they differ by
**5.39 %** (`-1.3701187` vs `-1.448199112790757`) for exactly that reason. Its
five per-atom sums are NOT producer returns and must not be quoted as such.

AME2020 ²H binding is **+2.2246 MeV**. Both columns are wrong-signed; the new
one is further away (11.37 -> 19.92 MeV at the production default). The drop
buys **honesty, not accuracy** — per AGENTS.md §"NO FITTING", a documented
honest miss is a result, and a more accurate selected route is worth less than
a less accurate derived one.

**Do not reinstate the gate and do not hunt a replacement selection that
restores the old numbers.** That is selection against the target.

## Two numbers that were not on the record before

1. **The production-default factor is 1.93, not 3.4-4.6.** Every prior statement
   of the gate's size (the code comment, #7251's table, #7237's content-block
   rewrite) quotes `k_exact = 4`. At the production default (193 partitions,
   425.5 s wall for one atom) the gate admitted **94 of 193** blocks and **52 %**
   of the magnitude, against 4 of 10 and 22 % at `k_exact = 4`. Its grip LOOSENS
   as the partition set grows.
2. **`k_exact` is not a small knob**: ²H ungated runs `-0.412 -> -1.227 -> -17.69`
   across `k_exact = 4 / 5 / 11`. Quote the tier with any UIC number.

## Why (refuted sorry-free, not merely doubted)

`QOU.MassTheory.UICGateNotFromComplementarySlackness` (#7251) — four
mismatches: index set (NF basis `d = n!` vs partitions `p(n)`), argument (CS
constrains `(Gx*)_i`, the gate reads an input `t_λ`), direction (`0 <= (Gx)_i`
makes `<= 0` and `= 0` the same predicate on any feasible point), no unique
optimum (positive-dimensional minimiser face). Partition-indexed repair excluded
**scope (b)**, invariant = primal feasibility + orthogonality of the Wedderburn
projectors (diagonal block Gram, CS decouples, atom traces never appear).

## Retraction this forced

`uic_sign_forced_by_gate_probe` claimed the wrong sign is **forced by** the gate.
Dropping the gate is the experiment that claim could not survive. Every atom's
**ungated** sum is negative too, and larger: ²H `-1.3657 -> -2.2511`,
³H `-0.9704 -> -1.8036`, ³He `-0.8079 -> -1.7466`, ⁴He `-0.8021 -> -1.3701`,
⁶Li `-1.0770 -> -1.9697`. Steps 1 and 3 survive (C_λ >= 0 on 682 partitions;
`|Tr| >= d` in 3.4 % of `Tr <= 0` vs 34.1 % of `Tr > 0`) and establish a **bias**;
step 2's inference from bias to forcing is withdrawn. scope-(a).

## Kept, not deleted

- `final_tr_sign` still computed and reported per step (real diagnostic data).
- The gated sum still computed, **renamed** `gated_total_MeV` ->
  `gated_total_DISPROVED_SELECTION_MeV`. Two consumers on `main` measured and
  updated: `where_the_a_dependence_is_lost_probe.py:182`,
  `uic_per_block_log_valley_scan_probe.py:134`.

## Still open (NOT closed by this)

- **The sign is still wrong and unexplained.** The gate was a candidate
  explanation and is now excluded — a narrowing, not an answer.
- `qou-brng` and `qou-zlra` stay open (rule 13a; no conjecture closed here).
- `qou-ai7v` and `qou-px38` — two further carriers of the same disproved
  argument in the same file, recorded and deliberately not changed.
- **Merge-order dependency:** #7237 rewrites
  `content/quantum-observable-universe/mass-theory/unified-iterative-correction.md`
  to state the gate as part of the proposition ("the total ... is the sum ...
  over those λ whose final seminormal trace satisfies tr <= 0") plus a "Scope of
  the selection rule" section. After the drop that text is wrong. **`main`'s
  current text is already correct post-drop** ("sums these strictly over all λ"),
  so nothing was edited here; whichever PR lands second must reconcile.
