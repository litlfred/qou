---
# qou-zvi7
title: 'qou-nmuz: four deltalambda consumers re-run on the borromean 5Li/6Li chi caches (#7160 follow-up)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T08:04:05Z
updated_at: 2026-10-04T15:13:39Z
parent: qou-5vkl
---

## Why this bean has this ID

The dispatch named bean `qou-nmuz` and said the file exists on `main`. It does
not (`beans show qou-nmuz` → not found; `grep -rl nmuz .beans/` → only the
parent `qou-vyvt` body). `beans create` mints its own ID, so the work is tracked
here as `qou-zvi7` with the intended ID in the title. Branch
`claude/deltalambda-consumers-borromean-rerun-2026-09-08`.

## The task

PR #7160 (`07d6584d94e`, `80102e6ceca`) regenerated five matrix-m χ caches
(D, T, ³He, ⁵Li, ⁶Li) on the BORROMEAN atom word; they had been on the
pre-2026-09-05 GROUPED word. Four producers read those caches. Re-run each,
diff the witness against `origin/main` with volatile keys masked, report what
moved, restore any sibling writes, do not edit producers or content.

## What each producer actually reads (measured, not assumed)

| producer | D/T/³He source | ⁴He source | ⁵Li/⁶Li source |
|---|---|---|---|
| `delta_lambda_empirical_tabulation.py` | tier-2 `wedderburn_jones_markov` float64 path (NOT a cache) | `chi-helium-4-h12-at-q0-50dps` (hoefsmit) | `chi-lithium-{5,6}-…-matrix-m` ← regenerated |
| `deltalambda/carrier_table_convention_d_rederivation.py` | `binding-reeb-phase-decomposition` θ + recomputed y | same | `…-matrix-m` ← regenerated |
| `deltalambda/li6_h18_amplification_discriminator_probe.py` | `chi-*-at-q0-50dps` (hoefsmit, NOT matrix-m) + reeb θ | same | `…-matrix-m` ← regenerated |
| `deltalambda/carrier_saturation_mechanism_probe.py` | same as li6 | same | `…-matrix-m` ← regenerated |

So of the five regenerated caches, only the two **Li** caches are in any of the
four read cones. The D/T/³He matrix-m regeneration reaches none of them (the
probes' anchors come from the `chi_at_q0_via_hoefsmit_mpfr.py` family,
`convention: colour-weighted-averaged-crossing`; the Li caches are
`seminormal-path-sum-lossless`, `convention: sign-only-crossings`,
`braid_word_intra_order: borromean`).

## Source drift vs cache drift, per producer

| producer | witness scriptHash | live sha256[:12] | source drift? |
|---|---|---|---|
| `delta_lambda_empirical_tabulation.py` | `45bf11e8c917` | `45bf11e8c917` | none — pure import-cone drift |
| `carrier_table_convention_d_rederivation.py` | `ed652d68f893` | `ed652d68f893` | none — pure import-cone drift |
| `li6_h18_amplification_discriminator_probe.py` | `3bbcaab5ef5b` | `c552f6b0e9c5` | YES — `be09ef66f14` (qou-k54t) re-pinned the D/⁴He assertion `expected` values (6.4161462→29.075377, 73.5943→702.409); pins + source strings only, no arithmetic |
| `carrier_saturation_mechanism_probe.py` | `3f0054cda5f4` | `f57d0e3ed39b` | YES — same re-pin commit |

`git diff origin/main -- <producer>` is empty for all four by construction
(branch is at `origin/main`); the two witnesses on `main` for the probes
predate the re-pin commit, which is why the drift shows in `scriptHash`.

## Results (masked diff: timestamp/computedAt/duration/commitSha/scriptCommitSha/invocation/environment)

All four: exit 0, < 3 s wall each, **no sibling witnesses written** (`git status`
after each run showed only the targeted file).

### 1. `delta-lambda-empirical-tabulation.witness.json` — 68 numeric leaves moved, all ⁵Li/⁶Li
- ⁵Li `tr_M` 3.34757 → 1.22403 (−63.4 %); ⁶Li 3.86477 → 1.15558 (−70.1 %)
- ansatz (a) best λ*: ⁵Li [12,3] → [15], |δ| 74.79 → 156.27; ⁶Li [14,4] → [18], |δ| 91.23 → 322.07
- ansatz (c) α: ⁵Li −0.2175 → −0.5194; ⁶Li −0.1643 → −0.4838
- ansatz (d) α: ⁵Li −8.46e10 → −3.95e11; ⁶Li −1.17e14 → −6.75e14
- verdicts: 0 assertions; "weak pattern, 2/8 atoms" unchanged in count
- (Class-A audit-only producer, fitted to CODATA by its own banner — nothing here is a prediction)

### 2. `carrier-table-convention-d-rederivation.witness.json` — 4 of 31 leaves moved
- `A_req_5Li` 64.1028 → 143.3966 (+123.7 %); `A_req_6Li` 82.8548 → 164.3530 (+98.4 %)
- `me_S_MeV_5Li` 0.41076 → 0.18362; `me_S_MeV_6Li` 0.38615 → 0.19467
- verdict unchanged: max|W−1| = 1.8e-71, 1/1 pass

### 3. `li6-h18-amplification-discriminator.witness.json` — 53 numeric leaves moved
- from the Li caches: 𝒜(⁵Li)_{y·dim} 64.10 → 143.40; 𝒜(⁶Li) 82.85 → 164.35; implied step ⁴He→⁵Li 0.871 → 0.204, ⁵Li→⁶Li 1.293 → 1.146; channel flips ⁵Li 6→3, ⁶Li 11→4; composite absolute B_pred 250.9 → 126.5 MeV vs B_AME 31.99
- from the re-pin (already on main's source, not yet in main's witness): anchors D/T/³He/⁴He 6.42/17.97/24.57/73.59 → 29.08/147.48/108.66/702.41; scatter band [395,1804] → [5672,50764]
- verdict UNCHANGED: "BREAKS — 4-point artifact", inside-band False→False, ±40 % gate False→False, 6/6 pass
- pre-existing raw-float64 warning (assertions[3..5].expected, wall-sec) — not touched

### 4. `carrier-saturation-mechanism.witness.json` — 74 numeric leaves moved; STILL RED, failing set rotated
- `A_required` ⁵Li 64.10 → 143.40, ⁶Li 82.85 → 164.35; `me_S_MeV` 0.411 → 0.184, 0.386 → 0.195
- `E_p|Δθ|` ⁵Li 0.804 → 0.359, ⁶Li 0.756 → 0.381; growth-share ⁵Li 0.556 → 0.294, ⁶Li 0.795 → 0.323 (rotation channel now dominant); growth blocks 7→4, 12→5
- carrier band max/min 10.197 → 4.832 (verdict text "BOUNDED, not flat" unchanged)
- 𝒜-step ⁴He→⁵Li 0.0913 → 0.2041; ⁵Li→⁶Li 1.2925 → 1.1461
- assertions: 3 FAIL before, 3 FAIL after —
  - `anchor_kappaD_reproduced` FAIL→PASS, `anchor_kappa4He_reproduced` FAIL→PASS (the qou-k54t re-pin now matches)
  - `li6_amplification_reproduced` PASS→FAIL (expected 82.85481 is the grouped-word value), `anchor_kappa5Li_reproduced` PASS→FAIL (expected 64.10282, grouped-word)
  - `carrier_band_ratio_pinned` FAIL→FAIL (expected 1.5025; computed 10.20 → 4.83)

**qou-k54t's falsifiable prediction is confirmed.** That bean wrote, before the
Li caches were regenerated: *"when the Li atom caches finish regenerating to the
borromean word, both will move and both assertions will FAIL. If they do not
move, my account of the mechanism is wrong."* Both moved, both fail.

## Durable artifacts quoting a moved number

Grepped `content/ docs/ .beans/` for every old figure above (excluding
`*.witness.json`). **No content block and no audit doc quotes any of them.**
Only two beans do, and both already describe the numbers as stale/straddled:
- `.beans/qou-k54t--…md:29-30, 379-381, 384, 402, 408, 484-485` (64.10282, 82.85481, 0.4108, 0.3861, 10.1966)
- `.beans/qou-8jfh--…md:210-211, 220-221` (64.102824, 82.854814)
Two grep hits in `recursive-atom-knot-atlas-registry.md` (87216.6121, 250.9095) and one qa.json timestamp are digit coincidences, not quotes.

## Still open — owner call, not taken here

1. **Re-pin the two Li assertions in `carrier_saturation_mechanism_probe.py`**
   (`li6_amplification_reproduced` 82.85481 → 164.35298,
   `anchor_kappa5Li_reproduced` 64.10282 → 143.39659). Same act as qou-k54t's
   D/⁴He re-pin, which explicitly deferred "the Li three". Cost: two literals +
   a provenance note, witness re-run (0.3 s). Default if nothing is done: the
   witness stays red on main with its own explanation in the assertion `source`.
2. **`carrier_band_ratio_pinned` expected 1.5025** is still red at 4.83. qou-k54t
   argued the old 10.20 was a mixed-word ratio and refused to pin it; 4.83 is
   now single-word (all six on borromean) but still straddles two χ
   *conventions* (hoefsmit colour-weighted anchors vs sign-only Li). Whether
   4.83 is a physics number or a convention artifact is unmeasured; do not pin it
   on this evidence.
3. **Anchors and Li read different χ conventions** (`colour-weighted-averaged-crossing`
   vs `sign-only-crossings`) in probes 3 and 4. Pre-existing, not introduced by
   #7160, but the 2.4–4.8× light-vs-Li carrier gap in the band may be that
   straddle rather than a saturation signal. Not measured here.
4. `delta_lambda_empirical_tabulation.py` tier 2 is float64 (`q0_float = float(Q_MP)`),
   engine label "python" by its own admission. Pre-existing; in scope for the
   precision exemption but out of scope for this bean.



## PR

https://github.com/litlfred/qou/pull/7172 (non-draft, opened 2026-09-08). Commits f63d8a0d50b / 78abdeef74b / 11cf449f38f / 1c75a957356 (one per producer) + 54dc0affd2a (this bean). Precision gates: every RED is on files this PR does not touch (list in the PR body); audit witnesses reverted per the gate.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.
