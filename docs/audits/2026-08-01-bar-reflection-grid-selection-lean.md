# Bar-reflection grid selection — the Lean two-point narrowing (2026-08-01)

**Tier:** Lean-proved structural result on the closing question of
[`conj:schwinger-measure-computational-time`](../../content/quantum-observable-universe/predicted-spectra/schwinger-measure-computational-time.md).
Formalize-first follow-on to the KSel campaign
([`2026-08-01-ksel1-singularity-selection.md`](2026-08-01-ksel1-singularity-selection.md),
[`2026-08-01-ksel2-gns-favard-canonicity.md`](2026-08-01-ksel2-gns-favard-canonicity.md),
[`2026-08-01-ksel3-modular-double-covariance.md`](2026-08-01-ksel3-modular-double-covariance.md)).
Nothing is wired; no numerics fitted.

## What is proved (sorry-free, lean-direct exit 0)

Two new modules:

- [`QOU/AlgebraicSubstrate/BarReflectionGridSelection.lean`](../../content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/BarReflectionGridSelection.lean)
  — generic `CommGroup G` core (§7c substrate side):
  - `barReflect v s = v⁻¹ * s⁻¹` is an involution
    (`barReflect_involutive`) and maps the theta grid `u·v^ℤ` to the
    grid `u⁻¹·v^ℤ` (`barReflect_mem_grid_iff`) — so the bar reflection
    acts on translate classes by `u ↦ u⁻¹`.
  - `grid_eq_grid_iff`: grid equality is translate equivalence.
  - `grid_barInvariant_iff`: the class of `u` is bar-fixed iff
    `u² ∈ v^ℤ`.
  - `grid_barInvariant_classification`: given a half-step `w` with
    `w² = v` and 2-torsion-freeness, the bar-fixed classes are
    **exactly two**: the unit class `grid 1 v` and the half-step class
    `grid w v`.
- [`QOU/Archimedean/BarReflectionGridSelectionReal.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/BarReflectionGridSelectionReal.lean)
  — wall-side instantiation at `ℝ_{>0}`: both hypotheses are
  **discharged** (`posReal_two_torsion_free` via `nlinarith`;
  `sqrtPos_sq` via `Real.sq_sqrt`), making the narrowing
  **unconditional** over the positive reals
  (`grid_barInvariant_iff_unit_or_half`); `barReflect_eq_div` confirms
  the reflection is literally `s ↦ q̃⁻¹/s`.

## What this settles, in the conjecture's frame

The extension-circle continuum of atomic kernels is parametrized by the
translate class `u ∈ ℝ_{>0}/q̃^ℤ`. The identified derivation route acts
the fibre bar involution `s ↦ q̃⁻¹/s` on this continuum; the theorem
says its action is `u ↦ u⁻¹` and its fixed classes are **exactly**
`{1, q̃^{1/2}}` — the two candidates the KSel-1 half-step discriminant
already separated. So: **IF** the distinguished kernel is atomic and
bar-invariant (bar-invariance being the natural selection principle,
since the balanced moment functional is exactly bar-invariant), **THEN**
its grid is `q̃^ℤ` or `q̃^{1/2+ℤ}` — a two-point set, machine-checked.

## Honest scope (what this does NOT do)

- It does not select between the two fixed classes (that is KSel-1's
  future output datum, or the Friedrichs identification in flight).
- It does not prove the distinguished extension is atomic — the
  absolutely continuous log-normal kernel is also bar-invariant (it is
  the zero mode of the same Gaussian), and N-extremal/Friedrichs
  arguments live at the operator level, not the grid level.
- It does not touch the conjecture's own (REP)/identification content;
  the Lean class `BorelProperTimeIdentification` is unchanged, no
  instance exists.

## Verification

`lean -D autoImplicit=false` (lean-direct, toolchain v4.24.0, restored
olean cache), exit 0 on both files; no `sorry`, no `axiom`, no
`native_decide`; imports registered in `QOU.lean`.

Bean: `qou-vpj2`.
