# ⁶Li: the production binding does not merely miss its target — it moves the wrong way

**Date:** 2026-09-05 · **Beans:** `qou-sv7h` (sign), `qou-brng` (extensive term)
· **Branch:** `claude/rag-document-ingestion-options-orasrw`

## The measurement

```
python3 -u /tmp/li6_run.py     # binding_energy(3, 3), kernel asserted live
6Li  A=6  B_pred=-3.065019520558719  AME=31.994  elapsed=4039.8s
```

The script asserts `hecke_core_legacy._HAS_LP_KERNEL` before running and
refuses otherwise, so this is **not** a fallback-matrix number. That guard
matters: measured earlier in this session on ²H, the same call returns
`-7.271102124876717` with the kernel live and `-8.52811254141235` through the
`_build_ysn_matrices` fallback — **17.29 % apart**, and the fallback matrices
violate the braid relation, so they are not a representation of `H_n(q)` at all.

## What it establishes, using only figures measured here

Two production points, both kernel-live, both by the same call:

| A | atom | `binding_energy` | AME2020 | B/A predicted | B/A AME |
|---|---|---|---|---|---|
| 2 | ²H | **−7.2711** | +2.2245662 | −3.636 | +1.112 |
| 6 | ⁶Li | **−3.0650** | +31.9939872 | −0.511 | +5.332 |

> AME figures read from the **vendored** AME2020 table via
> `codata_constants.ame_binding_mev(Z, A)`, not typed. The short literals
> `2.225` / `31.994` used in the first version of this doc are the hand-typed
> kind that `ame_2020_binding_energies.py` was written to retire — six of its
> nine predecessors disagreed with the publication table by up to 63 eV, against
> an AME uncertainty on B(⁴He) of 0.8 eV. The correction is far below anything
> claimed here, and is made because the habit is the defect.

- **The sign is negative at A = 6 as well.** Consistent with the Pass-2 gate
  mechanism, which forces `B < 0` for any nucleus.
- **The magnitude moves in the OPPOSITE direction to AME.** Predicted `|B|`
  *falls* 7.2711 → 3.0650 (×0.42) across the same span over which AME binding
  *rises* 2.2245662 → 31.9939872 (×14.4). Per nucleon the divergence is sharper:
  predicted `|B|/A` falls ×7.1 while AME's rises ×4.8.

So the defect is not only a sign error on a roughly right magnitude. Over the
two points that can be verified here, the prediction is **anti-correlated** with
the observable it is meant to reproduce.

## 🛑 What it does NOT establish, and a claim of mine it scopes

PR #6752 states, of the A-independence: *"The sibling measured −7.271 / −7.742 /
−7.456 / −6.829 while AME spans 12.7×."*

**Only the first of those four is verifiable.** `−7.271102124876717` was
measured in this session with the kernel live. The other three
(`−7.742`, `−7.456`, `−6.829`, for A = 3, 4, 5) appear **nowhere in the tree** —
a fixed-string grep across `--include=*.md --include=*.json --include=*.py`
returns no hit for any of them. They reached the PR from conversation context
attributed to a sibling session, and **their kernel-vs-fallback provenance is
unknown**. Given the 17.29 % kernel/fallback split above, that is not a detail:
an unverified figure from that series could be either.

Therefore:

- The **A-independence** claim — a near-constant plateau across A = 2..5 —
  **rests on three figures with no recorded provenance** and is scoped to that
  status. It is not retracted; it is unverified.
- The **anti-correlation** claim above uses only the two figures measured here
  and stands independently of it.
- If the plateau is real, ⁶Li **breaks it**: −3.065 is 2.4× smaller in magnitude
  than the smallest of the four. Whether that is a genuine A = 6 feature or an
  artefact of comparing against unverified numbers cannot be decided without
  re-measuring A = 3, 4, 5 with the kernel live (~2 h: cost grows ≈ A², A = 4
  alone took 2425 s).

## A second tension, recorded rather than resolved

The k_max = 6 / 28-partition direct-from-kernel reconstruction in
`uic-sign-forced-by-gate.witness.json` does **not** show the A = 6 drop. Its
`gated_sum` runs ²H −1.3657, ³H −0.9704, ³He −0.8079, ⁴He −0.8021,
⁶Li −1.0770 — ⁶Li is the *second largest* in magnitude there, whereas in
production it is the smallest.

The reconstruction omits the q-Gaussian tier and was never expected to
reproduce production's absolute values (²H: −1.366 against −7.271); it was
offered as evidence about *which partitions carry the sign*, which is invariant
to that truncation. But the two disagree about a **trend**, not merely a scale,
and that is outside what the truncation argument covers. Recorded as open.

Note also that the gated-set size at A = 6 is **15**, the largest recorded, so
the production magnitude falls where the gate admits the *most* partitions. Any
account of the A-dependence has to explain that.

> **🛑 And `[15, 9, 9, 10, 15]` is NOT "across A = 2..6", which is how PR #6752
> described it.** It is **per atom** — ²H, ³H, ³He, ⁴He, ⁶Li — so its A values
> are **2, 3, 3, 4, 6**: it double-counts A = 3 and contains **no A = 5 entry at
> all**. The corpus's own gated-set data therefore has a hole exactly at the A
> the plateau claim needed, which is a second reason that claim could not have
> been checked against it.

## Precision: these figures are float64, and the source says so

`binding_energy` ends `return float(B)`, and its own comment records why that
cast is not the narrowing that matters:

> `math.log(abs(tr_run))` already narrows to float64 INSIDE the accumulator
> (`math.log` returns a Python float whatever it is handed), so this path is
> float64-limited well upstream of here. That narrowing is a real,
> PRE-EXISTING precision defect and is tracked separately.

So every `B_pred` quoted here carries ~16 significant digits **of arithmetic**,
not of meaning, and the probe stores them as `mpf(str(B))` — faithful to the
float64 value, manufacturing no precision it does not have.

This does not weaken anything claimed above. The claims are ratios — ×0.42
against ×14.4, ×7.1 against ×4.8 — which are orders of magnitude clear of
float64 resolution. It does mean **no digit beyond the first few should be
read as a result**, and in particular that agreement or disagreement at the
1e-16 level between any two of these numbers would be the floor of the
arithmetic rather than evidence about the model.

## Reproduction

The run is 67 minutes and emits no witness — it was a direct call, not a
producer. To make it durable, a producer wrapping `binding_energy` across
A = 2..6 with the kernel guard would be the right artefact; it is not written
here because the honest first step is re-measuring A = 3, 4, 5, and that is a
~2 h compute that should be claimed as its own item rather than folded into
this tranche.
