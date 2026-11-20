---
# qou-21oc
title: 'Drop the UIC Pass-2 sign gate: enacted; the ungated total is ALSO wrong-signed'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T22:56:10Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-trd0
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
  `folio/quantum-observable-universe/mass-theory/unified-iterative-correction.md`
  to state the gate as part of the proposition ("the total ... is the sum ...
  over those λ whose final seminormal trace satisfies tr <= 0") plus a "Scope of
  the selection rule" section. After the drop that text is wrong. **`main`'s
  current text is already correct post-drop** ("sums these strictly over all λ"),
  so nothing was edited here; whichever PR lands second must reconcile.


---

## `binding_energy(1, 1)` RE-RUN — the derived cell is now MEASURED (2026-09-13)

**TIER: `k_exact = k_max = K_PARTITION_MAX = 11`, the production default**, for
every figure in this section. Kernel live (`_HAS_LP_KERNEL = True`,
`pyhecke_native 0.9.0`), `COMPUTE_DPS = 70`. Producer
`computations/binding_energy_ungated_deuteron_measurement.py`, 2361.9 s total;
log `/tmp/binding_energy_ungated_deuteron_measurement.log`.

The post-drop deuteron value in `docs/audits/2026-09-02-binding-energy-first-corrected-value.md`
was written **by arithmetic** on that document's own three-term decomposition
and marked "derived, NOT measured". That terms 2 and 3 are gate-independent had
been established by **reading** `binding_energy`, never by running it. This is
the first run of the public function since the drop.

| | measured | wall |
|---|---|---|
| term 1 `unified_iterative_correction` (mpf) | `-17.6908290020795447079223359605544029429608374879103157233577` | 413.6 s |
| term 2 `sdp_cross_channel_contribution` | `0.0` (float) | 0.0 s |
| term 3 `binding_from_frobenius_pairing` (mpf) | `+1.876634106144136334334544823923110976193880197699474143353897399142905884` | 768.3 s |
| sum of terms (mpf) | `-15.8141948959354083735877911366312919667669572902108415800038` | — |
| **`binding_energy(1, 1)`** (public float, 53-bit) | **`-15.81419489593541`** | 1180.0 s |

**VERDICT: the reading was right. Terms 2 and 3 are gate-independent — now
measured, not inferred.** Term 1 reproduces this bean's own
`-17.6908290020795` exactly (reldiff 2.53e-15). Term 2 is a genuine `0.0`.
Term 3 is unchanged and is measured **directly for the first time** — the
audit's `+1.876634106` had been obtained by *subtracting* term 1 from the 942 s
gated total, never evaluated on its own.

**The measured cell differs from the derived one by `+1.44091626e-10 MeV`
(relative `9.11e-12`), and that offset is entirely the banner's own quoting
precision, not a discrepancy:**

- term 3 quoted at 10 s.f. (`1.876634106` vs `1.8766341061441363343`): `+1.44136334e-10`
- term 1 quoted at 15 s.f. (`-17.6908290020795` vs `-17.690829002079544708`): `-4.47079e-14`
- sum of the two: `+1.44091626e-10` — unexplained remainder `-9.3e-61`, the
  60-dps arithmetic floor.

Two consistency checks that fall out of the same run: the public float sits
`-1.57e-15` from the mpf sum (relative `9.94e-17` < `2^-53 = 1.11e-16`), i.e.
exactly the cast at the public return and nothing more; and the measured terms
reproduce the ORIGINAL gated total,
`-9.14773623102088124311 + 1.87663410614413633433 = -7.27110212487674490878`,
against the `-7.271102125` the 2026-09-02 audit printed.

**Accuracy, and it is worse — which is the honest outcome.** Against AME2020
`+2.22456607 MeV`, `binding_energy(1,1)` goes `|ratio|` **3.26855x -> 7.10889x**
and residual **9.4956682 -> 18.038761 MeV**. Do NOT conflate those with the
`11.37 -> 19.92 MeV` in the table above, which is the residual of **term 1
alone** against AME — a different quantity.

**Not re-run, and left derived:** ⁴He `binding_energy(2, 2)`. Its term 1 is
measured (`-15.9926510049258`, 1165.1 s) but the full function is a ~2x longer
compute than the deuteron's 1180 s and was not attempted.


### Correction to the section above, same day — an AME literal I typed

The ratios above were first computed against `2.22456607`, a value I **typed**.
The registry says `2.2245662` (`ame_2020_binding_energies.ame_binding_mev(1, 2)`,
returns `mpf`). Disagreement `-1.3e-7`, relative `5.84e-8`.

**What it changed: one digit.** `|ratio|` 3.26855x / 7.10889x are unmoved at
6 s.f.; the gated residual goes `9.4956682 -> 9.4956683` MeV and the ungated
`18.038761` is unmoved. So no conclusion turns on it — **which is precisely why
a typed constant survives review**, and why the reference-literal ratchet exists.

Fixed AT THE PRODUCER: the script now calls `ame_binding_mev(1, 2)` instead of
carrying a literal. Caught by checking my own published figure against its
source rather than by any gate — the literal was new in this commit, so it would
have become baseline backlog on the next ratchet run.



*(Count correction, same day: the red-gate figure in the section above reads
"12 blocking reds"; counted off `precision-gates.sh`'s own RED line it is
**11**. The substantive claim — all pre-existing, none naming a file touched
here — is unaffected and was re-verified on a second full run.)*

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8396, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
