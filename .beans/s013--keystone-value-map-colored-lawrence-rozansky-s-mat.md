---
# s013
title: 'Keystone value-map: colored Lawrence-Rozansky S-matrix for Σ(2,3,5) → bwS0=d_q/D'
status: todo
type: task
created_at: 2026-06-30T23:50:37Z
updated_at: 2026-06-30T23:50:37Z
---


## Context (2026-06-30, merged PR #3190)

The s5-so3 keystone reduced to one field `bwS0 λ = d_q(λ)/D`
(`KeystoneVerlindeSMatrixBridge.lean`, `BWVacuumRowIsHecke`): does the geometric
WRT(S³/2I)=WRT(Σ(2,3,5)) data realize that unit vector? PR #3190 advanced the
geometric (colored-insertion) side; THIS bean is the remaining **value step**.

### What is established (PR #3190, `keystone_colored_sigma235_wrt.py`)
- Coloring the order-5 icosahedral fibre of Σ(2,3,5) by SU(2) colour α shifts the
  Lawrence–Zagier false-theta support `30(1±1/2±1/3±α/5)`. α=1 → bare {1,11,19,29}
  (validates the formula); α=2 → {7,13,17,23}; together = all 8 E₈ exponents.
- Bare support {1,11,19,29} = **H₄ exponents** (4D 600-cell, degrees {2,12,20,30},
  h=30); colour split = the **H₄ ⊂ E₈ folding**.
- E₈ exponents pair under Coxeter `e↔30−e` into 4 dual pairs ↔ the 4 conjugation
  classes of bwS0 at n=5, **4↔4 monotone** in magnitude. The Coxeter ℤ₂ mirrors the
  transpose/chirality ℤ₂ `λ↔λ′` of `S_{0λ}=S_{0λ′}` — supplying the `W_λ=W_{λ′}`
  symmetry the bosonic-colour foreclosure (#2608) showed `m_d` violates.
- **Value-map prune:** the naive exponent q-dimension `[e]_q` is REFUTED
  (`d_q/[e]_q` = 1.00, 0.54, 0.39, 0.36, non-constant).

### The task (the value step)
Derive the **genuine colored Lawrence–Rozansky / Hikami S-matrix amplitude** for the
colored Σ(2,3,5) invariant — the per-colour, per-block residue weights (NOT the total
`Ψ^{(α)}`, one number per colour; NOT the exponent label's `[e]_q`) — and check whether
it reproduces `bwS0(λ) = d_q(λ)/D` for n=5 (the lepton block), then general n.

### Discipline
- Validate each step against the bare invariant (α=1 must reproduce `Ψ(1/q₀)=2.3296`).
- No fit; no forced `Ψ=W_λ` numerology. The colored-amplitude FORMULA is where
  fabrication risk is real — build it rigorously against the literature structure
  (Lawrence–Rozansky 1999; Hikami arXiv:1811.05376, 2205.01282), not by guessing.
- Owner-gated keystone scope (narrow Subgoal-2 reversal, 2026-06-19).
- Feeds PR #2503 (keystone DG Step-1). Coordinate there.

### Cross-refs
- Audit: `docs/audits/2026-06-30-keystone-colored-sigma235-e8-family.md`
- Probe: `computations/probes/keystone_colored_sigma235_wrt.py`
- Bare probe: `docs/audits/scripts/keystone_habiro_wrt_s3_2i_probe.py`
- Modular-cat id: `docs/audits/2026-06-22-keystone-modular-category-identification.md`
- Ledger: `docs/coordination/s5-so3-keystone.md`

## First-pass result (2026-07-01, PR pending): compact candidates pruned

`keystone_valuemap_screen_s013.py` screened the natural closed-form value maps
against the 4 target d_q at q₀ (each class assigned its E₈ dual-pair exponent):
- **C1 [e]_q, C2 sin(πe/30), C3 sinh(ηe) — ALL REFUTED.** d_q=(1,4.11,5.22,6.22)
  vs [e]_q=(1,7.63,13.55,17.34); the E₈ exponents are NOT the value-map labels.
- **Sharp positive:** 3 of 4 d_q are single balanced q-integers with HECKE labels
  {1,4,5} (d_q(5)=[1], d_q(4,1)=[4], d_q(3,2)=[5]); only the self-conjugate ≥3-row
  d_q(3,1,1)=[4][3]/[2] is a product. **Difficulty is concentrated at the
  self-conjugate block** (where the SU(2) gate failed).
- **Narrowed target:** since compact maps fail and the arena is non-compact E_q(2)
  (2026-06-22 id), the value map is the **Hahn–Exton q-Bessel vacuum row**. Next:
  use the corpus q-Bessel infra (reeb-phase-qbessel) to compute the q-Bessel
  amplitude reproducing [1],[4],[5] on near-standard blocks + [4][3]/[2] on (3,1,1).

## Sharpened step-(a) target recorded (2026-07-01)

`docs/scope/2026-07-01-s013-qbessel-radial-part-target.md` records the falsifiable
q-Bessel radial-part target for the DG session: the 2nd-kind measure at the four λ⊢5
points must return {[1], [4], [5], [4][3]/[2]} (up to 1/D + the Z(5) normalisation).
The **discriminating test** is the self-conjugate (3,1,1) = [4][3]/[2] — the sole
non-single-q-integer block, and the ≥3-row block where the compact SU(2) gate failed.
Missing ingredient (⇒ owner-gated DG, not numerics): the partition-λ → q-Bessel-lattice
map, which is the open construction (inventing it = fabrication). Handoff to #2503.
