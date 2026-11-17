---
# qou-bsec
title: jones_wenzl_weight is wrong and LIVE at mass_at_3A_proper.py:592
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T18:17:08Z
updated_at: 2026-11-15T13:50:00Z
parent: qou-v2om
---

## Evidence

`computations/mass_at_3A_proper.py::jones_wenzl_weight` (line 89) implements

    omega_lam = z^{n-1} * prod_{x in lam} (1 - z q^{2c(x)}) / (1 - q^{2h(x)})

with a docstring claiming `Sum_lam omega_lam = 1`.

**It is live**, not dead code: `ocneanu_weights_3A` (line 123) wraps it and is called at
**line 592** (`weight_table = ocneanu_weights_3A((Z + N))`). It is also mirrored into
`qou-mass/src/qou_mass/_internal/mass_at_3A_proper.py` by the vendor sync.

**It is wrong.** Measured in exact sympy over Q(q,z)
(`computations/schurweyl/ocneanu_weight_validation.py`): across 160 convention
combinations -- exponent convention, four q-substitutions, ten z-substitutions, both
plausible targets -- it never reproduces the Lean-proved n=3 weights
`QOU.SchurWeyl.HeckeMarkov3.markovWeight0/1/2`, and never sums to 1.

Three separate defects:

1. **Wrong formula.** The correct closed form is derived in
   `computations/schurweyl/ocneanu_weight_general_n.py` and Lean-proved against the n=3
   case in `QOU/SchurWeyl/OcneanuWeightMarkov3.lean` (PR #5575):

       W_lam(q,z) = prod_{(i,j) in lam} [ q^{2i}(q^2-1-qz) + q^{2j+1} z ]
                    / prod_{(i,j) in lam} [ q^{2h(i,j)} - 1 ]

2. **Wrong normalisation in the docstring.** The Markov trace normalisation is
   `Sum_lam d_lam * W_lam = 1`, not `Sum_lam W_lam = 1` -- `d_lam` is the character of
   the identity in block lam. `computations/ocneanu_weights.py` states it correctly
   (its `omega_lam` is `d_lam * W_lam`); this file does not.

3. **float64.** `q: float = Q0`, `z: float = Z_MARKOV`, `product` accumulated in float.
   AGENTS.md NO-FLOAT64 applies to every `computations/` script.

## Why it survived

Nothing in the repo checked any weight above n = 3, and n <= 3 is where a wrong formula
is hardest to catch: every partition of n <= 3 has DISTINCT cell contents, so a formula
can be off by a whole monomial and still look plausible. The first content repeat is the
two content-0 cells of (2,2), at n = 4.

## Next step

Replace the body with the derived closed form, carried in `mpmath.mpf`; fix the
docstring's normalisation; re-run whatever consumes line 592 and diff the result. Note
that `computations/ocneanu_weights.py::omega_lambda_via_inversion` already computes the
correct weights by a p(n) x p(n) linear solve -- the closed form can replace that solve
outright (cross-checked at n = 2..5 in
`computations/schurweyl/ocneanu_weight_convention_d_support.py`), so the two paths should
converge on one implementation rather than three.


## CORRECTION to this bean's own title and severity claim (2026-08-23)

I wrote *"wrong and **LIVE** at mass_at_3A_proper.py:592"*, in this bean's title, in a
commit message and in PR #5575's body. **The mechanism was wrong.** Line 592 is not a call
site — it is the body of an `elif weight_scheme == "jones_wenzl":` branch. Both entry points
(`per_generator_V_hat_3A` line 543, `binding_3A_tower` line 739) default to
`weight_scheme="normalized_plancherel"`, and **every caller in the repo passes
`normalized_plancherel` or `plancherel` explicitly** — `pyhecke/atom.py:556`,
`binding_via_interface_knot.py:213,216`, `delta_lambda_v_hat_z_transfer_phase5d_4.py:109,111`.
Not one selects `jones_wenzl`. So it was a wrong formula on an unselected path, not a wrong
number in live output. The title overstates it and I am leaving it in place with this
correction rather than rewriting history.

## The actual consequence is worse, and it is in a sibling bean

`qou-2tuv` **did** exercise it, and built its headline recommendation on it:

> `jones_wenzl` — the Ocneanu weights built on z = q^3/(q^2+1), i.e. **convention D** — is
> the only scheme that leaves the tower's own precondition intact.
> **So the default weight scheme is inconsistent with the owner's trace-convention ruling.**

resting on a measured table where `jones_wenzl` gives `max|V_hat| = 0.06979` against ~1.08 for
every other scheme, and the best deuteron result on record (+37.7% vs production's +97.9%).

Measured in exact rational arithmetic at the live q0 and convention-D z, the old formula's
**total weight is not 1 and is sometimes negative**:

| n | old `jones_wenzl`  sum d_lam w_lam | derived Ocneanu |
|---|---|---|
| 3 | **-1.2053** | 1 |
| 6 (the deuteron, 3A with A=2) | **0.3772** | 1 |
| 9 | **-0.0549** | 1 |

A negative total weight means the functional was not a positive trace at all. `V_hat` is linear
in the weights, so `max|V_hat| = 0.0698` is **not comparable** to the other schemes' ~1.08 — it
is an unnormalised functional being compared against normalised ones. The "only scheme that
leaves the precondition intact" reads as a normalisation artifact.

**What I have NOT shown:** that the corrected weights give `max|V_hat| > 1`, or that the +37.7%
deuteron result disappears. Those need re-measuring, and they are `qou-2tuv`'s to re-run. What is
established is that the numbers the conclusion rests on came from a formula that is not the
Ocneanu weight and does not define a normalised trace.

## Fixed

`computations/mass_at_3A_proper.py::jones_wenzl_weight` now carries the derived, Lean-checked
formula in `mpmath.mpf` end to end, returning `mpf`. Verified `sum_lam d_lam w_lam = 1` exactly at
n = 2..6 and 9. The vendor mirror was regenerated with `scripts/sync-qou-mass-vendor.py --apply`
(never hand-edited). Safe to land precisely *because* nothing selects the branch.

Also fixed in the same file: the comment above `Z_MARKOV` claimed *"Matches
mass_endomorphism.z_mark = 1/(q^1/2 + q^-1/2)"* — convention **C** — while the line below it
computes `Q0**3/(Q0**2+1)`, convention **D**. Second instance of the `qou-pc7l` class in as many
files.

## 2026-11-15 — mpf defaults

`jones_wenzl_weight` and `ocneanu_weights_3A` defaulted to the float64 `Q0_PROTON` / `Z_MARKOV`, so every default call evaluated the weights at a double's worth of q. The defaults are now the mpf proton pin `Q_MP`, with z derived in mpf from that same q. Measured at 70 dps: the weights move by ~5e-17 relative (for example (3) → −5.3e-17, (2,1) → +4.3e-17).

Correction to a claim made earlier the same day: I said the normalisation Σ_λ d_λ w_λ = 1 held only to ~1e-16 because of the float64 default. That was wrong. The 1e-16 came from measuring at mpmath's default 15 digits. At 70 dps the identity holds to ~1e-70 with the old defaults and with the new ones, because it is a rational identity in (q, z) and holds for any z. So the "Fixed" section above stands as written.

## Progress Update (Round 64 — PR #8263)
- **Status**: `in-progress` (per active rule: no unilateral `qou` bean closures).
- **PR**: [`litlfred/qou#8263`](https://github.com/litlfred/qou/pull/8263) (branch `feat/round64-hooksum-formality-charge-ocneanu-coupling-43c1`, Commit 1 `30d0d4f4e437e19904cd4438468a9ecf56eadd3a`, Commit 2 / Head `545135545dc8e721846ea1fb0e54556f69a5a166`).
- **Lean 4 Artifact**: `folio/quantum-observable-universe/lean/QOU/SchurWeyl/OcneanuWeightMarkov3.lean (`markovWeights_three_sum_and_classical_values`)` (0 sorry, 0 findings across all 6 static vacuity audits).
- **80-dps Witness**: `computations/probes/hooksum_formality_charge_ocneanu_coupling_probe.py` (`scriptHash: dae747aae6b4`) + `test/results/witnesses/hooksum-formality-charge-ocneanu-coupling.witness.json` (`allPassed: true`).
