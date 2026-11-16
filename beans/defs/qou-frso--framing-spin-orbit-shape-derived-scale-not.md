---
# qou-frso
title: 'Framing spin-orbit: the 2l+1 shape is derived, the scale is not'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T00:00:00Z
updated_at: 2026-10-04T15:14:51Z
parent: qou-v2om
---

First real test of the framing route (`qou-mgq3` option 1), the only path to
{28, 50, 82, 126} not already excluded. One positive, one negative.

## DERIVED, parameter-free: the 2l+1 spin-orbit shape

`def:strand-twist-datum` warns that the per-strand label `T(t)` is a **free**
integer label, so a coupling built on it inherits that freedom — which is why
that bean flagged "fix the descent problem first". **The route does not need
it.** The same block records that the *ribbon* twist is not free: on the n-th
Jones–Wenzl idempotent it acts by `(-1)^n A^{n(n+2)}`, exponent `n(n+2)` = the
Casimir.

And spin-orbit *is* a difference of Casimirs:

    l·s = ½[ C(j) − C(l) − C(s) ],   C(x) = x(x+1)

so the ribbon-twist ratio between the two `j = l ± ½` channels carries exponent
`C(j₊) − C(j₋)`, which is **exactly `2l+1`** for every `l ≥ 1` — verified
symbolically over `Fraction`, `l = 1..12`, zero counterexamples.

`2l+1` is precisely the standard spin-orbit `l`-dependence: the growth with `l`
that pulls the high-`l` intruder down and opens the 28 / 50 / 82 gaps. **Nothing
was chosen to obtain it.** This is a real structural result and it sidesteps the
free-label problem entirely.

## NOT DERIVED: the strength, and the number that says so

The ladder depends on the spin-orbit strength `C` relative to the oscillator
spacing. Taking the twist to an energy gives `C ~ ln(q₀) = 0.10434`, which does
land in the window that reproduces the ladder. The window:

    ≥6 of 7 magic numbers for C ∈ [0.060, 0.195]
    width 0.135 = 46.7 % of the scanned range 0.005..0.30

**~Half of all plausible couplings work**, so membership constrains almost
nothing. This is the `S_leak` precedent in AGENTS.md — *"the flip is produced by
ANY constant strictly between the two values; compute that window and report its
width before claiming the feature is evidence."* Computed: the window is wide.

Verdict: **shape yes, scale no.** Scope (a) on the scale only; the 2l+1 result
is positive and unaffected.

## Two methodology notes, both load-bearing

**The 6/7 is a limit of my criterion, not of the framework.** Closures are read
as the 7 largest energy gaps with false positives counted; that tops out at
6 hits / 1 FP **anywhere** in the (C, D) scan, including at couplings the
literature reproduces all 7 with. Do not quote 6/7 as a measured shortfall.

**My first version of this test was worthless and I ran it before noticing.**
It scored "does each magic number appear among the cumulative sums" — no false
positives counted — and returned **7/7 for essentially every coupling**, because
any level scheme yields dozens of cumulative sums. That is the same
selection-blindness this session found in three other places (the δ²Φ table
tabulating only magic Z; `magic_ladder_member` hardcoded from `MAGIC_LADDER`;
`solve_shell_magic_sdp` refusing non-magic input) — the magic set entering as an
input and being presented as an output. Fourth instance, and the first one that
was mine.

## Next

1. **Derive the energy scale, or show it cannot be derived here.** The whole
   question is now `C/ħω`, one number. The twist gives a multiplicative
   `q^{2l+1}`; converting to an additive energy needs a scale that this probe
   supplies by hand. If the framework fixes it, the route closes positively; if
   it is free, the route yields shape-only and should be stated that way.
2. **Sharpen the closure criterion** before any further scoring, so a real 7/7
   is reachable and the metric stops capping at 6.
3. Do **not** re-attempt `l·s` from a scalar q-oscillator — proved scope-(b)
   exclusion, 2026-07-06 audit.


---

## Round 48 Execution Update (2026-11-16, PR #8181)

- **PR:** https://github.com/litlfred/qou/pull/8181 (`e3a0c2e1773d8a4bc1635ead95154cb8d9babb4d`)
- **Lean 4 Formalisation (`0` `sorry`, `0` `axiom`, wired into `QOU.lean`):**
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/FramingSpinOrbitMagicLadder.lean`
    - `fourCasimir_spin_orbit_diff`, `twoLdotS_eigen_diff`: proves the parameter-free Landé spin–orbit splitting `C(ℓ + 1/2) - C(ℓ - 1/2) = 2ℓ + 1` and `2L·S|_{j=ℓ+1/2} - 2L·S|_{j=ℓ-1/2} = ℓ - (-(ℓ + 1)) = 2ℓ + 1`.
    - `framingSpinOrbitShift_injective_in_scale`: isolates the unfixed radial scale `V_ls`.
    - `hoCumulative_first_seven`, `soIntruderCumulative_magic_upper`, `mayer_jensen_intruder_splits`, `mayer_jensen_ladder_eq_magicList`: proves the pure 3D harmonic-oscillator closures `[2, 8, 20, 40, 70, 112, 168]` vs the high-`j` spin–orbit intruder closures `[20 + 8 = 28, 40 + 10 = 50, 70 + 12 = 82, 112 + 14 = 126]` yielding `[2, 8, 20, 28, 50, 82, 126]`.
- **Probe & 50-dps Witness:**
  - `computations/probes/spin_orbit_magic_rstar_mirror_probe.py`
  - `computations/probes/spin-orbit-magic-rstar-mirror-probe.witness.json`
- **Status:** Kept at `in-progress` pending owner review and PR merge.
