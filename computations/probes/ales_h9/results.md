# qou-ales: reading-3 feasibility up the tower, H_3 → H_6 → H_9 (results)

Issue #7701, bean `qou-ales`. Pre-registration:
[`preregistration.md`](preregistration.md) (committed before any H_9 number).
Probe: [`ales_h9_reading3_tower_probe.py`](ales_h9_reading3_tower_probe.py).
Witness: [`ales-h9-reading3-tower.witness.json`](ales-h9-reading3-tower.witness.json).
Proton pin, convention D, mpmath at 60 dps, no measured target read, nothing selected.
Wall time 97 s (gmpy2 backend).

## Claim

**Going up the tower never rejects a candidate H_3 admitted, and it admits every
candidate H_3 rejected.** Across the whole pre-registered set, every element is
reading-3-feasible at H_6 and at H_9, in both bond columns (free product, and γγ
bond `G³` on every interface). The H_3 test is strictly the most discriminating
level in this family; the multi-nucleon tests discriminate nothing in it.

| family | level | bond | H_3 yes → H_n yes | REJECTED by tower | ADMITTED by tower | H_3 no → H_n no |
|---|---|---|---:|---:|---:|---:|
| F1 homogeneous (19 words) | H_6 | none / G³ | 9 / 9 | 0 / 0 | 10 / 10 | 0 / 0 |
| F1 homogeneous (19 words) | H_9 | none / G³ | 9 / 9 | 0 / 0 | 10 / 10 | 0 / 0 |
| F2 pp, pn, nn (81 each) | H_6 | none / G³ | 16 / 16 each | 0 | 65 / 65 each | 0 |
| F2 ³He = p\|p\|n, ³H = p\|n\|n (729 each) | H_9 | none / G³ | 64 / 64 each | 0 | 665 / 665 each | 0 |

The ten H_3-rejected F1 words — 4 of the proton k = 0 family, 4 of the neutron, and
both **live production elements** (`χ_(2,1) = −0.2806 / −0.3720` at H_3) — are all
admitted at H_6 and H_9. Smallest block character anywhere in F2: `0.3933` (nn, free).
Per-candidate `χ_λ` on every block at every level and both columns is in the
witness (`F1_homogeneous`, `F2_rows`).

## Evidence

Cross-checks, all passed before any H_6/H_9 verdict was read:

- `y_λ` exact over ℚ(q) at n = 3, 6, 9: `Σ y_λ f^λ = 1`, `y_λ = 0` exactly on every
  ≥3-row shape, `y_λ > 0` on every two-row shape. H_9 blocks (9),(8,1),(7,2),(6,3),(5,4),
  dims 1/8/27/48/42.
- H_3: trivial-block character equals the product of eigenvalues to 4e-60; the k = 0
  counts reproduce the merged `qbeta-cost-minimal-budget-under-reading3` witness
  (4/8 p, 4/8 n); the live words reproduce the merged `χ_(2,1)` (to the witness's 20
  stored digits).
- H_6: `tr_M(LIVE_p|LIVE_p·G³)/tr_M(LIVE_p|LIVE_p)` reproduces the merged
  `diproton-response-closed-form-probe` `ratio_atom_over_free` to **4.7e-60**.
- Detector-live calibration (post-hoc, not a candidate): `(σ_0⁻¹)³` per slot,
  `x = 1 − q⁶ = −0.8702`, is rejected at H_3, H_6 and H_9 — so the test can fail.

## Mechanism (hypothesis H1′, verified numerically, not proved in Lean)

Under convention D the weight support is the two-row blocks, i.e. the SU(2)
(Jones / Temperley–Lieb) quotient: `(3)` is spin 3/2, `(2,1)` spin 1/2, `(n−k,k)` spin
`(n−2k)/2`. For a free product the block character follows SU(2) Clebsch–Gordan:

`χ_(n−k,k)(w_1|…|w_m) = Σ_{μ_i ∈ {(3),(2,1)}} mult(spin (n−2k)/2 ⊂ ⊗_i spin μ_i) · ∏_i χ_{μ_i}(w_i)`.

Checked against the direct seminormal value on **8433** free-product block characters,
max deviation 5e-25 (the F2 values are stored at 25 digits). This also confirms the
pre-registered prediction **H1** (no REJECTED-by-tower in the free column): a two-row
block only branches to two-row factors with non-negative multiplicity.

For the homogeneous embedding, with `x = χ_(2,1)(w)/χ_(3)(w)` (and `χ_(3)(w) > 0` always,
since each letter acts on the trivial block by `q`, `q − h/2` or `1/q`), feasibility is a
one-variable test:

| level | binding block | condition | threshold |
|---|---|---|---|
| H_3 | (2,1) | `x ≥ 0` | 0 |
| H_6 | (5,1) | `2x + 1 ≥ 0` (other blocks `(x+1)²`, `x²+1`) | −1/2 |
| H_9 | (5,4) | `2x³ + 3x² + 6x + 2 ≥ 0` | −0.389488731310071 |

All candidates sit in `x ∈ [−0.3315, 1.994]`, above both multi-nucleon thresholds,
which is the whole reason nothing is rejected. LIVE_n (`x = −0.3315`) is the closest:
its (5,4) character at H_9 is `0.3915` against a block dimension of 42.

**The thresholds are not monotone in the level.** Continuing the same CG polynomials
(post-hoc, homogeneous only, depends on H1′): m = 1…8 nucleons give
0, −0.500, −0.389, −0.634, −0.552, −0.707, −0.643, −0.754. Odd m binds on the spin-½
block, even m on the spin-2 block, and odd-m thresholds are tighter. So an H_6-feasible
word with `x ∈ [−1/2, −0.3895)` would be REJECTED at H_9 — none exists in this family,
but the tower is not a one-way filter in general.

The γγ bond changes block characters by up to 17 % relative (F1 max) and flips no
verdict; its effect on the trivial block is exactly nil (`G³` acts as 1 there).

## Implications

- **For the live production element.** Its exclusion (bean `qou-99qc`) rests on reading 3
  applied at **H_3**. Applied at the A = 2 or A = 3 element the same reading admits it.
  Which algebra the "whole element" ruling (2026-09-13) refers to therefore decides
  whether the live element is excluded — this was not explicit before.
- **For the γγ selection programme.** Under reading 3 the multi-nucleon levels select
  nothing inside these families; any discrimination comes from H_3. Tracking the tower is
  still informative — it shows the per-level thresholds and that odd/even A differ — but
  at the present candidate set the H_9 test adds no constraint.

## Scope (AGENTS.md "Before declaring refuted")

- **(a) scope-limited:** "reading 3 at H_6/H_9 rejects nothing" holds for the
  pre-registered families (core, k = 0 nucleon words, the live words; homogeneous and
  physical compositions; no bond or G³ on every interface). It is not a statement about
  other words, other bonds, one-interface bonding, or other nucleon orderings.
- **Structural, conditional on H1′:** H_3-feasible free products are feasible at every
  level (non-negative CG multiplicities, two-row branching only). Not Lean-proved here.
- Not claimed: which level the owner's ruling intends; any re-scoring; any physical
  binding number.

## Owner decision this raises (not taken here)

**Which algebra does "reading 3 on the whole element" mean — the nucleon in H_3, or the
nucleus in H_{3A}?**

1. **H_3 (status quo).** Means: per-nucleon test, as in every merged probe. Costs nothing.
   Risks: none new. Commits to: the live element stays excluded (`qou-99qc` unchanged).
2. **H_{3A}, the nucleus.** Means: test the bonded A-nucleon element. Costs: re-run the
   `qou-99qc` exclusion argument at H_6/H_9 (this probe already has the machinery).
   Risks: under the present families it admits everything, so reading 3 stops selecting;
   the live element is re-admitted. Commits to: the selection must come from elsewhere
   (cost, SDP objective).
3. **Every level of the tower.** Means: feasible at H_3 and at every H_{3k}, k ≤ A. Costs:
   as option 2. In this family it coincides with option 1 (H_3 is the binding level), but
   the non-monotone thresholds mean it can be stricter than either in general.

Default if nothing is said: option 1 — nothing changes. My judgement (not a finding):
option 3 is the reading most faithful to "track the towers at every step", and on the
current data it costs nothing relative to option 1.

## Answered: owner ruling 2026-10-11, option 3 (every level)

The owner ruled that reading 3 applies **at every level of the tower** (recorded on
`qou-ales` and `qou-99qc`, commit `0212ad3a68c`). On this probe's families that
coincides with option 1, because H_3 is the binding level. So the live production
element stays excluded (`qou-99qc` unchanged), and nothing here is re-scored.

## Folded in from PR #7733: climbing the strand count by single collisions

#7733 (`computations/probes/gg_ntower/`) tests the **other** way to climb the tower.
Instead of composing whole nucleons (this probe: free products of confined triples),
it places successive γγ collisions V = σ_iσ_{i+1}⁻¹ on new strands with a rigid
shift s and closes the extra strands with the convention-D Markov conditional
expectation, testing reading 3 at every level up to H_9.

- **Result:** no climbing placement passes, for either vertex. Only same-strand
  collisions pass (s = 0, k = 3, 6). s = +1 telescopes to σ₀σ_k⁻¹ (Lean,
  `GammaGammaStaircaseTelescopes.lean`).
- **Mechanism, already at q = 1** (`gg_ntower/explanation.md`): closing a strand is a
  partial trace and shortens permutation cycles but never splits them. Same-strand
  collisions compose 3-cycles on one triple, and three of them cancel. Climbing
  collisions chain into one long cycle, which survives to level 3 as a 3-cycle, with
  χ_(2,1) < 0.

**What the two probes say together (my reading, scope (a)).** Within the families
tested, the strand-count tower passes reading 3 at every level only when it is built
out of **already-confined triples**, which is this probe's construction, where every
H_3-feasible free product stays feasible at H_6 and H_9. It does **not** pass when
single collisions walk up the strands. So in these families, confinement is a
per-triple, same-strand property, and the multi-nucleon levels add no selection
beyond H_3. Other closures of the climbing placements (bottom, Jones-projection pair
closure) are pre-registered on #7733 (`closures_preregistration.md`) and reported
there.
