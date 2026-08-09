# The hypercharge battery imposes one condition, not two

**Date:** 2026-08-09
**Branch:** `claude/hypercharge-second-invariant-2026-08-02` (PR #4597)
**Status:** proved (Lean, sorry-free) + exact-rational probe; scope-(a)

## Context

The eightfold-way chapter landed on `main` while PR #4597 was stalled.
[`eightfold-open-problems.md`](../../content/quantum-observable-universe/eightfold-way/eightfold-open-problems.md)
item 2 records hypercharge `Y` as **open**:

> The writhe map is falsified as a `Y` assignment (proton and neutron share
> `Y = +1` while their writhes differ). *Open:* identify a second crossing
> invariant independent of the writhe.

[`flavor-charge-assignments.md`](../../content/quantum-observable-universe/eightfold-way/flavor-charge-assignments.md)
states two batteries any candidate must pass:

* **B1** — Gell-Mann–Nishijima `Q = I₃ + Y/2` on the nucleon doublet, no
  tuned coupling.
* **B2** — first-generation spectrum: `Y` of `(u, d, e⁻, νₑ)` equal to
  `{+1/3, +1/3, −1, −1}` left-handed and `{+4/3, −2/3, −2, 0}` right-handed.

This audit asks what B1 and B2 actually constrain, before any candidate is
searched for — the forward prune of AGENTS.md §"Formalize-first probe
discipline".

## Results

All exact rational arithmetic, no floats, no fitted parameter
([`hypercharge_battery_reduction_probe.py`](../../computations/hypercharge_battery_reduction_probe.py)),
each also proved sorry-free over a generic `Field K` with `CharZero`
([`HyperchargeBatteryReduction.lean`](../../content/quantum-observable-universe/lean/QOU/StandardModel/HyperchargeBatteryReduction.lean)).

### R1 — the right-handed half of B2 is an identity, not a test

Right-handed fermions are weak singlets, `I₃ = 0`, so GMN reads `Q = Y/2`
and forces `Y = 2Q` termwise:

| fermion | `Q` | `Y = 2Q` | B2-RH target |
|---|---|---|---|
| `u` | `2/3` | `4/3` | `+4/3` ✓ |
| `d` | `−1/3` | `−2/3` | `−2/3` ✓ |
| `e⁻` | `−1` | `−2` | `−2` ✓ |
| `νₑ` | `0` | `0` | `0` ✓ |

Lean: `hypercharge_determined_of_isospin_zero` — any two candidate
assignments satisfying GMN against the *same* derived `Q` at `I₃ = 0` are
**equal**. So the right-handed rows are entailed by the framework's
already-derived `Q` and can separate no two candidates.

This is the same logical status as the Gell-Mann–Okubo relation, which
#4640 proved vacuous (`GellMannOkuboIdentity.lean`: `4m_K² − 3m_η² − m_π² = 0`
holds identically for *any* first-order octet breaking). **Passing the
right-handed battery is not evidence for any mechanism.**

### R2 — the left-handed half of B2 is exactly `B − L`

| fermion | `Y = 2(Q − I₃)` | `B − L` | B2-LH target |
|---|---|---|---|
| `u` | `1/3` | `1/3 − 0` | `+1/3` ✓ |
| `d` | `1/3` | `1/3 − 0` | `+1/3` ✓ |
| `νₑ` | `−1` | `0 − 1` | `−1` ✓ |
| `e⁻` | `−1` | `0 − 1` | `−1` ✓ |

Lean: `lh_hypercharge_eq_baryon_sub_lepton`.

### R3 — B1 is the `L = 0` restriction of R2

On the nucleon doublet `L = 0`, so `Y = B − L = B = +1` for both `p` and
`n`. Lean: `nucleon_hypercharge_eq_baryon_number`, which also proves
`Y(p) = Y(n)` — the very degeneracy the chapter records as falsifying the
writhe map (the writhe *does* separate `p` from `n`; `Y` does not).

## Consequence

**B2 imposes one independent condition, not two.** The battery reduces to:

> derive `B − L` on the left-handed sector,

of which B1 is the `L = 0` restriction `Y = B`. The apparent "two batteries,
eight rows" understates how little is being tested: four of the eight rows
are entailed by `Q`.

### Bearing on the candidates

This narrows the target; it endorses nothing.

* **PR #4597's Milnor triple linking `μ̄₁₂₃`** proposes `μ̄₁₂₃ = B`. That
  supplies the **`B` half** — closing B1 and the quark rows of B2-LH — and
  leaves the **`L` half open**: lepton number is not a baryon-sector
  invariant, and `B − L` is what the left-handed rows require. The
  well-motivated part of #4597 (a degree-2 invariant is *forced*, because
  every degree-1 crossing invariant vanishes on the Borromean baryon `𝓑₃`)
  is unaffected by this reduction and remains the load-bearing argument.
* **The chapter's ribbon-framing-twist candidate** and #4597's candidate
  table **disagree**, and the disagreement is not resolved here. #4597 lists
  the framing phase `q^{w·c}` as EXCLUDED ("factors through `w`"), while
  `flavor-charge-assignments.md` names the ribbon-framing twist `T(t)` as
  the candidate direction, asserting `T(t)` is independent of the crossing
  word. These may be different objects — a framing *phase* built from `w`
  does factor through `w` by construction, whereas an independent per-strand
  twist datum need not — in which case both statements stand and #4597's
  candidate-1 exclusion simply does not reach `T(t)`. **Unresolved; flagged
  for the chapter owner.** Recorded as bean `qou-6006`.

## Honest scope (anti-laundering)

`Y = B − L` on the left-handed sector is a **standard Standard-Model
identity**, not a QOU derivation. Nothing here derives `B`, `L`, or `Y` from
the substrate, and no candidate invariant is endorsed or excluded. The
content is the **reduction** — what a candidate must hit, and how much of
the stated battery is vacuous.

Per AGENTS.md §"Before declaring refuted": R1 is a **scope-(a)** statement
about the battery's information content (with the invariant cited: GMN at
`I₃ = 0` determines `Y`), *not* a scope-(b) exclusion of any invariant.

## Verification

* `lean`-direct v4.24.0 against restored Mathlib oleans: **exit 0**,
  0 `sorry`, 0 `native_decide`, 0 `axiom` declarations.
* `#print axioms` on all four theorems: `[propext, Classical.choice,
  Quot.sound]` only.
* Probe: all exact checks pass (`Fraction`, no floats).
* CI unavailable repo-wide (auto-triggers disabled); the above is the
  verification gate per AGENTS.md §Phase-4.

**Lean caught a real gap:** the first draft stated the uniqueness result
over a bare `Field K`. It is **false in characteristic 2** (`2 = 0`, so
`Y/2` is junk); `CharZero` is required, not decorative.
