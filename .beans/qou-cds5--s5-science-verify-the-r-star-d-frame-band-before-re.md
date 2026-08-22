---
# qou-cds5
title: 'S5 (SCIENCE): verify the r* D-frame band BEFORE re-scoring the six Delta_lambda ansaetze'
status: in-progress
type: task
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-21T16:58:20Z
---

Parent: `qou-cdx1`. **This bean exists to stop a re-scoring that has not earned
its target yet.**

## The claim, as relayed — NOT independently confirmed

Relayed into the ruling session: `r* ≈ 1.585` is a **convention-C** number, and
**PR #4766** measured **2.04–2.16 under D**; the **six Δ_λ closure ansätze** were
all tested against the C value.

**I could not locate the #4766 D-frame band in the tree** while writing
[`2026-08-15-owner-ruling-convention-d-proton-color.md`](../docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md).
It is recorded there as relayed, explicitly not as a corpus measurement. **Step 1
of this bean is to confirm or refute it.**

## What IS in-corpus

`r*` as the needed ratio in the A3-magnitude work:

- `docs/audits/2026-07-26-deltalambda-a3-magnitude-source-three-walls.md:32,39,48`
  — `r = κ_W/κ_y`; route closes iff derived `r = μ₃/v_y ≈ 1.585`. Derived
  `r = 52.6` vs needed `1.585` — overshoots by the wrong *order*.
- `docs/audits/2026-07-27-deltalambda-s5so3-geometric-wlambda.md:35,74,86,91`
  — `r_geom = 47.369`; `r_both = r_geom·Σy_λ = 47.37·0.03175 = 1.504`, recorded
  as *"a tantalizing 5.1 % short of r* ≈ 1.585"*.

## Why this matters, if the relay holds

`r_both = 1.504` is **5.1 % short of a C-frame target**. Under D the target
moves, and a "tantalizing near-miss" either becomes a hit, a miss, or a
different miss. The six ansätze were scored against the same moving target.

**Do not re-run the ansätze against a number nobody has re-measured.** That is
how a fit gets laundered into a derivation — score against an unverified target,
find the one ansatz that lands, and call it closure.

## Standing constraints that do not move

- The Δ_λ **value** is PROVED (`Δ_λ = (−1)^{n(λ)}·dim V_λ`,
  `dtEuler_eq_deltaLambda_unconditional`, sorry-free, general-n). What is open is
  the many-body binding **MAGNITUDE**.
- **No seventh fit-based ansatz for the magnitude.**
- PROBE-4 (Kashiwara-crystal / KL-weight) stays **pruned** — KL positivity vs a
  mixed-sign target, Lean-proved (`PartitionOf5.deltaSign_mixed`). That is a
  proved exclusion, not a scope gate.
- The gate is **open for all** (2026-07-13) for *derivation* routes; the
  anti-fit discipline is orthogonal and unchanged.

---

## STEP 1 DONE 2026-08-21 — CONFIRMED, and the gate STAYS UP

The relayed claim is real and traceable. It is **not** an independent measurement
of `r*` under D, and the band as quoted is **under-specified**. So the ansätze
still must not be re-scored against it — for a sharper reason than "unverified".

### Why nobody could find it: PR #4766 is OPEN and UNMERGED

The previous author's *"I could not locate the #4766 D-frame band in this tree"*
was correct, and the reason is now known. **PR #4766 has been open since
2026-08-08** (branch `claude/binding-channel-convention-exposure-2026-08-08`,
head `bb4ca9c0b`, +4557/−1 across 20 files) and **none of its 20 files are on
`main`** — verified file-by-file. The measurement lives only on that branch.

Its body states the claim verbatim:

> **`c₃` moves 22–26%, so `r* ≈ 1.585` is a C-convention number** (→ 2.04–2.16
> under D). Worth pausing on: the Δ_λ gate records six closure ansätze failing
> against `r* ≈ 1.585`.

### The measurement behind it

`computations/probes/mu3-door-sign-c-vs-d.witness.json` on that branch
(`mu3_door_sign_C_vs_D_probe.py`), proton pin, both mirror isotopes:

| isotope | variant | `c₃` C | `c₃` D | `c₃` D/C | `r_star_scale_factor` | `1.585 ×` |
|---|---|---|---|---|---|---|
| T | abs | −1.76877527 | −1.37233143 | 0.775865 | 1.288883 | **2.043** |
| ³He | abs | −1.40542443 | −1.03383626 | 0.735604 | 1.359427 | **2.155** |
| T | raw | −1.63248125 | −1.37233143 | 0.840641 | 1.189568 | 1.886 |
| ³He | raw | −1.32883757 | −1.03383626 | 0.778000 | 1.285346 | 2.037 |

`1.585 × {1.2889 … 1.3594}` = **2.043 … 2.155** → the quoted **2.04–2.16**.
**Arithmetically confirmed.** Both isotopes also reproduce the recorded C-frame
`c₃` first (`reproduces_upstream_c3 = True`, −1.769 / −1.405), so the C baseline
is not in question.

### Three qualifications, all load-bearing

**1. It is an inference from `c₃`, not a measurement of `r*`.** The witness's own
description says it *"reports how far c_3 moves, **hence** how far the A=3
magnitude target r* ~ 1.585 moves"*, and the field is named
`r_star_scale_factor`. Every one of its four assertions is about the **door
sign**; `r*` is explicitly a *by-product* in the PR body ("Two by-products"). So
`2.04–2.16` is `1.585` multiplied by a ratio measured on a different quantity —
defensible as a scoping estimate, **not** a D-frame determination of `r*`.

**2. The band is the `|χ|`-abs variant only.** The raw variant gives
**1.89–2.04**, a materially different interval that *overlaps the abs band only
at its endpoint*. The spread comes entirely from the **C** baseline: under D the
two variants coincide exactly (`D_abs = D_raw = −1.37233143…` for T), which is
the PR's own observation that the `|χ|`-vs-raw choice is *"an exact no-op under
D"*. So a bare "2.04–2.16" hides a modelling choice that moves the target by ~8%.
**Quoting the band without naming the variant is under-specified.**

**3. Two data points, both A=3.** T and ³He are a mirror pair. `r*` is the A=3
magnitude target so the scope is right, but the band is an interval across two
mirror isotopes, not a distribution.

### Consequence — the gate stands, sharpened

The bean's warning was *"do not re-run the ansätze against a number nobody has
re-measured."* Refined: the number **has** been derived, honestly and
reproducibly, but

- it is a **rescaled C value**, not a D-frame derivation of `r*`;
- it is **variant-dependent** (2.04–2.16 abs vs 1.89–2.04 raw); and
- `r_both = 1.504` — the *"tantalizing 5.1 % short"* figure — sits **below both
  bands**, so under D that near-miss gets *worse*, not better, on either variant.
  A re-scoring would therefore not rescue the near-miss; it would deepen it.

That last point is the useful one for the anti-fit posture: the risk this bean
guards against was "score against a moving target until one ansatz lands". The
target moves **away** from the best existing candidate, so no ansatz is rescued
by the D shift. Re-scoring against `2.04–2.16` would be scoring against a
rescaled C number, and would still fail.

**What would actually close Step 2:** a D-frame derivation of `r* = μ₃/v_y`
computed under D directly, rather than `1.585 ×` a `c₃` ratio. Not attempted
here — that is derivation work, and this bean exists to gate it, not to do it.

### Housekeeping: `qou-9ov8` is this bean's duplicate, and it is stranded

PR #4766 carries four beans, none on `main`: **`qou-9ov8`** (*"re-scope r 1585 as
a c convention value reads 2.04…"*) — which is **this bean's subject, filed first**
— plus `qou-rm47` (which integer fibre `N` binding traces), `qou-2xhl`, and
`qou-yotw`. `qou-cds5` was written without visibility of `qou-9ov8` because the
PR never merged. Whoever merges #4766 should reconcile the two rather than let
both run.

Flagging separately: a PR open 13 days holding a measurement two other beans
depend on is itself the finding. The corpus cannot see work parked on a branch,
and `cds5` and `qou-9ov8` are the same item filed twice because of it.
